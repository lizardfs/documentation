.. _mfsmaster.cfg.5:

****************
mfsmaster.cfg(5)
****************

NAME
====

mfsmaster.cfg - main configuration file for mfsmaster

DESCRIPTION
===========

The file **mfsmaster.cfg** contains the configuration of the LizardFS metadata
server process.

SYNTAX
======

::

  OPTION = VALUE

Lines starting with a *#* character are being ignored.

OPTIONS
=======

Configuration options:

PERSONALITY
  Current *personality* of this instance of the metadata server. Valid values
  are *master*, *shadow* and *ha-cluster-managed*. If the installation is
  managed by an HA cluster the only valid value is *ha-cluster-managed*,
  otherwise the only valid values are *master* and *shadow*, in which case
  only one metadata server in LizardFS shall have *master* personality. ::

    PERSONALITY = master

  means that this instance of metadata server acts as the main metadata server
  governing all file system metadata modifications. ::

    PERSONALITY = shadow

  means that this instance of the metadata server acts as backup metadata
  server  ready for immediate deployment as the new *master* in case of a
  failure of the current *master*.

  Metadata server personality can be changed at any moment as long as one
  changes personality from *shadow* to *master*, changing personality the
  other way around is forbidden. Note that this restriction only applies
  when trying to change the personality of a *running* master. You may
  change the personality from master to shadow if you restart the master
  service.::

    PERSONALITY = ha-cluster-managed

  means that this instance is managed by HA cluster, server runs in *shadow*
  mode as long as its not remotely promoted to *master*.

DATA_PATH
  where to store metadata files and lock file

WORKING_USER
  user to run daemon as

WORKING_GROUP
  group to run daemon as (optional - if empty then the default user group will
  be used)

SYSLOG_IDENT
  name of the process to place in syslog messages (default is mfsmaster)

LOCK_MEMORY
  whether to perform mlockall() to avoid swapping out mfsmaster process
  (default is 0, i.e. no)

NICE_LEVEL
  nice level to run daemon with (default is -19 if possible; note: process
  must be started as root to increase priority)

EXPORTS_FILENAME
  alternative name of the *mfsexports.cfg* file

TOPOLOGY_FILENAME
  alternative name of the *mfstopology.cfg* file

CUSTOM_GOALS_FILENAME
  alternative name of the *mfsgoals.cfg* file

PREFER_LOCAL_CHUNKSERVER
  If a client mountpoint has a local chunkserver, and a given chunk happens to
  reside locally, then mfsmaster will list the local chunkserver first.
  However, when the local client mount is issuing many read(s)/write(s), to
  many local chunks, these requests can overload the local chunkserver and
  disk subsystem. Setting this to 0(the default is 1) means that remote
  chunkservers will be considered as equivalent to the local chunkserver.

  This is useful when the network is faster than the disk, and when there is
  high-IO load on the client mountpoints.

BACK_LOGS
  number of metadata change log files (default is 50)

BACK_META_KEEP_PREVIOUS
  number of previous metadata files to be kept (default is 1)

AUTO_RECOVERY
  when this option is set (equals 1) master will try to recover metadata from
  changelog when it is being started after a crash; otherwise it will refuse
  to start and *mfsmetarestore* should be used to recover the metadata
  (default setting is 0)

REPLICATIONS_DELAY_INIT
  DEPRECATED - see *OPERATIONS_DELAY_INIT*

REPLICATIONS_DELAY_DISCONNECT
  DEPRECATED - see *OPERATIONS_DELAY_DISCONNECT*

OPERATIONS_DELAY_INIT
  initial delay in seconds before starting chunk operations (default is 300)

OPERATIONS_DELAY_DISCONNECT
  chunk operations delay in seconds after chunkserver disconnection (default
  is 3600)

MATOML_LISTEN_HOST
  IP address to listen on for metalogger connections (* means any)

