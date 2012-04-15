## MyCouch module for interacting with CouchDB (author: Lukasz Mokrzycki)

Build on top of the __requests__ module. (http://docs.python-requests.org/)
It's still under construction. 

Usage example:

```python
In [1]: import mycouch

In [2]: m = mycouch.MyCouch("http://localhost:5984", "admin", "restful")

In [3]: m.show_dbs()
Out[3]: '["tester","next_db","albums","new_db","baseball","_users","albums_backup"]\n'

In [4]: m.choose_db("next_db")
Out[4]: 'Changed databse to: next_db.'

In [6]: m.delete_db()
Out[6]: '{"ok":true}\n'

In [7]: m.choose_db("albums")
Out[7]: 'Changed databse to: albums.'

In [8]: m.actual_db()
Out[8]: 'You use: albums database.'

In [9]: m.insert_doc({"Pink Floyd": "The Dark Side of the Moon"})
Out[9]: '{"ok":true,"id":"0dcbc6996ddcce28f90be87cd4005448","rev":"1-aa392bbe6e2787238d1970425b9191c1"}\n'

In [23]: m.add_db("backup_db")
Out[23]: '{"ok":true}\n'

In [24]: m.replicate("backup_db")
Out[24]: '{"ok":true,"session_id":"863dad7474aecfa187783abf44546030","source_last_seq":27,"history":[{"session_id":"863dad7474aecfa187783abf44546030",
"start_time":"Sun, 15 Apr 2012 19:22:13 GMT","end_time":"Sun, 15 Apr 2012 19:22:13 GMT",
"start_last_seq":0,"end_last_seq":27,"recorded_seq":27,"missing_checked":0,
"missing_found":7,"docs_read":7,
"docs_written":6,"
doc_write_failures":1}]}\n'
```
- - -
