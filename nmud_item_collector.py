import parser
import os

dir_list = os.listdir("AreaFiles")
areaDict = {}

for file_name in dir_list:
	file = open("AreaFiles\\"+file_name)
	areaDict = parser.parseFile(file.read())
	print (areaDict["AreaName"])