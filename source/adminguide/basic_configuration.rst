.. _basic_config:

*******************
Basic Configuration
*******************
.. auth-status-proof1/none

Some basic rules first:

* The Master server works best on a dedicated machine, preferably with a SSD
  drive.
* The Chunk server works best with at least one dedicated disk.
* Do not put a metalogger on the same machine as the master server, it doesn't
  make your metadata any safer. Metaloggers are completely optional, though ;)
  It is fine, however, to install a metalogger along with a chunk server
* Increase your data safety by using shadow master servers

There are a range of settings that must be done on every server before we
start working on the LizardFS configuration itself.

* adjust network settings

* adjust kernel settings

Basic operating system settings for LizardFS
============================================

LizardFS runs on many UNIX and UNIX like operating systems. We will be
concentrating here on Debian and RH like systems to keep things simple. For
other OSes, please consult the :ref:`cookbook`.

The /etc/hosts file
-------------------

Since LizardFS is a network based Filesystem, your network setup is crucial,
especially the name resolution service which helps computers in the network
find each other. There are two basic ways that computers find each other by
name: static entries in the /etc/hosts file or the DNS System.

The DNS system provides a central database that resolves names to their
respective IP addresses. In many environments DNS is either automatic and
linked to other services (Active Directory, DHCP, etc ..) so that we strongly
recommend to use the /etc/hosts file to resolve between the LizardFS cluster
components. This will keep the cluster from loosing Data in case somebody
changes something in the DNS service. It involves some additional work from
the Administrator responsible for the LizardFS cluster to keep the files up
to date, but will safeguard you from storage failure and data loss in case
something happens to the DNS system.

The /etc/hosts file has not changed in the last 5 decades and is basically the
same on all operating systems. it's structure is::

  <ip-address>   <hostname> <alias>

one line per IP address.

Example::

  127.0.0.1        localhost
  192.168.16.100   mfsmaster
  192.168.16.101   shadowmaster
  192.168.16.10    chunkserver1 metalogger
  192.168.16.11    chunkserver2 cgiserver
  192.168.16.12    chunkserver3

In this example your Master is on 192.168.16.100 and your Shadow Master on
192.168.16.101. Chunkserver1 also provides the metalogger and is located at
192.168.16.10. Chunkserver2 also provides the cgi web interface and is located
at 192.168.16.11. Chunkserver3 is at 192.168.11.12.


.. note: The /etc/hosts file must be the same on all the LizardFS servers.


The ntpd time service
---------------------

.. todo: needs inclusion of article from Wolfram


Basic network adjustments for Linux
-----------------------------------

.. maybe this should go into the cookbook or into advanced config ??

By default Linux systems come with relatively small window sizes for tcp and
udp frames which could lead to fragmentation and lowered performance.
Especialy if your servers use 10G or faster interfaces we would recommend to
adjust your network settings by adding the following entries to your /etc/
sysctl.conf file or placing a new file called "lizardfs.conf" into the /etc/
sysconf.d/ directory containing the following entries::

  net.ipv4.tcp_window_scaling = 1

  net.core.rmem_max=1677721600
  net.core.rmem_default=167772160
  net.core.wmem_max=1677721600
  net.core.wmem_default=167772160
  net.core.optmem_max= 2048000

  # set minimum size, initial size, and maximum size in bytes
  net.ipv4.tcp_rmem= 1024000 8738000 1677721600
  net.ipv4.tcp_wmem= 1024000 8738000 1677721600
  net.ipv4.tcp_mem= 1024000 8738000 1677721600
  net.ipv4.udp_mem= 1024000 8738000 1677721600
  net.core.netdev_max_backlog = 30000
  net.ipv4.tcp_no_metrics_save = 1

These values are taken from a 10G setup, you probably need to adjust them if
you have lower or faster networking interfaces.

File systems for LizardFS servers
=================================

.. note:: Due to its speed and stability we recommend the XFS or ZFS
          filesystems on production servers. XFS was developed for Silicon
          Graphics, and is a mature and stable filesystem. ZFS was developed
          by SUN Microsystems and is used for heavy duty storage by Systems
          from numerous Storage System Vendors.

For the Master servers
----------------------

The Master keeps all of his records in memory but does frequent backups to
drives which should therefore be very fast, but do not have to be very large.
A standard 250G SSD should suffice. As a file system we would recommend
something fast, like XFS. Do not use a HW RAID controller to mirror your
drives, SSDs usualy have identical lifespan so block level mirroring would
just lead to two dead SSDs instead of one. An alternative would be ZFS
mirroring which is not lowlevel but data based and does not always write the
same block to both devices to the same position.


