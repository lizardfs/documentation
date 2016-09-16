.. _submitting_patches

Submitting Patches
******************
.. auth-status-proof1/none

If you want to improve LizardFS, we are happy to accept your changes. You
should use :ref:`GitHub` Pull Requests to make your changes available for
review.

You can read here:
https://help.github.com/articles/about-pull-requests/ how to use them.

Repository Rules
================

*  We keep the master stable enough to pass all our tests. If your change is
   spitted into many commits, each of them should be complete enough not to
   break any of them.

*  We do strive to maintain backward compatibility. Changes which make
   existing installations break during an upgrade, won't be accepted.

*  Your changes most probably will be rebased to the top of the master before
   being pushed to the repository. This makes the git tree simpler if there is
   no important reason to add any branches and merges there.

*  We document all the changes in commit messages. Please make your commit
   messages consistent with the rest of git log. Especially:

   The first must contain a summary of the change. It has to be no more than
   65 characters (this is a hard limit). It has to be in the following format
   tag: Description in the imperative mood. The description begins with a
   capital letter. It's role is describe what the commit does (does it fix a
   bug? refactor some code? adds a new test? adds a new feature? extends an
   existing feature? updates documentation?) and which functionality, part of
   code or module does it concern. Some real-life examples::

     debian: Add Jenkins BUILD_NUMBER to package version
     deb, rpm, cmake: Fix building packages
     mount: Fix returning wrong file length after truncate
     ha-cluster: Make the cluster manager more user friendly
     admin: Rename lizardfs-probe to lizardfs-admin
     master,mount: Add option allowing non-root users to use meta
     doc: Fix inconsistencies in ha-cluster README
     master: Clean up code in chunks.cc
     master, metalogger: Fix memory leak found by valgrind
     utils: Fix handling LIZ_MATOCL_METADATASERVER_STATUS in wireshark
     tests: Refactor add_metadata_server_ function

   After the summary there has to be a blank line followed by the rest of the
   commit message, wrapped at 72 or 80 characters, possibly containing
   multiple paragraphs. It should contain a comprehensive information about
   what and how the commit actually changes, why this change is being done,
   why this is the right way to do this, how to replicate bugs fixed be it.


   Put all the information required to review the commit there. Generally, we
   recommend following the same rules as suggested by maintainers of OpenStack
   here:
   https://wiki.openstack.org/wiki/GitCommitMessages#Information_in_commit_messages.

   Before creating your first commit messages, read the git log and try to
   follow any good practices found there. You should put all the information
   in the commit message even though it might be present in some gitHub issue
   or in the pull request itself -- GitHub might disappear some day!

*  Use reasonable number of commits (possibly one) per change. Don't create
   commits which fix many independent things. Don't split a single change into
   many commits it there is no reason to do this.

Most of the review process of LizardFS is done using Gerrit
(http://cr.skytechnology.pl:8081/) and this is why most changes include a
Change-Id: tag. You don't need it for changes committed via Pull Requests.

If a commit fixes some GitHub issue, please add a line Closes #xxx at the end
of the commit message, where #xxx is the issue's ID (e.g., Closes #123). It
would link the commit with the issue and the issue with the commit (like in
`7dc407da <https://github.com/lizardfs/lizardfs/commit/7dc407da8b53625c5d49c9040406813f5355ba5a>`_ )

When changing anything already documented, also update man pages.

New features have to be covered by our test suite and documented in man pages.

For bug fixes it's recommended to provide a test which verifies if the bug is
indeed fixed.
