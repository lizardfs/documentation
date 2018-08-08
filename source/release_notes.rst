##########
Release Notes
##########
.. auth-status-writing/none

*******
Release 3.13.0-rc1
*******
Date: 2018-07-14
 
**Assets**

* https://github.com/lizardfs/lizardfs/archive/v3.13.0-rc1.zip
* https://github.com/lizardfs/lizardfs/archive/v3.13.0-rc1.tar.gz
  
  
**Features**

* uRaft HA
* fixes to EC handling
* nfs-ganesha plugin changed to use only C code
* reduced number of secondary group retrievals
* new fuse3 client
* many fixes

**Detailed info**

* uRaft HA
uRaft is HA solution designed for use with LizardFS. It allows for seamless switching
of  the master server in case of hardware failure. More information about uRaft is available
in LizardfFS Handbook (https://docs.lizardfs.com/adminguide/advanced_configuration.html#deploying-lizardfs-as-a-ha-cluster)

* fixes to EC handling
After extensive tests we decided to improve the mechanism of calculating parities greater than 4 e.g EC( 6,5) After this upgrade the system will show chunks of parities as endangered until the system automatically recalculates. 

* nfs-ganesha plugin changed to use only C code
In preparation for moving LizardFS nfs-ganesha plugin to official nfs-ganesha repository,
we had to remove all occurrences of C++ code and replace it with plain C.

* reduced number of secondary group retrievals
In LizardFS we introduced handling of secondary groups. Unfortunately the function to retrieve
secondary groups in FUSE library used a lot of CPU resources. Thanks to removing
unnecessary calls to this function, mount performance increased significantly.

* added fuse3 client
LizardFS now includes mount3 client which uses FUSE3 library. Thanks to new features in FUSE3,
now the mount performs much better in many scenarios. Here are the most important changes visible
to LizardFS users:

* big_writes option is now enabled by default (not recognized as a parameter anymore).
* added writeback_cache option which with kernel 3.14 and later improving performance significantly
* increased read/write performance (specially for small operations)

Because most of the Linux distributions don't include FUSE3 library, we have build FUSE3 packages
and made them available on the LizardFS website (https://lizardfs.com/download)


*******
Release 3.12.0
*******
Date: 2017-12-21

**Assets**

* https://github.com/lizardfs/lizardfs/archive/v3.12.0.zip
* https://github.com/lizardfs/lizardfs/archive/v3.12.0.tar.gz

**Features**

* C API
* nfs-ganesha plugin
* RichACL - a new POSIX + NFSv4 compatible ACL standard
* OSX ACL support through osxfuse
* ACL in-memory deduplication
* client readahead enabled by default
* file lock fixes
* AVX2 support for erasure code goals
* MinGW compilation fixes
* more flexible chunkserver options
* many fixes

**Detailed info**

* C API
LizardFS 3.12 comes with liblizardfs-client library and C language API header.
It's now possible to build programs/plugins with direct support for LizardFS operations,
no FUSE needed. For reference, see:
src/mount/client/lizardfs_c_api.h
src/data/liblizardfs-client-example.c

For those building LizardFS from source, pass a -DENABLE_CLIENT_LIB=YES flag to cmake
in order to make sure you're building client library as well.

* nfs-ganesha plugin
Our official plugin for Ganesha NFS server is included as well. This plugin enables
a LizardFS FSAL (File System Abstraction Layer) to Ganesha, which is then used
to access LizardFS clusters directly. Our new plugin is pNFS and NFSv4.1 friendly.

For those building LizardFS from source, pass a -DENABLE_NFS_GANESHA=YES flag to cmake in order to make sure you're building client library as well.

* RichACL
In order to extend POSIX access control list implementation we introduced RichACL support.
Backward compatibility with POSIX ACLs is guaranteed. Additionally, it's possible to use NFSv4-style ACL tools (nfs4_getfacl/nfs4_setfacl) and RichACL tools (getrichacl/setrichacl) to manage more complicated access control rules.

* OSX ACL
Setting/getting ACLs is also possible on OSX via both command line chmod/ls -e interface and desktop.

* File lock fixes
Global file locking mechanism is now fully fixed and passes all NFS lock tests from connectathon suite.

* AVX2
Erasure code goal computing routines now take full advantage of AVX2 processor extensions.

* MinGW
LizardFS is now bug-free again for MinGW cross-compiling.

* Chunkserver options
Replication limits are now fully configurable in chunkserver config.
Also, chunk test (a.k.a. scrubbing) has 1 millisecond precision now instead of previous 1 second, which allows users to turn on more aggressive scrubbing with simple chunkserver reload.

*******
Release 3.11.1 -- 3.11.3
*******
Date: 2017-07-13

**Assets**

* https://github.com/lizardfs/lizardfs/archive/v3.11.3.zip
* https://github.com/lizardfs/lizardfs/archive/v3.11.3.tar.gz

**Features**
Bugfix releases, here's what we fixed:

* master: fix issues with reporting defective files
* mount: fix request size in read cache for empty results
* master: fix high cpu usage in fs_periodic_file_test
* master: fix dangling nodes in defective files list
* mount: fix direntry cache bug for repeated paths
* fixed wrong version number in 3.1.1

*******
Release 3.11.0
*******
Date: 2017-05-11

**Assets**

* https://github.com/lizardfs/lizardfs/archive/v3.11.0.zip
* https://github.com/lizardfs/lizardfs/archive/v3.11.0.tar.gz

**Features**

* master: improve ACL implementation
* master: add option to avoid same-ip chunkserver replication
* master: add minimal goal configuration option
* master: reimplement directory entry cache for faster lookups
* master: add whole-path lookups
* master: chunkserver add chunkserver load awareness
* mount: add readahead to improve sequential read perfromance
* mount: add secondary groups support
* tools: add correct-only flag to filerepair
* tools: add -s and -i options to snapshot command
* tools: add recursive remove operations (for removing large directories
* and snapshots)
* tools: add tool for stopping execution of tasks (snapshot, recursive remove, etc.)
* all: change to semantic versioning system
* all: many fixes

**Detailed info**

* Readahead
Clients can now benefit from integrated readahead mechanism.
In order to enable readahead, please mount with the following options:
-o cacheexpirationtime={MSEC}
-o readaheadmaxwindowsize={KB}
Example:
mfsmount -o cacheexpirationtime=1000 -o readaheadmaxwindowsize=8192

* Recursive remove
A tool for removing large directories/snapshots is finally implemented.
Example:
lizardfs rremove big_directory/
lizardfs rremove -h

* Tools for managing tasks
Two administration tools are available for managing long tasks:
lizardfs-admin list-tasks
lizardfs-admin stop-task
Run above commands for detailed usage information.

* Secondary groups support
LizardFS is now able to fully recognize secondary groups of users
and take them into account while evaluating permissions.

*******
Release 3.10.6
*******
Date: 2017-01-17

**Assets**

* https://github.com/lizardfs/lizardfs/archive/v3.10.6.zip
* https://github.com/lizardfs/lizardfs/archive/v3.10.6.tar.gz

**Features**
This release provides fixes only:

* (master) judy library fixes
* (master) ARM compilation fixes

*******
Release 3.10.4
*******
Date: 2017-10-19

**Assets**

* https://github.com/lizardfs/lizardfs/archive/v3.10.4.zip
* https://github.com/lizardfs/lizardfs/archive/v3.10.4.tar.gz

**Features**

* task manager performance improvements (speeding up massive metadata
* operations: snapshots, setting trash time, setting goal, etc.)
* fixing an error in trash files that caused #487 and #489 github issues
* other minor fixes and improvements

*******
Release 3.10.4
*******
Date: 2016-09-14

**Assets**

* https://github.com/lizardfs/lizardfs/archive/v3.10.2.zip
* https://github.com/lizardfs/lizardfs/archive/v3.10.2.tar.gz

**Features**

Master:

* redesign in-memory representation of file system objects - at least 30% reduction in RAM usage
* name storage: a possibility to keep all file names in BerkeleyDB, thus saving even more RAM
* redesign of trash - increased performance, reduced RAM usage and CPU pressure
* huge boost of responsiveness - lengthy operations split into asynchronous bits
* OPERATIONS_DELAY config entries, which allow postponing metadata operations on restart/disconnect
* mount: make big snapshot, setgoal and settrashtime operations asynchronous to improve responsiveness
* fix improper handling of endangered chunks

Chunkserver:

* memory optimizations - at least 60% reduction in RAM usage
* introduce smart descriptor management

Tools:

* brand new lizardfs command, a unified replacement for mfs* tools with prompt and bash completion

Other:

* various fixes and community requests

**Detailed info**

Master’s memory and CPU
With 3.10.2, the master is much more memory-efficient and responsive. RAM usage reduction was accomplished through redesigning the way it keeps metadata in memory, adding a possibility to keep some metadata in on-disk database (see USE_BDB_FOR_NAME_STORAGE in mfsmaster.cfg file for reference). Responsiveness was dramatically increased by recognizing all potentially lengthy operations and splitting their execution in smaller time bits. It applied to both in-master maintenance procedures and client’s requests like snapshotting/changing goal of very big directories.

lizardfs tool:
3.10.2 comes with new client tool: lizardfs utility. See man lizardfs, lizardfs -h for details. Aside from known functionalities like setting/getting goals, making snapshots, etc. it comes with bash-like prompt and bash completion.

Examples:
lizardfs setgoal -r ec32 a/

lizardfs makesnapshot dira/ dirb/

lizardfs fileinfo a/*

lizardfs <<EOF
fileinfo a/*
setgoal -r 3 a
getgoal a/2
EOF

What’s next:
In next release, paths and build system is to be unified with the one from official Debian repository (e.g. configuration directory will officially become /etc/lizardfs). Also, more asynchronous client commands are coming including recursive-remove operation. A so called “minimal goal setting”, which will probably be named MIN_REDUNDANCY_LEVEL is being implemented as well. Finally, more news on native HA (μRaft) will appear.

*******
Release 3.10
*******
Date: 2016-08-04

**Assets**

* https://github.com/lizardfs/lizardfs/archive/v.3.10.0.zip
* https://github.com/lizardfs/lizardfs/archive/v.3.10.0.tar.gz

**Features**

* erasure code goals (aka K+M goals)
* per directory quotas
* improved interaction with legacy chunkservers and mounts
* ports for OSX and FreeBSD
* updated mfsfileinfo output with xor/ec goals
* many fixes

**Detailed info**

* Erasure code goals

For each file using ec(K+M) goal, the system will split the file into K parts and generate M parity parts. Any K parts are required to be able to reproduce file contents.

If labels are specified, parts will be kept on chunkservers with these labels. Otherwise, default wildcard labels will be used.

This kind of goal allows M of K+M copies to be lost and the file would still remain accessible. Erasure code goal occupies M/K extra space.

Please note that minimal K value is 2 and minimal M value is 1.

Examples of new goal configuration:
5 ec32 : $ec(3,2){ A B _ _ _ }
6 ec43 : $ec(4,3)

* Per directory quotas

It is now possible to set inode/size limits per directory.
In case of multiple quota rules, the most restrictive one is always effective.
Example:

mfssetquota -d 10M 100M 50M 1G /mnt/lizardfs/a/directory

* Improved interaction with legacy chunkservers and mounts

Pre-2.6.0 mounts and chunkservers used to be not fully compatible with 3.9.x servers, which complicated the upgrade process. Those issues are now solved - new mounts are perfectly capable of communicating with legacy chunkservers and vice versa.
This rule has one exception: for consistency reasons, replication from new chunkservers to old ones is disabled.

* Ports for OSX and FreeBSD

LizardFS is now buildable for those systems.

Fixes:

* denying replication during scan
* atomicity of replication process
* sending proper error codes to master
* proper handling of replication limits during rebalancing
* removal of splice call
* removing possible livelock in master networking
* adding missing update in inodes id pool

Next release (unstable now) will contain a massive set of patches which make the cluster more responsive.
Also, a great reduction of master's and chunkserver's RAM usage is to be expected (at least 30% less resources needed).
An improved client tool for managing goals/quotas/files etc. is coming as well.
