
import os
import socket

debug = False

# read nodes from OAR env

nodes_file = os.getenv("OAR_FILE_NODES")

if debug:
  print nodes_file

f = open(nodes_file,"r")
nodes_all = f.readlines()
f.close()

ip = {}
alias = {}
xos0 = False
resources = ""

inode=0

for n in nodes_all:
  n=n[:-1]
  if not n in ip.keys():
     res  = socket.gethostbyname(n)
     ip[n] = res
     if not xos0:
	xos0=n
        ip0=res
     else:
       resources = resources + " " + n
     alias[n]="xos%d"%inode
     inode=inode+1
     	

# construction de hosts

hosts = "127.0.0.1 localhost"

for n in ip:
  hosts = hosts + "\n%s %s %s" % ( ip[n], n, alias[n])

if debug:
  print hosts

  print xos0
  print res

def writeFile(filename,s,**rep):
  if debug:
    print s
    print rep
  if len(rep):
    for pattern in rep:
      s = str.replace(s,pattern,rep[pattern])
  if debug:
    print s
  f = open(filename,"w")
  f.write(s)
  f.write("\n")
  f.close()

globalDefs = """#global definitions

#PROXY=http://proxypac.edf.fr:3128
PROXY=noProxy

NTP=ntp1.irisa.fr

GLOBALVOPSIP=__IP0__
SCALARISBOOTIP=__IP0__
OWBOOTSTRAPIP=__IP0__
RSSBOOTSTRAPIP=__IP0__
DIXIROOTHOST=__XOS0__
DIXIROOTIP=__IP0__
DIRHOSTIP=__IP0__
MRCHOSTIP=__IP0__
OSDHOSTIP=__IP0__
USESSL=false
"""
localDefs = """#local definitions

SETMEDIA=false
CONFIGUREVO=
MYHOSTNAME=__HOST__
MYIP=__IP__
MYINTERFACE=eth0_rename
MYDISK=/dev/sda3
MYNODETYPE=
XOSDADDRESSEXTERNALADDRESS=__IP__
XOSDADDRESSHOST=__IP__
ADDRESSHOST=__IP__
NOPROMPT=true
"""

  
# creations de hosts, globalDEfs, localDefs, nodeType
# pour chacun des noeuds

try:
  os.rmtree("OUT")
except:
  pass

try:
  os.mkdir("OUT")
except:
  pass

writeFile("OUT/hosts",hosts)

for n in alias:
  dir = "OUT/%s"%n
  try:
    os.mkdir(dir)
  except:
    pass
  writeFile("%s/globalDefs"%dir,globalDefs,__XOS0__=xos0,__IP0__=ip0)
  writeFile("%s/localDefs"%dir,localDefs,__HOST__=n,__IP__=ip[n])
  writeFile("%s/nodeTypes"%dir,"head-node: %s\n resource-node: %s" % \
            (xos0,resources))
  

for n in alias:
  cmd = """
     ssh root@__HOST__ hostname __ALIAS__
     scp OUT/hosts root@__HOST__:/etc/hosts
     scp OUT/hosts root@__HOST__:/etc/xos/xosautoconfig/etc/hosts
     scp OUT/__HOST__/* root@__HOST__:/etc/xos/xosautoconfig/
     scp ~/.ssh/id_rsa root@__HOST__:.ssh/
     scp ~/.ssh/id_rsa_sk.pub root@__HOST__:.ssh/
     ssh root@__HOST__ 'cat .ssh/id_rsa_sk.pub >> .ssh/authorized_keys'
     """
  cmd = str.replace(cmd,"__HOST__",n)
  cmd = str.replace(cmd,"__ALIAS__",alias[n])
  if debug:
    print cmd

  os.system(cmd)
  







