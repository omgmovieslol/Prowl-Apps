#!/usr/bin/env python

import prowlpy
import twitter
import time



apikey = 'e43f603a9b71c8eb6ccca5a7aa4631c935163ded'
twiuser = 'jamesrox'
twipass = 'password'
wait = 60 #seconds



prwl = prowlpy.Prowl(apikey)
t = twitter.Api(username=twiuser, password=twipass)
last = 0


while 1:
	try:
		  posts = t.GetFriendsTimeline()
		  for p in posts:
		  	print last
		  	if last == 0:
		  		last = p.id
		  	if p.id > last:
		  		print "Sent: %s: %s" % (p.user.screen_name, p.text)
			  	prwl.add('Twitter',p.user.screen_name,p.text)
			  	last = p.id
	except Exception,msg:
		  print msg
	
	finally:
		time.sleep(wait)
