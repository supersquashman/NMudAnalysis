import parser
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import random

dir_list = os.listdir("AreaFilesTest")
areaDict = {}
fullMobList = []

for file_name in dir_list:
	file = open("AreaFiles\\"+file_name)
	areaDict = parser.parseFile(file.read())
	for mob in areaDict["MobilesList"]:
		mobInfo = {
			"vnum": mob["vnum"],
			"shortDesc": mob["short"],
			"area": areaDict["AreaName"],
			"level": mob["level"],
			"hp": mob["hp"],
			"flags": mob["actFlags"],
			"aggressive": mob["actFlags"].__contains__('aggressive'),
			"pacifist": mob["actFlags"].__contains__('pacifist'),
			"deadly": mob["actFlags"].__contains__('deadly')
		}
		if "a newly created" not in mobInfo["shortDesc"]:
			fullMobList.append(mobInfo)
			#print (mobInfo)
	#print (areaDict["AreaName"])

