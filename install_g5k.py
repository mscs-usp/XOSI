
import os
import socket

nodes_file = os.getenv("OAR_FILE_NODES")

print nodes_file

f = open(nodes_file,"r")
nodes_all = f.readlines()
f.close()

nodes = {}

for n in nodes_all:
  if not n in nodes.keys():
     n=n[:-1]
     res  = socket.gethostbyname(n)
     nodes[n] = res

print nodes
