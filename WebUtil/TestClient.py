__author__ = 'sulantha'
import urllib2

url = 'http://www.neuroimagemap.info'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
