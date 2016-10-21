.. _versioning_and_releng:

**********************************
Versioning and Release Engineering
**********************************

.. _versioning:

Versioning
==========

LizardFS uses the following versioning::

  X.Y.Z

for releases

or ::

  X.Y-rc

for release candidates

where X gives the main release number, the YY digits give the subrelease
number and Z gives the microrelease version.

* X can be any natural number.
* Y is an even number for stable releases and an odd number for unstable tags.
* Z gives the subfix tag microrelease and can be any natural number or the
  string "rc" which indicates a "release candidate"

Master branch
+++++++++++++

The Master branch is always in change and represents the actual state of
development. It is being daily checked for completeness, and has to pass
smoke, build and load testing in our lab envitonment.

Unstable tags
+++++++++++++

Simultanous with creating a new release candidate we are tagging the current
master state as the current "unstable".

Milestones
++++++++++

Milestones are defined in the github milestones page which can be found at the
following address: https://github.com/lizardfs/lizardfs/milestones. The RE
team decides in monthly meetings if the current milestone state represent a
release candidate definition. Once this is agreed upon, feature freeze is
decided and a branch created for the decided upon stable release development,
named X.Y.. Within there the current state is tagged as X.Y-rc. Once the
release candidate reaches a define stable state, X.Y.0 is tagged and packages
are being build for the public to use.

Releases and stable branches
++++++++++++++++++++++++++++

Release branches are created as -rc microrelases for development. A -rc
microrelease is deemed as the "in preparation release candidate" microrelease
of a stable branch. X.Y is defined as the first stable release of a branch and
is than released to packaging and publishing to the respective repositories or
release to the respective distribution maintainer.

Microreleases
+++++++++++++

To allow for fixes to major bugs we added the microrelease tag to the stable
branches. A microrelease will contain no new features, no additional
functionality but just fixes to major bugs.

.. _releng:

Release Engineering
===================

Releases / stable branches have to pass the full sequence of short and long
testing in our lab plus go through some real life production runs at our
coporate sponsors. LTS releases get additional testing from partners running
larger LizardFS installation base. Once a release is marked stable, every
microrelease of it has to pass the same testing cycle the stable release had
to pass.

Release Cycles
==============

Stable Releases: 6 months

For commerical customers Long Term Support releases are available from Sky
Technology Sp. z o.o.








