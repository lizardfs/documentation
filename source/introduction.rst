########################
Introduction to LizardFS
########################
.. auth-status-writing/none

LizardFS is a distributed, scalable, fault-tolerant and highly available
file system. It allows users to combine disk space located on many servers
into a single name space which is visible on Unix-like and Windows systems
in the same way as other file systems. LizardFS makes files secure by
keeping all the data in many replicas spread over available servers. It can
be used also to build an affordable storage, because it runs without any
problems on commodity hardware.

Disk and server failures are handled transparently without any downtime or
loss of data. If storage requirements grow, it’s possible to scale an
existing LizardFS installation just by adding new servers - at any time,
without any downtime. The system will automatically move some data to newly
added servers, because it continuously takes care of balancing disk usage
across all connected nodes. Removing servers is as easy as adding a new one.

Unique features like:

* support for many data centers and media types,

* fast snapshots,

* transparent trash bin,

* QoS mechanisms,

* quotas

and a comprehensive set of monitoring tools make it suitable for a range of
enterprise-class applications.


Architecture
************

LizardFS keeps metadata (like file names, modification timestamps, directory
trees) and the actual data separately. Metadata is kept on metadata servers,
while data is kept on machines called chunkservers. A typical installation
consists of:

* At least two metadata servers, which work in master-slave mode for failure
  recovery. Their role is also to manage the whole installation, so the
  active metadata server is often called the master server. The role of other
  metadata servers is just to keep in sync with the active master servers, so
  they are often called shadow master servers. Any shadow master server is
  ready to take the role of the active master server at any time. A suggested
  configuration of a metadata server is a machine with fast CPU, at least 32
  GB of RAM and at least one drive (preferably SSD) to store several dozens
  of gigabytes of metadata.

* A set of chunkservers which store the data. Each file is divided into
  blocks called chunks (each up to 64 MiB) which are stored on the
  chunkservers. A suggested configuration of a chunkserver is a machine with
  large disk space available either in a JBOD or RAID configuration,
  depending on requirements. CPU and RAM are not very important. You can have
  as little as 2 chunkservers (a minimum to make your data resistant to any
  disk failure) or as many as hundreds of them. A typical chunkserver is
  equipped with 8, 12, 16, or even more hard drives. Each file can be
  distributed on the chunkservers in a specific replication mode which is one
  of standard, xor or ec.

* Clients which use the data stored on LizardFS. These machines use LizardFS
  mount to access files in the installation and process them just as those on
  their local hard drives. Files stored on LizardFS can be seen and
  simultaneously accessed by as many clients as needed.

.. figure:: images/lfs.png
   :scale: 50 %
   :align: center
   :alt: Figure 1: Architecture of LizardFS

   Figure 1: Architecture of LizardFS

Replication-Modes
*****************

The replication-mode of a directory or even of a file can be defined
individually.

**standard**
  this mode is for defining explicitly how many copies of the data-chunks
  you want to be stored in your cluster and on **which group of nodes the
  copies reside**. In conjunction with "custom-goals" this is handy for
  geo-replication.

**xor**
   xor is similar to the replication-mechanism also known by RAID5. For
   Details see the white paper on lizardfs.

**ec - erasure coding**
   ec mode is similar to the replication-mechanism also known by RAID6. In
   addition you can use parities above 2. For Details see the white paper on
   lizardfs.


Possible application of LizardFS
********************************

There are many possible applications of LizardFS

* archive - with using LTO tapes,

* storage for virtual machines (as an OpenStack backend or similar)

* storage for media files / cctv etc.

* storage for backups

* as a storage for Windows™ machine

* as a DRC (Disaster Recovery Center)

* HPC


Hardware recommendation
***********************

LizardFS will be working on any hardware, you can use commodity hardware as
well. Minimum requirements is two dedicated nodes with a bunch of disks, but
to achieve proper HA installation you should have at least 3 nodes.
We recommend that each node shall have at least two 1Gbps network interface
controllers (NICs). Since most commodity hard disk drives have a throughput
of approximately 100MB/second, your NICs should be able to handle the traffic
between the chunkservers and your host.

Minimal configuration of LizardFS strongly depends on its use case. LizardFS
will run on practically any reasonable machine, but a sample configuration
for a medium size installation could be as follows:

Master / Shadow

* CPU - at least 2 GHz CPU, 64bit

* RAM - depends on expected number of files (4GB should be enough for a small
  installation)

* Disk - 128G, SSD would improve performance, HDD is fine

Chunkserver - recommended 2GB RAM (or more)

Metalogger - recommended 2GB RAM (or more)


Additional Features
*******************

What makes LizardFS a mature enterprise solution are additional features
developed on the basis of a constantly improving core. They can transform the
probably best distributed file system in the world into Hierarchical Storage
Management (HSM), help to build Disaster Recovery Center with asynchronous
replication between sites, reduce disk space required for replication,
effectively manage storage pools (QoS, Quotas) and many more. If you see any
other use case for LizardFS that would require any other functionality please
let us know, we might put it into our Road Map or develop it especially for
you.

Support for LTO Libraries
=========================

LizardFS offers native support for LTO libraries. Storing archival backups
may consume a lot of memory, even though those files are almost never read.
Such data can be efficiently stored on a tape, so LizardFS offers a simple
way to cooperate with back-end LTO storage. Files can be chosen to have a
backup copy on a tape by setting a tape goal.
Examples of tape goals can be found in chapter “Advanced configuration”.

Setting a tape goal to a file makes it read-only for obvious reasons - tape
storage does not support random writes. Reading from tape storage is a timely
process (may last 48h or require manual work to insert correct tape to
library), so data stored in there should be archival - meant to be read very
rarely.

The way of reading a file which is stored on tape depends on its situation:

* If a regular copy of a file is still available, it will be used for reading

* If a file exists only on tape, it has to be restored to LizardFS first.
  To achieve that, one must use lizardfs-restore-tape-copy utility::

	$ lizardfs-restore-tape-copy file_path

  After running this command, all needed data will be read from tape storage
  and loaded to the file system, making the file accessible to clients.
