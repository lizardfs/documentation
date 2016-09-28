.. _cookbook_linux:

***********************
LizardFS linux CookBook
***********************
.. auth-status-proof1/none


.. _directio:

Setting DirectIO for your setup
===============================

.. warning: This is totally unsupported and may result in data loss and
           breaking your LizardFS cluster.

In some cases we have experienced that the caching mechanism in some systems
may slow down performance significantly. What has helped is switching the
caching off and moving to Direct IO which ommits the OS cache and writes
directly to the block device underneath.

To enable DirectIO on your installation, you need to update the
*.lizardfs_tweaks* file in the root of your mounted LizardFS. This is done by
issuing the following on a mounted filesystem::

  echo "DirectIO=true" > .lizardfs_tweaks

You can verify if the setting has changed to true by issuing the following
command::

  cat .lizardfs_tweaks | grep DirectIO

If you find that this does not improve your performance or in fact, slows it
down, you can always change it back by running::

  echo "DirectIO=false" > .lizardfs_tweaks

The changes are effective immediately.


.. _virtu_farms:

Using LizardFS for Virtualization Farms
=========================================

If you want to use LizardFS as a Backend for your virtualization Farm, there
are multiple options.

Use LizardFS from inside each VM
  The LizardFS client on Linux utilises the :ref:`fuse`libraray which has
  limits on the performance it can offer. To work around this one option would
  be to have each VM connect to the lizardfs system by itself. That way each
  VM has its own connection and gets the maximum performance possible via fuse.


Create one mountpoint on your host for each VM (especially cool with KVM)
  This is simple and efficient. Since the :ref:`fuse` library creates a new
  instance for every mountpoint, each mountpoint gets the full performance of
  a :ref:`fuse` connection and that way gets around the limits a single fuse
  connection currently has. So basically each VM, using a separate lizardfs
  mountpoint each, will get full throughput until the host runs out of network
  ressources.

  The setup is rather simple. Create multiple subdirectories in your lizardfs
  and mount each one separately for each VM::

    mfsmount -S <lizardfs subdirectory> -c <mfsmount config file>

  Each mount will have its own instance and create its own :ref:`fuse` process
  working like a totaly separate connection and process. This is a workaround
  for the know limitations of the :ref:`fuse` library.








