# Virtualenv、pipenv、conda虚拟环境设置方法及原理

## 1.为什么要创建虚拟环境

我第一次接触虚拟环境时第一感觉就是抵触，相信刚开始被各种配置折磨过的小伙伴能理解，我就想是否可以不用虚拟环境，就查了下推荐使用虚拟环境的理由：

(1)所有的项目的库都放到一个地方容易混乱，而且比较冗余，毕竟不是所有的项目都需要那么多的库（这一点我根本就不关心嘛，少一步配置就少被折磨一次）

(2)因为工作以后都是分工协作的，这个项目能在你电脑上运行，但是到了别人那如果没有安装相应的库就无法运行，所以需要大家能够在库上进行同步（就是一个库同步嘛，可以手动整理一个库列表就可以啦，为了少一步配置也是拼了）

(3)不同的项目对同一个库版本要求不一样，如果A项目要求一个库的版本低，B项目的要求同一个库版本高，运行B项目升级了这个库覆盖前一个版本，就会导致A项目无法运行(这倒是一个比较充足的理由，看样子非得要配置虚拟环境了)



## 2.配置虚拟环境(windows)

以下虚拟变量只针对python3，python2过时了就不说了。

### 使用Virtualenv配置虚拟环境

随便找一个目录新建一个文件夹，在此文件夹内打开命令提示符，输入下面命令：

```
python -m venv venv
```

虚拟环境就创建完成了，需要注意的点：

有的命令会说python3 -m venv venv,其实第一个python或者python3就是在命令行里运行python的命令，前提是你的python添加到了系统环境变量了。

所以你需要在命令行试一下

