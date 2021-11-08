# windows/Linux常用命令行

默认上面windows下面linux

### 1.查看本机IP地址

```
PS C:\Users\48967> ipconfig
```

```
(base) zxbylx@zxbylx-Lenovo-G470 ~ $ ifconfig
禁用某个网卡（enp7s0是网卡名）：
(base) zxbylx@zxbylx-Lenovo-G470 ~ $ sudo ifconfig enp7s0 down
开启某个网卡：
(base) zxbylx@zxbylx-Lenovo-G470 ~ $ sudo ifconfig enp7s0 up
```

### 2.快速回到行首和行尾

```
windows没有找到，只找到一个单词一个单词往前移动的方法，相比一个字母一个字母移动要快一点
Ctrl+←和Ctrl+→ ： 他们分别跳到前一个单词和后一个单词
```

```
Ctrl+A：回到行首
Ctrl+E：回到行尾
```

### 3.查看端口号

```
列出所有端口号情况
PS C:\Users\48967> netstat -ano
查看被占用端口对应的PID，注意findstr后面有空格
发现-ano和-aon都能用，也是奇怪
PS C:\Users\48967> netstat -ano|findstr "135"
PS C:\Users\48967> netstat -aon|findstr "3306"
查看进程的PID是哪个应用程序，注意前面两个数字是端口号，这个是PID
PS C:\Users\48967> tasklist|findstr "3040"
```

linux系统中netstat命令参数：

-a:表示所有
-t:显示TCP端口
-u：显示UDP端口
-p:查询占用的程序，显示进程标识符和程序名称，每一个套接字/端口都属于一个程序
-l:查询正在监听的程序（套接字就是使用应用程序能够读写与收发通讯协议与资料的程序）
-n:不进行DNS轮询，显示IP。

与grep结合可查询某个具体端口及服务情况

```
netstat -ntlp              #查看所有的tcp端口
netstat -ntulp |grep 80    #查看所有的80端口使用情况
netstat -an | grep 3306    #查看所有3306端口使用情况
```

查看一台服务器上有哪些服务及端口

```
netstat -lanp
```

查看一个服务有几个端口，比如要查看mysqld

```
ps -ef | grep mysqld
```

查看某一端口的连接数量，比如3306端口

```
netstat -pnt | grep :3306 | wc
```

查看某一端口的连接客户端IP，比如3306端口

```
netstat -anp | grep 3306
netstat -an  #查看所有网络端口
```

