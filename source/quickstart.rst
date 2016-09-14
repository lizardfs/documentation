#############################
LizardFS QuickStart on Debian
#############################

.. Important::  
   In case you downloaded the packages from the official Debian repository, 
   be aware of the differences in certain names and paths, including:

   * Configuration files directory is /etc/lizardfs instead of /etc/mfs, data 
     directory is /var/lib/lizardfs instead of /var/lib/mfs
   * Sample configuration files can be found in 
     /usr/share/doc/lizardfs-<name>/examples, where <name> can be master, 
     chunkserver or metalogger.
   * Chunk servers are run as user lizardfs, instead of user mfs.

   In order to allow lizardfs-<name> to be run as service, run the following 
   command::

      $ systemctl enable lizardfs-<name>

   where <name> is one of master, chunkserver, metalogger, cgiserv

Master server installation
**************************

Install the master server package

   Check :ref:`get_and_install_debian` for instructions how to install the 
   package.

Example::

   $ apt-get install lizardfs-master

Fill the configuration files with appropriate values.

THis involves setting up the following configuration files in /etc/mfs 
directory:

=============== ================================== ========
Filename        Description                        Required
=============== ================================== ========
mfsmaster.cfg   Master configuration file          X
mfsexports.cfg  Mountpoint locations configuration X
mfsgoals.cfg    Replication goals configuration
mfstopology.cfg Network topology definitions
=============== ================================== ========

Documentation for each file can be viewed by entering::

   $ man <filename>

in your shell.

Sample configuration files can be found in /etc/mfs/\*.dist

* Prepare the data directory /var/lib/mfs
* Create empty metadata.mfs file::

   $ cp /var/lib/mfs/metadata.mfs.empty /var/lib/mfs/metadata.mfs

The data directory will contain all changelogs and metadata files of your 
installation.

Example configuration
=====================

In our example configuration, the mfsmaster.cfg file can remain untouched.

In order to let clients from IP range 192.168.18.\* read and write to our 
installation, add this line to mfsexports.cfg::

   192.168.18.0/24 / rw,alldirs,maproot=0

In order to use lizardfs-master as a service (recommended), edit /etc/default/
lizardfs-master file and set::

   LIZARDFSMASTER_ENABLE=true

After this operation, you can launch LizardFS master daemon::

   $ service lizardfs-master start

Your first instance of LizardFS should have been successfully launched!

Explore your new master server's capabilities by looking into the mfsmaster 
man pages::

   $ man mfsmaster

Shadow master installation
**************************

* Follow the steps for installing a master server.
* Add mfsmaster entry to /etc/hosts, as in chunkserver steps.
* Add this line to master's config (mfsmaster.cfg)::

   PERSONALITY=shadow

* Run master service.

You now possess a shadow master server which makes your data much safer, ie. 
all data files from the master server are also saved to the shadow master.

Metalogger installation
***********************

Install the metalogger package

   Check :ref:`get_and_install_debian` for instructions how to install the 
   package

Example for Debian/Ubuntu::

   $ apt-get install lizardfs-metalogger

Fill the configuration file with appropriate values. You can find it in the 
/etc/mfs directory and it is called::

   mfsmetalogger.cfg

Documentation for this file can be viewed by entering::

   $ man mfsmetalogger.cfg

in your shell.


Sample configuration files can be found in /etc/mfs/\*.dist

For our example configuration, mfsmetalogger.cfg may remain unchanged.

By default, the metalogger uses the "mfsmaster" host as LizardFS master's 
address. It is advised to set it up in /etc/hosts file.

For example configuration mentioned at the top, /etc/hosts should include 
this line::

   192.168.16.100 mfsmaster

Allow metalogger to be run as service by editing 
/etc/default/lizardfs-metalogger file::

   LIZARDFSMETALOGGER_ENABLE=true

Run your metalogger::

   $ service lizardfs-metalogger start

Chunk server installation
*************************

Install chunk server package
   Check :ref:`get_and_install_debian` for instructions how to install package

Example for Debian/Ubuntu::

   $ apt-get install lizardfs-chunkserver

Fill configuration files with appropriate values.

It involves setting up following configuration files in /etc/mfs directory:

=================== =============================== 
Filename            Description                    
=================== ===============================
mfschunkserver.cfg  Chunk server configuration file 
mfshdd.cfg          Hard drive location settings   
=================== ===============================

Documentation for each file can be viewed by entering::

   $ man <filename>

in your shell.

Sample configuration files can be found in /etc/mfs/\*.dist

By default, chunk server uses "mfsmaster" host as LizardFS master's address. 
It is advised to set it up in /etc/hosts file. For example configuration 
mentioned at the top, /etc/hosts should include this line::

   192.168.16.100 mfsmaster

The mfshdd.cfg file is needed to indicate mountpoints of hard drives for your 
chunkserver. Assuming that there are 2 disks mounted at /mnt/chunk1 and 
/mnt/chunk2 locations, your mfshdd.cfg file should look like this::

   /mnt/chunk1
   /mnt/chunk2

Remember that chunk servers are run as user mfs, so directories above need 
appropriate permissions::

   $ chown -R mfs:mfs /mnt/chunk1
   $ chown -R mfs:mfs /mnt/chunk2

Allow chunk server to be run as a service
=========================================

As before, this can be achieved by editing /etc/default/lizardfs-chunkserver 
file::

   LIZARDFSCHUNKSERVER_ENABLE=true

Type::

  $ service lizardfs-chunkserver start

and congratulate yourself on launching your first LizardFS chunk server.

Cgi server installation
***********************

The cgi server offers a Web-based GUI that presents LizardFS status and 
various statistics.

Install the cgi-server package

       Check :ref:`get_and_install_debian` for instructions how to install 
       package

Example for Debian/Ubuntu::

   $ apt-get install lizardfs-cgiserv

Set mfsmaster host in /etc/hosts file. For our example configuration it would 
be::

   192.168.16.100 mfsmaster

Run your cgi-server::

   $ service lizardfs-cgiserv start

The Web interface is now available.

Assuming that lizardfs-cgiserv is installed on host 192.168.10.11, you can 
access LizardFS panel at 
http://192.168.10.11:9425/mfs.cgi?masterhost=mfsmaster

Command line administration tools
*********************************

Install administration tools package

   Check :ref:`get_and_install_debian` for instructions how to install package

Example for Debian/Ubuntu::

   $ apt-get install lizardfs-adm

See variety of options by running those commands::

   $ man lizardfs-admin or $ lizardfs-admin -h 


Now that you are done with your quick and dirty installation, you can try 
connecting clients to your fresh LizardFS instance. This is documented in the 
:ref:`connectclient` part of the :ref:`adminguide`.
