.. _gateways:

************************************
LizardFS Gateways to other protocols
************************************

.. auth-status-todo/none

.. _ganesha_nfs:

Providing advanced NFS services via the NFS Ganesha plugin
==========================================================

NFS Ganesha is a widely known and used userspace NFS daemon. It is being used
in LizardFS to provide:

* Basic NFS v3 and v4 Services
* pNFS Services

Our implementation supports all features ganesha provides and is able to handle
classic goal replication setups as well es erasure coding setups in the back.

The config part of our manual only handles the configuration of the LizardFS
FSAL plus some basic ganesha configuration. A full documentation describing
all configuration options and advaced setups is available at:

* https://github.com/nfs-ganesha/nfs-ganesha/wiki/Configurationfile

Basic considerations for the setup
----------------------------------

You can set the ganesha node to be either a data node or a metadata node or both.
There is probably no big deal if a node is set to both but never used.

The main rule is, a data node **HAS** to be located on the same node as a
chunkserver. Thiings will break if this is not the case.

A metadata node can be standalone.

Installing LizardFS-NFS-Ganesha on CentOS/RHEL 7
------------------------------------------------

If you use a minimal or a  container install of redhat or centos 7,
please install an openssh-server first so you can work remotely::

  # yum install openssh-server
  # systemctl enable sshd
  # systemctl start sshd

Install the epel repository for some basic back ports that will be required,
like python3.4 and some others::

  # yum -y install epel-release
  # yum -y update
  # yum -y upgrade

install man, vim and tmux to have sysadmin tools and help ready::

  # yum install man vim tmux

Add the lizardfs centos dependencies repository by putting the following into the file
/etc/yun.conf.d/lizardfs-deps.repo::

  [lizardfs-deps]
  name=LizardFS Dependency Packages
  baseurl=http://packages.lizardfs.com/yum/el7-deps/
  enabled=1
  gpgcheck=0
  gpgkey=


Update your repository index::

  # yum update


Install the lizardfs ganesha dependencies and nfs ganesha (same for master and chunk server)::

   # yum install -y lizardfs-nfs-ganesha lizardfs-lib-client libntirpc nfs-ganesha

After configuring ganesha, add it to your system startup with::

  # systemctl enable nfs-ganesha


If you have a subscription install the uraft for NFS packae on the master too::

  # yum -y install lizardfs-nfs-uraft


ganesha.conf example file
-------------------------

This is an example of a combined metadata node configuration. The ganesha metadata node connects to the lizardfs master
server with the ip address 192.168.99.100::


  ###################################################
  #
  # EXPORT
  #
  # To function, all that is required is an EXPORT
  #
  # Define the absolute minimal export
  #
  ###################################################

  EXPORT
  {
      # Export Id (mandatory, each EXPORT must have a unique Export_Id)
      Export_Id = 77;

      # Exported path (mandatory)
      Path = "/";

      # Pseudo Path (required for NFS v4)
      Pseudo = "/";

      # Required for access (default is None)
      # Could use CLIENT blocks instead
      Access_Type = RW;
      Squash = None;
      Attr_Expiration_Time = 0;

      # Exporting FSAL
      FSAL {
          Name = LizardFS;
          # The address of the LizardFS Master Server or Floating IP
          hostname = "192.168.99.100";
          # The port to connect to on the Master Server
          port = "9421";
          # How often to retry to connect
          io_retries = 5;
          cache_expiration_time_ms = 2500;
      }

      # Which NFS protocols to provide
      Protocols = 3, 4;
  }

  LizardFS {
      # Is this a NFS metadataserver ?
      PNFS_MDS = true;
      # Is this a NFS dataserver and is it installed on an active chunkserver?
      PNFS_DS = false;
  }

  NFSV4 {
      Grace_Period = 5;
  }


The chunkservers for this installation would have the same configuration file, except that PNDS_MDS would be set to
false and PNFS_DS set to true. All other settings would be the same. That way you would have configured a ganesha data
node, using the local chunkserver and connecting to the lizardfs master server at 192.168.99.100.



Options for the LizardFS FSAL part of the ganesha.conf file
-----------------------------------------------------------

+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| Option                           | min | max     | default     |                                                               |
+==================================+=====+=========+=============+===============================================================+
| name                             |     |         | LizardFS    | Name of the FSAL module. Must be LizardFS                     |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| hostname                         |     |         |             | Name/IP of the LizardFS Master or Floating IP for uraft       |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| port                             | 1   | 65535   | 9421        | Port the master is listening on                               |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| mountpoint                       |     |         | nfs-ganesha | Name / Label shown in GUI for this instance of ganesha        |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| subfolder                        |     |         | /           | Subfolder of LizardFS namespace to be exported                |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| io_retries                       | 0   | 1024    | 30          | I/O retries connecting to LizardFS                            |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| chunkserver_round_time_ms        | 0   | 65536   | 200         |                                                               |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| chunkserver_connect_timeout_ms   | 0   | 65535   | 2000        | Time after which a chunkserver connection is defined dead     |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| chunkserver_wave_read_timeout_ms | 0   | 65535   | 500         | Timeout for executing each wave of a read operation           |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| cache_expiration_time_ms         | 0   | 65536   | 1000        | How long till chunks get thrown out of the cache              |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| readahead_max_window_size_kB     | 0   | 65535   | 16384       | Maximum Window size of the radahead cache                     |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| write_cache_size                 | 0   | 1024    | 64          | Maximum size of the write cache                               |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| write_workers                    | 0   | 32      | 10          | How many worker processes to start for processing writes      |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| write_window_size                | 0   | 256     | 32          | How large to set the window size for writes                   |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| chunkserver_write_timeout_ms     | 0   | 60000   | 5000        | How long to wait for the chunkserver to complete a write cycle|
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| cache_per_inode_percentage       | 0   | 80      | 25          | Max. percentage of write cache per single inode               |                                                   |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| symlink_cache_timeout_s          | 0   | 60000   | 3600        | How long to wait for a response from the symlink cache in sec.|
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| debug_mode                       |     |         | false       | Run im debug mode and provide tons of aditional output        |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| keep_cache                       | 0   | 2       | 0           |                                                               |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| acl_enabled                      |     |         | true        | Enable handling of ACLs                                       |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| fileinfo_cache_timeout           | 1   | 3600    | 60          | How long to wait for a response from the fileinfo cache       |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| fileinfo_cache_max_size          | 100 | 1000000 |             | Maximum size of the fileinfo cache                            |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+


The **name** value has to be set to **LizardFS** or nfs-ganesha will not choose
the LizardFS FSAL and will not be able to use LizardFS as a backend.



Providing HA to the NFS Ganesha Plugin
======================================

For commercial customers HA is provided by the uraft package. Installation and
basic setup should be done according to the instrauctions in
:ref:’lizardfs_ha_cluster’ .

You should take into account that you need one uraft per service, so if you want
your masters and your ganesha metadata nodes on the same boxes, you need to
install uraft once for the masters and once for the nfs metadata servers. In
such a setup it is vital to make sure that the two instances listen on
different ports and manage different ip addresses.

Assuming that your master server uraft seetup is setup according to the defaults
in the :ref:’lizardfs_ha_cluster’ chapter, we would suggest to use port 9527 and
9528 as port and status port in your uraft setup for NFS as follows:

URAFT_PORT = 9527
URAFT_STATUS_PORT: 9528

and make sure that you use a designated floating IP for your NFS services.

All other settings should be as described in :ref:’lizardfs_ha_cluster’ .



.. _TODO: add descriptions for undescribed FSAL options
