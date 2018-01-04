.. _repository_rules:

*******************************
Repository rules
*******************************

.. auth-status-todo/none

*  We keep the master stable enough to pass all our tests. If your change is
   spitted into many commits, each of them should be complete enough not to
   break any of them.

*  We do strive to maintain backward compatibility. Changes which make
   existing installations break during an upgrade, won't be accepted.

*  Your changes most probably will be re based to the top of the master before
   being pushed to the repository. This makes the git tree simpler if there is
   no important reason to add any branches and merges there.

.. _commit_messages:

Commit messages
---------------

*  We document all the changes in commit messages. Please make your commit
   messages consistent with the rest of git log. Especially:

   The first line must contain a summary of the change. It has to be no more
   than 65 characters (this is a hard limit). It has to be in the following
   format::

     tag: Description in the imperative mood.

   The description begins with a capital letter. It's role is describe what
   the commit does (does it fix a bug? re factor some code? adds a new test?
   adds a new feature? extends an existing feature? updates documentation?)
   and which functionality, part of the code or module does it concern.

   Some real-life examples::

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

   Use present tense. tell what the change does. be terse. avoid "decorations"
   like dashes and brackets that waste space.

   Put all the information required to review the commit there. Generally, we
   recommend following the same rules as suggested by maintainers of OpenStack
   here:
   https://wiki.openstack.org/wiki/GitCommitMessages#Information_in_commit_messages.

*  Before creating your first commit messages, read the git log and try to
   follow any good practices found there. You should put all the information
   in the commit message even though it might be present in some gitHub issue
   or in the pull request itself -- GitHub might disappear some day!

*  Use reasonable numbers of commits (possibly one) per change. Don't create
   commits which fix many independent things. Don't split a single change into
   many commits if there is no reason to do this.

.. _code_review:

Code review process
-------------------

Most of the review process of LizardFS is done using Gerrit
(http://cr.skytechnology.pl:8081/). This is why most changes include a
Change-Id: tag. You don't need it for changes committed via Pull Requests.
Those will be reviewed and imported by the core development team.

Your patch will typically be reviewed within 1-2 days. You can follow the
progress in gerrit and you will also receive mail whenever there is a change.

In general 3 things can happen in the review:

* The committer reviewed and tested the patch successfully, then merged it to
  master (congratulations)

* The committer had some comments, which you need to look at

* Sometimes the patch breaks some other functionality and is marked as
  “Cannot merge”

In the 2 later cases, you need to update your patch.

Use of Code-Review and Verified
-------------------------------

If you look at your patch on [gerrit] you will see two status codes:

  Code-Review

  Verified

The reviewers, our CI system (jenkins) and potentially yourself will use these
two fields to qualify the patch.

**Code-Review**
  Can be assigned -2, -1, 0, +1, +2

  **-2** are to be used by the author, to signal "work in progress". The -2
  prevent the patch from being merged, and only the person who issued the -2
  can remove it.

  If you work on a larger patch, you are most welcome to upload a patch, mark
  it as -2, to see if it builds successfully on all platforms

  **-1** is used by the reviewer, if there are things in the patch that should
  be changed

  **0** is used when making comments, that has no effect on whether or not the
  patch should be merged.

  **+1** is used by the reviewer, to signal the patch is ok, but the reviewer
  would like a second opinion

  **+2** is used by the author to signal no review is needed (this can only be
  done by core developers, and should be used with care). The person who
  merges your patch, will use +2, just before merging, since only +2 can be
  merged

.. note:: a patch will NOT be merged as long as there are -1 or -2 unresponded
          to.


**Verified**
  Can be assigned -1, 0, +1

  **-1** is used by the CI system if the build fails (remark this is not
  always a problem in your patch, but can be due to a broken master).

  **-1** is used by the reviewer, if the expected result cannot be seen.

  **0** is used when making comments, that has no effect on whether or not the
  patch should be merged.

  **+1** is used by the CI system if the build is successful

  **+1** is used by the reviewer, when the expected result has been verified.

.. note:: a patch will NOT be merged unless the CI system shows a successful
          build.

Updating a patch
----------------

Checkout your branch::

  git checkout test1

make the needed changes and test them. It is polite to comment the lines of
code you do not want to change or where you do not agree with the committer,
this is done directly in gerrit.

Once you are ready to commit again it is important you use --amend ::

  git commit --amend -a

.. note::  do not use the -m parameter as it will wipe out the gerrit patch
           id. Let git open an editor, allowing you to edit the commit message
           (or leave it unchanged). When editing be careful not to remove/
           modify the last line with the patch id.

This will ensure you update the patch, instead of generating a new one (with a
new Change-Id:).

Closing issues with commits
---------------------------

If a commit fixes some GitHub issue, please add a line Closes #xxx at the end
of the commit message, where #xxx is the issue's ID (e.g., Closes #123). It
would link the commit with the issue and the issue with the commit (like in
`7dc407da <https://github.com/lizardfs/lizardfs/commit/7dc407da8b53625c5d49c9040406813f5355ba5a>`_ )

Other rules
-----------

* When changing anything already documented, also update its man pages.

* New features have to be covered by our test suite and documented in man
  pages.

* For bug fixes it's recommended to provide a test which verifies if the bug is
  indeed fixed.
