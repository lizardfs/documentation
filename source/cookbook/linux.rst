.. _cookbook_linux:

***********************
LizardFS linux CookBook
***********************
.. auth-status-proof1/none



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