For the chunkservers
--------------------

If you are using XFS as the filesystem for the chunkserver directories, we
recommend the following mount options::

  rw,noexec,nodev,noatime,nodiratime,largeio,inode64,barrier=0

This disables unneeded features from the mount which gives a slight
performance increase especially in case of many chunks. It also increases the
size of the directories gives lizardfs more space in to put its data.

Depending on the hardware you use and ifyou are utilising caching RAID
controllers, it could make sense to adjust the scheduler on your filesystems.
How you do a that is documented here:

http://www.cyberciti.biz/faq/linux-change-io-scheduler-for-harddisk/

Probably you will want the `deadline` scheduler but your mileage may vary.

Why you should do that and what performance gains you may achieve can be found
here:

http://xfs.org/index.php/XFS_FAQ

If you would like to use the high performance ZFS filesystem, please check the
:ref:`cookbook` for further information.

.. _master_server_config:

Configuring your Master
=======================

The master server is the heart of the LizardFS ecosystem. It keeps all meta
information about every file, every chunk and every slice if in ec mode. It
knows what is where and how to find it. It is also resposible to organize
georeplication and topology and fix the effects of broken drives and
chunkservers.

The metadata database
---------------------

For the master to work, you need to first give it a file where it will keep
its metadata database. The default location, which can be adjusted in the
:ref:`mfsmaster.cfg.5` file, is::

  /var/lib/mfs/metadata.mfs

There is an empty metdata file available which you can use to create a new
one. If you want to use the default location, just issue a::

  $ cp /var/lib/mfs/metadata.mfs.empty /var/lib/mfs/metadata.mfs

to copy the empty template into the default location and create a new database.

Now that you have a metadata database, you need to provide your master server
with the required information for operation.

The mfsmaster.cfg file
----------------------

In the mfsmaster.cfg file, there are a lot of settings for advanced usage
which we will get into in the :ref:`advanced_config` Guide. For a basic setup
the things that are important are:

  Current *personality* of this instance of the metadata server. Valid values
  are *master*, *shadow* and *ha-cluster-managed*. If the installation is
  managed by an HA cluster the only valid value is *ha-cluster-managed*,
  otherwise the only valid values are *master* and *shadow*, in which case
  only one metadata server in LizardFS shall have *master* personality. ::

    PERSONALITY = master

  means that this instance of metadata server acts as main metadata server
  govering all file system metadata modifications. ::

    PERSONALITY = shadow

  means that this instance of the metadata server acts as backup metadata
  server  ready for immediate deployment as the new *master* in case of a
  failure of the current *master*.

  Metadata server personality can be changed at any moment as long as one
  changes personality from *shadow* to *master*, changing personality the
  other way around is forbidden. ::

    PERSONALITY = ha-cluster-managed

  means that this instance is managed by a HA cluster, server runs in
  *shadow*  mode as long as its not remotly promoted to *master*. For details
  on running LizardFS with HA Master please refer to :ref:`lizardfs_ha_cluster`
  .

The addresses your master server is to listen on, if not all::

  ATOML_LISTEN_HOST # IP address to listen on for metalogger connections (* means any)
  MATOCS_LISTEN_HOST # IP address to listen on for chunkserver connections (* means any)
  MATOTS_LISTEN_HOST # IP address to listen on for tapeserver connections (* means any)
  MATOCL_LISTEN_HOST # IP address to listen on for client (mount) connections (* means any)

The ports your master server is supposed to listen on, if not the default ones::

  MATOML_LISTEN_PORT # port to listen on for metalogger connections (default is 9419)
  MATOCS_LISTEN_PORT # port to listen on for chunkserver connections (default is 9420)
  MATOCL_LISTEN_PORT # port to listen on for client (mount) connections (default is 9421)
  MATOTS_LISTEN_PORT # Port to listen on for tapeserver connections (default is 9424)

The user and group you would like your master to run as (default is *mfs*)::

  WORKING_USER # user to run daemon as
  WORKING_GROUP # group to run daemon as (optional - if empty then the default user group will be used)

Where to store metadata and lock files::

  DATA_PATH # where to store metadata files and lock file

Should the access time for every file be recorded or not ? ::

  NO_ATIME
  # when this option is set to 1 inode access time is not updated on every #
  # access, otherwise (when set to 0) it is updated (default is 0)

