#!/usr/bin/python
# mycouch: mini python module for CouchDB
# author: Lucas Mokrzycki

import httplib
import json

class MyCouch:
	
	def __init__(self):
		self.h = httplib.HTTPConnection('127.0.0.1:5984')
	
	def get(self, url):
		self.h.request("GET", "/" + url)
		return self.h.getresponse().read()
	
	def add_db(self, name):
		self.h.request("PUT", "/" + name)
		print self.h.getresponse().read()
	
	def insert(self, db, items):
		self.h.connect()
		pack = json.dumps(items)
		self.h.request("GET", "/_uuids")
		uuid = eval(self.h.getresponse().read())["uuids"][0]
		self.h.request("PUT", "/" + db + "/" + uuid, pack)
		print self.h.getresponse().read()