MATOML_LISTEN_PORT
  port to listen on for metalogger connections (default is 9419)

MATOML_LOG_PRESERVE_SECONDS
  how many seconds of change logs have to be preserved in memory (default is
  600; note: logs are stored in blocks of 5k lines, so sometimes the real
  number of seconds may be bit bigger; zero disables extra logs storage)

MATOCS_LISTEN_HOST
  IP address to listen on for chunkserver connections (\* means any)

MATOCS_LISTEN_PORT
  port to listen on for chunkserver connections (default is 9420)

MATOCL_LISTEN_HOST
  IP address to listen on for client (mount) connections (\* means any)

MATOCL_LISTEN_PORT
  port to listen on for client (mount) connections (default is 9421)

MATOTS_LISTEN_HOST
  IP address to listen on for tapeserver connections (\* means any)

MATOTS_LISTEN_PORT
  Port to listen on for tapeserver connections (default is 9424)

CHUNKS_LOOP_MAX_CPS
  Chunks loop shouldn't check more chunks per seconds than given number
  (default is 100000)

CHUNKS_LOOP_MIN_TIME
  Chunks loop will check all chunks in specified time (default is 300) unless
  *CHUNKS_LOOP_MAX_CPS* will force slower execution.

CHUNKS_LOOP_PERIOD
  Time in milliseconds between chunks loop execution (default is 1000).

CHUNKS_LOOP_MAX_CPU
  Hard limit on CPU usage by chunks loop (percentage value, default is 60).

CHUNKS_SOFT_DEL_LIMIT
  Soft maximum number of chunks to delete on one chunkserver (default is 10)

CHUNKS_HARD_DEL_LIMIT
  Hard maximum number of chunks to delete on one chunkserver (default is 25)

CHUNKS_WRITE_REP_LIMIT
  Maximum number of chunks to replicate to one chunkserver (default is 2)

CHUNKS_READ_REP_LIMIT
  Maximum number of chunks to replicate from one chunkserver (default is 10)

ENDANGERED_CHUNKS_PRIORITY
  Percentage of endangered chunks that should be replicated with high priority.
  Example: when set to 0.2, up to 20% of chunks served in one turn would be
  extracted from endangered priority queue.

  When set to 1 (max), no other chunks would be processed as long as there are
  any endangered chunks in the queue (not advised)

  (default is 0, i.e. there is no overhead for prioritizing endangered chunks).

ENDANGERED_CHUNKS_MAX_CAPACITY
  Max capacity of endangered chunks queue. This value can limit memory usage
  of master server if there are lots of endangered chunks in the system.
  This value is ignored if ENDANGERED_CHUNKS_PRIORITY is set to 0.
  (default is 1Mi, i.e. no more than 1Mi chunks will be kept in a queue).

ACCEPTABLE_DIFFERENCE
  The maximum difference between disk usage on chunkservers that doesn't
  trigger chunk re balancing
  (default is 0.1, i.e. 10%).

CHUNKS_REBALANCING_BETWEEN_LABELS
  When balancing disk usage, allow moving chunks between servers with
  different labels
  (default is 0, i.e. chunks will be moved only between servers with the same
  label).

REJECT_OLD_CLIENTS
  Reject **mfsmounts** older than 1.6.0 (0 or 1, default is 0). Note that
  *mfsexports* access control is NOT used for those old clients.

GLOBALIOLIMITS_FILENAME
  Configuration of global I/O limits (default is no I/O limiting)

GLOBALIOLIMITS_RENEGOTIATION_PERIOD_SECONDS
  How often mountpoints will request bandwidth allocations under constant,
  predictable load (default is 0.1)

GLOBALIOLIMITS_ACCUMULATE_MS
  After inactivity, no waiting is required to transfer the amount of data
  equivalent to normal data flow over the period of that many milliseconds (
  default is 250)

