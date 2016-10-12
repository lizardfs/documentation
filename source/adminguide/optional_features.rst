.. _optional_features:

*****************************
Configuring Optional Features
*****************************
.. auth-status-proof1/none

LizardFS comes with a range of optional features whose configuration does not
belong into the "basic" or "advanced" modes.


Configuring LTO handling
========================

Installation
------------

THe LizardFS tapeserver package can be installed via::

   $ apt-get install lizardfs-tapeserver # Debian/Ubuntu
   $ yum install lizardfs-tapeserver # CentOS/RedHat

Configuration
-------------

The configuration file for the lizardfs-tapeserver is located at
/etc/mfs/lizardfs-tapeserver.cfg.
The tapeserver needs a working mountpoint of your LizardFS installation.
Configuration consists mainly of listing changer and volume devices of a tape
library.

Example configuration::

   [lizardfs-tapeserver]
   # Name
   name = tapesrv
   # Master host network info
   masterhost = 192.168.1.5
   masterport = 9424
   # Path to mountpoint used for file reading/writing
   mountpoint = /mnt/tapemount
   # Path to temporary cache for files
   cachepath  = /tmp/cache
   # Path to sqlite3 database
   database = /opt/tape.db
   # Changer devices
   changers = /dev/sg3
   # Drive devices
   drives = /dev/st0,/dev/st1
   # Volume ids
   volumes = 000003,000180,000002
   # Label
   label = tapeserver1

Verifying your installation
---------------------------

Installation can be easily verified using the lizardfs-admin command::

   $ lizardfs-admin list-tapeserver MASTER_ADDR MASTER_PORT

If the installation succeeded, the command above should result in listing all
tapeservers connected to the current master.

Verification if tape storage works properly can be achieved by the steps below:

* create a test file

* set tape goal to the file: mfssetgoal your_tape_goal testfile

* wait for replication to take place, check its status with ‘mfsfileinfo’
  command::

   $ mfsfileinfo testfile

* Replication to tape is complete after tape copy status changes from Creating
  to Ok

* verify that the file was actually stored on tape::

	$ tar tf /dev/your_tape_volume # will list all files present on tape
	$ tar xvf /dev/your_tape_volume filename # will extract file ‘filename’ from tape

Configuring tape goals
----------------------

Tape goals are configured just like regular goals, save one difference in
naming. In order to create a tape goal, append a “@” sign to the end of its
definition.

Example mfsgoals.cfg contents::

	1 1 : _
	2 2 : _ _
	3 tape1 : _ _@
	4 tape2: ssd _@ ts@
	5 fast: ssd ssd _

The example above contains 2 tape goal definitions.

The first one (tape1), configures that there should be 2 copies of each chunk:

* 1 on any chunkserver
* 1 on any tape.

The second one (tape2) requires each chunk to have 3 copies:

* 1 on chunkserver labeled “ssd”
* 1 on any tape
* 1 on tape labeled “ts”


