.. _cookbook_hypervisors:

************************************************
LizardFS Hypervisors and Virtualization Cookbook
************************************************

.. auth-status-todo/none

.. _xenserver_storage:

Providing storage for XenServer
===============================

Requirements::

  LizardFS >= 3.10.4
  XenServer >= 7

XenServer 7 is required since it makes use of CentOS 7 as the underlying OS
and LizardFS provides packages for CentOS 7.

.. warning:: Installing 3rd party components – such as the LizardFS client,
             and server components may invalidate any support provided by Citrix
             for your installation.

Pre-requisites
--------------

This guide presumes you have already installed XenServer – and are familiar
with accessing the XenServer Console and using tools such as 'vi' to edit
files.

You should have already configured the networking on XenServer. This could be
just a single network – XenServer installations usually have an 'INTERNET
facing' network – and then one, or more 'storage networks' – make sure IP
addresses are setup that you can use for connecting to, or running LizardFS on
(i.e. probably not INTERNET facing).

Preparing Storage – if you need it
----------------------------------

If you are going to use the XenServer itself to provide storage – you'll
need to prepare drives / directories on the server.

As an example - we'll mount all the drives we want to place chunks on under
'/mnt'.
Once XenServer is booted – from the XenServer console you can see a list of
available drives by looking in '/dev/disk/by-id' – i.e. ::

  [root@XenServer-1 ~]# ls -l /dev/disk/by-id/
  total 0
  lrwxrwxrwx 1 root root  9 Mar 22 15:48 ata-Crucial_CT250MX200SSD1_153710904260 -> ../../sdi
  lrwxrwxrwx 1 root root  9 Mar 22 15:48 ata-Crucial_CT250MX200SSD1_154110CAA644 -> ../../sdh
  lrwxrwxrwx 1 root root  9 Mar 22 15:48 ata-SAMSUNG_HD204UI_S2H7J1CZ909998 -> ../../sdf
  lrwxrwxrwx 1 root root  9 Mar 22 15:48 ata-SAMSUNG_HD204UI_S2H7J1CZ910008 -> ../../sde


By using the '/dev/disk/by-id' entries we ensure if the disk is moved to
another bay – it will still mount correctly. You can use 'gpart' to partition
these disks, or just use the “raw” disk to create partitions on, e.g.:

.. code-block:: bash

  mkfs.ext4 /dev/disk/by-id/ata-Crucial_CT250MX200SSD1_153710904260
  mkfs.ext4 /dev/disk/by-id/ata-Crucial_CT250MX200SSD1_154110CAA644
  mkfs.ext4 /dev/disk/by-id/ata-SAMSUNG_HD204UI_S2H7J1CZ909998
  mkfs.ext4 /dev/disk/by-id/ata-SAMSUNG_HD204UI_S2H7J1CZ910008

And so on, for all the drives you want to use.

Once you've formatted the disks – we need to tell XenServer where to mount
them when the system comes up. First you need to create directories under the
'/mnt' directory – if you keep the name of the directory the same as the drive
device name, we'd do:

.. code-block:: bash

  mkdir /mnt/ata-Crucial_CT250MX200SSD1_153710904260
  mkdir /mnt/ata-Crucial_CT250MX200SSD1_154110CAA644
  mkdir /mnt/ata-SAMSUNG_HD204UI_S2H7J1CZ909998
  mkdir /mnt/ata-SAMSUNG_HD204UI_S2H7J1CZ910008
  chown mfs:mfs /mnt/ata-*

Once this is done you can add the drives to the systems 'fstab' to ensure they
are mounted automatically at boot-time – if you 'vi /etc/fstab' and then
create entries such as::

  /dev/disk/by-id/ata-Crucial_CT250MX200SSD1_153710904260 defaults,nofail 0 2
  /dev/disk/by-id/ata-Crucial_CT250MX200SSD1_154110CAA644 defaults,nofail 0 2
  /dev/disk/by-id/ata-SAMSUNG_HD204UI_S2H7J1CZ909998 ext4 defaults,nofail 0 2
  /dev/disk/by-id/ata-SAMSUNG_HD204UI_S2H7J1CZ910008 ext4 defaults,nofail 0 2

