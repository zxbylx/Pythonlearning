# python网络编程(1)：客户端与网络编程简介

很多情况下，网络编程就是选择并使用一个已经支持所需网络操作的库的过程。

### 1.使用pygeocoder实现地址和经纬度的转换

通过pipenv创建虚拟环境，安装pygeocoder，下面把207 N. Defiance St, Archbold, OH转换为经纬度的代码

```python
from pygeocoder import Geocoder

if __name__ == '__main__':
    address = "207 N. Defiance St, Archbold, OH"
    print(Geocoder.geocode(address)[0].coordinates)
```

结果运行报错：

```
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='maps.google.com', port=443): Max retries exceeded with url: /maps/api/geocode/json?address=207+N.+Defiance+St%2C+Archbold%2C+OH&sensor=false&bounds=&region=&language=&components= (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x031C1B38>: Failed to establish a new connection: [WinError 10061] 由于目标计算机积极拒绝，无法连接。'))

```

这我常见啊，然后打开VPN之后，再运行一遍发现还是不行，然后又尝试从PAC模式改为全局模式，发现还是报同样的错误。只能上网查一下，最终查到原因，需要设置代理，但不是电脑上开启代理。改动如下

```python
from pygeocoder import Geocoder

if __name__ == '__main__':
    #先实例Geocoder,然后设置proxy属性
    a = Geocoder()
    a.proxy = '127.0.0.1:8787'
    address = "207 N. Defiance St, Archbold, OH"
    print(a.geocode(address)[0].coordinates)
```

结果又报错了，不过和上个错误不一样，至少上一个问题是解决了啊

```
Traceback (most recent call last):
  File "D:/GitHub/python_network/search1.py", line 7, in <module>
    print(a.geocode(address)[0].coordinates)
  File "D:\GitHub\python_network\.venv\lib\site-packages\pygeocoder.py", line 127, in geocode
    return GeocoderResult(self.get_data(params=params))
  File "D:\GitHub\python_network\.venv\lib\site-packages\pygeocoder.py", line 212, in get_data
    raise GeocoderError(response_json['status'], response.url)
pygeolib.GeocoderError: Error REQUEST_DENIED
Query: https://maps.google.com/maps/api/geocode/json?address=207+N.+Defiance+St%2C+Archbold%2C+OH&sensor=false&bounds=&region=&language=&components=
```

上网查pygeolib.GeocoderError: Error REQUEST_DENIED报错原因没查到结果，看到Query后面是一个链接，打开链接发现里面有原因提示

```json
{
"error_message": "You must use an API key to authenticate each request to Google Maps Platform APIs. For additional information, please refer to http://g.co/dev/maps-no-account",
"results": [],
"status": "REQUEST_DENIED"
}
```

大概意思就是需要一个谷歌地图的API key，那就好办了，处理谷歌地图API key吧。

根据它的这个地址一步步申请了谷歌地图的API key。就是需要一个结算账户，谷歌对大陆没开放，我选的是香港，地址是瞎编的，然后需要填写一个信用卡号，一番处理完之后就申请成功，然后创建一个项目就生成了api key。

拿到api密钥后不知道咋用，然后继续查pygeocoder 使用API key的方法，最终找到了方法，实现代码如下

```python
from pygeocoder import Geocoder

if __name__ == '__main__':
    #这个API密钥有做改动，不用尝试，自己申请一个就好，下面两个写法都可以
    #a = Geocoder('AIzaSyAQBosdfjL6Dz-l9csflsdhPDDLsR0w40I')
    a = Geocoder(api_key='AIzaSyAQBosdfjL6Dz-l9csflsdhPDDLsR0w40I')
    a.proxy = '127.0.0.1:8787'
    address = "207 N. Defiance St, Archbold, OH"
    print(a.geocode(address)[0].coordinates)
```

最后终于返回了经纬度

```
D:\GitHub\python_network\.venv\Scripts\python.exe D:/GitHub/python_network/search1.py
(41.5219761, -84.3066486)

Process finished with exit code 0
```

### 2.使用requests库实现地址和经纬度转换

上面的第三方库完整的包装了谷歌地理编码API，使用requests则需要把具体的实现细节做出来，根据上面需要代理和API key的教训，把代码改成下面这样：

```python
import requests

def geocode(address):
    proxy = {'http':'127.0.0.1:8787'}
    parameters = {'address': address, 'sensor': 'false', 'api_key':'AIzaSyAQBosdfjL6Dz-l9csflsdhPDDLsR0w40I'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters, proxies=proxy)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
```

