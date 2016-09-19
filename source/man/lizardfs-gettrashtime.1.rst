.. _lizardfs-gettrashtime.1:

************************
lizardfs-gettrashtime(1)
************************

NAME
====

lizardfs-gettrashtime, lizardfs-settrashtime, lizardfs-rgettrashtime, lizardfs-rsettrashtime - get or set trash time

SYNOPSIS
========

::

 lizardfs gettrashtime [-r] [-n|-h|-H] 'OBJECT'...
 lizardfs rgettrashtime* [-n|-h|-H] 'OBJECT'...
 lizardfs settrashtime* [-r] [-n|-h|-H] SECONDS[+|-] 'OBJECT'...
 lizardfs rsettrashtime* [-n|-h|-H] SECONDS[+|-] 'OBJECT'...

DESCRIPTION
===========

**gettrashtime** and **settrashtime** operate on an object's 'trashtime'
value, i.e. the number of seconds the file is preserved in the special 'trash'
directory before it's finally removed from the filesystem. 'Trashtime' must be
a non-negative integer value. *gettrashtime* prints the current 'trashtime'
value of given object(s).

OPTIONS
=======

-r
  This option enables recursive mode, which works as usual for every given
  file, but for every given directory additionally prints the current
  'trashtime' value of all contained objects (files and directories).
N\[+|-]
  If a new value is specified in 'N'+ form, the 'trashtime' value is increased
  to 'N' for objects with lower 'trashtime' value and unchanged for the rest.
  Similarly, if a new value is specified as 'N'-, the 'trashtime' value is
  decreased to 'N' for objects with higher 'trashtime' value and unchanged for
  the rest. These tools can be used on any file, directory or deleted
  ('trash') file.
-n, -h, -H
  These options are described in lizardfs(1).


.. note:: *rgettrashtime* and *rsettrashtime* are deprecated aliases for
   *gettrashtime -r* and *settrashtime -r* respectively.

REPORTING BUGS
==============

Report bugs to <contact@lizardfs.org>.

COPYRIGHT
=========

Copyright 2008-2009 Gemius SA, 2016 Skytechnology Sp. z o.o.

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
