.. _workspace:

**********************************
Setting up a development workspace
**********************************
.. auth-status-todo/none

General
=======

LizardFS does not have too many dependences, so it is relatively simple to
develop on any platform you would like.

On Linux
========



.. _workspace_mac:

On Mac OS/X
===========

Compiling software like LizardFS on MacOS/X requires some additional software
to be installed on your Mac. You will need to install :ref:`xcode` from Apple
and than issue::

  xcode-select --install

to add the command line tools to your system.

To get all the goodies from the current LizardFS, you will require to build
LizardFS with :ref:`gcc` 6 and the latest :ref:`osxfuse` library.

We have had good experiences with using :ref:`homebrew` for adding open source
software to MacOS/X and would like to recommend to developers to use it to add
all additional software required.

To install homebrew, issue the following at your command prompt::

  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Than to install :ref:`cmake` issue::

  brew install cmake

and finally gcc6 with::

  brew install homebrew/versions/gcc6

To generate manpages please also add the :ref:`pandoc` document format
translator::

  brew install pandoc

And last but not least, if you would like to generate documentation as well,
install the sphinx documentation engine::

  brew install sphinx-doc

As on any other OS we have no preferences for a IDE on MacOS/X. You can use
Xcode, eclipse, netbeans or whatever else fickle's your fancy.

Our Documentation maintainer uses `Sublime Text 3 <http://www.sublimetext.com/>`_ and swears that it is the best editor since the
invention of writing, but YMMV ;)

To build with your installed gcc6 you will need to set the following variables
in your environment before invoking :ref:`cmake`::

  export CC=/usr/local/gcc6
  export CXX=/usr/local/g++-6
  export CPP=/usr/local/gcc6

homebrew is also the perfect place to get git and additions to git and gerrit.

Some people had good experiences using `SmartGIT <http://www.syntevo.com/smartgit/>`_ but its not free.

Now you are ready to compile a fully featured LizardFS package on your Mac.

On FreeBSD
==========

.. note:: At the time of the editing of this article, FreeBSD 11 is about to
   be released so all the instructions are for FreeBSD 11.

To create a working development environment on FreeBSD there are a range of
ports or packages you will need to install::

  gcc6
  binutils
  bash
  gmake
  cmake
  git

The packages will install other dependencies required automagically.

For building the manpages and documentation you will require additionaly::

  hs-pandoc
  hs-pandoc-types
  py27-sphinx-1.4.4

For linking to the right gcc version, you should set::

  export LDFLAGS=-Wl,-rpath=/usr/local/lib/gcc6

in your environment.

For making bash work correctly, please add the following to /etc/fstab::

  fdesc         /dev/fd         fdescfs rw      0   0

Before you can build LizardFS with your newly setup build envionment, please
set the following variables in your environment or add them to your .bashrc::

  export CC=/usr/local/gcc6
  export CXX=/usr/local/g++-6
  export CPP=/usr/local/gcc6
  export MAKE=/usr/local/bin/gmake
  export SHELL=/usr/local/bin/bash

We also strongly suggest to build LizardFS while working inside bash.




