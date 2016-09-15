# lizardfs-new-documentation
A take at a new documentation for the LizardFS project

Requires sphinx (http://www.sphinx-doc.org/en/stable/tutorial.html) to build

Documentation Rules
===================

Headers:

First Level:    ##############

Second Level:   **************

Third Level:    ==============

Fourth Level:   ++++++++++++++

Fifth Level:    --------------

ToC depth: 2 Levels

Subdirectories are for separate manuals that should be buildable standalone.

The manual pages should be buildable as man pages standalone.

Toolchain for specific Systems
==============================
Tips for installing the document-formatting-tools for building the
documentation (sphinx). 

debian8 (jessie)
++++++++++++++++++++++++++
Best way to get the documentation formatting-tools running is:

 * apt-get install python-pip
 * pip install Sphinx

This should be enough to build the html-documentation. 
If you want pdf also you will need texlive/pdflatex - caution, that one is 
really a *large* set of software. 

