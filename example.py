import manms

#获取身份证地址
print(manms.getsfzadd("513001199506200836"))
#获取身份证性别
print(manms.getsfzsex("513001199506200836"))
#检查身法有效性
print(manms.sfzcheck("513001199506200836"))
#分词功能
print(manms.fenci("你好世界"))
#找关键词
print(manms.gjc("你好世界"))
#英汉翻译
print(manms.yhfy("你好世界"))
#汉语转拼音
print(manms.piying("你好世界"))

	
	