All other settings should be left alone for a basic system.

Layout, access rights and other options
---------------------------------------

Now that we have the main configuration done, lets configure the layout of our
LizardFS. This is done in the :ref:`mfsexports.cfg.5` file, unless you specify
a different file in your :ref:`mfsmaster.cfg.5` file.

.. note:: LizardFS creates one big namespace. For fine tuned access you should
          create entries here for subdirectories and assign those to groups to
          have different clients access only different parts of the tree.

This file contains all the settings required to create a LizardFS namespace
and set its access rights and network permissions. Its format is pretty
simple::

  ADDRESS DIRECTORY [OPTIONS]

Basically you define which network address or address range has access to
which directory plus options for that access.

The address scheme looks like the following:

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

Your LizardFS namespace is a tree, starting with the root entry **/**.
So in the directory field you can specify the whole namespace, **/**, or
subdirectories like: **/home** or **/vm1**. The special value **.** represents
the meta file system, which is described in :ref:`mount_meta` .
You can specify different access rights, options, passwords and user mappings
for every single directory and split your namespace utlising those options
into multiple sub namespaces if required. Check out the examples for how
different directories can be set to different options.

Options
^^^^^^^

To give you maximum flexibility LizardFS provides a range of mount options so you can finetune settings for every piece of your namespace.

None of them are required. If you do not provide any options, the default set
of::

  ro,maproot=999:999

will be used.

The options are:

**ro, readonly**
  export tree in read-only mode (default)

**rw, readwrite**
  export tree in read-write mode

**ignoregid**
  disable testing of group access at *mfsmaster* level (it's still done at
  *mfsmount* level) - in this case "group" and "other" permissions are
  logically added; needed for supplementary groups to work.
  (*mfsmaster* only receives information about the users primary group)

**dynamicip**
  allows reconnecting of already authenticated client from any IP address (the
  default is to check the IP address on reconnect)

**maproot=USER[:GROUP]**
  maps root (uid=0) accesses to the given user and group (similarly to maproot
  option in NFS mounts);
  USER and GROUP can be given either as name or number; if no group is
  specified, USERs primary group is used. Names are resolved on *mfsmaster*
  side (see note below).

**mapall=USER[:GROUP]**
  like above but maps all non privileged users (uid!=0) accesses to a given
  user and group (see notes below).

**minversion=VER**
  rejects access from clients older than specified

**mingoal=N, maxgoal=N**
  specifies range in which goal can be set by users

**mintrashtime=TDUR, *maxtrashtime=TDUR**
  specifies range in which trashtime can be set by users. See :ref:`meta_trash`

**password=PASS, md5pass=MD5**
  requires password authentication in order to access specified resource

**alldirs**
  allows to mount any subdirectory of the specified directory (similarly to
  NFS)

**nonrootmeta**
  allows non-root users to use filesystem mounted in the meta mode (option
  available only in this mode). See :ref:`mount_meta` .


Examples
^^^^^^^^

::

  *                    /       ro
  # Give everybody access to the whole namespace but read-only. Subdirs can
  # not be mounted directly and must be accessed from /.

  192.168.1.0/24       /       rw
  # Allow 192.168.1.1 - 192.168.1.254 to access the whole namespace read/write.

  192.168.1.0/24       /       rw,alldirs,maproot=0,password=passcode
  # Allow 192.168.1.1 - 192.168.1.254 to access the whole namespace read/write
  # with the password *passcode* and map the root user to the UID *0*.

  10.0.0.0-10.0.0.5    /test   rw,maproot=nobody,password=test
  # Allow 10.0.0.0 - 10.0.0.5 to access the directory /test except for its
  # subdirectores in a read/write fashion using the password *test*. Map all
  # accesses by the root user to the user *nobody*.

  10.1.0.0/255.255.0.0 /public rw,mapall=1000:1000
  # Give access to the /public directory to the network 10.1.0.0/255.255.0.0
  # in a read/write fashion and map everybody to the UID *1000* and GID *1000*.

  10.2.0.0/16          /      rw,alldirs,maproot=0,mintrashtime=2h30m,maxtrashtime=2w
  # Give access to the whole namespae to the 10.2.0.0/16 network in a
  # read/write fashion. Also allowsubdirectories to be mounted directly by
  # those clients.
  # Map the root user to UID *0*. Allow users to set the trahtime (time when
  # files in the tash get autopruned) between
  # 2h30m and 2 weeks.

