.. _lizardfs-appenchunks.1:

************************
lizardfs appendchunks(1)
************************

NAME
====

lizardfs appendchunks - lazy append chunks

SYNOPSIS
********

::

  lizardfs appendchunks 'SNAPSHOT_FILE' 'OBJECT'...

DESCRIPTION
===========

**lizardfs appendchunks** (equivalent of mfssnapshot from MooseFS 1.5) appends
a lazy copy of specified file(s) to the specified snapshot file ("lazy" means
that creation of new chunks is delayed to the moment one copy is modified). If
multiple files are given, they are merged into one target file in the way that
each file begins at 'chunk' (64MB) boundary; padding space is left empty.

COPYRIGHT
=========

2013-2017 Skytechnology Sp. z o.o.

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

lizardfs(1),lizardfs(7)
