from androguard_module import androguard_getpermission
from androguard import misc
from radare2_module import radare2_getapi


#a,d,dx = misc.AnalyzeAPK("malware/smack/smack.apk")

#androguard_getpermission.getPermissionDetails(a)



#construct of r2 class by malware classes.dex file
newapk = radare2_getapi.r2_cmd("malware/smack/anal/classes.dex")

newapk.getFunctionCall()



