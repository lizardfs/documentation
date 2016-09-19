.. _lizardfs-admin.8:

*****************
lizardfs-admin(8)
*****************


NAME
====

lizardfs-admin, lizardfs-probe - LizardFS monitoring and administration tool

SYNOPSIS
========

::

  lizardfs-admin  COMMAND [OPTIONS...] [ARGUMENTS...]

Available COMMANDs
==================


chunks-health <master ip> <master port>
  Returns chunks health reports in the installation.
  By default (if no report is specified) all reports will be shown.
  In replication and deletion states, the column means the number of chunks
  with number of copies specified in the label to replicate/delete.

  Possible command-line options:

  --availability
    Print report about availability of chunks.
  --replication
    Print report about about number of chunks that need replication.
  --deletion
    Print report about about number of chunks that need deletion.

info <master ip> <master port>
  Prints statistics concerning the LizardFS installation.

iolimits-status <master ip> <master port>
  Prints current configuration of global I/O limiting

list-chunkservers <master ip> <master port>
  Prints information about all connected chunkservers.

list-disks <master ip> <master port>
  Prints information about all connected chunkservers.

  Possible command-line options:

  --verbose
    Be a little more verbose and show operations statistics.

list-goals <master ip> <master port>
  List goal definitions.

  Possible command-line options:

  --pretty
    Print nice table

list-mounts <master ip> <master port>
  Prints information about all connected mounts.

  Possible command-line options:

  --verbose
    Be a little more verbose and show goal and trash time limits.

metadataserver-status <master ip> <master port>
  Prints status of a master or shadow master server

list-metadataservers <master ip> <master port>
  Prints status of active metadata servers.

ready-chunkservers-count <master ip> <master port>
  Prints number of chunkservers ready to be written to.

promote-shadow <shadow ip> <shadow port>
  Promotes metadata server. Works only if personality 'ha-cluster-managed' is used.
  Authentication with the admin password is required.

stop-master-without-saving-metadata <master ip> <master port>
  Stop the master server without saving metadata in the metadata.mfs file.
  Used to quickly migrate a metadata server (works for all personalities).
  Authentication with the admin password is required.

reload-config <master ip> <master port>
  Requests reloading configuration from the config file.
  This is synchronous (waits for reload to finish).
  Authentication with the admin password is required.

save-metadata <metadataserver ip> <metadataserver port>
    Requests saving the current state of metadata into the metadata.mfs file.
    With --async fail if the process cannot be started, e.g. because the
    process is already in progress. Without --async, fails if either the
    process cannot be started or if it finishes with an error (i.e., no
    metadata file is created).

    Authentication with the admin password is required.

    Possible command-line options:

    --async
      Don't wait for the task to finish.

COMMON COMMAND OPTIONS
======================


--porcelain
  Make the output parsing-friendly.

REPORTING BUGS
==============

Report bugs to <contact@lizardfs.org>.


COPYRIGHT
=========

2015-2016 Skytechnology Sp. z o.o.

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

lizardfs(7)
