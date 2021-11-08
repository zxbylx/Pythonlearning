# Flask代码解读

### 1.app=Flask(\__name__)

几乎所有的flask项目的主程序都包含这么两行代码

```python
from flask import Flask

app = Flask(__name__)
```

第一行比较好理解，从flask里导入Flask这个类，第二行就稍微有点难理解了，至少我在学过简单的python基础的时候还看不太懂这行代码，因为好多python基础教程里知识都讲得比较简单，深入的地方都没有讲。整体上来说，是创建一个Flask类的实例app。

这个主要看右边，Flask(\__name__)，Flask是个类，这个应该好理解，里面传入一个参数，那应该就是Flask类的构造函数\_\_init\_\_()里有一个参数，我去看了下flask源码最初版本，代码太长，Flask类和构造函数\_\_init\_\_()截不到一个屏了，可以看左侧，Flask包含构造函数\_\_init\_\_()，且需要传入一个package_name参数，pack_name参数

[![UsrGWT.png](https://s1.ax1x.com/2020/07/17/UsrGWT.png)](https://imgchr.com/i/UsrGWT)

的解释在右侧方框了，包名称用于从内部解析资源，包或包含模块的文件夹，取决于参数解析为一个实际的python包（带有文件夹）的\__init__.py或是一个标准模块（只是一个.py文件）。

读起来挺难懂的，大致意思就是如果简单项目，一般就写一个主程序，package_name最终解析为就是这个主程序的名字，如果是一个python包，这个代码一般就是在构造文件里，解析出来就是包的名字。

要把上面解释通，还得需要说一下\__name__字段。之前遇到这个字段多是

```python
def hello():
    print('hello world')
if __name__ == '__main__':
	hello()
```

这个意思就是如果直接运行这个文件时，\__name__的值是'\_\_main\_\_'，那么就会运行hello函数，打印“hello world”，如果这个文件被其他文件导入，\_\_name\_\_的值就是文件名，那么就不会运行hello函数，一般下面这段用作测试用。

做个简单的测试，直接运行下面代码

```python
#文件名：hello.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    return '<h1>Hello, %s!</h1>' % name

print(__name__)
```

```
D:\GitHub\flask\helloflask\.venv\Scripts\python.exe D:/GitHub/flask/helloflask/demos/http/hello.py
__main__

Process finished with exit code 0
```

返回值是\__main__

如果用flask  run启动服务器

```
(helloflask) D:\GitHub\flask\helloflask\demos\http>flask run
 * Serving Flask app "hello" (lazy loading)
 * Environment: development
 * Debug mode: on
hello
 * Restarting with windowsapi reloader
hello
 * Debugger is active!
 * Debugger PIN: ********
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

返回hello，这也对应了上次在flask项目的配置信息里讲的，运行flask run命令，flask会自动探测程序实例，也就是把这个文件导入，所以返回值就是文件名了。



### 2.@app.route('/')