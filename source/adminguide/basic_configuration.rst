Basic Configuration
*******************

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

* setup all participating hosts in the /etc/hosts file

* setup time synchronization via ntp

* select the filesystem type and create the filesystems the chunkservers shall
  use

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

  127.0.0.1	       localhost
  192.168.16.100   mfsmaster
  192.168.16.101   shadowmaster
  192.168.16.10    chunkserver1 metalogger
  192.168.16.11    chunkserver2 cgiserver
  192.168.16.12    chunkserver3

In this example your Master is on 192.168.16.100 and your Shadow Master on
192.168.16.101. Chunkserver1 also provides the metalogger and is located at
192.168.16.10. Chunkserver2 also provides the cgi web interface and is located
at 192.168.16.11. Chunkserver3 is at 192.168.11.12.


The file must be the same on all the LizardFS servers.




The ntpd time service
---------------------



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

Probably you will want the `deadline`scheduler but your mileage may vary.

Why you should do that and what performance gains you may achieve can be found
here:

http://xfs.org/index.php/XFS_FAQ

If you would like to use the high performance ZFS filesystem, please check the
:ref:`cookbook`for further information.


Configuring your Master
=======================


Configuring your Shadowmaster
=============================


Configuring your Chunkservers
=============================


Configuring the Metalogger
==========================


Configuring the Web Interface
=============================


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

Show labels of connected chunkservers
-------------------------------------

From the command line::

   $ lizardfs-admin list-chunkservers <master ip> <master port>

Via the cgi (webinterface):

In the ‘Servers’ tab in the table ‘Chunk Servers’ there is a column ‘label’
where labels of the chunkservers are displayed.




