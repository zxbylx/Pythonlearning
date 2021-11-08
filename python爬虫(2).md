# python爬虫(2)

一个标准的链接

```
http://www.baidu.com/index.html;user?id=5#comment
```

解析链接

```python
from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
```

返回值

```
<class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
```

urlparse()方法将其拆分为6个部分。大体观察可以发现，解析时有特定的分隔符。比如，://前面的就是scheme，代表协议；第一个/符号前面便是netloc，即域名，后面是path，即访问路径；问好?前面是params，代表参数；问好?后面是查询条件query，一般作用于GET类型的URL；井号后面是锚点，用于直接定位页面内部的下拉位置。

```python
#只有在前面没有scheme信息时后面的scheme参数才起作用，放到上面的scheme就没有用。
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
#allow_fragments:即是否忽略fragment，如果被设置为False就会忽略，解析出来fragment部分为空
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https',allow_fragments=False)
```

返回的ParseResult实际上是一个元组，可以用索引顺序来获取，也可以用属性名来获取。

```python
from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(result.scheme, result[0], result.netloc, result[1], sep='\n')
```

##### urljoin()拼接链接

```python
#urljoin()链接拼接
from urllib.parse import urljoin

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://zhaoxinbo.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://zhaoxinbo.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://zhaoxinbo.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://zhaoxinbo.index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))
```

```
http://www.baidu.com/FAQ.html
https://zhaoxinbo.com/FAQ.html
https://zhaoxinbo.com/FAQ.html
https://zhaoxinbo.com/FAQ.html?question=2
https://zhaoxinbo.index.php
http://www.baidu.com?category=2#comment
www.baidu.com?category=2#comment
www.baidu.com?category=2
```

可以看出，第一个参数base_url，提供了三项内容scheme，netloc和path，如果这3项在第二个参数中不存在，就予以补充；如果新的链接中存在，就是用新的链接。第一个参数中params，query和fragment不起作用。

### requests

```python
#知乎cookies测试
import requests

headers = {
    'Cookie': '_zap=2ecc4dbd-9873-481a-ab80-345cef37a870; d_c0="AEAZD9uxNhGPTszWQRldyxNaqC_Cdwe70Pc=|1588508278"; '
              '_ga=GA1.2.1836073403.1588508280; z_c0="2|1:0|10:1588563892|4:z_c0|92:Mi4xV0k1dUFRQUFBQUFBUUJrUDI3RTJFU1l'
              'BQUFCZ0FsVk50TjJjWHdCRmR3aV9fS1lnLU84SktsbXVYMVpTVWdkYjR3|27b9c8d224c03ededb14b23ce4b58e680a7e9fdce8b7af'
              'f94d5ee196f121ead4"; tst=r; ff_supports_webp=1; q_c1=96c07b1d18384ec8abe80974e3d1149e|1594355962000|'
              '1588564687000; _gid=GA1.2.374081753.1595777261; _xsrf=cb710bb1-8d62-48bd-94fa-9ed7d6425b7e; '
              'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1596214962,1596252460,1596261370,1596261621; '
              'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1596286783; SESSIONID=kf8r1QBL6QG3eUOgLhg3nnPMD2bDsnjQbGDhu0ANSJH; '
              'JOID=U1AdBkMygyF5yV6eGjaT-RqUiQwCUOUUBvEG3FsN22ZHoQLYfXrpBCLJV5MaIEzASjLmosBTUlkmneQp56iMzhY=; '
              'osd=VFodBk81iSF5xVmUGjaf_hCUiQAFWuUUCvYM3FsB3GxHoQ7fd3rpCCXDV5MWJ0bASj7hqMBTXl4sneQl4KKMzho=; '
              'KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1596286789|1596286780',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)

```

这里有一个注意的地阿芳，就是由于cookies太长需要换行时，注意如果是想着空格处换，记得要在空格后面换行，前面换行会把空格自动给去掉导致报错。

```
requests.exceptions.InvalidHeader: Invalid return character or leading space in header: Cookie
```

