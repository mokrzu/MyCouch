#!/usr/bin/python
# mycouch: mini python module for CouchDB
# author: Lucas Mokrzycki

import requests
import json

class MyCouch:
	
    ''' You should provide path to server, login and password for your Couch '''
    def __init__(self, home="http://localhost:5984", login="admin", passwd="restful"):
        self.home = home
        self.login = login
        self.passwd = passwd
        self.current_db = ""
        self.h = {'content-type': 'application/json'}
    
    ''' Returns all available databases ''' 
    def show_dbs(self):
        r = requests.get(self.home + "/_all_dbs")
        return r.content
    
    ''' Create new database '''
    def add_db(self, name):
        r = requests.put(self.home + "/" + name, auth=(self.login, self.passwd))
        return r.content
    
    ''' Choose database, other methods will use current database '''
    def choose_db(self, name):
        r = requests.get(self.home + "/" + name, auth=(self.login, self.passwd))
        info = json.loads(r.content)
        # Check if name is correct
        try:
            info['error']
            return "Wrong databse name"
        except KeyError:
            self.current_db = name
            return "Changed databse to: " + name + "."
    
    ''' Returns current database '''
    def actual_db(self):
        return "You use: " + self.current_db + " database."
    
    ''' Delete current database '''
    def delete_db(self):
        r = requests.delete(self.home + '/' + self.current_db, auth=(self.login, self.passwd))
        self.current_db = ""
        return r.content
    
    ''' Replicate current databse to selected target '''
    def replicate(self, target_db):
        info = json.dumps({"source": self.current_db, "target": target_db})
        r = requests.post(self.home + "/_replicate", data=info, headers=self.h, auth=(self.login, self.passwd))
        return r.content
    
    ''' Insert document to databse, given as python dictionary '''
    def insert_doc(self, doc):
        uuids = json.loads(requests.get(self.home + "/_uuids").content)["uuids"]
        r = requests.put(self.home + '/' + self.current_db + '/' + uuids[0], json.dumps(doc), headers=self.h, auth=(self.login, self.passwd))
        return r.content
    
    ''' Returns view form give design, and current database '''
    def show_view(self, design, view_name):
        request_text = self.home + '/' + self.current_db + '/_design/' + design + '/_view/' + view_name
        print request_text
        r = requests.get(request_text, auth = (self.login, self.passwd))
        return r.content