The 'nofail' option means that the system continues to boot even if the disk
or disks are unavailable. Once this is done you can mount all of those disks
with::

  mount -a

Installing LizardFS
-------------------

Before you can install any of the LizardFS components we need to tell the XenServer nodes where to get the LizardFS RPM's from.

For each node in the system (or any nodes you add) you need to log in to the
XenServer console on the node and run once::

  curl http://packages.lizardfs.com/yum/el7/lizardfs.repo > /etc/yum.repos.d/lizardfs.repo

This fetches the LizardFS repository details to somewhere XenServer can find
them (with the 'yum' command).

LizardFS Client
---------------

To connect XenServer to LizardFS you need to install the 'lizardfs-client'.
Even if you're not installing full LizardFS on XenServer you still need to
install the client package as well as the FUSE library package.

The repo file XenServer points to packages that are no longer present on
the CentOS site (they've been moved to the CentOS 'Vault') – so we need to
adjust the URL so the system can pull in FUSE as part of the 'lizardfs-client'
install.

Edit the file '/etc/yum.repos.d/CentOS-Base.repo' – change the “[base]” URL to
read::

  baseurl=http://vault.centos.org/7.2.1511/os/x86_64

And save the file.

We can now install 'lizardfs-client' (which will also install FUSE) with::

  yum --disablerepo=extras --disablerepo=updates install lizardfs-client

If you're just using XenServer to access another LizardFS installation (i.e.
on another server / system) you don't need to add the following other software
components – just skip ahead to :ref:`xenserver_client_conf` .


LizardFS Chunk-Server and Meta-Server
-------------------------------------

If you're using the XenServer as either a 'chunk-server' (holds data) or
'meta-server' (holds meta-data) you'll need to install other components of
LizardFS on the XenServer as well.

You can use the following to install the 'master' server (meta-server),
chunkserver – and Admin tools respectively:

.. code-block:: bash

  yum --disablerepo=base --disablerepo=extras --disablerepo=updates install lizardfs-master
  yum --disablerepo=base --disablerepo=extras --disablerepo=updates install lizardfs-chunkserver
  yum --disablerepo=base --disablerepo=extras --disablerepo=updates install lizardfs-adm

Setting up the Chunk Server
+++++++++++++++++++++++++++

By now you should have the LizardFS chunk-server software installed – and your
drives setup ready to hold data chunks.
The LizardFS chunk-server installs with a default config – but you need to
copy it into place first::

  cd /etc/mfs
  cp mfshdd.cfg.dist mfshdd.cfg

You'll need to edit '/etc/mfs/mfshdd.cfg' to tell the chunk-server what drives
it has available. For our example we edited 'mfshdd.cfg' and added::

  # Our Chunk Drives/Directories
  /mnt/ata-Crucial_CT250MX200SSD1_153710904260
  /mnt/ata-Crucial_CT250MX200SSD1_154110CAA644
  /mnt/ata-SAMSUNG_HD204UI_S2H7J1CZ909998
  /mnt/ata-SAMSUNG_HD204UI_S2H7J1CZ910008

Setting up the Meta Server ('master')
+++++++++++++++++++++++++++++++++++++

If you're running the master / meta-server under XenServer you need to make one
node a 'master' and the other a 'shadow'.
You will need to copy the example configs to the real configuration files:

.. code-block:: bash

  cd /etc/mfs
  cp mfsmaster.cfg.dist mfsmaster.cfg
  cp mfsexports.cfg.dist mfsexports.cfg

You need to edit '/etc/mfs/mfsmaster.cfg' one (and only one) node should have
a personality of 'master' – the other should be a 'shadow'. It is also
recommended in that file that you set an 'ADMIN_PASSWORD'.
If the XenServer is going to be running as a master, or shadow – you'll also
need to edit '/etc/mfs/mfsexports.cfg' – by default this just sets up a basic
config (this is similar to an nfs exports file).
Finally – you'll need to install a blank database for the 'master' server –
and any shadows – this involves copying an empty database i.e.:

