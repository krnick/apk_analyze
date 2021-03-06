from androguard_module import androguard_getpermission
from androguard import misc
from radare2_module import Radare2_getAPI
from Signature.SIGNATURE import SIGNATURE
from virustotal_module.vt import VT
from hash_module.hash import HASH
import inspect
import r2pipe
import argparse



# Radare2 wrapper functions
def r2_check(strings, r2p, r2cmd):
    cmd = r2cmd + "~+" + ",".join(strings)
    results = r2p.cmd(cmd)
    return results


def r2_check_strings(strings, r2p, message=None):
    return r2_check(strings, r2p, "izzq")


def r2_check_classes_and_methods(strings, r2p, message=None):
    return r2_check(strings, r2p, "icq")


def r2_check_imports(strings, r2p, message=None):
    return r2_check(strings, r2p, "iiq")


def r2_check_symbols(strings, r2p, message=None):
    return r2_check(strings, r2p, "isq")


# Do searches with radare2
def analyse(checks, r2p):
    result = {}
    if "strings" in checks:
        result["strings"] = r2_check_strings(checks["strings"], r2p)
    if "methods" in checks:
        result["methods"] = r2_check_classes_and_methods(
            checks["methods"], r2p)
    if "imports" in checks:
        result["imports"] = r2_check_imports(checks["imports"], r2p)
    if "symbols" in checks:
        result["symbols"] = r2_check_symbols(checks["symbols"], r2p)
    return result


# Output analysis results
def print_results(analysis_results, messages, r2p):
    for key, result in analysis_results.items():
        if len(result) > 0:
            print(messages["found"] % key)
            if key in ["strings", "symbols", "methods", "imports"]:
                print("------------" + key + "-----------------")
                print(result)
                print("-------------" + key + "-----------------")
                print("\n\n")
            else:
                print(result)

            print("\n\n")
        else:
            print(messages["not_found"] % key)

    return



#arg parse 

parser = argparse.ArgumentParser()
parser.add_argument("-apk", help="apk path file",dest="apk_file")
parser.add_argument("-dex", help="dex path file",dest="dex_file")
args = parser.parse_args()



if(args.apk_file is not None and args.dex_file is not None):

	# 分析

	path_apk_file = args.apk_file
	path_dex_file = args.dex_file

	# reflection 取得每一個變數
	attributes = inspect.getmembers(SIGNATURE())

	newapk = Radare2_getAPI.R2_cmd(path_dex_file)

	# 要檢查的特徵
	for check_list in attributes:
		if (not check_list[0].startswith("_")):

			for num in range(0, len(check_list[0]) + 2):
				print("#", end="")
			print("")
			print("#" + check_list[0] + "#")

			for num in range(0, len(check_list[0]) + 2):
		    		print("#", end="")

			print("")

			result = analyse(check_list[1], newapk.r2)

			print_results(
		    	result, {
			"found": "\n[*] " + check_list[0] + " usage found in %s\n",
			"not_found": "\n[*] No " + check_list[0] + " usage found in %s"
		    	}, newapk.r2)

	# 列出權限

	a, d, dx = misc.AnalyzeAPK(path_apk_file)

	androguard_getpermission.getPermissionDetails(a)


	# Virustotal positive
	API_KEY = "6d863d8f7130148d479775ac69079999ff02f8d4ab0003ad4b50128331509760"
	apk_file_hash_obj = HASH(path_apk_file)	

	apk_file_hash = apk_file_hash_obj.getAPKHASH()
	
	
	vt_result = VT(API_KEY,apk_file_hash)
	vt_result.getVT_result()

else:
	print("usage python main.py -h")


