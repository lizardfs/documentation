***
 R
***
.. auth-status-writing/none

.. _raft:

raft
====

What is Raft?
-------------
Raft is a consensus algorithm that is designed to be easy to understand. It's
equivalent to Paxos in fault-tolerance and performance. The difference is that
it's decomposed into relatively independent subproblems, and it cleanly
addresses all major pieces needed for practical systems. We hope Raft will
make consensus available to a wider audience, and that this wider audience
will be able to develop a variety of higher quality consensus-based systems
than are available today.

Hold on—what is consensus?
--------------------------

Consensus is a fundamental problem in fault-tolerant distributed systems.
Consensus involves multiple servers agreeing on values. Once they reach a
decision on a value, that decision is final. Typical consensus algorithms make
progress when any majority of their servers are available; for example, a
cluster of 5 servers can continue to operate even if 2 servers fail. If more
servers fail, they stop making progress (but will never return an incorrect
result).

Consensus typically arises in the context of replicated state machines, a
general approach to building fault-tolerant systems. Each server has a state
machine and a log. The state machine is the component that we want to make
fault-tolerant, such as a hash table. It will appear to clients that they are
interacting with a single, reliable state machine, even if a minority of the
servers in the cluster fail. Each state machine takes as input commands from
its log. In our hash table example, the log would include commands like set x
to 3. A consensus algorithm is used to agree on the commands in the servers'
logs. The consensus algorithm must ensure that if any state machine applies
set x to 3 as the nth command, no other state machine will ever apply a
different nth command. As a result, each state machine processes the same
series of commands and thus produces the same series of results and arrives at
the same series of states.


.. seealso::

   * `The Raft Consensus Algorithm <https://raft.github.io/>`_
      Contains a nice visualisatio of how the election process works.


.. _rpm:

rpm
===

RPM Package Manager (RPM) (originally Red Hat Package Manager; now a recursive
acronym) is a package management system.[5] The name RPM refers to the
following: the .rpm file format, files in the .rpm file format, software
packaged in such files, and the package manager program itself. RPM was
intended primarily for Linux distributions; the file format is the baseline
package format of the Linux Standard Base.

Even though it was created for use in Red Hat Linux, RPM is now used in many
Linux distributions. It has also been ported to some other operating systems,
such as Novell NetWare (as of version 6.5 SP3) and IBM's AIX (as of version 4).
An RPM package can contain an arbitrary set of files. The larger part of RPM
files encountered are “binary RPMs” (or BRPMs) containing the compiled version
of some software. There are also “source RPMs” (or SRPMs) files containing the
source code used to produce a package. These have an appropriate tag in the
file header that distinguishes them from normal (B)RPMs, causing them to be
extracted to /usr/src on installation. SRPMs customarily carry the file
extension “.src.rpm” (.spm on file systems limited to 3 extension characters,
e.g. old DOS FAT).

.. seealso::

   Wikipedia article on the RPM Package Manager
     https://en.wikipedia.org/wiki/RPM_Package_Manager

   Glossary entry for :ref:`yum`



