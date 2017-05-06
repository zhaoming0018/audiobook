#-*- coding:utf-8 -*-
from urllib import request

st = 'http://www.5tps.com/down/83_47_1_78.html'

url = 'http://www.5tps.com/play/flv_down.asp?urlid=%B5%A5%CC%EF%B7%BC%2F2009%2F%C0%CF%B5%EA%B7%E7%D4%C6%2F%C0%CF%B5%EA%B7%E7%D4%C6%5F078%2Emp3&title=%C0%CF%B5%EA%B7%E7%D4%C6&ji=78&id=83&said=47'

opener = request.build_opener()
opener.addheaders = [('Referer',st)]
page = opener.open(url)

html = page.read() 
print(html.decode('gb2312'))