.. code-block:: bash

  cp /var/lib/mfs/metadata.mfs.empty /var/lib/mfs/metadata.mfs
  chown mfs:mfs /var/lib/mfs/metadata.mfs

You will only need to do this when installing the 'master' service.


.. seealso::
             * :ref:`basic_config`
             * :ref:`advanced_config`


.. _xenserver_client_conf:

Client Configuration
++++++++++++++++++++

XenServer ships with a firewall – we'll need to configure that to allow
LizardFS traffic to pass. To do this edit '/etc/sysconfig/iptables' – we need
to add our rules before the REJECT line and COMMIT statement so you should end
up with::

  # LizardFS
  -A RH-Firewall-1-INPUT -m conntrack --ctstate NEW -m tcp -p tcp --dport 9421 -j ACCEPT
  -A RH-Firewall-1-INPUT -m conntrack --ctstate NEW -m tcp -p tcp --dport 9422 -j ACCEPT
  -A RH-Firewall-1-INPUT -m conntrack --ctstate NEW -m tcp -p tcp --dport 9420 -j ACCEPT
  -A RH-Firewall-1-INPUT -m conntrack --ctstate NEW -m tcp -p tcp --dport 9419 -j ACCEPT
  -A RH-Firewall-1-INPUT -j REJECT --reject-with icmp-host-prohibited
  COMMIT

You must now restart the firewall service with::

  service iptables restart

LizardFS requires the host name 'mfsmaster' to resolve and point to the IP of
the master server. The easiest way to achieve this is to edit '/etc/hosts' –
and add an entry for it::

  192.168.0.100    mfsmaster

The '192.168.0.100' IP address should be the IP address of a LizardFS 'master'
server (not shadow). If you're running XenServer with an existing LizardFS
system on other hosts – you should already have a 'master' server. If you're
running LizardFS master service on XenServer it'll be the IP of whichever node
you setup as 'master' (not 'shadow').

If you are running an HA setup of LizardFS it should be the
"URAFT_FLOATING_IP" you defined in your URAFT configuration.

Assuming you installed the LizardFS admin tools – you can make life easier by
adding the following lines to '/root/.bashrc':

.. code-block:: bash

  alias lfschunks='lizardfs-admin list-chunkservers mfsmaster 9421'
  alias lfshealth='lizardfs-admin chunks-health mfsmaster 9421'
  alias lfsmounts='lizardfs-admin list-mounts mfsmaster 9421'
  alias lfsdisks='lizardfs-admin list-disks mfsmaster 9421'

Once the service has started we can use these aliases / commands to check on
things (if you haven't installed the LizardFS admin tools and want to use
these commands – see above for info on how to install them).

Testing your LizardFS setup
---------------------------

If you're **connecting XenServer to an existing LizardFS system** – you should
be able to just mount the LizardFS at this point, e.g.::

  mkdir /mnt/lizardfs
  mfsmount /mnt/lizardfs

This should mount the LizardFS file system under '/mnt/lizardfs'. If it's an
existing system you'll need to make sure you mount at the correct point (i.e.
check how the existing system is setup).

If you're **running LizardFS on the actual XenServers** we'll need to bring up
the 'master' service – and the chunk- servers. You can do this with::

  service lizardfs-master start
  service lizardfs-chunkserver start

