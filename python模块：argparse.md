# python模块：argparse

argparse模块是python标准库中推荐的命令行解析模块。是一个用于解析和验证命令行参数的接口。它支持将字符串转换为整数和其他类型。遇到某个选项时可以运行回调，可以为用户未提供的选项设置默认值，还可以为程序自动生成使用说明。

还有另外两个模块可以完成同样的任务，称为getopt(对应C语言中的getopt()函数)和被弃用的optparse。argparse是基于optparse的，因此用法非常相似。

argparse模块包含一些工具来构建命令行参数和选项处理器。给我的感觉就是，以前我们运行python文件只能

```powershell
PS D:\GitHub\python_network\chapter2> python prog.py
```

后面是没有任何参数的，有了argparse可以在这个命令行后面添加参数来做一些事情了。例如下面在命令行输入一个数字返回它的平方

```powershell
PS D:\GitHub\python_network\chapter2> python prog.py 4
16
```



### 使用步骤

1. 创建ArgumentParser()对象
2. 调用add_argument()方法添加参数
3. 使用parse_args()解析添加参数

### 简单示例

```python
import argparse

parser = argparse.ArgumentParser(description='这是一个简单的示例')
parser.add_argument('echo', help='echo the string you use here')
parser.parse_args()
print(args.echo)
```

这个在命令行中就是你输入什么就打印什么

```powershell
(python_network) D:\GitHub\python_network\chapter2>python prog.py hello
hello
```

https://www.cnblogs.com/iMX8mm/p/10821468.html