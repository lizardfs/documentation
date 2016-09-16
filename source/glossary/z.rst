***
 Z
***
.. auth-status-writing/none


.. _zfs:

ZFS
===

   The Z File System, or ZFS, is an advanced file system designed to overcome
   many of the major problems found in previous designs.

   Originally developed at Sun™, ongoing open source ZFS development has moved
   to the <OpenZFS Project http://www.open-zfs.org>_ .

   ZFS has three major design goals:

   * Data integrity: All data includes a checksum of the data. When data is
     written, the checksum is calculated and written along with it. When that
     data is later read back, the checksum is calculated again. If the
     checksums do not match, a data error has been detected. ZFS will attempt
     to automatically correct errors when data redundancy is available.

   * Pooled storage: physical storage devices are added to a pool, and storage
     space is allocated from that shared pool. Space is available to all file
     systems, and can be increased by adding new storage devices to the pool.

   * Performance: multiple caching mechanisms provide increased performance.
     ARC is an advanced memory-based read cache. A second level of disk-based
     read cache can be added with L2ARC, and disk-based synchronous write
     cache is available with ZIL.

.. seealso::

   OpenZFS Project:
      http://www.open-zfs.org/

   ZFS Manual in the FreeBSD Handbook
      https://www.freebsd.org/doc/handbook/zfs.html


   The ZFS on Linux project supplies packages and documentation for every
   major distro:
      http://zfsonlinux.org/




