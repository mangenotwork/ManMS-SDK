__version__ = '0.1.1'
__author__  = "ManGe"
__date__    = "20190923"

from manms import method

def getsfzadd(arg):
	#获取身份证地址
	return method.ManMS_Autoc._sfzverify_add(arg)


