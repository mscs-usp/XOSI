
import os
from socket import *

nodes_file = os.getenv("OAR_FILE_NODES")

print nodes_file

f = open(nodes_file,"r")
nodes_all = f.readlines()
f.close()

nodes = {}

for n in nodes_all:
  if not n in nodes.keys():
     print n	
     res  = os.system(" gethostip "+n)
     print str(res).split(' ')
     nodes[n] = addr+" "+name

print nodes
