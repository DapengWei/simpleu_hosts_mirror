# -*- coding: utf-8 -*-
import urllib2
proxy_handler = urllib2.ProxyHandler({'http': '127.0.0.1:1984'})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)
print "downloading hosts with proxy"
response = urllib2.urlopen("https://simpleu.googlecode.com/svn/trunk/hosts")
data = response.read()
with open("hosts", "wb") as hosts_file:     
    hosts_file.write(data) 
print "downloading complete"