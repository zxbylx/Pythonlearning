# Flask项目的配置信息

#### 1.安装pipenv并创建虚拟环境

```
windows:
pip install pipenv

Linux或macOS:
sudo pip install pipenv
```

如果有多个版本的python注意是安装到哪个python上，查看使用pip还是pip3。

检查pipenv是否安装和版本号

```
pipenv --version
```

##### 创建虚拟环境

先在项目跟目录下创建.venv文件夹，这样使得虚拟环境安装在本项目下。默认情况下pipenv会统一管理虚拟环境，在windows中虚拟环境文件夹在C:\Users\Administrator\.virtualenvs\目录下，在Linux或macOS中会在~/.local/share/virtualenvs目录下创建。命令行在创建完成会提示虚拟环境文件夹位置。

```
pipenv install
```

如果目录下没有pipfile和pipfile.lock文件，则会创建这两个文件，如果有，会安装pipfile里列出的依赖包。

##### 激活虚拟环境

```
pipenv shell
```

除了显示地激活虚拟环境，pipenv还提供了一个pipenv run命令，这个名利允许在不显示激活虚拟环境即可在当前目录的虚拟环境中执行命令，例如：

```
pipenv run python hello.py
```

pipenv install只要在当前目录，无论激不激活虚拟环境，安装包时都会装在虚拟环境中。

pipfile和pipfile.lock用于管理依赖，替代requirements.txt文件，优势是无需手动维护这两个文件，当使用pipenv安装/删除/更新依赖包时，这两个文件会自动更新。requirements.txt需要手动维护，在文件中指出了包和对应版本号，但是这并不能保证不同计算机安装的就是同一个包，但是pipfile.lock将包的具体版本进行hash，使用这个hash安装的包就会是相同版本的相同包，不会出现相同版本，但是包不一样的情况。

另外pipfile文件内还区分普通依赖包和开发专属依赖包，普通依赖包是开发环境和生产环境都需要用到的，开发专属依赖包则只在开发环境使用，生产环境用不到。安装开发环境依赖包命令在普通安装命令后面加--dev：

```
pipenv install watchdog --dev
```

查看依赖列表

```
pipenv graph
或在虚拟环境中使用
pip list
```

前者展示的内容会更详细些，会写出需要的依赖包需要高于哪个版本，而当前的包版本号是多少。

升级命令

```
pipenv update flask
```

#### 2.安装并运行flask

##### 安装flask

```
pipenv install flask
```

安装flask时还同时安装了5个依赖包：

- Jinja2(模板渲染引擎)
- MarkupSafe(HTML字符转义工具，escape)
- Werkzeug(WSGI工具集，处理请求与相应，内置WSGI开发服务器、调试器和重载器)
- click(命令行工具)
- itsdangerous(提供各种加密签名命令)

在项目根目录下创建app.py，名字可以随便取，但是非app.py需要设置环境变量FLASK_APP=文件名

##### 启动开发服务器

flask通过依赖包Click内置了一个CLI(Command Line Interface, 命令行交互界面)系统。当安装flask后，会自动添加一个flask命令脚本。可以通过flask命令执行内置命令、扩展提供的命令或自定义的命令。前提是需要提前激活虚拟环境，如果没有激活需要在前面添加pipenv run例如pipenv run flask run.

可以通过flask --help查看所有可用的命令

```
Usage: flask [OPTIONS] COMMAND [ARGS]...
命令：
flask assets  关于压缩css/js等文件的命令，还没用过，会列出如flask --help的命令介绍
flask db      执行数据库迁移
flask routes  显示路由命令
flask run     运行开发服务器(development)，这个用的最多
flask shell   在虚拟环境下运行一个python shell。
```

flask run命令运行的开发服务器默认会监听127.0.0.1:5000/,按Ctrl + C退出。并开启多线程支持。如果执行flask run命令后显示命令未找到提示(command not found)或其他错误，可以尝试使用python -m flask run命令。

##### 自动发现程序实例

运行flask run命令之所以不需要提供程序实例(app=Flask(__name__))所在模块(app.py)的位置，是因为flask会自动探测程序实例，自动探测规则：

