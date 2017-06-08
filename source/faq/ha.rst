******************
High Availability
******************
.. auth-status-writing/none

**What do you mean by High Availability?**
   With the help of multiple chunk servers and good goals,
   files can be stored multiple times. Therefore, a certain level of
   high availability on a file level can be achieved easily.

   In addition, it is important to know that per default, the master service
   only can be active in a master role on one node at the time. If this node
   fails, e.g. because of broken hardware or out-of-memory situations, the
   current master has to be demoted (if still possible) and an existing shadow
   has to be promoted manually.

   If the failover happens automatically, a good state of high availability is
   achieved on a service level. Thus the term "High Availability" refers to
   keeping the master role alive when everything goes down under.


**How can I achieve High Availability of the master?**
   There are multiple ways of keeping the master highly available.

   One would be to demote and promote manually if you need to.
   The better way would be to delegate that task to a mechanism
   which knows the current state of all (possible) master nodes and
   can perform the failover procedure automatically.

   Known methods, when only using open-source software, are building Pacemaker/
   Corosync clusters with self-written OCF agents. Another way could be using
   keepalived.

**This is too complicated! I need a better solution for High Availability.**

  An officialy supported way to achieve high availablity of the master is to
  obtain the uRaft component from Skytechnology Sp. z o.o., the company behind
  LizardFS.
  Based on the :ref:`raft` algorithm, the uRaft service makes sure that all
  masternodes talk to each other and exchange information regarding their
   health states.

  In order to ensure that a master exists, the nodes participate in votes.
  If the current master fails, uRaft moves a floating IP from the formerly
  active node to the new designated master. All uRaft nodes have to be part of
  one network and must be able to  talk to each other.

  The uRaft component can be obtained by signing a support contract with
  SkyTechnology Sp. z o.o..

.. seealso::

   :ref:`raft`

   :ref:`lizardfs_ha_cluster

