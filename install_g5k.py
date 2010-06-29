
import os
import socket
import sys

debug = False
debug=1

# read nodes from OAR env

try:
   nodes_file = sys.argv[1]
except:
   nodes_file = os.getenv("OAR_FILE_NODES")

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
  chunks = n.split(".")
  shortname = chunks[0]
  hosts = hosts + "\n%s %s %s" % ( ip[n], n, shortname)
#for n in ip:
#  hosts = hosts + "\n%s %s" % ( ip[n], alias[n])

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

  

for n in alias:
  cmd = """
     ssh root@__HOST__ hostname __HOST__
     scp ~/.ssh/id_rsa root@__HOST__:.ssh/
     scp ~/.ssh/id_rsa_sk.pub root@__HOST__:.ssh/
     scp cmd.sh root@__HOST__:. """

  order = """
     cat .ssh/id_rsa_sk.pub >> .ssh/authorized_keys
     urpmi git --auto
     urpmi emacs --auto
     urpmi x11 --auto
     urpmi expect --auto
git clone ssh://skortas@frontend/home/skortas/XOSI
git clone ssh://skortas@frontend/home/skortas/XOST
git clone ssh://skortas@frontend/home/skortas/XOSO
git clone ssh://skortas@frontend/home/skortas/XOSZ
     ln -s XOSI/CONF/emacs.g5k .emacs
     ln -s XOSI/CONF/bashrc-xos .bashrc-xos
     echo "export XOSHOST=__ALIAS__" >> .bashrc
     echo ". /root/.bashrc-xos" >> .bashrc
     
     """
  cmd = str.replace(cmd,"__HOST__",n)
  cmd = str.replace(cmd,"__ALIAS__",alias[n])
  fic = open("cmd.sh","w")
  fic.write(order)
  fic.close()

   
  if debug:
    print cmd

  os.system(cmd)
  








