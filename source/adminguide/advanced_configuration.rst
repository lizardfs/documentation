.. _advanced_config:

**********************
Advanced configuration
**********************
.. auth-status-proof1/none


.. _rack_awareness:

Configuring rack awareness (network topology)
=============================================

The topology of a LizardFS network can be defined in the mfstopology.cfg file.
This configuration file consists of lines matching the following syntax::

   ADDRESS SWITCH-NUMBER

ADDRESS can be represented as:

+-------------------+-------------------------------------------------------+
|  \*               | all addresses                                         |
+-------------------+-------------------------------------------------------+
|  n.n.n.n          | single IP address                                     |
+-------------------+-------------------------------------------------------+
|  n.n.n.n/b        | IP class specified by network address and bits number |
+-------------------+-------------------------------------------------------+
|  n.n.n.n/m.m.m.m  | IP class specified by network address and mask        |
+-------------------+-------------------------------------------------------+
|  f.f.f.f-t.t.t.t  | IP range specified by from-to addresses (inclusive)   |
+-------------------+-------------------------------------------------------+

The switch number can be specified as a positive 32-bit integer.

Distances calculated from mfstopology.cfg are used to sort chunkservers during
read/write operations. Chunkservers closer (with lower distance) to a client
will be favoured over further away ones.

Please note that new chunks are still created at random to ensure their equal
distribution. Rebalancing procedures ignore topology configuration as well.

As for now, distance between switches can be set to 0, 1, 2:

  0 - IP addresses are the same

  1 - IP addresses differ, but switch numbers are the same

  2 - switch numbers differ

The topology feature works well with chunkserver labeling - a combination of
the two can be used to make sure that clients read to/write from chunkservers
best suited for them (e.g. from the same network switch).


.. _lizardfs_qos:

Configuring QoS
===============

Quality of service can be configured in the /etc/mfs/globaliolimits.cfg file.

Configuration options consist of:

* subsystem <subsystem>
  cgroups subsystem by which clients are classified
* limit <group> <throughput in KiB/s>
* limit for clients in cgroup <group>
* limit unclassified <throughput in KiB/s>
* limit for clients that do not match to any specified group.

If globaliolimits.cfg is not empty and this option is not set, not specifying
limit unclassified will prevent unclassified clients from performing I/O on
LizardFS

Example 1::

   # All client share 1MiB/s bandwidth
	limit unclassified 1024

Example 2::

   # All clients in blkio/a group are limited to 1MiB/s, other clients are blocked
	subsystem blkio
	limit /a 1024

Example 3::

   # The directory /a in the blkio group is allowed to transfer 1MiB/s
   # /b/a group gets 2MiB/s
   # unclassified  clients share 256KiB/s of bandwidth.
        subsystem blkio
       	limit unclassified 256
       	limit /a   1024
       	limit /b/a 2048

.. _lizardfs_quotas:

Configuring Quotas
==================

Quota mechanism can be used to limit inodes usage and space usage for users
and groups. By default quotas can be set only by a superuser. Setting the
SESFLAG_ALLCANCHANGEQUOTA flag in the mfsexports.cfg file would allow
everybody to change quota.

In order to set quota for a certain user/group you can simply use mfssetquota
tool::

   mfssetquota  (-u UID/-g GID)   SL_SIZE   HL_SIZE   SL_INODES   HL_INODES   MOUNTPOINT_PATH

where:

* SL - soft limit
* HL - hard limit

.. _mount_meta:

Mounting the metadata
=====================

LizardFS metadata can be managed through a special mountpoint called META.
META allows to control trashed items (undelete/delete them permanently) and
view files that are already deleted but still held open by clients.

To be able to mount metadata you need to add the “mfsmeta” parameter to the
mfsmount command::

   # mfsmount /mnt/lizardfs-meta -o mfsmeta

after that you will see the following line at mtab::

   mfsmeta#10.32.20.41:9321 on /mnt/lizardfs-meta type fuse (rw,nosuid,nodev,relatime,user_id=0,group_id=0,default_permissions,allow_other)

The structure of the mounted metadata directory will look like this::

   /mnt/lizardfs-meta/
                      ├── reserved
                      └── trash
                      └── undel

.. _meta_trash:

Trash directory
----------------

Each file with a trashtime higher than zero will be present here. You can
recover those files or delete files permanently.

Recovering files from the trash
-------------------------------

In order to recover a file, just must move it to the undel/ directory. Files
are represented by their inode number and path, so the file dir1/dir2/file.txt
with inode 5 will be present at trash/5|dir1|dir2|file.txt,
recovering it would be performed like this::

   $ cd trash
   $ mv ‘5|dir1|dir2|file.txt’ undel/

Removing files permanently
--------------------------

In order to delete a file permanently, just remove it from trash.

Reserved directory
------------------

If you delete a file, but someone else use this file and keep an open
descriptor, you will see this file in here until descriptor is closed.

.. _lizardfs_ha_cluster:

Deploying LizardFS as a HA Cluster
==================================

