.. _mfsrestoremaster.8:

*******************
mfsrestoremaster(8)
*******************

NAME
====

mfsrestoremaster - a networking, distributed, highly available file system

SYNOPSIS
========

::

  mfsrestoremaster <net-interface> [<etc-mfs-dir>]

<net-interface> - network interface to reconfigure.

<etc-mfs-dir> - mfs configuration directory to use (default: /etc/mfs).

DESCRIPTION
===========

**mfsrestoremaster** automates starting a spare master server on a metalogger
machine.

It performs the following steps:

 * verify basic sanity of configuration files
 * update metadata image with data from metalogger changelogs
 * set master's IP address on given network interface
 * start the master server

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

lizardfs(1), lizardfs(7)

