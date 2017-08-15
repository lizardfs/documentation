.. _mfsmaster.8:

************
mfsmaster(8)
************

NAME
====

mfsmaster - start, restart or stop Lizard File System metadata server process

SYNOPSIS
========

::

  mfsmaster [-f] [-c CFGFILE] [-u] [-d] [-t LOCKTIMEOUT] [-p PIDFILE] [ACTION]
  mfsmaster -s [-c CFGFILE]
  mfsmaster -v
  mfsmaster -h

DESCRIPTION
===========

**mfsmaster** is the metadata server program of Lizard File System. Depending
on parameters it can start, restart or stop the LizardFS metadata server
process. Without any options it starts the LizardFS metadata server, killing
first the running process if a lock file exists.

The metadata server can work in one of two modes (personalities):

* master
* shadow

If the metadata server works with *master* personality it acts as the main
metadata server governing all file system metadata modifications.
If the metadata server works with *shadow* personality it acts as backup
metadata server ready for immediate deployment as new *master* in case of the
current *master* failing.

Shadow only accepts connections from lizardfs-admin, i.e. mfschunkserver,
mfsmetalogger and mfsmount (the client) are not allowed to connect to the
*shadow* instance.

Current metadata server personality is defined in the metadata server
configuration file and can be changed on the fly from *shadow* to *master* by
proper modification and reloading of its configuration file.

*Master* and *shadow* are designed to run simultaneously in sync forever. It
is very unlikely but still (due to a memory corruption or a bug) possible that
after some time their metadata will somehow differ. Since version 2.5.2
metadata checksum is maintained both by *master* and *shadow*, in order to
detect and fix possible metadata corruptions. In case a mismatch is detected
*shadow* asks *master* to double check its metadata and dump its current
snapshot.

After the metadata is dumped and the checksum in the *master* is recalculated,
shadow downloads the new metadata snapshot, which should ensure that the
master and all its shadows have exactly the same metadata.

SIGHUP (or *reload* ACTION) forces **mfsmaster** to reload all configuration
files.

-v
  print version information and exit
-h
  print usage information and exit
-f
  (deprecated, use *start* action instead)
  forcibly run LizardFS master process, without trying to kill
  previous instance (this option allows to run LizardFS master if stale PID
  file exists)
-s
  (deprecated, use *stop* action instead)
  stop LizardFS master process
-c CFGFILE
  specify alternative path of configuration file (default is *mfsmaster.cfg*
  in system configuration directory)
-u
  log undefined configuration values (when default is assumed)
-d
  run in foreground, don*t daemonize
-t LOCKTIMEOUT
  how long to wait for lockfile (default is 60 seconds)
-p PIDFILE
  write process ID (pid) to given file

ACTION
  is one of *start*, *stop*, *restart*, *reload*, *test*, *isalive* or
  *kill*. The default action is *restart*.

FILES
=====

mfsmaster.cfg
  configuration file for the LizardFS master process (see :manpage:`mfsmaster.cfg(5)`)

mfsexports.cfg
  LizardFS access control file (used with *mfsmount`s* 1.6.0 or later, see
  :manpage:`mfsexports.cfg(5)`)

mfstopology.cfg
  Network topology definitions (see :manpage:`mfstopology.cfg(5)`)

mfsmaster.lock
  PID file of running LizardFS master process

.mfsmaster.lock
  lock file of the running LizardFS master process
  (created in data directory)

metadata.mfs, metadata.mfs.back
  LizardFS filesystem metadata image

changelog.\*.mfs
  LizardFS filesystem metadata change logs (merged into *metadata.mfs* once
  per hour)

data.stats
  LizardFS master charts state

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

mfsmetarestore(8), mfschunkserver(8), mfsmount(1),
mfsmaster.cfg(5), mfsexports.cfg(5), mfstopology.cfg(5),
lizardfs(7)