总之就报错了

```
D:\GitHub\python_network\.venv\Scripts\python.exe D:/GitHub/python_network/search2.py
Traceback (most recent call last):
  File "D:/GitHub/python_network/search2.py", line 42, in <module>
    geocode('207 N. Defiance St, Archbold, OH')
  File "D:/GitHub/python_network/search2.py", line 39, in geocode
    print(answer['results'][0]['geometry']['location'])
IndexError: list index out of range

Process finished with exit code 1
```

实在是没想到为什么是这种错误,list index out of range，这个我知道原因，就是切片[0]都超过索引最大值了，然后直接print(answer)发现结果是[]。具体一步步怎么找出问题来已经无法完全复现了，中间经过这么几步

api_key被指出字段错误，查了下改为key

URL前面协议指出必须用https，

后面怎么查都找不到解决方案遂打算看源代码，发现源码里因为谷歌需要密钥的原因已经改成其他接口了（源码是不需要代理和API密钥的，不想折腾直接看源码比较好），不过看源码还是给了我灵感，将代码改成下面这样就成功了

```python
import requests

def geocode(address):
    # proxy = {'https':'127.0.0.1:8787'} 这个和下面都可以，里面顺序颠倒也可以
    proxy = {'http':'127.0.0.1:8787','https':'127.0.0.1:8787'}
    parameters = {'address': address, 'sensor': 'false', 'key':'AIzaSyAQBosdfjL6Dz-l9csflsdhPDDLsR0w40I'}
    base = 'https://maps.googleapis.com/maps/api/geocode/json'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    response = requests.get(base, params=parameters, proxies=proxy, headers=headers)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
```

URL用https，代理也需要使用https协议，requests里参数增加了headers。

然后想了一下从刚开始各种报错找解决方案，看各种帖子最后感觉是碰运气碰出了结果。这个有点不可取。这是知道正确结果凑解决过程。

其实这个问题就涉及了一个库和一个API，只要对着两个的文档就能比较轻松的解决这个问题，然后看了下文档，发现确实文档里都写了:

- 请求的URL格式需要用https协议，格式：https://maps.googleapis.com/maps/api/geocode/outputFormat?parameters
- 为什么在后面加json是因为这是outputFormat要求的两种格式之一，另一种是xml
- 密钥字段用key，地址用address等
- 输出json格式示例决定了下面这段代码的产生

```
print(answer['results'][0]['geometry']['location'])
```

- 以前API要求包含sensor参数，以指示程序是否使用传感器来确定用户位置，现在不用了。

还有headers在这也不是必须的，所以最后简化一下代码为：

```python
import requests

def geocode(address):
    proxy = {'https':'127.0.0.1:8787'}
    parameters = {'address': address, 'key':'AIzaSyAQBosdfjL6Dz-l9csflsdhPDDLsR0w40I'}
    base = 'https://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters, proxies=proxy)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
```

这个问题给我最大的教训就是，该看文档就看文档，要养成看文档的习惯，报错去网上找各种帖子一个个试错不如文档来的实在。

用requests方法并没有通过地址和维度这样的语义直接解决该问题，而是通过构造URL，获取查询响应，然后将结果转化为JSON，一步一步地解决了这个问题。这一区别在研究网络协议栈高层与底层协议时相当常见，高层的代码描述了查询的意义，而底层的代码展示了查询的构造细节。

### 3.使用HTTP操作连接谷歌地图完成地址和经纬度转换

刚开始最大的问题还是不知道如何设置代理

