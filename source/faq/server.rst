******************
Server related FAQ
******************

**How do I completely reset a cluster?**
   The simplest way is to create a new metadata file.
   Go to your metadata directory on your current master server (look at the 
   DATA_PATH in the mfsmaster.cfg file), than stop the master and create a new 
   empty metadata file by executing::

     echo -n "MFSM NEW" > metadata.mfs

   Start the master and your cluster will be clear, all remaining chunks will 
   be deleted.

   