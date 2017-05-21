.. _lizardfs-filerepair.1:

**********************
lizardfs-filerepair(1)
**********************

NAME
====

lizardfs-filerepair - repair broken files

SYNOPSIS
========

::

  lizardfs filerepair [-n|-h|-H] 'FILE'...

DESCRIPTION
===========

**filerepair** deals with broken files (those which cause I/O errors on read
operations) to make them partially readable. In case of a missing chunk it
fills the missing parts of the file with zeros; in case of a chunk version
mismatch it sets the chunk version known to *mfsmaster* to the highest one
found on the chunkservers.

.. note:: Because in the second case content mismatch can occur in chunks with
   the same version, it is advised to make a copy (not a snapshot!)
   and delete the original file after "repairing".

OPTIONS
=======

-c
  This option enables correct-only mode, which will restore chunk to a
  previous version if possible, but will never erase any data.


-n, -h, -H
  These options are described in lizardfs(1).

OPYRIGHT
=========

Copyright 2008-2009 Gemius SA, 2013-2016 Skytechnology Sp. z o.o.

LizardFS is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, version 3.

LizardFS is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
LizardFS. If not, see <http://www.gnu.org/licenses/>.

SEE ALSO
========

lizardfs(1)
