
import os

nodes_file = os.getenv("OAR_FILE_NODES")

print nodes_file

f = open(nodes_files,f)
nodes = f.readlines()
f.close()