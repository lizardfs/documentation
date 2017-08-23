.. _cookbook_linux:

***********************
LizardFS linux CookBook
***********************
.. auth-status-proof1/none

.. _linux_network_tuning

Basic network adjustments for Linux
-----------------------------------

By default Linux systems come with relatively small window sizes for TCP and
UDP frames which could lead to fragmentation and lowered performance.
Especially if your servers use 10G or faster interfaces we would recommend to
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


.. _directio:

Setting DirectIO for your setup
===============================

.. warning: This is totally unsupported and may result in data loss and
           breaking your LizardFS cluster.

In some cases we have experienced that the caching mechanism in some systems
may slow down performance significantly. What has helped is switching the
caching off and moving to Direct IO which omits the OS cache and writes
directly to the block device underneath.

To enable DirectIO on your installation, you need to update the
*.lizardfs_tweaks* file in the root of your mounted LizardFS. This is done by
issuing the following on a mounted file system::

  echo "DirectIO=true" > .lizardfs_tweaks

You can verify if the setting has changed to true by issuing the following
command::

  cat .lizardfs_tweaks | grep DirectIO

If you find that this does not improve your performance or in fact, slows it
down, you can always change it back by running::

  echo "DirectIO=false" > .lizardfs_tweaks

The changes are effective immediately.

.. _uraft_cookbook:

URAFT Cookbook
==============

The HA system utilized by LizardFS to keep your master servers always alive is
called uraft. It has been developed by Sky Technologies Sp. z o.o. and is based
on the :ref:`raft` algorithm developed by Diego Ongaro and John Ousterhout.

HA with only 2 masters
----------------------

.. warning:: This is unsupported and only recommended if setup by certified engineering personnel.

Since it is a :ref:`quorum` based algorithm we usually recommend to users to
have 1 master and 2 shadow nodes. But there is a way to run your HA with one
master, one shadow and a raft only add-on on one of your chunkservers. This
stub will still run a master server daemon but it will never switch it to
active so it can be running anything.

All that is required to switch a node to "non master" mode is setting::

  URAFT_ELECTOR_MODE = 1

in the lizardfs-uraft.cfg file. Everything else must be setup like it would
be a normal lizardfs-master with uraft node except that the master will never
be put into a real **master** role.



.. _zol:

ZFS on Linux
============

:ref:`zfs` is a high performance 128 bit file system developed by SUN
Microsystems. We will show you here the basics how to install it on Linux. For
specifics how to fine tune, optimize and manage zfs, please consult the links
in the "see also" part at the end of the ZFS articles. On Linux we use the
Open-ZFS way and do not use FUSE to get maximum performance.

Installing ZFS on RHEL/Centos 7
===============================

To avoid all the licensing discussions (we do not get into that but you can
read up on it <here https://www.softwarefreedom.org/resources/2016/
linux-kernel-cddl.html>_ if you like) the Open-ZFS project has a way where you
while installing the driver compile it yourself and that way get around all
the license discussions for binary modules it seems. So here we go:

You will require to add the epel repository to your system::

  $ yum install epel-release
  $ yum update

And than the open-zfs project repository::

  $ yum localinstall -y --nogpgcheck http://archive.zfsonlinux.org/epel/zfs-release.el7.noarch.rpm

after which you can install the sources required and automatically build the
required modules on your system::

  yum install -y kernel-devel zfs

Test if your installation worked::

  modprobe zfs
  lsmod | zfs

Test if you can use the zfs commands::

  zfs list
  zpool list

Now you can install zpools and file systems with ZFS.

.. seealso::

   * `A guide to install and use zfs on centos 7 <`http://linoxide.com/tools/guide-install-use-zfs-centos-7/">`_

   * `The Open-ZFS Project <http://www.open-zfs.org/>`_

   * `ZFS Manual in the FreeBSD Handbook <https://www.freebsd.org/doc/handbook/zfs.html>`_

   * The `ZFS On Linux - ZOL <http://zfsonlinux.org/>`_ project supplies
     packages and documentation for every major distro:
     `ZFS On Linux - ZOL <http://zfsonlinux.org/>`_

   * `ZFS in the Ubuntu Wiki <https://wiki.ubuntuusers.de/ZFS_on_Linux/>`_

   * `How to install and use ZFS on Ubuntu and why you'd want to <http://www.howtogeek.com/272220/how-to-install-and-use-zfs-on-ubuntu-and-why-youd-want-to/>`_

   * `An extensive Guide about ZFS on Debian by Aaron Toponce <https://pthree.org/2012/04/17/install-zfs-on-debian-gnulinux/>`_

   * `Performance tuning instructions from the Open-ZFS Project <http://open-zfs.org/wiki/Performance_tuning>`_







