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




On Mac OS/X
===========

Compiling software like LizardFS on MacOS/X requires some additional software
to be installed on your Mac. You will need to install xcode from Apple and
than issue::

  xcode-select --install

to add the command line tools to your system.

To get all the goodies from the current LizardFS, you will require to build
LizardFS with gcc6 and the latest :ref:`osxfuse` library.

We have had good experiences with using :ref:`homebrew` for adding open source
software to MaxOS/X and would like to recommend to developers to use it to add
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
Xcode, eclipse, netbeans or whatever else fickles your fancy.



On FreeBSD
==========

