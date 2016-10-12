.. _mfsmetalogger.8:

****************
mfsmetalogger(8)
****************

NAME
====

mfsmetalogger - start, restart or stop Lizard File System metalogger process

SYNOPSIS
========

::

  mfsmetalogger [-f] [-c CFGFILE] [-u] [-d] [-t LOCKTIMEOUT] [ACTION]
  mfsmetalogger -s [-c CFGFILE]
  mfsmetalogger -v
  mfsmetalogger -h

DESCRIPTION
===========

**mfsmetalogger** is the metadata replication server of the Lizard File
System. Depending on the parameters given to it, it can start, restart or stop
the LizardFS metalogger process. Without any options it starts the LizardFS
metalogger, killing any previously run process if a lock file exists.

SIGHUP (or *reload* *ACTION*) forces **mfsmetalogger** to reload all
configuration files.

-v
  print version information and exit
-h
  print usage information and exit
-c CFGFILE
  specify alternative path of the configuration file (default is
  **mfsmetalogger.cfg** in the system configuration directory).
-u
  log undefined configuration values (for which defaults are assumed)
-d
  run in the foreground, don't daemonize
-t LOCKTIMEOUT
  how long to wait for lockfile (default is 60 seconds)

ACTION
  is one of *start*, *stop*, *restart*, *reload*, *test*, *isalive* or *kill*.
  Default action is *restart*.

FILES
=====

*mfsmetalogger.cfg*
  configuration file for LizardFS metalogger process; refer to the
  mfsmetalogger.cfg(5) manual page for defails

*mfsmetalogger.lock*
  PID file of running LizardFS metalogger process

*.mfsmetalogger.lock*
  lock file of running LizardFS metalogger process (created in data directory)

*changelog_ml.\*.mfs*
  LizardFS filesystem metadata change logs (backup of master change log files)

*metadata.ml.mfs.back*
  Latest copy of complete metadata.mfs.back file from LizardFS master.

*sessions.ml.mfs*
  Latest copy of sessions.mfs file from LizardFS master.

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

mfsmaster(8), mfsmetalogger.cfg(5), lizardfs(7)
