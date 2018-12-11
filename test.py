from Signature.SIGNATURE import SIGNATURE
import inspect



attributes = inspect.getmembers(SIGNATURE())





for i in attributes :
	if( '_' not in i[0]):
		print(i[0])
		print(i[1])
		print("----------------")





