.. _workspace:

**********************************
Setting up a development workspace
**********************************
.. auth-status-todo/none

General
=======

LizardFS does not have too many dependences, so it is easy to develop on any platform you like.

On Linux
========

.. _workspace_debian:

Debian / Ubuntu
---------------

Installing all required dependencies on Debian based distributions is easy – just run:

  apt install git cmake g++ libspdlog-dev libfuse3-dev libfuse-dev fuse isal libisal-dev libboost-all-dev asciidoc-base zlib1g-dev pkg-config libthrift-dev libcrcutil-dev libjudy-dev libpam0g-dev libdb-dev libgtest-dev

and you should be ready to go.

.. _workspace_centos7:

CentoOS-7 / RHEL-7 / SL 7
-------------------------

Luckily the friendly people from CERN have created a complete environment for ``gcc6`` based development. Install the following packages:

  For the backports from Fedora (needed or current cmake and buildtools)::

    sudo yum install epel-release

  For ``gcc6``:

    * On RHEL::

        sudo yum-config-manager --enable rhel-server-rhscl-7-rpms

    * On CentOS and SL::

        sudo yum install centos-release-scl

    * On all of them::

        sudo yum install cmake zlib-devel fuse-devel Judy-devel asciidoc libtool automake autoconf rpm-build rpmlint a2x boost-devel

        sudo yum install devtoolset-6 devtoolset-6-gcc-c++ devtoolset-6-libstdc++-devel

    * If you want to build the ``libisal2`` stuff yurself, add ``yasm and ``nasm`` to the list::

        sudo yum install yasm nasm

To start working with the freshly installed ``gcc6`` toolset, please enter::

  scl enable devtoolset-6 bash

Additional packages required and not provided by standard repos::

  libisal2

These dependencies can be obtained from our CentOS repositories and should work on all 3 enterprise repos.

.. _workspace_centos6:

CentoOS-6 / RHEL-6 / ScientificLinux 6
--------------------------------------

As for the 7 series of the enterprise Linuces, the friendly people from CERN have created a complete environment for ``gcc-6`` based development for all Enterprise Linuces. Install the following packages:

  For the backports from Fedora (needed or current cmake and buildtools)::

    sudo yum install epel-release

  For ``gcc6``:

    * On RHEL::

        sudo yum-config-manager --enable rhel-server-rhscl-7-rpms

    * On Centos and SL::

        sudo yum install centos-release-scl

    * On all of them::

        sudo yum install cmake zlib-devel fuse-devel Judy-devel asciidoc libtool automake autoconf-2.69 rpm-build rpmlint a2x

        sudo yum install devtoolset-6 devtoolset-6-gcc-c++ devtoolset-6-libstdc++-devel

    * If you want to build the ``libisal2`` stuff yurself, add ``yasm`` and ``nasm`` to
      the list::

        sudo yum install yasm nasm

To start working with the freshly installed ``gcc6`` toolset, please enter::

  scl enable devtoolset-6 bash

Additional packages required and not provided by standard repos::

  libisal2, current boost edition, autoconf-2.69.

These dependencies can be obtained from our CentOS repositories and should work on all 3 enterprise repos.

.. _workspace_mac:

Mac OS/X
========

Compiling software like LizardFS on MacOS/X requires some additional software to be installed on your Mac. You will need to install :ref:`xcode` from Apple and than issue::

  xcode-select --install

to add the command line tools to your system.

To get all the goodies from the current LizardFS, you will require to build LizardFS with :ref:`gcc` 6 and the latest :ref:`osxfuse` library.

We have had good experiences with using :ref:`homebrew` for adding open source software to MacOS/X and would like to recommend to developers to use it to add all additional software required.

To install homebrew, issue the following at your command prompt::

  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Than to install :ref:`cmake` issue::

  brew install cmake

and finally ``gcc6`` with::

  brew install homebrew/versions/gcc6

To generate manpages please also add the :ref:`pandoc` document format translator::

  brew install pandoc

And last but not least, if you would like to generate documentation as well, install the ``sphinx`` documentation engine::

  brew install sphinx-doc

As on any other OS we have no preferences for a IDE on MacOS/X. You can use ``Xcode``, ``Eclipse``, ``Netbeans``, ``Sublime Text 3`` or whatever else fickle's your fancy.

To build with your installed ``gcc6`` you will need to set the following variables in your environment before invoking :ref:`cmake`::

  export CC=/usr/local/bin/gcc-6
  export CXX=/usr/local/bin/g++-6
  export CPP=/usr/local/bin/cpp-6

``homebrew`` is also the perfect place to get git and additions to ``git`` and ``gerrit``.

Some people had good experiences using `SmartGIT <http://www.syntevo.com/smartgit/>`_ but it is not free.

What you will require for acceptable ``ec`` speed will be the ``isa-l`` library.

Now you are ready to compile a fully featured LizardFS package on your Mac.

.. _workspace_freebsd:

FreeBSD
=======

.. note:: All the instructions are for FreeBSD 11.

To create a working development environment on FreeBSD there are a range of ports or packages you will need to install::

  gcc6 binutils bash gmake cmake git judy boost

If you want to make use of the storage extensions for Intel platforms by Intel, please install the ``isa-l`` package as well. The packages will install other required dependencies auto-magically.

For building the manpages and documentation you will require additionally::

  hs-pandoc
  hs-pandoc-types
  py-sphinx

For linking to the right gcc version, you should set::

  export LDFLAGS=-Wl,-rpath=/usr/local/lib/gcc6

in your environment.

For making bash work correctly, please add the following to /etc/fstab::

  fdesc         /dev/fd         fdescfs rw      0   0

Before you can build LizardFS with your newly setup build environment, please set the following variables in your environment or add them to your ``.bashrc``::

  export CC=/usr/local/bin/gcc6
  export CXX=/usr/local/bin/g++6
  export CPP=/usr/local/bin/cpp6
  export MAKE=/usr/local/bin/gmake
  export SHELL=/usr/local/bin/bash

We also strongly suggest to build LizardFS while working inside ``bash``.

Make sure your FreeBSD as well as your packages and ports are always up to date.
