.. _documentation_howto:

*******************
Documentation-HowTo
*******************

Welcome to the documenters-project for lizardfs. This pages shall introduce you
to our Tools and Workflows. 

Documentation is written in reStructuredText
(http://docutils.sourceforge.net/rst.html), then we build the different Formats
with the Help of sphinx (http://www.sphinx-doc.org/en/stable/tutorial.html).

If you want to generate nroff man pages as well, you also will need to install
pandoc.

===================
Documentation Rules
===================

Headers are taken from the Python documentation project::

  Parts:            ############## (with overline)

  Chapters:         ************** (with overline)

  Sections:         =========== 

  Subsections:      -----------

  Subsubsections:   ^^^^^^^^^^^

  Paragraphs:	     """"""""""

ToC depth: 2 Levels (Also 2 levels in every Part except for the glossary)

Subdirectories are for separate manuals that should be buildable standalone.

The manual pages should be buildable as man pages standalone.

Add .. code-block:: <lang> to literal blocks so that they get highlighted. Prefer relying on automatic highlighting simply using :: (two colons). This has the benefit that if the code contains some invalid syntax, it won’t be highlighted. Adding .. code-block:: python, for example, will force highlighting despite invalid syntax.

In section titles, capitalize only initial words and proper nouns.

Wrap the documentation at 80 characters wide, unless a code example is significantly less readable when split over two lines, or for another good reason.

=============
Writing style
=============

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
Best way to get the documentation formatting-tools running is:

 * apt-get install python-pip
 * pip install Sphinx

This should be enough to build the html-documentation. 
If you want pdf also you will need texlive/pdflatex - caution, that one is 
really a *large* set of software. 

