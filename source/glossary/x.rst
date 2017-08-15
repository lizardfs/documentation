***
 X
***
.. auth-status-writing/none

.. _xcode:

Xcode
=====

  Xcode is an integrated development environment (IDE) containing a suite of
  software development tools developed by Apple for developing software for
  macOS, iOS, WatchOS and tvOS. First released in 2003, the latest stable
  release is version 8 and is available via the Mac App Store free of charge
  for OS X El Capitan users. Registered developers can download preview
  releases and prior versions of the suite through the Apple Developer
  website. However, Apple recently made a beta version of version 8.0 of the
  software available to those of the public with Apple Developer accounts.

  Xcode supports source code for the programming languages C, C++,
  Objective-C, Objective-C++, Java, AppleScript, Python, Ruby, ResEdit (Rez),
  and Swift, with a variety of programming models, including but not limited
  to Cocoa, Carbon, and Java. Third parties have added support for GNU
  Pascal, Free Pascal, Ada, C#, Perl, and D.

  Thanks to the Mach-O executable format, which allows fat binary files,
  containing code for multiple architectures, Xcode can build universal binary
  files, which allow software to run on both PowerPC and Intel-based (x86)
  platforms and that can include both 32-bit and 64-bit code for both
  architectures. Using the iOS SDK, Xcode can also be used to compile and
  debug applications for iOS that run on ARM architecture processors.
  Xcode includes the GUI tool Instruments, which runs atop a dynamic tracing
  framework, DTrace, created by Sun Microsystems and released as part of
  OpenSolaris.

.. seealso::

   **Wikipedia entry for Xcode**
     https://en.wikipedia.org/wiki/Xcode

   **Xcode at the Mac App Store**
     https://itunes.apple.com/us/app/xcode/id497799835

   **Xcode at Apples Developer Site**
     https://developer.apple.com/xcode/

.. _xfs:

XFS
===

  XFS is a high-performance 64-bit journaling file system created by Silicon
  Graphics, Inc (SGI) in 1993. It was the default file system in the SGI's
  IRIX operating system starting with its version 5.3; the file system was
  ported to the Linux kernel in 2001. As of June 2014, XFS is supported by
  most Linux distributions, some of which use it as the default file system.

  XFS excels in the execution of parallel input/output (I/O) operations due to
  its design, which is based on allocation groups (a type of subdivision of
  the physical volumes in which XFS is used- also shortened to AGs). Because
  of this, XFS enables extreme scalability of I/O threads, file system
  bandwidth, and size of files and of the file system itself when spanning
  multiple physical storage devices.

  XFS ensures the consistency of data by employing metadata journaling and
  supporting write barriers. Space allocation is performed via extents with
  data structures stored in B+ trees, improving the overall performance of the
  file system, especially when handling large files. Delayed allocation
  assists in the prevention of file system fragmentation; online
  defragmentation is also supported. A feature unique to XFS is the
  pre-allocation of I/O bandwidth at a pre-determined rate, which is suitable
  for many real-time applications; however, this feature was supported only on
  IRIX, and only with specialized hardware.

  A notable XFS user, NASA Advanced Supercomputing Division, takes advantage
  of these capabilities deploying two 300+ terrabyte XFS filesystems on two SGI
  Altix archival storage servers, each of which is directly attached to
  multiple Fibre Channel disk arrays.

.. seealso::

   **XFS FAQ**
      http://xfs.org/index.php/XFS_FAQ

   **Wikipedia entry for XFS**
      https://en.wikipedia.org/wiki/XFS
