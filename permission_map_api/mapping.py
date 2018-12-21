from androguard_module import androguard_getpermission
from androguard import misc
from radare2_module.Radare2_getAPI import R2_cmd
from Signature.SIGNATURE import SIGNATURE
from virustotal_module.vt import VT
from hash_module.hash import HASH
import inspect
import r2pipe
import argparse
import pymysql




#arg parse 

parser = argparse.ArgumentParser()
parser.add_argument("-apk", help="apk path file",dest="apk_file")
parser.add_argument("-dex", help="dex path file",dest="dex_file")
args = parser.parse_args()

path_apk_file = args.apk_file
path_dex_file = args.dex_file

#mysql

db = pymysql.connect("localhost","nick","nickapk","apimapping" )
 
cursor = db.cursor()



# 列出權限

a, d, dx = misc.AnalyzeAPK(path_apk_file)
r2 = r2pipe.open(path_dex_file)
r2.cmd("aa")


for permission in a.get_permissions():

	permission = permission.split(".")[-1]

	
	sql = "SELECT DISTINCT class_name ,method_name FROM `axplorer` WHERE `permission` LIKE %s" % ("'%"+permission+"%'")


	cursor.execute(sql)	
	results = cursor.fetchall()
	api_list = []
	print("使用到的權限----"+permission+"----確實使用的API:")
	for row in results:
		class_name = row[0].split(".")[-1]
		method_name = row[1]
		permission_map_api = r2.cmd("iiq~"+method_name+"~"+class_name)
		print(permission_map_api,end='')
	print(" ")

