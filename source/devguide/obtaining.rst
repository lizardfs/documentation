.. _obtaining_source:

*********************************************
Obtaining and installing LizardFS from source
*********************************************

.. auth-status-todo/none

Installing LizardFS from source
+++++++++++++++++++++++++++++++

The current LizardFS source code can be obtained from our :ref:`GitHub` `project page <https://github.com/lizardfs/lizardfs>`_. You can either download a ``zip`` archive by choosing the respective version in the ``Branch`` tab or use :ref:`git` to clone the source tree.

LizardFS uses :ref:`CMake` as its build system. To compile the sources, follow the directions outlined below.

0. Install all required dependencies. For `Debian-based distributions <https://en.wikipedia.org/wiki/Category:Debian-based_distributions>`_ run::

    apt install git cmake g++ libspdlog-dev libfuse3-dev libfuse-dev fuse isal libisal-dev libboost-all-dev asciidoc-base zlib1g-dev pkg-config libthrift-dev libcrcutil-dev libjudy-dev libpam0g-dev libdb-dev libgtest-dev
    
   Note that packages' names may vary on different Linux distributions.

1. Create a build directory ``build`` inside the source directory::

    cd lizardfs
    mkdir build
    cd build

2. Inside ``build`` directory run::

     cmake ..

   Useful options include ``-DENABLE_TESTS``, ``-DCMAKE_INSTALL_PREFIX``, ``-DCMAKE_BUILD_TYPE`` as well as various LizardFS-specific ``-DENABLE_<something_or_other>`` options. Options are listed when CMake is ran and can be modified by re-running CMake::
   
    cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/lizardfs
   
   Alternatively you can list all available options by running::
   
     cmake -LAH ..
   
   If you want to enable Google tests, run::
   
     cmake .. -DENABLE_TESTS=ON

3. Run ``make`` in the build directory::

    make
   
   If you want to speed up your compilation, make use of multiple jobs running simultaneously::
   
    make -j4

4. Run ``make install`` to install files (you may need to be ``root`` user)::

    sudo make install

Now you have a full installation of LizardFS compiled from source code.

For build instructions on operating systems other than Linux, please refer to :ref:`workspace`.
