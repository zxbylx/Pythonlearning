# Python3 struct报错: argument for 's' must be a bytes object

在用python3进行文件打包二进制数据的存储与解析过程中使用struct模块运行下面代码发生错误：

```python
F = open('data.bin', 'wb')
import struct
data = struct.pack('>i4sh', 7, 'spam', 8)
data
```

报错信息如下：

```
error                                     Traceback (most recent call last)
<ipython-input-12-9b7a8e6cf48b> in <module>
      1 F = open('data.bin', 'wb')
      2 import struct
----> 3 data = struct.pack('>i6sh', 7, 'spam', 8)
      4 data

error: argument for 's' must be a bytes object
```

先说解决方案：格式化字符串的值在python的类型是bytes类型，而python3中所有文本都是Unicode，所以需要转换为bytes类型，在'spam'前面加’b'进行转换。

```python
F = open('data.bin', 'wb')
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)
data
```

输出结果是：

```
b'\x00\x00\x00\x07spam\x00\x08'
```

## python3新增的bytes类型

在python2中字节类型和字符类型区别不大，但是在python3中最重要的特性是对文本和二进制数据做了更加清晰的区分。

文本总是Unicode,由字符类型表示，而二进制数据则由bytes类型表示。

python3不会以任意隐式方式混用字节型和字符型，也因此在python3中不能拼接字符串和字节包（python2中可以，会自动进行转换），也不能在字节包中搜索字符串，也不能将字符串传入参数为字节包的函数。

需要注意的是，在网络数据传输过程中，python2可以通过字符串(string)方式传输，但是python3只能通过二进制(bytes)方式来传输，因此要对传输文本进行转换。

转化方式：

str → byte 用encode()方法
byte → str 用decode()方法

中文字符串转二进制：

```python
'你好'.encode('utf-8')
```

输出：

```
b'\xe4\xbd\xa0\xe5\xa5\xbd'
```

二进制转回字符串：

```python
b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8')
```

输出：'你好'



英文字符串转二进制

```python
'hello world'.encode('utf-8')
```

输出：

```
b'hello world'
```

encode（）和decode（）方法中**默认编码**为utf-8，但是为了避免错误，最好将编码加上。



仅仅知道加'b'可以解决问题但是感觉还是不够，'>i4sh'看不懂，所以去官方文档查struct看到结果如下：

struct.pack(format, v1, v2, ...)
返回一个 bytes 对象，其中包含根据格式字符串 format 打包的值 v1, v2, ... 参数个数必须与格式字符串所要求的值完全匹配。

![tYpo1f.png](https://s1.ax1x.com/2020/06/02/tYpo1f.png)

可以看出i对应的是python中的整数，s对应的是字符串，h对应的是整数。

格式字符之前可以带有整数重复计数。 例如，格式字符串 `'4h'` 的含义与 `'hhhh'` 完全相同。

所以测试了一下，在h前加数字2：

```python
F = open('data.bin', 'wb')
import struct
data = struct.pack('>i4s2h', 7, b'spam', 8)
data
```

报错如下：

```
---------------------------------------------------------------------------
error                                     Traceback (most recent call last)
<ipython-input-33-a27281e58db6> in <module>
      1 F = open('data.bin', 'wb')
      2 import struct
----> 3 data = struct.pack('>i4s2h', 7, b'spam', 8)
      4 data

error: pack expected 4 items for packing (got 3)
```

也是就说2h就需要在s后面有2个整数参数，但是'4s'却不是需要四个bytes参数。

对于 's' 格式字符，计数会被解析为字节的长度，而不是像其他格式字符那样的重复计数；例如，'10s' 表示一个 10 字节的字节串，而 '10c' 表示 10 个字符。 如果未给出计数，则默认值为 1。 对于打包操作，字节串会被适当地截断或填充空字节以符合要求。

所以做了个测试，先后将s前的数字从1慢慢涨到6得到的输出结果如下：

```
b'\x00\x00\x00\x07s\x00\x08'               #'>i1sh'
b'\x00\x00\x00\x07sp\x00\x08'              #'>i2sh'
b'\x00\x00\x00\x07spa\x00\x08'             #'>i3sh'
b'\x00\x00\x00\x07spam\x00\x08'            #'>i4sh'       
b'\x00\x00\x00\x07spam\x00\x00\x08'        #'>i5sh'
b'\x00\x00\x00\x07spam\x00\x00\x00\x08'    #'>i6sh'
```

在数字小于后面字节长度时会截取，超过长度时会在后面填充空字节。