[![Uka0aD.png](https://s1.ax1x.com/2020/07/07/Uka0aD.png)](https://imgchr.com/i/Uka0aD)

像我这边使用python和py -3能正常使用python shell，所以我这边使用

```
python -m venv venv
py -3 -m venv venv
```

都可以创建虚拟环境，有的人同时装了python2.7和python3.7或其他python3版本，如果默认python是2.7那么就使用py -3 -m venv venv就可以了。一定要试一下，下面的python shell显示的是python3版本的才可以了。因为venv是python3新增的虚拟环境设置方法。

我在D:\GitHub\git仓库\test运行上面命令后就在此文件夹下创建了一个venv的文件夹，所以呢，这个命令行的最后一个venv是可以自定义的，比如

```
python -m venv hello
```

然后就在test文件夹下创建了一个hello文件夹，文件夹里面就是解释器和需要的库文件夹。

[![UkBlO1.png](https://s1.ax1x.com/2020/07/07/UkBlO1.png)](https://imgchr.com/i/UkBlO1)

如果使用

```
python -m venv .
```

后面使用点号，那么虚拟环境就会创建在test文件夹下，而不是在test文件夹下新建一个文件夹来创建虚拟环境。

##### 激活虚拟环境：

首先我们需要进入到虚拟环境的Scripts文件夹下，然后输入activate

[![UkwRUS.png](https://s1.ax1x.com/2020/07/07/UkwRUS.png)](https://imgchr.com/i/UkwRUS)

虚拟环境前面会有一个小括号的标记，激活虚拟环境后再用pip安装包时就会安装到此虚拟环境中，而不是系统环境中了。

退出虚拟环境的命令：deactivate，目录对是不是Scripts没有要求。但是激活虚拟环境必须在Scripts环境中。

##### 复制或者导出虚拟环境

在虚拟环境内输入：

```
pip freeze > requirements.txt
```

注意，这个在哪个目下输入，requirements.txt文件就在当前目录生成，包含库和对应的版本号，每运行一次，会覆盖上一次生成的文件。

[![Ukrri8.png](https://s1.ax1x.com/2020/07/07/Ukrri8.png)](https://imgchr.com/i/Ukrri8)

新建一个项目，创建并激活虚拟环境，把上面的requirements.txt文件复制到Scripts文件夹下，输入：

```
pip install -r requirements.txt
```

然后就把上一个项目的库导入到这个项目中来了。这样的好处是大家用的是相同版本号的库，不会出现项目不兼容的情况。

### 使用pipenv配置虚拟环境

我还是用D:\GitHub\git仓库\test这个目录，顺便说一下删除虚拟环境，把虚拟环境文件夹直接删除就可以了，这样也比较方便。

因为pipenv不是python自带的，所以我们需要先安装这个库，因为经常用就全局安装

```
pip install pipenv
在Linux或macOS中全局安装
sudo pip install pipenv
```

##### 创建虚拟环境

```
pipenv install
```

默认情况下pipenv会同一管理所有的虚拟环境。在Windows中，虚拟环境文件夹会在C:\Users\你的用户名文件\.virtualenvs

文件夹下，

[![Uk6UsJ.png](https://s1.ax1x.com/2020/07/07/Uk6UsJ.png)](https://imgchr.com/i/Uk6UsJ)

记不住目录没有关系，命令行里会有提示

[![Ukc7A1.png](https://s1.ax1x.com/2020/07/07/Ukc7A1.png)](https://imgchr.com/i/Ukc7A1)

但是我并不想把虚拟环境放到C盘目录下，想把虚拟环境放到项目文件夹下，有两种方法：

在使用pipenv install之前先在项目文件夹下创建一个文件.venv，然后再运行pipenv install就可以了；

另一种方法，先在命令行下配置环境变量

```
PIPENV_VENV_IN_PROJECT=True
```

意思是pipenv的虚拟环境在项目里，然后再隐形pipenv install创建环境变量，这样就在项目文件夹下创建了虚拟环境文件夹。虚拟环境跟着项目走，比较方便。

有个小插曲：我看到上面的图片上创建虚拟环境的解释器是用的anaconda的python3.7.6，我一直理解是通过系统变量里的python3版本创建，因为我没有把anaconda的python3添加到环境变量，出了这个情况我就检查了下原因，新建了一个文件夹并创建虚拟环境发现又回到python3.8，也就是添加到环境变量的那个python，不是集成anaconda里的python，想起是因为test文件夹刚才试过用conda的虚拟环境导致的问题。所以，我的理解没啥问题，还是默认用python3且是系统变量里的那个版本。

在当前文件夹下创建虚拟环境文件夹的同时，还创建了两个文件Pipfle和Pipfile.lock，这两个文件用于管理依赖。作用等同与上一个方法中的requirements.txt，不过好处是不许要手动维护，在安装python库时会自动更新两个文件。前者用来记录项目依赖包列表，而后者记录了固定版本的详细依赖包列表。当我们使用pipenv 安装/删除/更新依赖包时，二者自动更新。

所以要记得，这里安装包用pipenv命令。由于官方源比较慢，所以记得安装包时提前打开Pipfile更换国内源，把原来的地址替换为国内源地址即可

![Uk4OIJ.png](https://s1.ax1x.com/2020/07/07/Uk4OIJ.png)



我这个是替换为清华的，其他的也一样。原地址为https://pypi.org/simple，会比较慢。

然后运行pipenv安装库，例如

```
pipenv install flask
```

上面的图已经安装了flask，在[packages]下面就显示了flask，[dev-packages]下的是只用于开发环境的包，安装时在后面加”--dev"即可

```
pipenv install watchdog --dev
```

这里只显示了包列表，没有显示具体版本信息，这些内容在Pipfile.lock文件内显示

[![UkILC9.png](https://s1.ax1x.com/2020/07/07/UkILC9.png)](https://imgchr.com/i/UkILC9)

运行pipenv install时，会检测当前文件夹下有没有这两个文件，如果有的话，就创建虚拟环境并安装Pipfile里的包，就如同上个方法用pip install -r requirements.txt命令一样。如果没有则创建者两个文件。这两个文件上传git时需要记得传上去。

##### 激活虚拟环境

可以用pipenv shell命令显示的激活虚拟环境，而且不需要进入scripts文件即可激活虚拟环境

[![UkHTMR.png](https://s1.ax1x.com/2020/07/07/UkHTMR.png)](https://imgchr.com/i/UkHTMR)

退出用exit命令。

除了显示地激活虚拟环境，Pipenv还提供了一个pipenv run命令，这个命令允许不显示激活虚拟环境即可在当前项目的虚拟环境中执行命令，比如：

```
pipenv run python app.py
```

这会使用当前项目虚拟环境中的python解释器，而不是全局的python解释器。这个命令可以让你不用关心自己是否忘记激活虚拟环境的问题。相比上一个方法必须激活才能运行要方便的多。同时pipenv install numpy这种安装包的命令也可以忽略是否激活了虚拟环境。

总体上来讲，pipenv从管理依赖、激活虚拟环境和运行命令方面要比上一个方法方便。推荐大家使用。

### 使用conda创建虚拟环境

首先打开Anaconda Prompt，这个与cmd命令行类似，打开之后直接是运行了anaconda基础的虚拟环境。

[![UkLjiT.png](https://s1.ax1x.com/2020/07/07/UkLjiT.png)](https://imgchr.com/i/UkLjiT)

打开之后

[![UkO9y9.png](https://s1.ax1x.com/2020/07/07/UkO9y9.png)](https://imgchr.com/i/UkO9y9)

这就算打开了anaconda自带的base虚拟环境。cmd也可以运行这个，只不过麻烦一点，先找到anaconda安装目录，找到Scripts文件夹，运行activate激活虚拟环境就进入anaconda了，下面是用cmd命令行打开的

[![UkO26J.png](https://s1.ax1x.com/2020/07/07/UkO26J.png)](https://imgchr.com/i/UkO26J)

用conda创建虚拟环境不需要提前创建文件夹什么的，因为conda专门在anaconda文件下指定了一个虚拟环境的目录envs,直接运行下面命令即可创建虚拟环境

```
conda  create -n python37 

conda  create -n python37  python=3.7
或者
conda  create -name python37  python=3.7
```

第一个没有指定python版本，后面两个指定了python版本。这是conda与上面两个稍微不同的地方，也许上面连个也能指定，但是暂时不清楚，毕竟anaconda可以同时存在python3.5,python3.6，python3.7，python3.8等，但是上面两个应该不行。

运行完命令后可以在envs下面看到新建的虚拟环境文件夹。

[![UkXO8U.png](https://s1.ax1x.com/2020/07/07/UkXO8U.png)](https://imgchr.com/i/UkXO8U)

name后面的就是虚拟环境的名字，文件夹内对应出现python37文件夹。

虚拟环境创建完成需要切换环境，用activate 环境名

```
activate python37
```

如果忘记了可以用conda env list查看虚拟环境列表

[![UASQmQ.png](https://s1.ax1x.com/2020/07/07/UASQmQ.png)](https://imgchr.com/i/UASQmQ)

进入虚拟环境之后就可以用conda安装包了，推荐用conda，比pip要好用一点。导出上第一个方法一样

```
pip freeze > requirements.txt
```

这有个问题就是虚拟环境时固定在anaconda安装包里的，把项目创建者anaconda安装包里的情况应该是不常见的，所以在别的地方创建了项目，需要把解释器指定到这个虚拟环境里，用pycharm为例，打开File>Settings>Project:test>Python Interpreter

点击右侧设置，选择show all

[![UAp5KU.png](https://s1.ax1x.com/2020/07/07/UAp5KU.png)](https://imgchr.com/i/UAp5KU)如果是第一次点击右侧加号添加这个虚拟环境，如果已经有了从列表中选择即可

[![UApIrF.png](https://s1.ax1x.com/2020/07/07/UApIrF.png)](https://imgchr.com/i/UApIrF)选择已经存在的环境，点击右侧按钮进入目录选择

[![UAphvT.png](https://s1.ax1x.com/2020/07/07/UAphvT.png)](https://imgchr.com/i/UAphvT)这里要注意一下，上面两个的python.exe都是在Scripts文件夹中，conda的就是在根目录中

[![UApf2V.png](https://s1.ax1x.com/2020/07/07/UApf2V.png)](https://imgchr.com/i/UApf2V)

设置完就可以使用anaconda创建的虚拟环境了。

## 3.虚拟环境原理

说到虚拟环境，是与python实际的环境对应的，虚拟环境就是python实际环境的一个副本，不过是一个简化版的副本。那虚拟环境到底做了些什么呢，其实也很简单，我们可以对比一下path环境变量

![UAen1J.png](https://s1.ax1x.com/2020/07/07/UAen1J.png)

上面的是激活了虚拟环境的环境变量，下面的是没有激活虚拟环境的系统环境变量，仔细对比一下就是虚拟环境在系统环境变量前插入了一个变量，截胡了。因为谁在前面运行谁，所以在虚拟环境中运行的python就都是虚拟环境中设置的python了。取消激活虚拟环境后，系统的环境变量就恢复成下面的样子了。