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

See the :ref:`mfsmount.1` and :ref:`mfsmount.cfg.5` manpage for more options

See :ref:`fuse` to find out more about the fuse library.


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

Windows™ service
================

The Windows™ Client can also be run as a Windows™ Service. This is provided by
the **LizardSControler** command.

Basic configuration
-------------------

Minimal configuration::

  LizardSControler -p -lic-file <LICENSE_FILE> -H <ADDRESS_OF_MASTER>

where LICENSE_FILE should be the name of the file containing a valid License
and ADDRESS_OF_MASTER should be the hostname or IP address of the LizardFS
master server.

Further configuration options
-----------------------------

(Must follow the -p command)

======================= =======================================================
Command                 Description
======================= =======================================================
-H HOST                 set master server host address.
-P PORT                 set master server port. Default 9421.
-D DRIVE                set <DRIVE> as a mount point i.e. \D:\. Default L:
-f SUBFOLDER            mount only given LizardFS subfolder
-uid UID                set new UID. Default is 1000.
-gid GID                set new GID. Default is 1000.
-umask UMASK            set new UMASK. Default is 000.
-pass PASS              authenticate to LizardFS master using MD5 password.
-lic LICENSE            set new LICENSE.
-lic-file LICENSE_FILE  load new LICENSE from LICENSE_FILE.
======================= =======================================================

Installation and runtime
------------------------

After you have done the configration, you can add the service to your Windows
system by running::

  LizardSControler -i

and start it by running::

  LizardSControler -s

If you would like to uninstall the service again, just run::

  LizardSControler -u

A full list of options can be displayed using::

  LizardSControler -help




