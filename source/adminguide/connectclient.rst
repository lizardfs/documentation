.. _connectclient:

************************************************
Connecting Clients to your LizardFS installation
************************************************
.. auth-status-proof1/none

The most exciting part of this tutorial - you will finally be able to store
files on your installation!

Linux / \*NIX / \*BSD / MacOS/X client
======================================

Install the client package

   Check :ref:`get_and_install` for instructions how to install package

Example for Debian/Ubuntu::

   $ apt-get install lizardfs-client

Make sure that the mfsmaster host is set in your /etc/hosts file. For our
example configuration it would be::

   192.168.16.100 mfsmaster

Create a mountpoint::

   $ mkdir /mnt/lizardfs

Mount the filesystem to the mountpoint with just the default options from
mfsmount.cfg if any::

   $ mfsmount /mnt/lizardfs

That's it.

On most systems adding big_writes to the options will significantly increase
your throughput since it will force the fuse libraray to use writes > 4k.
Example::

  $ mfsmount -o big_writes,nosuid,nodev,noatime /mnt/lizardfs

will mount with fuse option: big_writes and default system mount options:
nosuid, nodev and noatime.

You can now store your files on your brand new installation.
See man *mfsmount* or *mfsmount -h* for more advanced mount options.
See :ref:`mfsmount.1` and :ref:`mfsmount.cfg.5` manpage for more options


Windows™ client
===============

Install our client from exe package provided

Add your credentials and the address and port of the master server.

Select the drive you want your lizardFS filesystem to appear as in your
windows session.

It should look like in the following image:


.. image:: ../images/lizardwinclient.png
   :align: center
   :alt: Figure 2: main view of LizardFS Windows™ client

Figure 2: main view of LizardFS Windows™ client


Figure 3: My Computer view after mounting LizardFS client


