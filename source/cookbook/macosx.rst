.. _cookbook_macosx:

***********************
LizardFS MacOS Cookbook
***********************

.. auth-status-todo/none

.. _macos_automount:

Automounting a lizardFS volume
==============================

Since macOS is a bit restrictive starting with the ElCapitain version,
auto mounting LizardFS requires a bit of fiddling.

First you will need to disable Apple's SIP, also known as the "rootless"
feature. The rootless feature is aimed at preventing Mac OS X compromise by
malicious code, whether intentionally or accidentally, and essentially what
SIP does is lock down specific system level locations in the file system while
simultaneously preventing certain processes from attaching to system-level
processes.

SIP locks down the /System, /sbin and /usr (except for /usr/local/)
directories, but we need to add a script to /sbin, so we have to temporarily
disable SIP.

* Reboot the Mac and press the Command and R keys simultaneously after you
  hear the startup sound, this will boot OS X into Recovery Mode.

* When booted, pull down the *Utilities* menu at the top of the screen
  and choose *Terminal*.

* Type the following command into the terminal then hit return::

    csrutil disable; reboot

  You’ll see a message saying that System Integrity Protection has been
  disabled and the Mac needs to restart for changes to take effect, and the
  Mac will then reboot itself automatically, just let it boot up as normal.


Now check if SIP is disabled, type::

  csrutil status

It should give you the message::

  System Integrity Protection status: disabled.

Now you are ready to add the required script to /sbin. Use your favorite
editor and create the file **/sbin/mount_lizardfs** with the following
contents::

  #!/bin/bash
  /usr/local/bin/mfsmount $@ 2>>/dev/null
  sleep 3

Save the file. Now lets add the required things to your automounter.

In **/etc/auto_master** add the following line::

  /-      auto_lizardfs

Save the file and now create a file called **/etc/auto_liazrdfs** with the
following contents for the directory you want to mount::

  DIRECTORY -fstype=mfs,rw,big_writes,mfsmaster=IP_OF_MASTER,mfsport=PORT_THE_MASTER_LISTENS_ON " "

.. note:: Make sure to add an empty line to the end of the file.

example::

  /mnt/lizardfs -fstype=lizardfs,rw,big_writes,mfsmaster=192.168.66.112,mfsport=9421 " "

This will automount /mnt/lizardfs from master 192.168.66.112 port 9421

Reload the automounter::

  automount -vc

and test if your automounting works:

  ls -l DIRECTORY

If everything works OK, reboot again into *Recovery Mode* by pressing CMD and
follow the steps to disable SIP, but put **enable** after csrutil instead of
**disable**. After reboot your mac will be protected again and have a nice
LizardFS automount running.

.. note:: The mounted file system will not show up in the finder. You will need
   to either access it from the command line or if you want to use the finder,
   press Shift + Command + G and enter the folder path there manually.

.. seealso::
   * http://useyourloaf.com/blog/using-the-mac-os-x-automounter/
   * https://www.igeeksblog.com/how-to-disable-system-integrity-protection-on-mac/
   *



