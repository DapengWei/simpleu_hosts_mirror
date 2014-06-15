# -*- coding: utf-8 -*-
import urllib2
import httplib
import socket

def MyResolver(host):
  if host == 'simpleu.googlecode.com':
    return '74.125.128.82' 
  else:
    return host

class MyHTTPConnection(httplib.HTTPConnection):
  def connect(self):
    self.sock = socket.create_connection((MyResolver(self.host),self.port),self.timeout)

class MyHTTPHandler(urllib2.HTTPHandler):
  def http_open(self,req):
    return self.do_open(MyHTTPConnection,req)

class MyHTTPSHandler(urllib2.HTTPSHandler):
  def https_open(self,req):
    return self.do_open(MyHTTPSConnection,req)

proxy_handler = urllib2.ProxyHandler({'http': '127.0.0.1:1984'})

opener = urllib2.build_opener(proxy_handler,MyHTTPHandler)
urllib2.install_opener(opener)

print "downloading hosts with proxy"
response = urllib2.urlopen("http://simpleu.googlecode.com/svn/trunk/hosts")
data = response.read()
with open("hosts", "wb") as hosts_file:     
    hosts_file.write(data) 
print "downloading complete"