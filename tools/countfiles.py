#!/usr/bin/env python

# todo: add by-author functionality

import sys, os, re

filepat = re.compile("^.*\.rst$")	# pattern for rst-files
# pattern for authoring-tags in file
authpat = re.compile("^\.\. auth-status-(.*)/(.*)$")
# pattern for todo-tag in file
todopat = re.compile("^\.\. todo::(.*)$")
toolspath =  os.path.dirname(os.path.abspath(sys.argv[0]))
topdir =  os.path.join( os.path.split(toolspath)[0], 'source')

def addto_list_in_hash(h, key, elem):
  """adds elem to list in h[key], creates list if necessary"""
  if h.has_key(key):
    h[key].append(elem)
  else: 
    h[key] = [elem]

def addto_hash_in_hash(h, key, subkey, val):
  """adds elem to hash in h[key], creates hash if necessary
  resulting structure is hash[key] -> hash[subkey] -> list
  """
  if not h.has_key(key):
    h[key] = {}
  addto_list_in_hash(h[key], subkey, val)

class AuthStati:
  def __init__(self, topdir):
    self.topdir = topdir
    self.bypath = {}		# hash[filepath] -> auth-stati
    self.bystat = {}		# hash[auth-status] -> filepathes
    self.byauthor = {}		# hash[author] -> hash[auth-status] -> filepathes
    self.todos_bypath = {}      # hash[filepath] -> count of todos

  def strip_topdir(self, fullpath):
    """strips topdir from beginning of fullpath, exits program
    if fullpath does not start with topdir"""
    if not fullpath.startswith(self.topdir):
      # should never go here
      sys.stderr.write(
        "ERROR: fullpath to remeber is not under topdir, exiting.\n")
      sys.exit(1)
    return(fullpath[len(self.topdir)+1:])	# strip common prefix
    
  def remember_authstat(self, fullpath, auth_status, author):
    path = self.strip_topdir(fullpath)
    addto_list_in_hash(self.bypath, path, auth_status + '/' + author)
    addto_list_in_hash(self.bystat, auth_status, path)
    addto_hash_in_hash(self.byauthor, author, auth_status, path)

  def add_todo(self, fullpath, todostr):
    """add 1 to number of todos found for file fullpath"""
    path = self.strip_topdir(fullpath)
    addto_list_in_hash(self.todos_bypath, path, todostr)
    
  def process_rstfile(self, pathname, filename):
    """scan rstfile for auth-stat pattern and trigger "remember them" """
    fullpath = os.path.join(pathname, filename)
    input = open(fullpath, 'rb')
    for line in input:  # find and remember authoring-tags
      m = authpat.match(line)
      if m:
        (auth_status, author) = m.groups()
        self.remember_authstat(fullpath, auth_status, author)
      m = todopat.match(line)
      if m:
        self.add_todo(fullpath, line.strip())
    input.close()

  def count_hash_valslen(self, h):
    """counts the length of values in h for each key"""
    result = {}
    for key, val in h.items():
      result[key] = len(val)
    return(result)

  def __str__(self):
    result = ""
#    tags_total = 0
#    result += "\nNumber of Auth-Status tags per file:\n"
#    for key, val in self.count_hash_valslen(self.bypath).items():
#      result += "  %i\t%s\n" % (val, key)
#      tags_total += val
#    result += "total: %i\n" % tags_total
    tags_total = 0
    result += "\nNumber of Auth-Stati by Status-type\n"
    for key, val in self.count_hash_valslen(self.bystat).items():
      result += "  %i\t%s\n" % (val, key)
      tags_total += val
    result += "  total: %i\n" % tags_total
    result += "Tags listed by author:\n"
    for key, subhash in self.byauthor.items():
      result += "Author=%s\n" % key
      tags_total = 0
      for key, val in self.count_hash_valslen(subhash).items():
        result += "  %i\t%s\n" % (val, key)
        tags_total += val
      result += "  total: %i\n" % tags_total
    tags_total = 0
    result += "Number of todo-tags per file\n"
    for key, val in self.count_hash_valslen(self.todos_bypath).items():
      result += "  %i\t%s\n" % (val, key)
      tags_total += val
    result += "  total: %i\n" % tags_total   
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
