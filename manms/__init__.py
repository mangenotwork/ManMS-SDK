__version__ = '0.1.1'
__author__  = "ManGe"
__date__    = "20190923"

from manms import method

def getsfzadd(sfznumber):
	#获取身份证地址
	return method.ManMS_Autoc._sfzverify_add(sfznumber)

def getsfzsex(sfznumber):
	#获取身份证性别
	return method.ManMS_Autoc._sfzverify_sex(sfznumber)

def sfzcheck(sfznumber):
	#验证身份证有效性
	return method.ManMS_Autoc._sfzcheck(sfznumber)

def fenci(string):
	#分词功能
	return method.ManMS_Lang._fenci(string)

def gjc(string):
	#找关键词
	return method.ManMS_Lang._gjc(string)

def yhfy(string):
	#英汉翻译
	return method.ManMS_Lang._yhfanyi(string)

def piying(string,types="0"):
	#汉语转拼音
	return method.ManMS_Lang._pingyin(string,types)

