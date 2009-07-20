#!/usr/bin/env python


import prowlpy
import feedparser
import time

apikey = 'e43f603a9b71c8eb6ccca5a7aa4631c935163ded'
wait = 60 #seconds
feeds = [
	"http://ja.meswilson.com/blog/feed/",
	"http://reddit.com/.rss",
]

guids = [ ]
first = 1

prwl = prowlpy.Prowl(apikey)

while 1:
	try:
		for feed in feeds:
			xml = feedparser.parse(feed)
		
			for e in xml.entries:
				if first:
					guids.append(e.guid)
				elif e.guid not in guids:
					prwl.add("RSS", e.title, "%s - %s" % (xml.feed.title, e.link))
					print("Sent: %s, %s" % (e.title, e.link))
				else:
					pass
				
		
	
		first = 0
	except Exception, msg:
		print(msg)
	finally:
		time.sleep(60)
