# HTTP(2)

HTTP是一种无状态（stateless）协议。协议自身不对请求和响应之间的通信状态进行保存。每当有新的请求发送时，就会有对应的新的响应产生。协议本身并不保留之前一切的请求或响应报文信息。

原因：为了更快的处理大量事物，确保协议的可伸缩性，而特意将HTTP协议设计成如此简单。

优点：由于不保存状态，自然可以减少服务器的CPU以及内存资源的消耗。

但是有时候需要保存状态，比如用户的登录状态，这时候引入cookie技术，就可以管理状态了。

### 请求报文

请求报文由报文首部（请求方法、请求URI、协议版本、可选的请求首部字段）和报文主体（内容实体）构成，两者由空行分割，报文的主体内容一般为空。

[![UUcPTU.png](https://s1.ax1x.com/2020/07/14/UUcPTU.png)](https://imgchr.com/i/UUcPTU)

### 响应报文

响应报文基本上是由报文首部（协议版本、状态码（status code）、用以解释状态码的原因短语、可选的响应首部字段）以及报文主体（实体主体）构成，二者空格隔开。

[![UUchAU.png](https://s1.ax1x.com/2020/07/14/UUchAU.png)](https://imgchr.com/i/UUchAU)

### HTTP方法

##### GET方法：获取资源

用来请求访问已被URI识别的资源。指定的资源经服务器端解析后返回响应内容。如果请求的是文本，则保持原样返回；如果是CGI（Common Gateway Interface，通用网关接口）那样的程序，则返回经过执行后的输出结果。

[![UU8hBq.png](https://s1.ax1x.com/2020/07/14/UU8hBq.png)](https://imgchr.com/i/UU8hBq)

##### POST方法：传输实体主体

[![UUYjDs.png](https://s1.ax1x.com/2020/07/14/UUYjDs.png)](https://imgchr.com/i/UUYjDs)

##### PUT方法：传输文件

PUT方法用来出传输文件，要求请求报文的主体中包含文件内容，然后保存到请求URI指定的位置。

但是，鉴于HTTP/1.1的PUT方法自身不带验证机制，任何人都可以上传文件，存在安全性问题，因此一般的web网站不使用此方法。若配合web应用程序的验证机制，或架构设计采用REST(REpresentational State Transfer, 表征状态转移)标准的同类web网站，就可能会开放使用PUT方法。

[![UUNCdI.png](https://s1.ax1x.com/2020/07/14/UUNCdI.png)](https://imgchr.com/i/UUNCdI)

这个响应的意思是请求执行成功了，但无数据返回。

##### HEAD方法：获得报文首部

HEAD方法和GET方法一样，只是不返回报文主体部分。用于确认URI的有效性及资源更新的日期时间等。

[![UUNjkq.png](https://s1.ax1x.com/2020/07/14/UUNjkq.png)](https://imgchr.com/i/UUNjkq)

##### DELETE方法：删除文件

DELETE方法是与PUT反复相反的方法。按请求URI删除指定的资源。但是HTTP/1.1的DELETE本身也不带验证机制，所以一般也不实用。当配合web应用程序的验证机制或遵守REST标准时还是有可能开放使用的。

[![UUUwuQ.png](https://s1.ax1x.com/2020/07/14/UUUwuQ.png)](https://imgchr.com/i/UUUwuQ)

##### OPTIONS方法：询问支持的方法

用来查询针对请求URI指定的资源支持的方法。

[![UUaErQ.png](https://s1.ax1x.com/2020/07/14/UUaErQ.png)](https://imgchr.com/i/UUaErQ)

##### TRACE方法：追踪路径

TRACE方法是让web服务器将之前的请求通信环回客户端的方法。

发送请求时，在Max-Forwards首部字段填入数值，每经过一个服务器端就将该数字减1，当数值刚好为0时，就停止继续传输，最后接收到请求的服务器端则返回状态码200 OK的响应。

客户端通过TRACE方法可以查询发出去的请求时怎么样被加工/篡改的。这是因为，请求想要连接到源目标服务器可能会通过代理中转，TRACE方法就是用来确认连接过程中发生的一系列操作。本身不常用，再加上容易引发XST（Cross-Site Tracing，跨站攻击）攻击，就更不会用到了。

[![UUdylT.png](https://s1.ax1x.com/2020/07/14/UUdylT.png)](https://imgchr.com/i/UUdylT)

##### CONNECT方法：要求用隧道协议连接代理

CONNECT方法要求在与代理服务器通信时建立隧道，实现用隧道协议进行TCP通信。主要使用SSL（Secure Sockets Layer，安全套接层）和TLS（Transport Layer Security， 传输层安全）协议把通信内容加密后经网络隧道传输。

格式：

CONNECT 代理服务器名：端口号 HTTP版本



[![UU0FxK.png](https://s1.ax1x.com/2020/07/14/UU0FxK.png)](https://imgchr.com/i/UU0FxK)

[![UUD8EQ.png](https://s1.ax1x.com/2020/07/14/UUD8EQ.png)](https://imgchr.com/i/UUD8EQ)

### 持久连接节省通信

HTTP协议初始版本中，每进行一次HTTP通信就要端口一次TCP连接。以前都是容量很小的文本传输，所以没什么问题。现在一个网页中有大量图片，每次请求会造成无畏的TCP连接建立和断开，增加通信的开销。

为解决这个问题，HTTP/1.1和一部分HTTP/1.0想出了持久连接（HTTP Persistent Connections， 也称为HTTP keep-alive 或HTTP connection reuse）的方法。特点是，只要任意一端没有明确提出断开连接，则保持TCP连接状态。

好处：减少了TCP连接和断开造成的额外开销，减轻了服务器端的负载。另外，减少开销的那部分时间，使HTTP请求和响应能够更早地结束，这样web页面的显示速度也就相应提高了。

##### 管线化

前提是需要持久连接。从前发送请求后需要等待并收到响应才能发送下一个请求，管线化技术出现后，不用等待响应亦可直接发送下一个请求。并行发送多个请求。管线化技术比持久连接还要快，请求数越多，时间差越明显。

### 使用Cookie的状态管理

Cookie会根据从服务器端发送的响应报文内的一个叫做Set-Cookie的首部字段信息，通知客户端保存cookie。当下次客户端再往服务器端发送请求时，客户端会自动在请求报文中加入cookie值后发送出去。

服务器端发现客户端发送过来的cookie之后，会去检查究竟是从哪个客户端发送过来的请求，然后对比服务器上的记录，最后得到之前的状态信息。