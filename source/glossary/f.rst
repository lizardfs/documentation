***
 F
***
.. auth-status-writing/none

.. _FC:

.. _FibreChannel:

FC/FibreChannel
===============

  Fibre Channel, or FC, is a high-speed network technology (commonly running at 1, 2, 4, 8, 16, 32, and 128 gigabit per second rates) primarily used to connect computer data storage to servers. Fibre Channel is mainly used in storage area networks (SAN) in enterprise storage. Fibre Channel networks are known as a Fabric because they operate in unison as one big switch. Fibre Channel typically runs on optical fiber cables within and between data centers.

  Most block storage runs over Fibre Channel Fabrics and supports many upper level protocols. Fibre Channel Protocol (FCP) is a transport protocol that predominantly transports SCSI commands over Fibre Channel networks. Mainframe computers run the FICON command set over Fibre Channel because of its high reliability and throughput. Fibre Channel is the most popular network for flash memory being transported over the NVMe interface protocol.

  The folowing Variants of FC are an overview of FC native speeds:

  *Fibre Channel Variants*


  +----------------+-----------+-------------+---------------------------------------+-----------------------------------+--------------+
  | NAME           | Line-rate | Line coding | Nominal throughp. per direction; MB/s | Net throughp. per direction; MB/s | Availability |
  +================+===========+=============+=======================================+===================================+==============+
  | 1GFC           | 1.0625    | 8b10b       | 100                                   | 103.2                             | 1997         |
  +----------------+-----------+-------------+---------------------------------------+-----------------------------------+--------------+
  | 2GFC           | 2.125     | 8b10b       | 200                                   | 206.5                             | 2001         |
  +----------------+-----------+-------------+---------------------------------------+-----------------------------------+--------------+
  | 4GFC           |4.25       | 8b10b       | 400                                   | 412.9                             | 2004         |
  +----------------+-----------+-------------+---------------------------------------+-----------------------------------+--------------+
  | 8GFC           | 8.5       | 8b10b       | 800                                   | 825.8                             | 2005         |
  +----------------+-----------+-------------+---------------------------------------+-----------------------------------+--------------+
  | 10GFC          | 10.51875  | 64b66b      | 1,200                                 | 1,239                             | 2008         |
  +----------------+-----------+-------------+---------------------------------------+-----------------------------------+--------------+
  | 16GFC "Gen 5"  | 14.025    | 64b66b      | 1,600                                 | 1,652                             | 2011         |
  +----------------+-----------+-------------+---------------------------------------+-----------------------------------+--------------+
  | 32GFC "Gen 6"  | 28.05     | 64b66b      | 3,200                                 | 3,303                             | 2016         |
  +----------------+-----------+-------------+---------------------------------------+-----------------------------------+--------------+
  | 128GFC "Gen 6" | 4×28.05   | 64b66b      | 12,800                                | 13,210                            | 2016         |
  +----------------+-----------+-------------+---------------------------------------+-----------------------------------+--------------+

  For more information please check the Wikipedia entry for SAN: https://en.wikipedia.org/wiki/Fibre_Channel where most of the info in this entry is from.


.. _fuse:

FUSE
====

  FUSE (Filesystem in Userspace) is an interface for userspace programs to
  export a filesystem to the Linux kernel. The FUSE project consists of two
  components: the fuse kernel module (maintained in the regular kernel
  repositories) and the libfuse userspace library (maintained in this
  repository). libfuse provides the reference implementation for communicating
  with the FUSE kernel module.

  A FUSE file system is typically implemented as a standalone application that
  links with libfuse. libfuse provides functions to mount the file system,
  unmount it, read requests from the kernel, and send responses back. libfuse
  offers two APIs: a "high-level", synchronous API, and a "low-level"
  asynchronous API. In both cases, incoming requests from the kernel are
  passed to the main program using callbacks. When using the high-level API,
  the callbacks may work with file names and paths instead of inodes, and
  processing of a request finishes when the callback function returns. When
  using the low-level API, the callbacks must work with inodes and responses
  must be sent explicitly using a separate set of API functions.

.. seealso::

   Fuse on github
      https://github.com/libfuse/libfuse

   Fuse mailing lists
      https://lists.sourceforge.net/lists/listinfo/fuse-devel
