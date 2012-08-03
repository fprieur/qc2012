#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import json
import toolbox
import datetime
import os

def tweetsqc2012():
	search = urllib.urlopen("http://search.twitter.com/search.json?q=qc2012&rpp=50&include_entities=true&result_type=mixed")
 	dict = json.loads(search.read())
 	objects_list = []
 	chemin = toolbox.determinerEnvironnement()
 	for result in dict["results"]:
  		objects_list.append(result)

  	j = json.dumps(objects_list)
	f = open(chemin + "/var/www/qc2012/qc2012.json",'w')
	f.write(j)
	f.close()

	now = datetime.datetime.now()
	f2 = open(chemin +  "/var/www/qc2012/updateDate.txt",'w')
	f2.write("Dernière mise à jour le : " + str(now.day) + " " +  toolbox.moisEnFrancais(now.month) + " " + str(now.year) + " " + "à " + str("%02d" %(now.hour)) + ":" + str("%02d" %(now.minute)))
	f2.close


tweetsqc2012()