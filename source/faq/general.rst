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

**Is there support for different RAM amount in one lizardFS deployment?**
  Yes. Different chunkservers can have different amounts of RAM.

**Is there support for encryption, if yes what kind?**
  Encryption of any kind supported by the platform you run your master and
  chunkservers on is supported since we make use of the underlying POSIX
  filesystems to store the bits and pieces.





