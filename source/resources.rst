##########
Resources
##########
.. auth-status-writing/none

*******
General
*******

**LizardFS Community Site**
  http://www.lizardfs.org/

**LizardFS Forum**
  http://www.lizardfs.org/forum/

**Wikipedia article**
  https://en.wikipedia.org/wiki/LizardFS

**LizardFS review by Valentin Hörbel from NFON AG**
  https://www.itcentralstation.com/product_reviews/lizardfs-review-34235-by-valentin-hobel

**LizardFS Youtube channel**
  https://www.youtube.com/channel/UCyDn7vchGZxDUyr-CajFzfg

**LizardFS Twitter channel**
  https://www.twitter.com/lizardfs/

**LizardFS on Facebook**
  https://www.facebook.com/lizardfs/

**LizardFS users mailing list on Sourceforge**
  https://sourceforge.net/p/lizardfs/mailman/?source=navbar

**LizardFS on irc**
  #lizardfs on freenode.net

**LizardFS article on golem.de in german**
  http://www.golem.de/news/lizardfs-software-defined-storage-wie-es-sein-soll-1604-119518.html

******************
Developer Specific
******************

**Main code repository**
  http://cr.skytechnology.pl:8081/lizardfs

**GitHub repository mirror**
  https://github.com/lizardfs/lizardfs

**Code review system**
  http://cr.skytechnology.pl:8081/

**Continuous integration system**
  http://jenkins.lizardfs.org/

**Roadmap**
  https://github.com/lizardfs/lizardfs/wiki/Roadmap


******************
Third Party AddOns
******************

**LizardFS in Grafana**
  This plugin/script for Telegraf will collect the metrics from LizardFS and
  stores it into InfluxDB, then you can view your metrics in Grafana on a
  \templated dashboard.

  https://blog.kruyt.org/lizardfs-in-grafana/

**puppet-lizardfs**

  The puppet-lizardfs module lets you use Puppet to install and configure LizardFS automatically.

  You can configure with puppet-lizardfs:

    * The LizardFS master (ready for High-availability with tools like
      keepalived or Pacemaker. Check out the explanation below)
    * The LizardFS chunkserver
    * The LizardFS metalogger
    * The LizardFS client and mount points

  Author: Asher256

  Github repository: https://github.com/Asher256/puppet-lizardfs

  Puppet Forge page: https://forge.puppet.com/Asher256/lizardfs/readme

**lizardfs ansible playbook**

  Ansible playbook for automated installation of LizardFS Master,
  Shadowmaster, multiple Chunkservers, Metalogger and CGIserv.

  Author: stenub

  Github repository: https://github.com/stenub/lizardfs_ansible_playbook

**lizardfs docker plugin**

  A Docker volume driver plugin for mounting a LizardFS filesystem.
  Allows you to transparently provide storage for your Docker containers
  using LizardFS. This plugin can be used in combination with our
  LizardFS Docker Image to create a fully containerized, 
  clustered storage solution for Docker Swarm.
  
  Author: zicklag
  
  Github repository: https://github.com/kadimasolutions/docker-plugin_lizardfs
  
***************************
Packages from the community
***************************

**Archlinux**
  https://aur.archlinux.org/packages/lizardfs/

**Debian / Ubuntu**
  LizardFS is part of Debian. The Debian packages have a bit of a different
  directory layout than the upstream ones and are not being compiled with the
  Intel Storage Acceleration Library

**Fedora**
  There are now official packages in Fedora. The official packages are not
  being compiled with the Intel Storage Acceleration Library




