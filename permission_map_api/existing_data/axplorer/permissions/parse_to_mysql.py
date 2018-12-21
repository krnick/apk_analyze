import pymysql
import re
import os

db = pymysql.connect("localhost","nick","nickapk","apimapping" )
cursor = db.cursor()




for root,dirs,files in os.walk("/home/nick/axplorer/permissions/"):
	for dir_ in dirs:
		if dir_.startswith("api"):
			print(dir_)
			api_level = (dir_.split("-")[1])
			print(api_level)

			with open(dir_+'/sdk-map-'+api_level+'.txt','r') as file:
				for line in file.readlines():
					line = line.replace(" ", "").rstrip().split("::")
					class_and_method_name = line[0][:line[0].find("(")]		

					last_dot = [m.start() for m in re.finditer('\.',class_and_method_name)][-1]

					class_name = class_and_method_name[:last_dot]
					method_name = class_and_method_name[last_dot+1:]
					permission = line[1]

					sql = "insert into axplorer(`class_name`, `method_name`, `permission`, `api_level`) values (%s,%s,%s,%s)" %("'"+class_name+"'","'"+method_name+"'","'"+permission+"'","'"+api_level+"'")
					
					cursor.execute(sql)
					db.commit()

