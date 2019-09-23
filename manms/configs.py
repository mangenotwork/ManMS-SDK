#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'man'

#Man URL
ManURL = "127.0.0.1"

#Man Port
ManPort = "8686"

#APPID
APPID = "sdk19950620"

#APPKey
APPKEY = "mangenotwork"

#api
def ManAPI_Get(apiurl):
	return "http://"+ManURL+":"+ManPort+apiurl+"?appid="+APPID+"&appkey="+APPKEY

def ManAPI_Post(apiurl):
	return "http://"+ManURL+":"+ManPort+apiurl