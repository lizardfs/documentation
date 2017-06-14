*****************
General Questions
*****************
.. auth-status-writing/none

**Why is it called LizardFS ?**
  It's a metaphor for something that can grow back if partially lost

**Can I move my systems from MooseFS to LizardFS ?**
  Yes. This is documented in the :ref:`upgrading` manual.

**Why a fork from MooseFS ?**
  *  At the time we did the fork there was nearly no movement in the GIT repo
     of MosseFS
  *  Only 2 devs had access to the sourceforge repo and there were no more
     committers
  *  increase in the number of possible contributors with a simultaneous lack
     of response on the part of MooseFS maintenance

**What kind of erasure coding does LizardFS use ?**
  Reed-Solomon

**Is there support for different storage sizes in one lizardFS deployment ?**
  Yes

**Is there support for different network bandwidth in one lizardFS deployment?**
  Yes. You can have different chunkservers having different bandwidth.

  As for different bw per client, check out: :ref:`lizardfs_qos` .

**Is there support for different RAM amount in one lizardFS deployment?**
  Yes. Different chunkservers can have different amounts of RAM.

**Is there support for encryption, if yes what kind?**
  Encryption of any kind supported by the platform you run your master and
  chunkservers on is supported since we make use of the underlying POSIX
  filesystems to store the bits and pieces.

**How are the deletes managed, if there’s a garbage collector?**
  Deleted files are sent to trash and removed when trashtime expires

**Are the meta data servers “inside” lizard or “outside”?**
  Inside

**How do LizarFS chunks get distributed ?**

  The operation is daisy chained. The process actually looks roughly the following way:

    * Client starts writing chunk to the first chunkserver.
    * As soon as the header and the data part of the first slice of the chunk
      arrive at the chunkserver it starts writing to the next one if goal >=2.
    * Same goes for the next chunkserver if goal >=3
    * As soon as the client has finished writing the chunk, it selects another
      chunkserver to start the same process for the next chunk, unless you
      define something else in your topology setup of course.

  This, of course, is only true for replication goals. In EC mode it will be
  distributed writes from the client to as many chunkservers as defined in the
  EC goal so nothing of the above would apply.