- 从运行flask run的当前目录寻找app.py和wsgi.py模块，并从中寻找名为app或application的程序实例。
- 从环境变量FLASK_APP对应的值寻找app或application的程序实例。

程序主模块命名为app.py，flask run能自动在其寻找程序实例，如果不是app.py，则必须设置环境变量FLASK_APP，将包含程序实例的模块名赋值给这个变量。只有这样，flask run才能正确扎到这个模块。

Linux 或 macOS命令：

```
export FLASK_APP=hello  #hello是包含程序实例的模块名hello.py
```

windows命令：

```
set FLASK_APP=hello
```

##### 管理环境变量

除了FLASK_APP之外，后面还会有其他的环境变量要设置，在命令行设置的缺点就是关掉命令行后环境变量就消失了，再运行flask时还需要重新设置，所以人们为了不频繁设置环境变量，决定用配置文件来设置，这就涉及了一个依赖包python-dotenv,用这个依赖来管理环境变量，安装后在**项目跟目录下**创建.env和.flaskenv两个文件。

.flaskenv用来存储和flask相关的公开环境变量，比如FLASK_APP、FLASK_ENV等，.env用来存储包含敏感信息的环境变量，比如用来配置email服务器的账户名密码。内容格式使用键值对形式如FLASK_APP=hello，不需要引号，#用作注释。.env文件都是私有信息，不要上传到远程仓库，记得把它的名称添加到.gitignore文件中，会告诉git忽略这个文件。

优先级：手动在命令行设置的环境变量>.env中设置的环境变量>.flaskenv中设置的环境变量。

##### flask run命令扩展

flask run命令后面可以带主机和端口

```
flask run --host=0.0.0.0   #这会让服务器监听所有外部请求
flask run --port=8000      #监听8000端口
```

主机和端口也可以用环境变量来设置FLASK_RUN_HOST=0.0.0.0和FLASK_RUN_PORT=8000。

##### 设置运行环境

环境变量FLASK_ENV可以设置运行环境，development为开发环境，production为生产环境，flask run运行的是开发环境，如果设置为production会有警告，但是可以运行。一般这个环境变量在.flaskenv文件中设置

在开发环境中，调试模式(Debug Mode)将开启，运行flask run程序会自动激活Werkzeug内置的调试器和重载器。

注意在生产环境绝对不能开启调试模式。

调试器：当程序出错时，会在网页上看到详细的错误追踪，有时候内容实在太多，把顶部的报错信息复制，通过Ctrl + F查找，可以迅速确定到报错位置。

调试器允许在网页上运行python代码。单机错误信息右侧的命令行图标，会弹出窗口要求输入PIN码，也就是在启动服务器在命令行窗口打印出的调试器PIN码。输入PIN码后，可以单击错误堆栈的某个节点右侧的命令行节面图标，这回打开一个包含代码执行上下文信息的python shell，可以利用它来进行调试。

重载器：每次修改代码后，会自动重启服务器即可看到修改的变化。HTML文件修改不会重启服务器，直接刷新网页就可以了。

默认使用的是Werkzeug内置的stat重载器，缺点是耗电严重，准确性一般。改用python库中的Watchdog，因为只有开发环境使用，所以安装时在后面添加--dev.会在pipfile文件的dev-packages部分显示开发依赖包。

```
pipenv install watchdog --dev
```

##### 3.python shell

在flask项目中可以使用flask shell命令打开python shell,退出可以执行exit()或quit()，windows中可以使用Ctrl+Z并按Enter退出，Linux和macOS则按Ctrl+D直接退回。

使用flask shell命令打开的python shell自动包含程序上下文，并且已经导入了app实例：

```
>>> app
<Flask 'hello'>
>>> app.name
'hello'
```

我试了下用python打开python shell，然后直接输入app会报错

```
(helloflask) D:\GitHub\flask\helloflask\demos\hello>python
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> app
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'app' is not defined
```

需要提前导入app实例才行

```
>>> from hello import app
>>> app
<Flask 'hello'>
>>> app.name
'hello'
```

上下文(context)可以理解为环境。为了正常运行，一些相关操作的状态和数据需要被临时保存下来，这些状态和数据被统称为上下文，在flask中，上下文有两种，分为程序上下文和请求上下文。后面记得单独整一篇上下文的笔记。