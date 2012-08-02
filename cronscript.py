#!/usr/bin/python
import urllib
import json

def tweetsqc2012():
	search = urllib.urlopen("http://search.twitter.com/search.json?q=qc2012&rpp=50&include_entities=true&result_type=mixed")
 	dict = json.loads(search.read())
 	objects_list = []
 	for result in dict["results"]:
  		objects_list.append(result)

  	j = json.dumps(objects_list)
	f = open("qc2012.json",'w')
	f.write(j)
	f.close()

tweetsqc2012()