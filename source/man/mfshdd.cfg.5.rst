.. _mfshdd.cfg.5:

*************
mfshdd.cfg(5)
*************

NAME
====

mfshdd.cfg - list of LizardFS storage directories for mfschunkserver

DESCRIPTION
===========

The file *mfshdd.cfg* contains a list of directories (mountpoints) used for
LizardFS storage (one per line). A directory prefixed by a single *\**
character causes that directory to be freed by replicating all data already
stored there to different locations. Lines starting with a *#* character are
ignored.


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

mfschunkserver(8), mfschunkserver.cfg(5)