`HTTPConnection.``set_tunnel`(*host*, *port=None*, *headers=None*)[¶](https://docs.python.org/zh-cn/3.7/library/http.client.html#http.client.HTTPConnection.set_tunnel)

为 HTTP 连接隧道设置主机和端口。 这将允许通过代理服务器运行连接。

host 和 port 参数指明隧道连接的位置（即 CONNECT 请求所包含的地址，而 *不是* 代理服务器的地址）。

headers 参数应为一个随 CONNECT 请求发送的额外 HTTP 标头的映射。

例如，要通过一个运行于本机 8080 端口的 HTTPS 代理服务器隧道，我们应当向 [`HTTPSConnection`](https://docs.python.org/zh-cn/3.7/library/http.client.html#http.client.HTTPSConnection) 构造器传入代理的地址，并将我们最终想要访问的主机地址传给 [`set_tunnel()`](https://docs.python.org/zh-cn/3.7/library/http.client.html#http.client.HTTPConnection.set_tunnel) 方法。

也就是说，如果没有设置代理，那么直接用

```
conn = http.client.HTTPConnection('www.baidu.com')
```

这样就可以了，如果需要设置代理，上面的设置成代理的地址，然后用set_tunnel()方法设置目标主机。

最终设置的代码为：

```python
import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
    key = 'AIzaSyAQBosdfjL6Dz-l9csflsdhPDDLsR0w40I'
    path = '{}?address={}&key={}'.format(base, quote_plus(address), key)
    connection = http.client.HTTPSConnection('127.0.0.1', 8787)
    connection.set_tunnel('map.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
```

结果报错如下：

```
D:\GitHub\python_network\.venv\Scripts\python.exe D:/GitHub/python_network/search3.py
Traceback (most recent call last):
  File "D:/GitHub/python_network/search3.py", line 44, in <module>
    geocode('207 N. Defiance St, Archbold, OH')
  File "D:/GitHub/python_network/search3.py", line 39, in geocode
    reply = json.loads(rawreply.decode('utf-8'))
  File "d:\python3.8\lib\json\__init__.py", line 357, in loads
    return _default_decoder.decode(s)
  File "d:\python3.8\lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "d:\python3.8\lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

报json.decoder.JSONDecodeError错误说明没有能够正确访问，json decode失败，然后print(rawreply)后返回的是这样的HTML文件

```shell
D:\GitHub\python_network\.venv\Scripts\python.exe D:/GitHub/python_network/search3.py
b'<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">\n<TITLE>301 Moved</TITLE></HEAD><BODY>\n<H1>301 Moved</H1>\nThe document has moved\n<A HREF="https://maps.google.com/maps/api/geocode/json?address=207+N.+Defiance+St%2C+Archbold%2C+OH&amp;key=AIdzaSyAQsadaBoWGI3dfjL6Dsdz-l9comIuhPDDLsR0w40I">here</A>.\r\n</BODY></HTML>\r\n'

Process finished with exit code 0

```

返回了一个301错误，说明需要重定向，这里使用的是HTTPS协议，因此不会像浏览器一样直接重定向，可能是Google反爬虫行为。

因此使用正则表达式提取字符串，更改后代码如下：

```python
import http.client
import json
import re
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
    key = 'AIzaSyAQBoWGI3jL6Dz-l942sdfPDDLsR0w40I'
    # path = '{}?address={}&key={}'.format(base, quote_plus(address), key)
    address = quote_plus(address)
    path = '{}?address={}&key={}'.format(base, address, key)
    connection = http.client.HTTPSConnection('127.0.0.1', 8787)
    connection.set_tunnel('map.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read().decode('utf-8')
    print(rawreply)
    newweb = re.findall(r'HREF=\"(.+?)\"', string=rawreply)
    print(newweb)
    connection.request('GET', newweb[0])
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
```

输出结果，报错了

```shell
D:\GitHub\python_network\.venv\Scripts\python.exe D:/GitHub/python_network/search3.py
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="https://maps.google.com/maps/api/geocode/json?address=207+N.+Defiance+St%2C+Archbold%2C+OH&amp;key=AIzaSyAQBoWGI3jL6Dz-l942sdfPDDLsR0w40I">here</A>.
</BODY></HTML>

['https://maps.google.com/maps/api/geocode/json?address=207+N.+Defiance+St%2C+Archbold%2C+OH&amp;key=AIzaSyAQBoWGI3jL6Dz-l942sdfPDDLsR0w40I']
Traceback (most recent call last):
  File "D:/GitHub/python_network/search3.py", line 52, in <module>
    geocode('207 N. Defiance St, Archbold, OH')
  File "D:/GitHub/python_network/search3.py", line 49, in geocode
    print(reply['results'][0]['geometry']['location'])
IndexError: list index out of range

Process finished with exit code 1

```

我把网址输入到浏览器里发现报错是需要api key，当时就觉得这个URL里参数key和address中间的“&”不对劲，为什么后面多了amp;，查了下发现是被转义了。把amp;去掉是正常的。

然后尝试过下面方案，在path后的字符串前加r，虽然觉得和quote_plus（对字符串编码，尤其中文字符）没有关系，还是用变量把quote_plus隔出去了。最后发现都不行，上网查了下发现替换字符串是个解决办法，然后就试着把字符串替换一下。最终正确的代码如下

```python
import http.client
import json
import re
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
    key = 'AIzaSyAQBoWGI3jL6Dz-l942sdfPDDLsR0w40I'
    # path = '{}?address={}&key={}'.format(base, quote_plus(address), key)
    address = quote_plus(address)
    path = '{}?address={}&key={}'.format(base, address, key)
    connection = http.client.HTTPSConnection('127.0.0.1', 8787)
    connection.set_tunnel('map.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read().decode('utf-8')
    # print(rawreply)
    #正则表达式是为了把HREF后面的URL给取出来，取出结果是list格式
    newweb = re.findall(r'HREF=\"(.+?)\"', string=rawreply)
    #替换字符串&amp;为&
    newweb = newweb[0].replace('&amp;','&')
    # print(newweb)
    connection.request('GET', newweb)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
```

### 4.直接使用套接字(socket)与谷歌地图通信

由于需要使用代理，所以上网查了下需要socks模块，然后就安装了这个包，结果发现还是报这个包没安装。最后发现现在需要安装PySocks包，但是代码中却是import socks.刚开始代码如下

```python
import socket
import socks   #需要安装PySocks
from urllib.parse import quote_plus   #用于URL字符编码

request_text = '''\
GET /maps/api/geocode/json?address={}&key={} HTTP/1.1\r\n
Host: maps.google.com:80\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36\r\n
Connection: close\r\n
\r\n
'''

def geocode(address):
    #设置代理，里面可以用socks.PROXY_TYPE_SOCKS代替
    socks.set_default_proxy(socks.PROXY_TYPE_HTTP, '127.0.0.1', 8787)
    socket.socket = socks.socksocket
    sock = socket.socket()
    sock.connect(('maps.google.com', 80))
    key = 'AIzaSyAQBoWGI3jL6Dz-l942sdfPDDLsR0w40I'
    request = request_text.format(quote_plus(address), key)
    sock.sendall(request.encode('ascii'))

    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
    # geocode('杭州市')
    # geocode('北京市')



```

结果报错，发现还是存在和上一个一样的问题，“&”被转义了，然后需要进行替换，截取要改动的一段代码

```python
request = request_text.format(quote_plus(address), key)
request = request.replace('&amp;', '&')
# print(request)
sock.sendall(request.encode('ascii'))
```

然后发现还是不能使用HTTP，需要使用HTTPS，那就需要导入ssl，然后将圆脸的连接再包装一次

```python
import socket
import socks
import ssl
from urllib.parse import quote_plus

request_text = '''\
GET /maps/api/geocode/json?address={}&key={} HTTP/1.1\r\n
Host: maps.google.com\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36\r\n
Connection: close\r\n
\r\n
'''


def geocode(address):
    socks.set_default_proxy(socks.PROXY_TYPE_HTTP, '127.0.0.1', 8787)
    socket.socket = socks.socksocket
    sock = socket.socket()
    sock.connect(('maps.google.com', 80))
    #使用ssl对原来的连接进行包装
    sock = ssl.wrap_socket(sock)
    key = 'AIzaSyAQBoWGI3jL6Dz-l942sdfPDDLsR0w40I'
    request = request_text.format(quote_plus(address), key)
    request = request.replace('&amp;', '&')
    #print(request)
    sock.sendall(request.encode('ascii'))

    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
    # geocode('杭州市')
    # geocode('北京市')



```

但是结果报错了

```shell
D:\GitHub\python_network\.venv\Scripts\python.exe D:/GitHub/python_network/search4.py
Traceback (most recent call last):
  File "D:/GitHub/python_network/search4.py", line 36, in <module>
    geocode('207 N. Defiance St, Archbold, OH')
  File "D:/GitHub/python_network/search4.py", line 20, in geocode
    sock = ssl.wrap_socket(sock)
  File "d:\python3.8\lib\ssl.py", line 1405, in wrap_socket
    return context.wrap_socket(
  File "d:\python3.8\lib\ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "d:\python3.8\lib\ssl.py", line 1040, in _create
    self.do_handshake()
  File "d:\python3.8\lib\ssl.py", line 1309, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1108)

Process finished with exit code 1

```

几番查找原因，发现是端口的问题，使用ssl就不能使用80端口了，需要使用443

```python
import socket
import socks
import ssl
from urllib.parse import quote_plus

request_text = '''\
GET /maps/api/geocode/json?address={}&key={} HTTP/1.1\r\n
Host: maps.google.com\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36\r\n
Connection: close\r\n
\r\n
'''


def geocode(address):
    socks.set_default_proxy(socks.PROXY_TYPE_HTTP, '127.0.0.1', 8787)
    socket.socket = socks.socksocket
    sock = socket.socket()
    sock.connect(('maps.google.com', 443))
    sock = ssl.wrap_socket(sock)
    key = 'AIzaSyAQBoWGI3jL6Dz-l942sdfPDDLsR0w40I'
    request = request_text.format(quote_plus(address), key)
    request = request.replace('&amp;', '&')
    #print(request)
    sock.sendall(request.encode('ascii'))

    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
    # geocode('杭州市')
    # geocode('北京市')



```

再返回正确结果的同时，也产生了一个400错误

```shell
D:\GitHub\python_network\.venv\Scripts\python.exe D:/GitHub/python_network/search4.py
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Date: Tue, 21 Jul 2020 04:19:44 GMT
Pragma: no-cache
Expires: Fri, 01 Jan 1990 00:00:00 GMT
Cache-Control: no-cache, must-revalidate
Access-Control-Allow-Origin: *
Server: mafe
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Server-Timing: gfet4t7; dur=28
Alt-Svc: h3-29=":443"; ma=2592000,h3-27=":443"; ma=2592000,h3-25=":443"; ma=2592000,h3-T050=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
Accept-Ranges: none
Vary: Accept-Language,Accept-Encoding
Transfer-Encoding: chunked

a1a
{
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "207",
               "short_name" : "207",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "North Defiance Street",
               "short_name" : "N Defiance St",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Archbold",
               "short_name" : "Archbold",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "German Township",
               "short_name" : "German Township",
               "types" : [ "administrative_area_level_3", "political" ]
            },
            {
               "long_name" : "Fulton County",
               "short_name" : "Fulton County",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "Ohio",
               "short_name" : "OH",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "43502",
               "short_name" : "43502",
               "types" : [ "postal_code" ]
            },
            {
               "long_name" : "1160",
               "short_name" : "1160",
               "types" : [ "postal_code_suffix" ]
            }
         ],
         "formatted_address" : "207 N Defiance St, Archbold, OH 43502, USA",
         "geometry" : {
            "bounds" : {
               "northeast" : {
                  "lat" : 41.521994,
                  "lng" : -84.30646179999999
               },
               "southwest" : {
                  "lat" : 41.521935,
                  "lng" : -84.30683739999999
               }
            },
            "location" : {
               "lat" : 41.5219761,
               "lng" : -84.3066486
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 41.5233134802915,
                  "lng" : -84.30530061970849
               },
               "southwest" : {
                  "lat" : 41.5206155197085,
                  "lng" : -84.3079985802915
               }
            }
         },
         "place_id" : "ChIJk4BHnIy0PYgRXbKj5GjFe_U",
         "types" : [ "premise" ]
      }
   ],
   "status" : "OK"
}

