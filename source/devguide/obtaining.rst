.. _obtaining_source:

*********************************************
Obtaining and installing LizardFS from Source
*********************************************

.. auth-status-todo/none

Installing LizardFS from source
+++++++++++++++++++++++++++++++

The current LizardFS source code can be obtained from our :ref:`github`
(https://github.com/lizardfs/lizardfs) project page.
You can either download a tar ball from there by choosing the respective
version in the **Branch** tab on the left or use :ref:`git` to clone the
source tree.

LizardFS uses :ref:`CMake` as its build system. To compile the sources, follow
the directions outlined below.

1. Create a build directory inside the source directory::

    cd lizardfs-source
    mkdir build

2. Run ::

     cmake ..

   inside the build directory. Useful options include
   -DCMAKE_INSTALL_PREFIX, -DCMAKE_BUILD_TYPE as well as various
   LizardFS-specific "-DENABLE_<something_or_other>" options. Options are listed when
   cmake is ran and can be changed by re-running cmake::

    cd build
    cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/lizardfs

3. Run make in the build directory::

    make

4. Run make install to install files (you may need to be root)::

    make install

Now you have a full installation of LizardFS from source code.

For build instructions on operating systems other than Linux, please refer to
:ref:`workspace` .