LizardFS can be run as a high-availability cluster on several nodes. When
working in HA mode, a dedicated daemon watches the status of the metadata
servers and performs a failover whenever it detects a master server crashed
(e.g. due to power outage). Running LizardFS installation as a HA-cluster
significantly increases its availability. Since uRaft uses :ref:`quorum` a
reasonable minimum of metadata servers in a HA installation is at least 3.

In order to deploy LizardFS as a high-availability cluster, follow the steps
below.

These steps should be performed on all machines chosen to be in a cluster.

Install the lizardfs-uraft package::

   $ apt-get install lizardfs-uraft for Debian/Ubuntu
   $ yum install lizardfs-uraft for CentOS/RedHat

Prepare your installation:

Fill lizardfs-master config file (/etc/mfs/mfsmaster.cfg) according to
:ref:`master_server_config`. Details depend on your personal configuration,
the only fields essential for uraft are::

   PERSONALITY = ha-cluster-managed
   ADMIN_PASSWORD = your-lizardfs-password

For a fresh installation, execute the standard steps for the lizardfs-master
(creating mfsexports file, empty metadata file etc.). Do not start the
lizardfs-master daemon yet.

Fill the lizardfs-uraft config file (/etc/mfs/lizardfs-uraft.cfg). Configurable
fields are:

**URAFT_NODE_ADDRESS**
  identifiers of all the machines in your cluster
**URAFT_ID**
  node address ordinal number; should be unique for each machine
**URAFT_FLOATING_IP**
  IP at which LizardFS will be accessible for the clients
**URAFT_FLOATING_NETMASK**
  a matching netmask for floating IP
**URAFT_FLOATING_IFACE**
  network interface for the floating IP
**URAFT_ELECTOR_MODE**
  ...
**LOCAL_MASTER_ADDRESS**
  The address of the local master controlled by this uraft node, defaults to
  localhost.
**LOCAL_MASTER_MATOCL_PORT**
  The port the local master listens on, defaults to 9421
**ELECTION_TIMEOUT_MIN**
  Minimum election timeout (ms), defaults to 400
**ELECTION_TIMEOUT_MAX**
  Maximum election timeout (ms), defaults to 600
**HEARTBEAT_PERIOD** = 20
  Period between hearbeat messages between uraft nodes (ms), defaults to 20.
**LOCAL_MASTER_CHECK_PERIOD**
  How often uRaft checks if local master is alive (ms), defaults to 250.


Example configuration for a cluster with 3 machines:
----------------------------------------------------

The first, node1, is at 192.168.0.1, the second node gets hostname node2, and
the third one gets hostname node3 and operates under a non-default port number
- 99427.

All machines are inside a network with a 255.255.255.0 netmask and use
their network interface eth1 for the floating ip.

The LizardFS installation will be accessible at 192.168.0.100 ::

   # Configuration for node1:
   URAFT_NODE_ADDRESS = 192.168.0.1            # ip of first node
   URAFT_NODE_ADDRESS = node2                  # hostname of second node
   URAFT_NODE_ADDRESS = node3:99427            # hostname and custom port of third node
   URAFT_ID = 0                                # URAFT_ID for this node
   URAFT_FLOATING_IP = 192.168.0.100           # Shared (floating) ip adddress for this cluster
   URAFT_FLOATING_NETMASK = 255.255.255.0      # Netmask for the floating ip
   URAFT_FLOATING_IFACE = eth1                 # Network interface for the floating ip on this node

  # Configuration for node2:
   URAFT_NODE_ADDRESS = 192.168.0.1            # ip of first node
   URAFT_NODE_ADDRESS = node2                  # hostname of second node
   URAFT_NODE_ADDRESS = node3:99427            # hostname and custom port of third node
   URAFT_ID = 1                                # URAFT_ID for this node
   URAFT_FLOATING_IP = 192.168.0.100           # Shared (floating) ip adddress for this cluster
   URAFT_FLOATING_NETMASK = 255.255.255.0      # Netmask for the floating ip
   URAFT_FLOATING_IFACE = eth1                 # Network interface for the floating ip on this node

   # Configuration for node3:
   URAFT_NODE_ADDRESS = 192.168.0.1            # ip of first node
   URAFT_NODE_ADDRESS = node2                  # hostname of second node
   URAFT_NODE_ADDRESS = node3:99427            # hostname and custom port of third node
   URAFT_ID = 2                                # URAFT_ID for this node
   URAFT_FLOATING_IP = 192.168.0.100           # Shared (floating) ip adddress for this cluster
   URAFT_FLOATING_NETMASK = 255.255.255.0      # Netmask for the floating ip
   URAFT_FLOATING_IFACE = eth1                 # Network interface for the floating ip on this node

Enable arp broadcasting in your system (for the floating IP to work)::

	$ echo 1 > /proc/sys/net/ipv4/conf/all/arp_accept

Start the lizardfs-uraft service:

Change “false” to “true” in /etc/default/lizardfs-uraft::

   $ service lizardfs-uraft start

You can check your uraft status via telnet on URAFT_STATUS_PORT
(default: 9428)::

	$ telnet NODE-ADDRESS 9428

When running telnet locally on a node, it is sufficient to use::

	$ telnet localhost 9428

Please check if you have the :ref:`sudo` package installed and that the 'mfs'
user has been added with the right permissions to the /etc/sudoers file.

