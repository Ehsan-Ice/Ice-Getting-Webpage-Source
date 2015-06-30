#!/usr/bin/python
echo "#######################";
echo "# Ehsan Ice";
echo "# Ehsanice12@gmail.com";
echo "#######################";
import urllib2
link = raw_input ("Enter url of webpage , Exam ashiyane.org ")
url = "http://" + link
html = urllib2.urlopen(url).read()
print html
