import urllib.request as urllib2
r=urllib2.urlopen("http://192.168.0.11:8080/shot.jpg")
o=open("abc.jpg","wb")
o.write(r.read())
o.close()
