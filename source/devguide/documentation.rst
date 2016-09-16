.. _documentation_howto:

*******************
Documentation-HowTo
*******************
.. auth-status-proof1/none

Welcome to the documenters-project for lizardfs. This pages shall introduce you
to our Tools and Workflows. 

Documentation is written in reStructuredText
(http://docutils.sourceforge.net/rst.html), then we build the different Formats
(html, pdf) with the Help of sphinx (http://www.sphinx-doc.org/en/stable/tutorial.html).

If you want to generate nroff man pages as well, you also will need to install
pandoc (http://pandoc.org/).

==================
Editorial Workflow
==================
.. auth-status-proof1/none

To ease the authoring-process and to uphold quality of our documentation at
least every section goes through the following stages:

#. **todo** (this section needs a helping hand)
#. **writing** (somebody is writing content, others: please dont interfere)
#. **proof1** (proofreading stage 1, somebody with appropriate knowledge checks 
   the written content for correctness regarding facts and for understndability)
#. **proof2** (proofreading stage 2, somebody - preferably a native speaker - 
   checks the content for grammar, spelling etc. No content/fact-changes here,
   if necessary set state back to proof1 and add an todo-remark)
#. **frozen** (this section is done, find another one to work with, there is 
   plenty of work available :)

While authoring the status of a section can go forth and back, writing is not 
a oneway-road...

The implementation of those stages is done with the comment-directive of rst.
Put a line below the section-title like::

  .. auth-status-todo/none
  .. auth-status-writing/<my-own-email>
  .. auth-status-proof1/<my-own-email>
  .. auth-status-proof2/<my-own-email>
  .. auth-status-frozen/none

the part after the "/" indicates *who* is working at the section.  If you just
finished a stage and want to indicate the next stage is to be done by "somebody"
use "none" instead of an email-address.

All in all a section-start should look like::

  =============
  Section-Title
  =============

  .. auth-status-writing/wolfram@example.com

.. note:: This mechanism is meant to make our lives easier, *please* dont 
   use it for commanding others! The only one who is entitled to put an
   email-addres in a authoring-tag is the person owning that address. It is used
   to indicate "i take responsibility for that section". Misusing mechanisms for
   command-like "you take responsibility" definitly will kill our motivation. 


==========
ToDo notes
==========
.. auth-status-proof1/none

These notes can be used anywhere in the documentation as anonymous reminders.
It is a good idea to also note keywords for content to be written as todo note
when they come to your mind. ToDo notes have the syntax::

  .. todo:: explain something

  .. todo::
     explain something complex
     * explain part 1
     * explain part 2
     * explain part 3

ToDo notes go to the documentation in the place where they are written and to 
the ToDo-List (you need to "make clean" to generate a new ToDo-List). 
It is easy to generate documentation while leaving todo-notes
out. To do that find the line::

  todo_include_todos = True

in conf.py of the documentation-directory and change its value to "False"
before generating the docs. 

=============================
Styleguide / Organizing Files
=============================
.. auth-status-proof1/none

Headers are taken from the Python documentation project::

  Parts:            ############## (with overline)

  Chapters:         ************** (with overline)

  Sections:         =========== 

  Subsections:      -----------

  Subsubsections:   ^^^^^^^^^^^

  Paragraphs:	     """"""""""


* Table of Content (ToC) depth: 2 Levels (Also 2 levels in every Part except
  for the glossary)
* Subdirectories are for separate manuals that should be buildable standalone.
* The manual pages should be buildable as man pages standalone.
* Add .. code-block:: <lang> to literal blocks so that they get highlighted.
  Prefer relying on automatic highlighting simply using :: (two colons). This
  has the benefit that if the code contains some invalid syntax, it won’t be
  highlighted. Adding .. code-block:: python, for example, will force
  highlighting despite invalid syntax.
* In section titles, capitalize only initial words and proper nouns.
* Wrap the documentation at 80 characters wide, unless a code example is
  significantly less readable when split over two lines, or for another good
  reason.

=============
Writing style
=============
.. auth-status-proof1/none

When using pronouns in reference to a hypothetical person, such as “a user with a session cookie”, gender neutral pronouns (they/their/them) should be used. Instead of::

  he or she... use they.
  him or her... use them.
  his or her... use their.
  his or hers... use theirs.
  himself or herself... use themselves.

=======================================================
Installing the documenters Tools on different Platforms
=======================================================

----------------
debian8 (jessie)
----------------
.. auth-status-writing/wolfram@lizardfs.com

The best way to get the documentation formatting-tools up and running is:

 * apt-get install python-pip
 * pip install Sphinx

This should be enough to build the html-documentation. 
If you want pdf also you will need texlive/pdflatex - caution, that one is 
really a *large* set of software. 

.. todo:: describe the installation of pandoc for deb8

-------
macos X
-------
.. auth-status-todo/none

.. todo:: describe the installation of documenters-tools for macos

=============
Build-Process
=============

.. auth-status-proof1/none

There is a Makefile in the repo for building documentation. It is derived from
the one generated by sphinx-quickstart.

To build html-documentation in one huge html-file (plus images)::

  make singlehtml

To build html-documentation splitted up to different files::

  make html

To build pdf-documentation::

  make latexpdf

If things go wrong when building the documentation first check if all tools
for the target-format are available (check terminal-output for
"command not found"-messages)

