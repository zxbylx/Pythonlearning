# HTTP(11)：web的攻击技术

目前，大多的攻击是冲着web站点来的，把web应用作为攻击目标。

##### 针对web应用的攻击模式

主动攻击和被动攻击。

以服务器为目标的主动攻击(active attack):是指攻击者通过直接访问web应用，把攻击代码传入的攻击模式。具有代表性的攻击是SQL注入攻击和OS命令注入攻击。

以服务器为目标的被动攻击（passive attack）：是指利用全套策略执行攻击代码的攻击模式。不直接对目标web应用访问发起攻击。

[![UBdCCj.png](https://s1.ax1x.com/2020/07/16/UBdCCj.png)](https://imgchr.com/i/UBdCCj)

### 因输出值转义不完全引发的安全漏洞

实施web应用的安全对策可大致分为以下两部分：

- 客户端验证
- web应用端（服务器端）验证：输入值验证，输出值转义

多数情况采用JavaScript在客户端验证数据。但JavaScript验证允许篡改数据或关闭JavaScript，使用这个只是为了提高UI体验。

web应用端输入字验证通常是指检查是否符合系统业务逻辑的数值或检查字符编码等预防对策。

从数据库、文件系统、HTML、邮件等输出web应用处理的数据，针对输出做值转义处理是一项至关重要的安全对策，当输出值转义不完全时，会因触发攻击者传入的攻击代码，而给输出对象带来损害。

##### 跨站脚本攻击（Cross-site scripting，XSS），属于被动攻击

造成影响：

- 利用虚假输入表单骗取用户个人信息
- 利用脚本窃取用户的Cookie值，在被害者不知情的情况下，帮助攻击者发送恶意请求。
- 显示伪造的文章或图片。

##### SQL注入攻击

是指针对web应用使用的数据库，通过非法的SQL而产生的攻击。

影响：

- 非法查看或篡改数据库内数据
- 规避认证
- 执行和数据库服务器业务关联的程序等。

##### OS命令注入攻击

通过web应用，执行非法的操作系统命令达到攻击的目的。只要在能调用shell函数的地方就有存在被攻击的风险。

##### HTTP首部注入攻击

通过响应首部字段内插入换行，添加任意响应首部或主体的一种攻击。被动攻击。

向首部主体添加内容的攻击称为HTTP响应截断攻击。

影响：

设置任何cookie信息

重定向至任意URL

显示任意的主体（HTTP响应截断攻击）

##### 邮件首部注入攻击

web应用中的邮件发送功能，攻击者通过向邮件首部To或Subject内任意添加非法内容发起的攻击。利用存在安全漏洞的web网站，可对任意邮件地址发送广告邮件或病毒邮件。

##### 目录遍历攻击

对本无意公开的文件目录，通过非法截断其目录路径后，达成访问目的的攻击。也称为目录遍历攻击。

##### 远程文件包含漏洞

当部分脚本内容需要从其他文件读入时，攻击者利用外部服务器的URL充当依赖文件，让脚本读取之后，就可以运行任意脚本的一种攻击。主要是PHP存在的安全漏洞。

### 因设置或设计上的缺陷引发的安全漏洞

##### 强制浏览

从安置在web服务器公开目录下的文件中，浏览那些原本非自愿公开的文件。

文件目录一览：通过制定文件目录名称，即可在文件一览众看到显示的文件名

```
http:www.example.com/log/
```

容易被推测的文件名及目录名

```
http://www.example.com/entry/entry_081202.log 
```

可推出下一个文件时entry_081203.log

备份文件

```
http://www.example.com/cgi-bin/entry.cig（原始文件）
http://www.example.com/cgi-bin/entry.cig~（备份文件）
http://www.example.com/cgi-bin/entry.bak（备份文件）
```

由编辑软件自动生成的文件无执行权限，有可能直接以源码形式显示。

##### 不正确的错误消息处理

web应用的错误消息内包含对攻击者有用的信息：web应用抛出的错误消息，数据库等系统抛出的错误消息。

比如输入账户名密码时提示密码错误，就可以认定此账号已注册，只需要不断尝试密码。所以应用用户名或密码错误。

##### 开放重定向

对任意URL作重定向的功能，可能会被诱导跳转至恶意web网站。

### 因会话管理疏忽引发的安全漏洞

##### 会话劫持

攻击者过某种数段拿到用户的会话ID，并非法使用会话id伪装成用户达到攻击目的。会话ID记录客户端的cookie等信息。

获得会话ID的途径：

- 通过非正规的生成方法推测会话ID
- 通过窃听或XSS攻击盗取会话ID
- 通过会话固定攻击强行获取会话ID

[![UBrinI.png](https://s1.ax1x.com/2020/07/16/UBrinI.png)](https://imgchr.com/i/UBrinI)

##### 会话固定攻击

会话固定攻击会强制用户使用攻击者指定的会话ID，属于被动攻击。

##### 跨站点伪造请求（Cross-Site Request Forgeries， CSRF）

攻击者通过设置好的陷阱，强制对已完成认证的用户进行非预期的个人信息或设定信息等某些状态更新，属于被动攻击。

影响：

- 利用已通过认证的用户权限更新设定信息等；
- 利用已通过认证的用户权限购买商品
- 利用已通过认证的用户权限在留言板上发表言论。

### 其他安全漏洞

##### 密码破解

通过网络的密码试错：穷举法、字典攻击

字典攻击中有一种利用其他网站已泄露的ID及密码列表进行的攻击。很多用户习惯随意地在多个web网站使用同一套ID及密码，因此攻击有相当高的几率。

对已加密密码的破解（指攻击者入侵系统，已获得加密或散列处理的密码数据情况）：

- 穷举法、字典攻击类推
- 彩虹表：明文密码与对应散列值构成的数据表
- 拿到密钥
- 加密算法的漏洞

##### 点击劫持

利用透明的按钮或链接做成陷阱覆盖在web页面之上。又称为界面伪装。一些视频网站会在用户第一次点击播放时跳转到广告网站，回来第二次点击才能播放视频也是这种点击劫持。

##### DoS攻击

是一种让运行中的服务呈现停止状态的攻击。不仅限于web网站，还包括网络设备及服务器。

方式：

- 集中用访问请求造成资源过载，资源用尽的同时，实际上服务也就呈现停止状态。多台计算机发起的DoS攻击被称为DDoS攻击。通常利用那些感染病毒的计算机作为攻击者的跳板。
- 通过攻击安全漏洞使得服务停止。

##### 后门程序

开着设置的隐藏入口，可不按正常步骤使用受限功能。

- 开发阶段作为debug调用的后门程序。
- 开发者为了自身利益植入的后门程序。
- 攻击者通过某种方法设置的后门程序。