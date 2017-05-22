*******************
Installing LizardFS
*******************
.. auth-status-proof1/none

.. _get_and_install:

Getting and installing LizardFS
===============================

There are several methods for getting LizardFS software. The easiest and most
common method is to get packages by adding repositories for use with package
management tools such as the Advanced Package Tool (APT) or Yellowdog Updater,
Modified (YUM). You may also retrieve pre-compiled packages from the LizardFS
repository. Finally, you can retrieve tarballs or clone the LizardFS source
code repository and build LizardFS yourself.


.. _get_and_install_debian:

Installing from Debian packages
+++++++++++++++++++++++++++++++

First, add a our key which is needed to verify the signatures of LizardFS
packages::

   # wget -O - http://packages.lizardfs.com/lizardfs.key | apt-key add -

Now add a proper entry in /etc/apt/sources.list.d/

For Debian do::

   # apt-get install lsb-release
   # echo "deb http://packages.lizardfs.com/debian/$(lsb_release -sc) $(lsb_release -sc) main" > /etc/apt/sources.list.d/lizardfs.list
   # echo "deb-src http://packages.lizardfs.com/debian/$(lsb_release -sc) $(lsb_release -sc) main" >> /etc/apt/sources.list.d/lizardfs.list

For Ubuntu do::

   # echo "deb http://packages.lizardfs.com/ubuntu/$(lsb_release -sc) $(lsb_release -sc) main" > /etc/apt/sources.list.d/lizardfs.list
   # echo "deb-src http://packages.lizardfs.com/ubuntu$(lsb_release -sc) $(lsb_release -sc) main" >> /etc/apt/sources.list.d/lizardfs.list

This will have created the lizardfs.list file. To use the newly added
repository, update the packages index::

   # apt-get update

Now you are able to install LizardFS packages (listed below) using::

   # apt-get install <package>

It is also possible to download the source package using::

   # apt-get source lizardfs

.. important:
   Before upgrading any existing LizardFS installation, please read the
   instructions here: :ref:`upgrading`

LizardFS consists of the following packages:

* lizardfs-master – LizardFS master server
* lizardfs-chunkserver – LizardFS data server
* lizardfs-client – LizardFS client
* lizardfs-adm – LizardFS administration tools (e.g, lizardfs-probe)
* lizardfs-cgi – LizardFS CGI Monitor
* lizardfs-cgiserv – Simple CGI-capable HTTP server to run LizardFS CGI Monitor
* lizardfs-metalogger – LizardFS metalogger server
* lizardfs-common – LizardFS common files required by lizardfs-master,
  lizardfs-chunkserver and lizardfs-metalogger
* lizardfs-dbg – Debugging symbols for all the LizardFS binaries


Installing from RedHAT EL / CentOS Packages
+++++++++++++++++++++++++++++++++++++++++++

First, add a file with information about the repository:

for RHEL 6 and CentOS 6::

   # curl http://packages.lizardfs.com/yum/el6/lizardfs.repo > /etc/yum.repos.d/lizardfs.repo
   # yum update

for RHEL 7 and CentOS 7::

   # curl http://packages.lizardfs.com/yum/el7/lizardfs.repo > /etc/yum.repos.d/lizardfs.repo
   # yum update

To get libjudy which is used by parts of LizardFS, install the epel repository for RHEL 7::

   yum install epel-release

Now you are able to install LizardFS packages (listed below) using::

   # yum install <package>

It is also possible to download the source package (SRPM) using::

   # yum install yum-utils
   # yumdownloader --source lizardfs

..important: Before upgrading any existing LizardFS installation, please read the instructions here: :ref:`upgrading` .

LizardFS consists of following packages:

* lizardfs-master – LizardFS master server
* lizardfs-chunkserver – LizardFS data server
* lizardfs-client – LizardFS client
* lizardfs-adm – LizardFS administration tools (e.g, lizardfs-probe)
* lizardfs-cgi – LizardFS CGI Monitor
* lizardfs-cgiserv – Simple CGI-capable HTTP server to run LizardFS CGI Monitor
* lizardfs-metalogger – LizardFS metalogger server
* lizardfs-debuginfo – (CentOS 7 / RHEL 7 only) Debugging symbols and sources for all the LizardFS binaries

Installing LizardFS from downloaded .deb packages
+++++++++++++++++++++++++++++++++++++++++++++++++

Make sure to install the *lizardfs-common* package first before installing
other packages.

Also, remember to install lizardfs-cgi before installing lizardfs-cgiserv

In order to install a .deb package, run::

   # dpkg -i <package>

If installing fails due to dependency problems, run:

   # apt-get -f install

.. _get_and_install_from_source:

Installing LizardFS from source
+++++++++++++++++++++++++++++++

Installing LizardFS from source.


The current LizardFS source code can be obtained from our :ref:`github`
(https://github.com/lizardfs/lizardfs) project page.
You can either download a tarball from there by choosing the respective
version in the **Branch** tab on the left or use :ref:`git` to clone the
sourcetree.

LizardFS uses :ref:`CMake` as its build system. To compile the sources, follow
the directions outlined below.

1. Create a build directory inside the source directory::

    cd lizardfs-source
    mkdir build

2. Run *cmake ..* inside the build directory. Useful options include
   *-DCMAKE_INSTALL_PREFIX*, *-DCMAKE_BUILD_TYPE* as well as various
   LizardFS-specific *-DENABLE_...* options. Options are listed when
   cmake is ran and can be changed by re-running cmake::

    cd build
    cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/lizardfs

3. Run make in the build directory::

    make

4. Run make install to install files (you may need to be root)::

    make install

5. Now continue to the configuration pages.


If you want to participate in developing LizardFS, please refer to the
:ref:`devguide` and the :ref:`participation_rules`.



