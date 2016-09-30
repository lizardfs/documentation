.. _cookbook_linux:

***********************
LizardFS linux CookBook
***********************
.. auth-status-proof1/none


.. _directio:

Setting DirectIO for your setup
===============================

.. warning: This is totally unsupported and may result in data loss and
           breaking your LizardFS cluster.

In some cases we have experienced that the caching mechanism in some systems
may slow down performance significantly. What has helped is switching the
caching off and moving to Direct IO which ommits the OS cache and writes
directly to the block device underneath.

To enable DirectIO on your installation, you need to update the
*.lizardfs_tweaks* file in the root of your mounted LizardFS. This is done by
issuing the following on a mounted filesystem::

  echo "DirectIO=true" > .lizardfs_tweaks

You can verify if the setting has changed to true by issuing the following
command::

  cat .lizardfs_tweaks | grep DirectIO

If you find that this does not improve your performance or in fact, slows it
down, you can always change it back by running::

  echo "DirectIO=false" > .lizardfs_tweaks

The changes are effective immediately.


.. _virtu_farms:

Using LizardFS for Virtualization Farms
=========================================

If you want to use LizardFS as a Backend for your virtualization Farm, there
are multiple options.

Use LizardFS from inside each VM
  The LizardFS client on Linux utilises the :ref:`fuse`libraray which has
  limits on the performance it can offer. To work around this one option would
  be to have each VM connect to the lizardfs system by itself. That way each
  VM has its own connection and gets the maximum performance possible via fuse.


Create one mountpoint on your host for each VM (especially cool with KVM)
  This is simple and efficient. Since the :ref:`fuse` library creates a new
  instance for every mountpoint, each mountpoint gets the full performance of
  a :ref:`fuse` connection and that way gets around the limits a single fuse
  connection currently has. So basically each VM, using a separate lizardfs
  mountpoint each, will get full throughput until the host runs out of network
  ressources.

  The setup is rather simple. Create multiple subdirectories in your lizardfs
  and mount each one separately for each VM::

    mfsmount -S <lizardfs subdirectory> -c <mfsmount config file>

  Each mount will have its own instance and create its own :ref:`fuse` process
  working like a totaly separate connection and process. This is a workaround
  for the know limitations of the :ref:`fuse` library.


.. _uraft_cookbook:

URAFT Cookbook
==============

The HA system utilised by LizardFS to keep your master servers always alive is
called uraft. It has been developed by Sky Technology Sp. z o.o. and is based
on the :ref:`raft` algorithm developed by Diego Ongaro and John Ousterhout.

HA with only 2 masters
----------------------

.. warning:: This is unsupported and only recommended if setup by certified engineering personel.

Since it is a :ref:`quorum` based algorithm we usualy recommend to users to
have 1 master and 2 shadow nodes. But there is a way to run your HA with one
master, one shadow and a raft only addon on one of your chunkservers. This
stub will still run a master server daemon but it will never switch it to
active so it can be running anything.

All that is required to switch a node to "non master" mode is setting::

  URAFT_ELECTOR_MODE = 1

in the *lizardfs-uraft.cfg* file. Everything else must be setup like it would
be a normale lizardfs-master with uraft node except that the master will never
be put into a real **master* role.



.. _zol:

ZFS on Linux
============

:ref:`zfs` is a high performance 128 bit filesystem developed by SUN
Microsystems. We wil show you here the basics how to install it on Linux. For specifics how to finetune, optimize and manage zfs, please consult the links in the seealso part at the end of the ZFS articles. On Linux we use the Open-ZFS way and do not use FUSE to get maximum performance.

Installing ZFS on RHEL/Centos 7
===============================

To aoid all the licensing discussions (we do not get into that but you can
read up on it <here https://www.softwarefreedom.org/resources/2016/
linux-kernel-cddl.html>_ if you like) the Open-ZFS project has a way where you
while installing the driver compile it yourself and that way get around all
the license discussions for binary modules it seems. So here we go:

You will require to add the epel repository to your system::

  $ yum install epel-release
  $ yum update

And than the open-zfs project repository::

  $ yum localinstall -y --nogpgcheck http://archive.zfsonlinux.org/epel/zfs-release.el7.noarch.rpm

after which you can install the sources required and automativaly build the
required modules on your system::

  yum install -y kernel-devel zfs

Test if your installation worked::

  modprobe zfs
  lsmod | zfs

Test if you can use the zfs commands::

  zfs list
  zpool list

Now you can install zpools and flesystems with ZFS.

.. seealso::

   * `A guide to install and use zfs on centos 7 <`http://linoxide.com/tools/guide-install-use-zfs-centos-7/">`_

   * `The Open-ZFS Project <http://www.open-zfs.org/>`_

   * `ZFS Manual in the FreeBSD Handbook <https://www.freebsd.org/doc/handbook/zfs.html>`_

   * The `ZFS On Linux - ZOL <http://zfsonlinux.org/>`_ project supplies
     packages and documentation for every major distro:
     `ZFS On Linux - ZOL <http://zfsonlinux.org/>`_

   * `ZFS in the Ubuntu Wiki <https://wiki.ubuntuusers.de/ZFS_on_Linux/>`_

   * `How to install and use ZFS on Ubuntu and why you'd wnat to <http://www.howtogeek.com/272220/how-to-install-and-use-zfs-on-ubuntu-and-why-youd-want-to/>`_

   * `An extensive Guide about ZFS on Debian by Aaron Toponce <https://pthree.org/2012/04/17/install-zfs-on-debian-gnulinux/>`_

   * `Performance tuning instructions from the Open-ZFS Project <http://open-zfs.org/wiki/Performance_tuning>`_







