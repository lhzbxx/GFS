# -*- coding: utf-8 -*-

from django.shortcuts import *
from django.http import *
from django.template import *
from .models import *

# Create your views here.

#
# 页面
#
# 显示新闻的详细页面
def showNewsDetail(request, newsId):
	t = loader.get_template('news.html')
	news = News.objects.get(id = newsId)
	context = {'news': news}
	html = t.render(context)
	return HttpResponse(html)

# 显示新闻列表
def showNewsList(request):
	t = loader.get_template('index.html')
	count = getCount()
	news = News.objects.all()
	context = {'news': news}
	html = t.render(context)
	return HttpResponse(html)

#
# 功能函数
# 
# 获取访问次数
def getCount():
	countfile  = open('count.dat','a+') # 以读写形式打开记录计数的文件
	counttext = countfile.read()   
	try:
		count = int(counttext) + 1
	except:
		count = 1    
	countfile.seek(0)
	countfile.truncate() # 清空文件
	countfile.write(str(count)) # 重新写入新的访问量
	countfile.flush()
	countfile.close()
	return count