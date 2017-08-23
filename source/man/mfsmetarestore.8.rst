.. _mfsmetarestore.8:

*****************
mfsmetarestore(8)
*****************

NAME
====

mfsmetarestore - replay LizardFS metadata change logs or dump LizardFS
metadata image

SYNOPSIS
========

::

  mfsmetarestore [-z] -m OLDMETADATAFILE -o NEWMETADATAFILE [CHANGELOGFILE...]

  mfsmetarestore -m METADATAFILE

  mfsmetarestore [-z] -a [-d DIRECTORY]

  mfsmetarestore* -g -d DIRECTORY

  mfsmetarestore -v

  mfsmetarestore -?

DESCRIPTION
===========

When *mfsmetarestore* is called with both *-m* and *-o* options, it replays
given *CHANGELOGFILEs* on *OLDMETADATAFILE* and writes result to
*NEWMETADATAFILE*. Multiple change log files can be given.

*mfsmetarestore* with just the *-m* *METADATAFILE* option dumps LizardFS
metadata image file in human readable form.

*mfsmetarestore* called with -a option automatically performs all operations
needed to merge change log files. The master data directory can be specified
using -d DIRECTORY option.

*mfsmetarestore* -g with path to metadata files, prints the latest metadata
version that can be restored from disk.

Prints 0 if metadata files are corrupted.

-a
  autorestore mode (see above)
-d <DATAPATH>
  master data directory (for autorestore mode)
-m <METADATAFILE>
  specify input metadata image file
-o <NEWMETADATAFILE>
  specify output metadata image file
-z
  ignore metadata checksum inconsistency while applying changelogs
-v
  print version information and exit

FILES
=====

**metadata.mfs**
  Lizard File System metadata image as read by *mfsmaster* process

**metadata.mfs.back**
  Lizard File System metadata image as left by killed or crashed *mfsmaster*
  process

**changelog.\*.mfs**
  Lizard File System metadata change logs

REPORTING BUGS
==============

Report bugs to <contact@lizardfs.org>.

COPYRIGHT
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

mfsmaster(8), lizardfs(7)
