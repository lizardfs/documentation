Basic Configuration
*******************

There are a range of settings that must be done on every server before we start working with LizardFS itself.

* setup all participating hosts in the /etc/hosts file

* setup time synchronization via ntp

* select the filesystem type and create the filesystems the chunkservers shall 
  use 

* adjust network settings

* adjust kernel settings


Labeling your chunkserver
=========================

To be able to setup which goals are going to be performed on which 
chunkservers, you need to be able to identify them in your goal definition.
To achieve this, we use labels.

The label for the Chunkservers is set in the mfschunkserver.cfg file. ::

   LABEL = ssd

After changing the configuration you must reload the chunkserver:: 

   $ mfschunkserver -c path/to/config reload

If there is no LABEL entry in the config, the chunkserver has a default label of “_” (i.e. wildcard), which has a special meaning when defining goals and means “any chunkserver”.

Show labels of connected chunkservers
-------------------------------------

From the command line::

   $ lizardfs-admin list-chunkservers <master ip> <master port>

Via the cgi (webinterface):

In the ‘Servers’ tab in the table ‘Chunk Servers’ there is a column ‘label’ where labels of the chunkservers are displayed.




