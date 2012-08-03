#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import os

def moisEnFrancais(intMois):
	if (intMois == 1):
		return 'Janvier'
	elif (intMois == 2):
		return 'Février'
	elif (intMois == 3):
		return 'Mars'
	elif (intMois == 4):
		return 'Avril'
	elif (intMois == 5):
		return 'Mai'
	elif (intMois == 6):
		return 'Juin'
	elif (intMois == 7):
		return 'Juillet'
	elif (intMois == 8):
		return 'Août'
	elif (intMois == 9):
		return 'Septembre'
	elif (intMois == 10):
		return 'Octobre'
	elif (intMois == 11):
		return 'Novembre'
	elif (intMois == 12):
		return 'Décembre'

def determinerEnvironnement():
	path = ""
	if(str(os.getlogin()) == "ubuntu"):
		path = "/var/www/qc2012/"
	return path
