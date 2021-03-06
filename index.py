#-*- coding:utf-8 -*-
from urllib import request,parse
import re
import time

# 获取所有下载链接
def getDLink(relurl,refurl):
    host = 'http://www.5tps.com'
    opener = request.build_opener()
    # 加Referer头请求
    opener.addheaders = [('Referer',host+refurl)]
    page = opener.open(host+relurl)
    html = page.read().decode('gb2312')
    # 前半部分
    reg = r'url\[0\]= "(.*?)"'
    preReg = re.compile(reg)
    pre = (re.findall(preReg,html))[0]
    # 后半部分
    reg = r'm.*?= \'(\d+?)\''
    numReg = re.compile(reg)
    nums = re.findall(numReg,html)
    targetUrl = pre + '?' + nums[0] + 'x' + nums[1] + 'x' + nums[2] + '-' + nums[3] + '?2'
    return targetUrl 

# 获取iframe的链接
def getIframe(relurl):
    host = 'http://www.5tps.com'
    html = getHtml(host + relurl).decode('gbk')
    reg = r'<iframe src="(.*?)" id="play"'
    iframeReg = re.compile(reg)
    iframes = re.findall(iframeReg,html)
    return iframes[0]

def getAllLinks(html):
    reg = r'<li>.*?<a.*?>.*?<a href=\'?(.*?)\'? title=.*?><b>.*?</b></a>'
    linkReg = re.compile(reg)
    links = re.findall(linkReg,html)
    return links

def getAuthorAndTitle(html):
    reg = r'<div id=i><h2><a.*?>(.*?)</a></h2>.*?<h1>(.*?)</h1>.*?<\/div>'
    divReg = re.compile(reg,re.IGNORECASE)
    div = re.findall(divReg,html)
    return div[0]

def getHtml(url):
    # urllib中的request模块中，
    # urlopen函数可以直接请求一个网址
    page = request.urlopen(url)
    # 返回的page是一个ContextManger(上下文管理)对象
    # 可以作为文件资源使用
    html = page.read()
    return html

# 用urllib获取html代码
html = getHtml("http://www.5tps.com/html/20518.html").decode('gb2312')

# 获取作者和标题
(author,title) = getAuthorAndTitle(html)

# 获取所有下载页面链接
links = getAllLinks(html)
linksNum = len(links)

i = 0 
# 循环所有页面
for link in links:
    # 获取下载链接
    iframeLink = getIframe(link)
    dLink = getDLink(iframeLink,link)
    print(dLink)
    # 下载
    i = i+1
    print(author,title)
    print("正在下载第%d集" % i)
    f = request.urlopen(parse.quote(dLink).replace('%3A',':').replace('%3F','?'))
    data = f.read()
    with open("c:/MyFolds/temp/%d.mp3" % i,"wb") as code:
        code.write(data)
    # 停止5秒，减轻爬取网站负担
    time.sleep(5)