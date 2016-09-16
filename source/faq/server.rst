******************
Server related FAQ
******************
.. auth-status-writing/none

**How do I completely reset a cluster ?**
   The simplest way is to create a new metadata file.
   Go to your metadata directory on your current master server (look at the
   DATA_PATH in the mfsmaster.cfg file), than stop the master and create a new
   empty metadata file by executing::

     echo -n "MFSM NEW" > metadata.mfs

   Start the master and your cluster will be clear, all remaining chunks will
   be deleted.

.. not completely ready yet ....

    **What is the format of the chunk names on the chunkservers ?**
   The format for the chunkservers is hardcoded in the files::

     src/chunkserver/chunk_filename_parser.h
     src/chunkserver/chunk_filename_parser.cc

   in the lizardfs chunkserver source code. The current Format as of 3.10.2 is:

   Example::

     ./chunks00/chunk_0000000000001BB3_00000001.mfs
     # break into 6 portions for readability
     1:./chunks 2:00 / 3:chunk_0000000000 2:00  4:1BB3 _  5:00000001 . 6:mfs

   This translates to:

   * chunks: indicate a chunk folder.

   * 00: unique chunk folder id in a disk, can have duplicates across disks or
     chunkservers.
     IDs range from "00" to "FF" in Hex number. So there are max 256 chunks folders in a disk.

   * chunk_0000000000: prefix? placeholder? I don't know.

   * 1BB3: Hex unique ID across chunk folders with the same ID (00 in this
   case).
   This ranges from 0000 to FFFF, so there are max 65535 chunks in across
   chunks with the same ID.

   This is true in the whole cluster.

   * 00000001: Chunk replicate ID?

   * mfs: File extension, of course.

   First asked in: https://github.com/lizardfs/lizardfs/issues/454



