.. _lizardfs-makesnapshot.1:

************************
lizardfs-makesnapshot(1)
************************

NAME
====

lizardfs-makesnapshot - make lazy copies

SYNOPSIS
========

::

  lizardfs makesnapshot [-o] [-f] [-i] [-s <VALUE>] 'SOURCE'... 'DESTINATION'

DESCRIPTION
===========

**makesnapshot** makes a "real" snapshot (lazy copy, like in case of
*appendchunks*) of some object(s) or a subtree (similarly to the *cp -r*
command). It's atomic in respect to each 'SOURCE' argument separately. If
'DESTINATION' points to an already existing file, an error will be reported
unless *-f* (force) or it's alias *-o* (overwrite) option is given.

The new object exists only in metadata until changes to the data are done
which will trigger creation of chunks for the changed files or removing
metadata entries for erased chunks, unless the trash feature is utilized.

NOTE: if 'SOURCE' is a directory, it's copied as a whole; but if it's followed
by a trailing slash, only the directory content is copied.

OPTIONS
=======

-s <value>
  This option is used to specify number of nodes that will be atomically
  cloned.
-i
  ignore missing source nodes in snapshot request

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

lizardfs(1), lizardfs-appendchunks(1)
