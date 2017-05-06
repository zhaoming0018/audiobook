#-*- coding:utf-8 -*-
from urllib import request,parse

def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' % per)

st = 'http://163l-d.ysts8.com:8000/刑侦反腐/血月迷局/第01章_引子.mp3?10103754310008x1494084995x10104084922762-059500737469129169?2'
#st = 'http://dxpse-d.ysts8.com:8000/%E5%8D%95%E7%94%B0%E8%8A%B3/2009/%E8%80%81%E5%BA%97%E9%A3%8E%E4%BA%91/%E8%80%81%E5%BA%97%E9%A3%8E%E4%BA%91_001.mp3?10103754302759x1494081716x10104216915513-961340'
st = parse.quote(st).replace('%3A',':').replace('%3F','?')
print(st)
request.urlretrieve(st,'c:/MyFolds/temp/1.mp3',Schedule)