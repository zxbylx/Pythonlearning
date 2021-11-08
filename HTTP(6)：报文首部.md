# HTTP(6)：报文首部

### HTTP首部字段

HTTP首部字段根据实际用途被分成四种类型。

通用首部字段：请求报文和响应报文都会使用的首部；

请求首部字段：从客户端向服务器端发送请求报文时使用的首部，补充了请求的附加内容，客户端信息、响应内容相关优先级等信息；

响应首部字段：从服务器端向客户端返回响应报文时使用的首部，补充了响应的附加内容，也会要求客户端附加额外的内容信息；

实体首部字段：针对请求报文和响应报文的实体部分使用的首部。补充了资源内容更新时间等实体有关的信息。

[![UdmKmT.png](https://s1.ax1x.com/2020/07/15/UdmKmT.png)](https://imgchr.com/i/UdmKmT)

[![UdmfHS.png](https://s1.ax1x.com/2020/07/15/UdmfHS.png)](https://imgchr.com/i/UdmfHS)

[![Udmz4J.png](https://s1.ax1x.com/2020/07/15/Udmz4J.png)](https://imgchr.com/i/Udmz4J)

[![UdnbPH.png](https://s1.ax1x.com/2020/07/15/UdnbPH.png)](https://imgchr.com/i/UdnbPH)

[![Udn7Ie.png](https://s1.ax1x.com/2020/07/15/Udn7Ie.png)](https://imgchr.com/i/Udn7Ie)

[![UdnqGd.png](https://s1.ax1x.com/2020/07/15/UdnqGd.png)](https://imgchr.com/i/UdnqGd)

HTTP首部字段根据是否定义成缓存代理，分成两种类型，端到端首部(End-to-end Header)和逐跳首部(Hop-by-hop Header)。

端到端首部会转发给请求/响应对应的最终目标，且必须保存在由缓存生成的响应中，另外规定它必须被转发。

逐跳首部只对单次转发有效，会因通过缓存或代理而不再转发。HTTP/1.1和之后版本，如果要使用需要提供Connection首部字段。除了以下8个，其他都是端到端首部。

- Connection
- Keep-Alive
- Proxy-Authenticate
- Proxy-Authorization
- Trailer
- TE
- Transfer-Encoding
- Upgrade