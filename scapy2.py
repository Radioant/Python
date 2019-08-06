# scrapy2.py

import urllib.request
import urllib.parse
url='http://itcast.cn'
header={'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0','Host':'httpbin.org'}
dict_demo={'name':'itcast'}
data=bytes(urllib.parse.urlencode(dict_demo).encode('utf-8'))

# 将url作为Request（）方法的参数，构造并返回一个Request对象
request=urllib.request.Request(url,data=data,headers=header)

# 将Request 对象作为urlopen()方法的参数，发送给服务器并接收响应
response=urllib.request.urlopen(request)

#　使用read()方法读取获取到的网页内容
html=response.read(response).decode('utf-8')

# 打印网页内容
print(html)

