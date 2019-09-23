from manms import util,configs
import json

class ManMS_Autoc(object):
	"""docstring for ManMS_Autoc"""
	#创造器

	def __init__(self, arg):
		super(ManMS_Autoc, self).__init__()
		self.arg = arg

	@classmethod
	def _sfzverify_add(cls,sfz_number=" "):
		api = "/sfzverify/address"
		apiurl = configs.ManAPI_Get(api)+"&sfz_number="+sfz_number
		datas = util.get_data(apiurl)
		address = json.loads(datas)["data"]
		return address

class ManMS_Cr(object):
	"""docstring for ManMS_Cr"""
	#加密解密，字符处理

	def __init__(self, arg):
		super(ManMS_Cr, self).__init__()
		self.arg = arg

class ManMS_Lang(object):
	"""docstring for ManMS_Lang"""
	#自然语言处理

	def __init__(self, arg):
		super(ManMS_Lang, self).__init__()
		self.arg = arg
		
class ManMS_XY(object):
	"""docstring for ManMS_XY"""
	#信用查询

	def __init__(self, arg):
		super(ManMS_XY, self).__init__()
		self.arg = arg
		
class ManMS_QRBar(object):
	"""docstring for ManMS_QR"""
	#二维码，验证码

	def __init__(self, arg):
		pass
		
class ManMS_Shop(object):
	"""docstring for ClassName"""
	#商品，购物

	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
class ManMS_Toutiao(object):
	"""docstring for ManMS_Toutiao"""
	#文章头条

	def __init__(self, arg):
		super(ManMS_Toutiao, self).__init__()
		self.arg = arg
		