METADATA_CHECKSUM_INTERVAL
  how often metadata checksum shall be sent to backup servers (default is:
  every 50 metadata updates)

METADATA_CHECKSUM_RECALCULATION_SPEED
  how fast should metadata be recalculated in the background (default : 100
  objects per function call)

DISABLE_METADATA_CHECKSUM_VERIFICATION
  should checksum verification be disabled while applying changelog

NO_ATIME
  when this option is set to 1 inode access time is not updated on every
  access, otherwise (when set to 0) it is updated (default is 0)

METADATA_SAVE_REQUEST_MIN_PERIOD
  minimal time in seconds between metadata dumps caused by requests from shadow
  masters (default is 1800)

SESSION_SUSTAIN_TIME
  Time in seconds for which client session data (e.g. list of open files)
  should be sustained in the master server after connection with the client
  was lost. Values between 60 and 604800 (one week) are accepted. (default is
  86400)

USE_BDB_FOR_NAME_STORAGE
  When this option is set to 1 Berkley DB is used for storing file/directory
  names in file (DATA_PATH/name_storage.db). By default all strings are kept
  in system memory. (default is 0)

BDB_NAME_STORAGE_CACHE_SIZE
  Size of memory cache (in MB) for file/directory names used by Berkeley DB
  storage. (default is 10)

FILE_TEST_LOOP_MIN_TIME
  The test files loop will try to check all files within the specified time
  given in seconds (default is 300).
  It is possible for the loop to take more time if the master server is busy
  or the machine doesn't have enough processing power to make all the needed
  calculations.

AVOID_SAME_IP_CHUNKSERVERS
  When this option is set to 1, process of selecting chunkservers for chunks
  will try to avoid using those that share the same ip. (default is 0)

SNAPSHOT_INITIAL_BATCH_SIZE
  This option can be used to specify initial number of snapshotted nodes that
  will be atomically cloned before en queuing the task for execution in
  fixed-sized batches. (default is 1000)

SNAPSHOT_INITIAL_BATCH_SIZE_LIMIT
  This option specifies the maximum initial batch size set for snapshot
  request. (default is 10000)

Options below are mandatory for all Shadow instances:

MASTER_HOST
  address of the host running LizardFS metadata server that currently acts as
  *master*

MASTER_PORT
  port number where LizardFS metadata server currently running as *master*
  listens for connections from shadows and metaloggers (default is 9420)

MASTER_RECONNECTION_DELAY
  delay in seconds before trying to reconnect to metadata server after
  disconnection (default is 1)

MASTER_TIMEOUT
  timeout (in seconds) for metadata server connections (default is 60)

LOAD_FACTOR_PENALTY
  When set, percentage of load will be added to a chunkserver disk usage
  while determining the most fitting chunkserver. Heavy loaded chunkservers
  will be picked for operations less frequently.
  (default is 0, correct values are in the range of 0 to 0.5)

SNAPSHOT_INITIAL_BATCH_SIZE
  This option can be used to specify initial number of snapshotted nodes that
  will be atomically cloned before en queuing the task for execution in
  fixed-sized batches. (default is 1000)

.. note:: Chunks in master are tested in loop. Speed (or frequency) is
   regulated by the two options *CHUNKS_LOOP_MIN_TIME* and
   *CHUNKS_LOOP_MAX_CPS*. The first one defines the minimal time of the loop
   and the second one the maximal number of chunk tests per second. Typically
   at the beginning, when the number of chunks is small, time is constant,
   regulated by *CHUNK_LOOP_MIN_TIME*, but when the number of chunks becomes
   bigger then the time of the loop can increase according to
   *CHUNKS_LOOP_MAX_CPS*.

Deletion limits are defined as *soft* and *hard* limit. When the number of
chunks to delete increases from loop to loop, the current limit can be
temporary increased above the soft limit, but never above the hard limit.

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

mfsmaster(8), mfsexports.cfg(5), mfstopology.cfg(5)
