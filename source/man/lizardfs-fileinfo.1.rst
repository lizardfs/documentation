.. _lizardfs-fileinfo.1:

********************
lizardfs fileinfo(1)
********************

NAME
====

lizardfs fileinfo - locate chunks

SYNOPSIS
========

::

  lizardfs fileinfo 'FILE'...

DESCRIPTION
===========

**fileinfo** prints the location ('chunkserver' host and port) of each chunk
copy belonging to specified file(s). It can be used on any file, included
deleted ones ('trash').

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

lizardfs(1),
lizardfs(7)
