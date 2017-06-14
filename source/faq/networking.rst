.. _faq_networking:

****************
Networking
****************
.. auth-status-todo/none

**What do you recommend for interface bonding ?**

  This depends largely on your policies. Since LizardFS does round robin
  between chunkservers if using goals, rr woould probably gain the best
  results. If you use erasure coding, advanced balancing in LACP would be
  probably the most optimal way to do it.
