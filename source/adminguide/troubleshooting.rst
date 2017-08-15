.. _troubleshooting:

*********************
Troubleshooting
*********************
.. auth-status-todo/none

Linux
=====

Basic checks
------------

* Check if your nodes are all reachable by IP address as well as by hostname
* Check if your network has the right throughput
* Check if your disks are all working and do not report errors
* Check your Chunkservers for:

  * Broken Disks
  * Slow Disks
  * permissions on your directories (the user which is running the chunkserver
    must be the owner of the directories)
  * network performance to other chunkserver
  * network performance to master server
  * network performance to clients

* Check your license files for the correct name and location
* Check your log files for errors. LizardFS is very talkative and reports a
  lot.

Check the speed of your network interface
-----------------------------------------

Verifying what your network interface is set to is pretty simple on Linux, you
can just use the *ethtool* program to tell you what your interface is actually
set to::

  ethtool <interface>

example::

  # ethtool eth0
    Settings for eth0:
        Supported ports: [ TP ]
        Supported link modes:   10baseT/Half 10baseT/Full
                                100baseT/Half 100baseT/Full
                                1000baseT/Full
        Supported pause frame use: No
        Supports auto-negotiation: Yes
        Advertised link modes:  10baseT/Half 10baseT/Full
                                100baseT/Half 100baseT/Full
                                1000baseT/Full
        Advertised pause frame use: No
        Advertised auto-negotiation: Yes
        Speed: 100Mb/s
        Duplex: Full
        Port: Twisted Pair
        PHYAD: 1
        Transceiver: internal
        Auto-negotiation: on
        MDI-X: on (auto)
        Supports Wake-on: pumbg
        Wake-on: g
        Current message level: 0x00000007 (7)
                               drv probe link
        Link detected: yes

As you can see, the interface reports a speed of 100Mb/s. It has
Auto-negotiation enabled so is most probably connected to a 100Mb/s switch
port.

.. seealso: https://www.kernel.org/pub/software/network/ethtool/

Checking the throughput of your network
---------------------------------------

The best tool to verify if your network throughput is according to what you
think it is would be the *iperf* tool. *iperf* allows you to verify the
throughput between two machines. It is available for Linux, Windows, MacOS,
FreeBSD and all other POSIX compliant systems and also most mobile phone OSes
and is very easy to use.

For more information about iperf, please check out https://iperf.fr/ .