You'll need to repeat this on each node – remembering only one can be the
'master' meta-server – the other has to be a shadow (set in
'/etc/mfs/mfsmaster.cfg)
You should then be able to mount the default LizardFS then with::

  mkdir /mnt/lizardfs
  mfsmount /mnt/lizardfs

This should be repeated on each node.

Once that's done – if you've installed the LizardFS admin tools (and added the
above Bash aliases) you can use::

  lfshealth - Display info on the 'health' of the LizardFS
  lfsmounts - Display info on what's mounted the LizardFS file system
  lfsdisks - Display info on all the disks provided by the chunk-servers on the system
  lfschunks - Display info on the chunk-servers on the system

As a quick test – if you create a test-file in '/mnt/lizardfs' on one node –
the other should show it, i.e.::

  [root@XenServer-1 ~]# cd /mnt/lizardfs
  [root@XenServer-1 lizardfs]# echo “Hello World!” >/mnt/lizardfs/test.txt

(switch to XenServer-2 Console) ::

  [root@XenServer-1 ~]# cd /mnt/lizardfs
  [root@XenServer-2 lizardfs]# cat test.txt
  Hello World!
  [root@XenServer-2 lizardfs]#

At this point we can create a 'xen-sr' directory – and set a 'goal' on it.
Again, if you're tying into an existing LizardFS system you'll need to see how
that's configured before you go creating directories / setting goals in place.

If you're running XenServer as it's own LizardFS system we can do::

  mkdir /mnt/lizardfs/xen-sr
  mfssetgoal 2 /mnt/lizardfs/xen-sr

Using a goal of “2” means (by default) that LizardFS will keep 2 copies (one
on each node) of any chunks – so if one chunk server (XenServer fails) the
other can still access the data.

Creating a storage repository (SR)
----------------------------------

Now we need to create a XenServer Storage Repository (SR) on the LizardFS. If
you have more than one XenServer – you should log into the pool master and
then run::

  xe host-list

Make a note of the pool master's uuid (and the other nodes uuid) – you'll need
those in a moment.

Now do:

.. code-block:: bash

  export MYUUID=`uuidgen`
  xe sr-introduce uuid=$MYUUID name-label="LizardFS" content-type=user type=file shared=true 61625483-3889-4c55-8eee-07d14e9c9044
  xe pbd-create sr-uuid=$MYUUID device-config:location=/mnt/lizardfs/xen-sr host-uuid=(uuid of pool master) 62c9a88a-5fe4-4720-5a85-44b75aebb7fd
  xe pbd-create sr-uuid=$MYUUID device-config:location=/mnt/lizardfs/xen-sr host-uuid=(uuid of 2nd node) a91b77ee-949d-49d9-186f-259cd96b5c00
  xe pbd-plug uuid=62c9a88a-5fe4-4720-5a85-44b75aebb7fd
  xe pbd-plug uuid=a91b77ee-949d-49d9-186f-259cd96b5c00

At this point in XenCenter (the GUI admin tool for XenServer) you should be
able to see a new storage repository called “LizardFS”

System Startup
--------------

Ok – so we've now got a LizardFS system – and a XenServer Storage Repository.

At boot time – it's obviously important that LizardFS is up and running (
either just the client, or the client – and server components if you're
running everything on XenServer).

The easiest way to achieve this (at present) is to create a startup script –
and have that invoked, just before XenServer attaches to the LizardFS based
storage repository.
So we'll edit a file called '/root/lizardfs-sr-start.sh' – and put into it:

.. code-block:: bash

   #!/bin/sh
   # Start the LizardFS 'master' Service (if you need to)
   service lizardfs-master start
   # Start the LizardFS 'chunkserver' Service (if you need to)
   service lizardfs-chunkserver start
   # Mount the LizardFS
   mfsmount /mnt/lizardfs
   # Return 'Ok' back
   exit 0

You need to 'chmod u+x lizardfs-sr-start.sh' to make sure it's executable.

This needs to be hooked into the XenServer startup – this means editing one of
the XenServer python files.

If you 'vi /opt/xensource/sm/FileSR.py' – and then search for a line that says
“def attach” - you need to change that function to read:

.. code-block:: python

   def attach(self, sr_uuid):
      if not self._checkmount():
        try:
            import subprocess
            subprocess.call(['/root/lizardfs-sr-start.sh'])


At boot time, as the local file repository gets attached – the
'lizardfs-sr-start.sh' script will be called – which makes sure the services
are started, and LizardFS mounted up.

At this point you can test the system by restarting the 2nd node (if you have
one) – then the first node (pool master) – both should come back, re-attach
the LizardFS – and have the LizardFS storage repository available.

NOTES
-----

.. note:: If you make one of your XenServer's the meta-server master – it must
          be up and running in order for the other nodes to use the storage.

.. note:: If the meta-server 'master' fails – you can promote one of the
          remaining 'shadow' servers to be the new master – but there must be
          only one 'master' on the system at any time (so the previous master
          will have to be reconfigured and come back as a 'shadow' server).

