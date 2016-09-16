#!/usr/bin/env python

import sys, os, re

filepat = re.compile("^.*\.rst$")	# pattern for rst-files
# pattern for authoring-tag in file
linepat = re.compile("^\.\. auth-status-(.*)/(.*)$")
toolspath =  os.path.dirname(os.path.abspath(sys.argv[0]))
topdir =  os.path.join( os.path.split(toolspath)[0], 'source')

def addto_list_in_hash(h, key, elem):
  """adds elem to list in h[key], creates list if necessary"""
  if h.has_key(key):
    h[key].append(elem)
  else: 
    h[key] = [elem]

class AuthStati:
  def __init__(self, topdir):
    self.topdir = topdir
    self.bypath = {}		# filepath -> auth-stati
    self.bystat = {}		# auth-status -> filepathes

  def remember(self, fullpath, auth_status, author):
    if not fullpath.startswith(self.topdir):
      # should never go here
      print "ERROR: fullpath to remeber is not under topdir, exiting."
      sys.exit(1)
    path = fullpath[len(self.topdir)+1:]	# strip common prefix
    addto_list_in_hash(self.bypath, path, auth_status + '/' + author)
    astat = auth_status		# tag status with '*' if there is no author
    if (author == 'none') or (author == ''): astat = '*' + astat
    addto_list_in_hash(self.bystat, astat, path)

  def process_rstfile(self, pathname, filename):
    """scan rstfile for auth-stat pattern and trigger "remember them" """
    fullpath = os.path.join(pathname, filename)
    input = open(fullpath, 'rb')
    l = []
    for line in input: 
      m = linepat.match(line)
      if m:
        l.append(m.groups())
    input.close()
    if l:
      for elem in l: 
        self.remember(fullpath, elem[0], elem[1])

  def count_hash_valslen(self, h):
    """counts the length of values in h for each key"""
    result = {}
    for key, val in h.items():
      result[key] = len(val)
    return(result)

  def __str__(self):
    result = ""
    tags_total = 0
    result += "\nNumber of Auth-Status tags per file:\n"
    for key, val in self.count_hash_valslen(self.bypath).items():
      result += "  %i\t%s\n" % (val, key)
      tags_total += val
    result += "total: %i\n" % tags_total
    tags_total = 0
    result += "\nNumber of Auth-Stati by Status-type, "
    result += "types tagged with '*' have no author\n"
    for key, val in self.count_hash_valslen(self.bystat).items():
      result += "  %i\t%s\n" % (val, key)
      tags_total += val
    result += "total: %i\n" % tags_total
    return(result)

# store to hold information about files/auth-stati
authstats = AuthStati(topdir)

print "Searching '%s' for rst-files" % topdir
filecount = 0
for root, dirs, files in os.walk(topdir):
  for rstfile in filter(filepat.match, files):
    filecount += 1
    authstats.process_rstfile(root, rstfile)
print "Searching done, %i rst-files found" % filecount

print authstats