Utilising all of these options you will be able to do quite flexible setups,
like optimizing for virtualization as described in out Cookbook at
:ref:`virtu_farms` .

Now that you know how to setup your namespace, the next step would be to set
custom goals/replication modes, described in :ref:`replication` and QoS/IO
Limits, described in the :ref:`lizardfs_qos` chapter.

Network awareness / topology are further advanced topics, especialy required
for georeplication. A description of how to set them up can be found here
:ref:`rack_awareness` .


.. _shadow_server_config:

Configuring your Shadowmaster
=============================

Your shadowmaster is configured in nearly the same way as your Master. Since
it is supposed to take over the functionality of the Master in case of a
failure of the Master, it has to keep its metadatabase in sync and besides that have all the configurations of the masterserver mirrored.

Settings specific to the Shadowmaster:

In the mfsmaster.cfg file::

  # Set the personality to be that of a Shadowmaster:
  PERSONALITY = shadow

  # Set the address where the metadatabase is synced from:
  MASTER_HOST = 10.0.10.230

The files mfsexports.cfg, mfsgoals.cfg and mfstopology.cfg must be
synchronized with the master server.


.. _chunk_server_config:

Configuring your Chunkservers
=============================

Your chunkservers are pretty simple to set up.
Usualy, if your /etc/hosts files are setup correctly with the address of the master server and you do not require labeling (:ref:`labeling_chunkserver`), the mfschunkserver.cfg file can stay as it is. If you require to lock down the masterserver address, adjust the following line::

  MASTER_HOST = 10.0.10.230

to lock down the master server to the 10.0.10.230 address.

Now you need to specify where the chunkserver process will keep the actual data. This is done in the mfshdd.cfg file. You specify directories with their full path, one per line.

Example::

  # use directory '/mnt/hd1' with default options:
  /mnt/hd1

  # use directory '/mnt/hd2', but replicate all data from it:
  */mnt/hd2

  # use directory '/mnt/hd3', but try to leave 5GiB on it:
  /mnt/hd3 -5GiB

  # use directory '/mnt/hd4', but use only 1.5TiB on it:
  /mnt/hd4 1.5TiB

The settings always assume that the directory is a dedicated device, so a HDD,
a Raidset or a SSD and bases it's space calculation on that.

Once this is setup, your chunkserver is ready and actively taking part in your
lizardfs.

To remove a directory from being used by lizardfs, just add a *\** to the beginning of the line in mfshdd.cfg::

  # use directory '/mnt/hd2', but replicate all data from it:
  */mnt/hd2

Lizardfs will replicate all the data from it somewhere else. Once you see in
the webinterface that all data has been safely copied away, you can update the
file and remove the line and than remove the device associated with it from
your chunkserver.

Configuring the Metalogger
==========================

The metalogger is used for desaster recovery should the master and
shadowservers fail. The metadatabase can be rebuild from them. The setup is
straightforward. You basically do not need to setup anything if your
/etc/hosts is setup accordingly, otherwise you need to set the following in your mfsmetalogger.cfg file::

  MASTER_HOST
  # address of LizardFS master host to connect with (default is mfsmaster)

  MASTER_PORT
  # number of LizardFS master port to connect with (default is 9419)

and you are ready to go.

Configuring the Web Interface
=============================

The lizardfs cgiserver does not require much configuration. After the
installation either follow the example installation and just add an entry for
*mfsmaster* to your /etc/hosts file, or,  ...

.. todo: how do we change the place this looks for the master server ? Any
         config possible ?

.. _labeling_chunkserver:

Labeling your chunkserver
=========================

To be able to setup which goals are going to be performed on which
chunkservers, you need to be able to identify them in your goal definition.
To achieve this, we use labels.

The label for the Chunkservers is set in the mfschunkserver.cfg file. ::

   LABEL = ssd

After changing the configuration you must reload the chunkserver::

   $ mfschunkserver -c path/to/config reload

If there is no LABEL entry in the config, the chunkserver has a default label
of “_” (i.e. wildcard), which has a special meaning when defining goals and
means “any chunkserver”.

Multiple chunkservers can have the same label than they are basically a group
of chunkservers where you can use the label to write a chunk or a piece of XOR
or EC set to "any" chunkserver in that group.

Show labels of connected chunkservers
-------------------------------------

From the command line::

   $ lizardfs-admin list-chunkservers <master ip> <master port>

Via the cgi (webinterface):

In the ‘Servers’ tab in the table ‘Chunk Servers’ there is a column ‘label’
where labels of the chunkservers are displayed.

