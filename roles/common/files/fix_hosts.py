#!/usr/bin/env python

# author Nikolaj Majorov
# nmajorov@redhat.com

"""Fix hosts resolutions of servers
   rewrite /etc/hosts for proper host resolution
"""

hosts_file='/etc/hosts'

# server names
fuse_master='fuse-server.elginscotland.org'
node_one='node1.elginscotland.org'
node_two='node2.elginscotland.org'

## etc entries 
fuse_master_entry='10.42.0.2       ' + fuse_master + '   fuse-server\n'
node_one_entry='10.42.0.3       '+ node_one + '   node1\n'
node_two_entry='10.42.0.4       ' + node_two +   '    node2\n'

out = []

fp = open(hosts_file, 'r')
out = fp.readlines()
fp.close()

### add entries
if out.count(node_one_entry) == 0 :
    out.append(node_one_entry)

if out.count(fuse_master_entry) == 0 :
    out.append(fuse_master_entry)


if out.count(node_two_entry) == 0 :
    out.append(node_two_entry)

# remove all 127.0.0.1 unnecessary entries 
for line in out:
    if '127.0.0.1' in line:
        #print("find line:" + line)
        line_array=line.split()
        if (line_array.count(fuse_master) > 0
            or line_array.count(node_one) > 0 
            or line_array.count(node_two) > 0):
                # remove line
                out.pop(out.index(line))



# write hosts file back
fp = open(hosts_file, 'w')
for line in out:
    fp.write(line)
fp.close()


