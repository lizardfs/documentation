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

* Basic NFS Services
* pNFS Services

Our implementation supports all features ganesha provides and is able to handle
classic goal replocation setups as well es erasure coding setups in the back.

The config part of our manual only handles the configuration of the LizardFS
FSAL plus some basic ganesha configuration. A full documentation describing
all configuration options and advaced setups is available at:

* https://github.com/nfs-ganesha/nfs-ganesha/wiki/Configurationfile

Installing LizardFS-NFS-Ganesha on CentOS/RHEL 7
------------------------------------------------

If you use a minimal or a  container isntall of redhat or centos 7,
please install an openssh-server first so you can work remotely::

  # yum install openssh-server
  # systemctl enable sshd
  # systemctl start sshd

install man, vim and tmux to have sysadmin tools and help ready::

  # yum install man vim

Install the epel repository for some basic back ports that will be required,
like python3.4 and some others::

  # yum -y install epel-release
  # yum -y update
  # yum -y upgrade

Now install the required dependencies first::

  # yum install python34

Now go to the directory you downloaded our packages to and install::

  # yum -y install ./libntirpc-1.5.3-1.el7.centos.x86_64.rpm
  # yum -y install ./libtirpc-1.0.2-0.el7.centos.x86_64.rpm ./nfs-utils-2.1.1-5.rc5.el7.centos.x86_64.rpm ./rpcbind-0.2.4-7.rc2.el7.centos.x86_64.rpm ./gssproxy-0.7.0-9.el7.centos.x86_64.rpm

It is important that the second command is one line becuase the packages depend on each other.
Now install the nfs-ganesha packages we provide::

  # yum -y install nfs-ganesha-2.5.1.1-1.el7.centos.x86_64.rpm
  # yum -y install nfs-ganesha-vfs-2.5.1.1-1.el7.centos.x86_64.rpm

And finally the packages from our addon::

  # yum -y install lizardfs-lib-client-3.12.0-0el7.x86_64.rpm
  # yum -y install lizardfs-nfs-ganesha-3.12.0-0el7.x86_64.rpm

On the master also install the uraft for NFS package::

  # yum -y install lizardfs-nfs-uraft-3.9.3-0el7.x86_64.rpm

If you require the services of autofs, install our back ported autofs as well::

  # yum -y install autofs-5.1.2-2.el7.centos.x86_64.rpm

On the Ganesha Metadataserver which can but do not have to be installed on the
lizardfs masters ( they can also be running on separate boxes, just need to
connect to the masters via IP) you will need to run::

  # yum -y install lizardfs-nfs-uraft-3.9.3-0el7.x86_64.rpm

to install the HA uraft system for NFS.


ganecha.conf example file
-------------------------

This is an example of a combined metadata and data node. A node with this
configuration has to be on a chunkserver and will connect to a masterserver at

::

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

      # Exporting FSAL
      FSAL {
          Name = LizardFS;
          hostname = "192.168.99.100";
          port = "9421";
          io_retries = 5;
          cache_expiration_time_ms = 2500;
      }

      # Which NFS protocols to provide
      Protocols = 3, 4;
  }

  LizardFS {
      # Is this a NFS metadataserver ?
      PNFS_MDS = true;
      # Is this a NFS dataserver ?
      PNFS_DS = true;
  }

  NFSV4 {
      Grace_Period = 5;
  }



Options for the LizardFS FSAL part of the ganesha.conf file
-----------------------------------------------------------

+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| Option                           | min | max     | default     |                                                               |
+==================================+=====+=========+=============+===============================================================+
| name                             |     |         | LizardFS    | Name of the FSAL module. Must be LizardFS                     |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| hostname                         |     |         |             | Name or IP address of PNFS_MD node                            |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| port                             | 1   | 65535   | 9421        | Port the PNDS_MD node listens on                              |
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
| chunkserver_wave_read_timeout_ms | 0   | 65535   | 500         |                                                               |
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
| cache_per_inode_percentage       | 0   | 80      | 25          |                                                               |
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| symlink_cache_timeout_s          | 0   | 60000   | 3600        | How long to wait for a response from the symlink cache in sec.|
+----------------------------------+-----+---------+-------------+---------------------------------------------------------------+
| debug_mode                       |     |         | false       | Rin im debug mode and provide tons of aditional output        |
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

