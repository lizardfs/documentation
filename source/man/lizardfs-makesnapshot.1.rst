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

  lizardfs makesnapshot [-o] [-f] 'SOURCE'... 'DESTINATION'

DESCRIPTION
===========

**makesnapshot** makes a "real" snapshot (lazy copy, like in case of
*appendchunks*) of some object(s) or a subtree (similarly to the *cp -r*
command). It's atomic in respect to each 'SOURCE' argument separately. If
'DESTINATION' points to an already existing file, an error will be reported
unless *-f* (force) or it's alias *-o* (overwrite) option is given.

NOTE: if 'SOURCE' is a directory, it's copied as a whole; but if it's followed
by a trailing slash, only the directory content is copied.

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
