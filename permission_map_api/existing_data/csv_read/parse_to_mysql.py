import csv
import pymysql
import os


for root,dirs,files in  os.walk("/home/nick/csv_read"):
	for file_csv in files:
		if(file_csv.endswith(".csv")):

# mysql
			db = pymysql.connect("localhost","root","nickapk","apimapping" )
			cursor = db.cursor()
			with open(file_csv) as csvfile:
				rows = csv.reader(csvfile)
				for line in rows:
					sql = "insert into api(`CallerClass`, `CallerMethod`, `CallerMethodDesc`, `Permission`, `Version`) values (%s,%s,%s,%s,%s)" %("'"+line[0]+"'","'"+line[1]+"'","'"+line[2]+"'","'"+line[3]+"'","'"+line[4]+"'")
		
					cursor.execute(sql)
					db.commit()


