
import os
import socket

nodes_file = os.getenv("OAR_FILE_NODES")

print nodes_file

f = open(nodes_file,"r")
nodes_all = f.readlines()
f.close()

nodes = {}
alias = {}
xos0 = False

inode=0

for n in nodes_all:
  if not n in nodes.keys():
     n=n[:-1]
     res  = socket.gethostbyname(n)
     nodes[n] = res
     if not xos0:
	xos0=n
     alias[n]="xos%d"%inode
     inode=inode+1
     	

# construction de hosts

hosts = "127.0.0.1 localhost"

for n in nodes:
   

print nodes