.. note:: LizardFS provide 'lizard-uraft' – which utilizes the :ref:`raft`
          protocol to keep a 'master' server always available. It's designed
          for use by a minimum of 3 nodes (two of which can be the XenServer).

   This is covered in :ref:`lizardfs_ha_cluster` – along with 'best practices'.

   Having a third node also ensures there is always a 'master' server available for when the XenServer nodes boot. It is often common to need things like DNS, and 'routing' for XenServer to come up any way – so whilst you can build a 2 node system – 3 nodes is almost certainly better (even if one is not a XenServer – and just a basic machine providing DNS, LizardFS meta-server etc.)

   Additionally – the third node can be used to provide a small amount of NFS storage. By creating a XenServer Storage Repository using this NFS space – XenServer's HA (High Availability) mode can be enabled.

.. warning:: XenServer patches / updates may replace the modifications to the "FileSR.py" file – so remember to check this after installing updates.

             Usually in a XenServer 'pool' situation you would update the master first (make sure that restarts OK – including the LizardFS side of things) – then update the other nodes in turn.


.. _virtu_farms:

Using LizardFS for Virtualization Farms
=========================================

If you want to use LizardFS as a back end for your virtualization Farm, there
are multiple options.

Use LizardFS from inside each VM
  The LizardFS client on Linux utilizes the :ref:`fuse` library which has
  limits on the performance it can offer. To work around this one option would
  be to have each VM connect to the lizardfs system by itself. That way each
  VM has its own connection and gets the maximum performance possible via fuse.


Create one mount point on your host for each VM (especially cool with KVM)
  This is simple and efficient. Since the :ref:`fuse` library creates a new
  instance for every mount point, each mount point gets the full performance of
  a :ref:`fuse` connection and that way gets around the limits a single fuse
  connection currently has. So basically each VM, using a separate LizardFS
  mount point each, will get full throughput until the host runs out of network
  resources.

  The setup is rather simple. Create multiple subdirectories in your LizardFS
  and mount each one separately for each VM::

    mfsmount -S <lizardfs subdirectory> -c <mfsmount config file>

  Each mount will have its own instance and create its own :ref:`fuse` process
  working like a totally separate connection and process. This is a workaround
  for the know limitations of the :ref:`fuse` library.

.. _vmware_network:

Best Practice for VMWare Networking
===================================

Currently only NFS is supported for connections from VMWare ESX Hosts.

.. _proxmox:

Using LizardFS as shared storage for ProxmoxVE
==============================================

Requirements::

  Proxmox >= 4
  LizardFS >= 3.10.6

.. note:: This guide assumes you are familiar with Proxmox and the Linux command
          line and can mount / unmount and work with file systems on a standard
          Debian stretch platform.

Using LizardFS as shared storage with Proxmox is pretty straightforward. There
are a couple of models in which you can do this.

ProxmoxVE nodes as LizardFS clients
-----------------------------------

This one is rather easy. Either add the Lizardfs.com repositories or use the
official lizardFS packages from the Debian project and install the
lizardfs-client package.

Now create multiple shared directories on each node, as described
in :ref:`virtu_farms`. Than goto datacenter=>storage in your Proxmox GUI and
select **add**. Select directory and in the pop up select one of the
directories you just mounted. Mark the box for **shared** and your done.
Perform the same for each mount point and than go ahead and place your
containers and VM's inside.

You can also use those shared directories for your templates and backups to
have them accessible in parallel from all the nodes.

ProxmoxVE nodes as chunkservers and LizardFS clients
----------------------------------------------------

This is what we use for functional testing, development and some even for their private lizard setups.
It is pretty simple.

Just use lxc containers as chunk servers and masters. Nothing much to it. Standard setup like any other lizardFS server.


Using ProxmoxVE to manage a combined node with chunkservers in lxc containers
-----------------------------------------------------------------------------

This will have to wait until someone will write a proxmox gui module for lizardfs :)

.. TODO:: write the cobined proxmox article

.. seealso:: https://www.proxmox.com/