0

HTTP/1.0 400 Bad Request
Content-Type: text/html; charset=UTF-8
Referrer-Policy: no-referrer
Content-Length: 1555
Date: Tue, 21 Jul 2020 04:19:44 GMT

<!DOCTYPE html>
<html lang=en>
  <meta charset=utf-8>
  <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">
  <title>Error 400 (Bad Request)!!1</title>
  <style>
    *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png) no-repeat;margin-left:-5px}@media only screen and (min-resolution:192dpi){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat 0% 0%/100% 100%;-moz-border-image:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) 0}}@media only screen and (-webkit-min-device-pixel-ratio:2){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat;-webkit-background-size:100% 100%}}#logo{display:inline-block;height:54px;width:150px}
  </style>
  <a href=//www.google.com/><span id=logo aria-label=Google></span></a>
  <p><b>400.</b> <ins>That’s an error.</ins>
  <p>Your client has issued a malformed or illegal request.  <ins>That’s all we know.</ins>


Process finished with exit code 0

```

尝试过各种方法，最后也没能解决，倒是不影响结果。看到前面返回的是HTTP/1.1 200，后面返回的却是1.0，不知道是不是兼容性问题。后面找到原因再解决。

这个里面涉及了recv函数，一时也没理解完全，找了一篇博客，后面把这个弄清楚再写。

博客链接：https://www.cnblogs.com/ellisonzhang/p/10412021.html

还有一个关于quote_plus，这个涉及URL编码问题，也找了一篇博客，觉得不错，留作后面参考

https://www.cnblogs.com/jerrysion/p/5522673.html

### 5.协议栈

协议栈：先构建利用网络硬件在两台计算机之间传送文本字符串的原始对话功能，然后在此基础上创建更复杂，更高层、语义更丰富的对话。

前面例子分析过的协议栈包含4层：

- 最上层的谷歌地理编码，对如何用URL表示地理信息查询和如何获取包含坐标信息的JSON数据进行了封装。
- URL，标识了可通过HTTP获取的文档。
- HTTP层，支持面向文档的命令（例如GET）。该层的操作使用了原始的TCP/IP套接字。
- TCP/IP套接字，只处理字节串的发送和接收。

第一点，协议栈每一层都使用了其底层协议提供的功能，并同时向上层协议提供服务。

第二点，python对涉及的各网络层都提供了非常全面的支持。

### 6.编码与解码

每个Unicode的字符串均有一个叫做编码点（code point）的数字标识符与之对应。python3 对字符的处理相当谨慎，除非使用者主动请求python对字符和外部可见的实际字节进行相互转化，否则对使用者可见的只有字符。

解码（decoding）是在应用程序使用字节时发生的，从字节码转化为字符串。

编码（encoding）是程序将字符串对外输出时发生的，从字符串转化为字节码。

### 7.网际协议

网络互连（networking）指的是通过物理链路将多态计算机连接，使之可以相互通信。

网际互连（Internetworking）指的是将相邻的物理网络相连，使之形成更大的网络系统，比如互联网。

网络设备之间进行共享的基本单元是数据包（packet），数据包就像货币一样，只要有需要就可以交换。一个数据包是一串长度在几字节到几千字节之间的字节串。

数据包在物理层通常只有两个属性：包含的字节串数据以及目标传输地址。物理数据包的地址一般是一个唯一的标识符。**它标识了在计算机传输数据包的过程中，插入同一以太网段的其他网卡或无线信道。网卡负责发送和接收这样的数据包**，使得计算机操作系统不用关心网络是如何处理网线、电压及信号这些细节。

网际协议（IP，注意不是IP地址）是为全世界通过互联网连接的计算机赋予统一地址系统的一种机制，它使得数据包能够从互联网的一端发送到另一端。理想情况下，网络浏览器无需了解具体使用哪种网络设备来传输数据包，就能够连接上任意一台主机。

将主机名解析为IP地址这一复杂的细节是由操作系统来处理的。

特殊IP：

```
10.*.*.*
172.16-31.*.*
192.168.*.*
```

这些IP地址段是为私有子网（private subnet）预留的。运营互联网的机构保证局不会把这三个地址段中的任何地址分发给运行服务器或服务的实体公司。因此在连接互联网时，这些地址是没有意义的。所以如果要构建组织内部网络，可以随意使用这些地址。不需要让外网访问这些主机。

无线路由器或DSL调制调节器经常会把某个私有地址段中的IP地址分配各家用电脑和笔记本，这样就可以吧所有的网络流量隐藏起来。而网络服务商在分配给我们使用另一个“真正的”IP地址。

### 8.路由

根据目的IP地址选择将IP数据包发往何处就叫做路由（routing）。

大部分python代码都运行在网络边缘，因此路由就只需要决定将数据包留在本地网络还是将其发送到网络的其他部分。

如果IP地址以127开头，操作系统会知道数据包的目的地址是本机上运行的另一个应用程序，这个数据包甚至不会被传送给物理网络设备，而是直接通过操作系统的内部数据复制交给另一个程序。

如果目的的IP地址与本机处于同一子网，那么可以通过简单的检查本地以太网段、无线信道，或是其他任何网络信息来找到目标主机。然后就可以将数据包发送给本地连接的机器。

否则计算机将数据包转发给以太网关机器（Gateway machine）。这台机器将本地子网连接至互联网，然后决定将数据包发往何处。



操作系统通过结合IP地址和掩码来表示子网。掩码指出了某主机属于某子网所需的高位比特数。

```
127.0.0.0/8：表示前8位是网络号，必须与127匹配，后面24位（3字节）则可以是任意值
192.168.0.0/16:表示前16位（2字节）时网路号必须完全匹配，后面则任意。
192.168.5.0/24:前24位必须匹配，后面8位任意。这就允许有256个不同的地址。
```

通常说.0是用来表示子网名，.255则用作“广播数据包”的目标地址，广播数据包会被发送到子网内的所有主机。.1地址通常用于连接外网的网关。

额外内容：

utf-8是常见的Unicode编码方法。

python3做了一项尝试，永远不会自动将字节转换为字符串，原因在于要完成这一转换操作，就必须实现知道所使用的编码方法。