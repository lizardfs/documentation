##########
Release Notes
##########
.. auth-status-writing/none

*******
Release 3.13.0-rc1
*******

**Assets**
  https://github.com/lizardfs/lizardfs/archive/v3.13.0-rc1.zip
  https://github.com/lizardfs/lizardfs/archive/v3.13.0-rc1.tar.gz
  
  
Featuring:
* uRaft HA
* fixes to EC handling
* nfs-ganesha plugin changed to use only C code
* reduced number of secondary group retrievals
* new fuse3 client
* many fixes

Detailed info:
* uRaft HA *
uRaft is HA solution designed for use with LizardFS. It allows for seamless switching
of  the master server in case of hardware failure. More information about uRaft is available
in LizardfFS Handbook (https://docs.lizardfs.com/index.html)

* fixes to EC handling *
After extensive tests we decided to improve the mechanism of calculating parities greater than 4 e.g EC( 6,5) After this upgrade the system will show chunks of parities as endangered until the system automatically recalculates. 

* nfs-ganesha plugin changed to use only C code *
In preparation for moving LizardFS nfs-ganesha plugin to official nfs-ganesha repository,
we had to remove all occurrences of C++ code and replace it with plain C.

* reduced number of secondary group retrievals *
In LizardFS we introduced handling of secondary groups. Unfortunately the function to retrieve
secondary groups in FUSE library used a lot of CPU resources. Thanks to removing
unnecessary calls to this function, mount performance increased significantly.

* added fuse3 client *
LizardFS now includes mount3 client which uses FUSE3 library. Thanks to new features in FUSE3,
now the mount performs much better in many scenarios. Here are the most important changes visible
to LizardFS users:

* big_writes option is now enabled by default (not recognized as a parameter anymore).
* added writeback_cache option which with kernel 3.14 and later improving performance significantly
* increased read/write performance (specially for small operations)

Because most of the Linux distributions don't include FUSE3 library, we have build FUSE3 packages
and made them available on the LizardFS website (https://lizardfs.com/download)
