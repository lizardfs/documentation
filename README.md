# lizardfs-new-documentation
A take at a new documentation for the LizardFS project

Requires sphinx (http://www.sphinx-doc.org/en/stable/tutorial.html) to build

Documentation Rules
===================

Headers are taken from the Python documentation project:

Parts:            ############## (with overline)

Chapters:         ************** (with overline)

Sections:         =========== 

Subsections:       -----------

Subsubsections:    ^^^^^^^^^^^

Paragraphs:	   """"""""""

ToC depth: 2 Levels (Also 2 levels in every Part)

Subdirectories are for separate manuals that should be buildable standalone.

The manual pages should be buildable as man pages standalone.

Add .. code-block:: <lang> to literal blocks so that they get highlighted. Prefer relying on automatic highlighting simply using :: (two colons). This has the benefit that if the code contains some invalid syntax, it won’t be highlighted. Adding .. code-block:: python, for example, will force highlighting despite invalid syntax.


In section titles, capitalize only initial words and proper nouns.

Wrap the documentation at 80 characters wide, unless a code example is significantly less readable when split over two lines, or for another good reason.

Writing style

When using pronouns in reference to a hypothetical person, such as “a user with a session cookie”, gender neutral pronouns (they/their/them) should be used. Instead of:

he or she... use they.
him or her... use them.
his or her... use their.
his or hers... use theirs.
himself or herself... use themselves.

