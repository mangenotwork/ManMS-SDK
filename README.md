# ManMS-SDK
ManMS:开源服务接口

## ManMS 是漫鸽网络服务的微服务开放接口

## ManMS - SDK 是漫鸽网络服务的微服务开放接口开发包，集成了所有的接口功能，注意：只支持在网络环境；


### 1. 开始使用，下载 ManMS-DSK到本地复制manms目录到您的项目
### 2. import manms
### 3. 依赖包 ： requests  （ pip install requests ）
### 4. 支持Python3

# 功能介绍

功能|使用方式|参数说明|返回
---|:--:|---:|---:
获取身份证地址|  manms.getsfzadd(sfznumber)| 1.sfznumber：身份证号码， |返回字典
获取身份证性别|  manms.getsfzsex(sfznumber)| 1.sfznumber：身份证号码， |返回字典
验证身份证有效性|  manms.sfzcheck(sfznumber)| 1.sfznumber：身份证号码， |返回字典
分词功能|  manms.fenci(keys,type)| 1.keys：需要分词的内容，2.type分词类型 |返回列表
找关键词|  manms.gjc(keys)| 1.keys：找关键词内容， |返回列表
英汉翻译|  manms.yhfy(keys)| 1.keys：需要翻译的内容， |返回列表
汉语转拼音|  manms.piying(keys)| 1.keys：需要转换拼音的内容， |返回列表

