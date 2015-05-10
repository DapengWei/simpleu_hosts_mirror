# -*- coding: utf-8 -*-
import requests

print "downloading hosts with proxy"
r = requests.get("https://raw.githubusercontent.com/vokins/simpleu/master/hosts")
data = r.content
with open("hosts", "wb") as hosts_file:     
    hosts_file.write(data) 
print "downloading complete"

print "begin to modify hosts"
with open("hosts", "a") as hosts_file_org:
    with open("hosts.add", "r") as hosts_file_add:
        hosts_add_file = hosts_file_add.read()
    hosts_file_org.write(hosts_add_file)

print "modify hosts complete"
