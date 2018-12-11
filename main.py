from androguard_module import androguard_getpermission
from androguard import misc
from radare2_module import Radare2_getAPI
from Signature.SIGNATURE import SIGNATURE

#a,d,dx = misc.AnalyzeAPK("malware/smack/smack.apk")

#androguard_getpermission.getPermissionDetails(a)

#construct of r2 class by malware classes.dex file
#newapk = Radare2_getAPI.R2_cmd("malware/smack/anal/classes.dex")

#newapk.getFunctionCall()

print(SIGNATURE().apkchecks['strings'])
