.. _lizardfs.7:

***********
lizardfs(7)
***********

NAME
====

lizardFS - a networking, distributed, highly available file system

DESCRIPTION
===========

LizardFS is a networking, highly available, distributed file system. It
spreads data over several physical localizations (servers), which are visible
to a user as one resource. For standard file operations LizardFS acts as other
Unix-alike file systems. It has hierarchical structure (directory tree),
stores file attributes (permissions, last access and modification times) as
well as making it possible to create special files (block and character
devices, pipes and sockets), symbolic links (file names pointing to another
file accessible locally, not necessarily on a LizardFS) and hard links
(different names of files which refer to the same data on LizardFS). Access to
the file system can be limited based on IP address and/or password.

Distinctive features of LizardFS are:

* higher reliability (data can be stored in several copies on separate
  computers)

* dynamically expanding disk space by attaching new computers/disks

* possibility of storing deleted files for a defined period of time ("trash
  bin" service on a file system level)

* possibility of creating snapshot of a file, which means a coherent copy of
  the whole file, even while the file is being written to.


ARCHITECTURE
============

A LizardFS installation consists of five types of machines:

 master metadata server (or 'the master')
   a managing server - single computer managing the whole filesystem, storing
   metadata for every file (information on size, attributes and file
   localization(s), including all information about non-regular files, i.e.
   directories, sockets, pipes and devices.

 metadata server shadows (or 'the shadow master')
   almost identical to the master, there can be any number of those, they work
   as master metadata server backup and they are ready for immediate
   deployment as the new master in case of current master failure.

 data servers (or 'the chunkservers')
   any number of commodity servers storing files data and replicating it among
   themselves (if a certain file is supposed to exist in more than one copy.

 metadata backup servers (or 'the metaloggers')
   any number of servers, all of which store metadata changelogs and
   periodically downloading base metadata file; it's easy to run the mfsmaster
   process on such a machine if the primary master stops working.

 client computers referring to LizardFS stored files (or 'the clients')
   any number of machines with working mfsmount process that communicates with
   the managing server to receive and modify file information and with the
   chunkservers to exchange actual file data.

Metadata is stored in the memory of the managing server and is simultaneously
being saved to disk (as a periodically updated binary file and immediately
updated incremental logs). The main binary file as well as the logs are
replicated to the metaloggers (if present).

File data is divided into fragments (chunks) of a maximum size of 64MB each
which are stored as files on selected disks on the data servers
(chunkservers). Each chunk is saved on different computers in a number of copies equal to a "goal" for the given file.

REPORTING BUGS
==============

Report bugs to <contact@lizardfs.org>.

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

mfschunkserver(8), mfsmaster(8), mfsmetalogger(8), mfsmount(1), lizardfs(1),
lizardfs-admin(8)
