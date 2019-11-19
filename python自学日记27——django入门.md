# python自学日记27——django入门

这段时间一直在折腾数据结构和算法问题，弄得我也是相当头大。有的资料确实不适合入门，看到二叉搜索树和图时确实有点懵，只讲了如何构建，但没讲怎么用，看着代码敲完一遍也没啥感觉。有些还难以理解。

这段时间也让我对学习python和学习编程有了新的认识。就像我昨天回答一个知乎提问说的，有的人想学Python应该要想清楚是喜欢Python还是喜欢编程，如果喜欢编程那应该多学几门语言。因为这就像学习自然语言一样，你认知的边界就是你语言的边界，你可以通过学习另一门语言来拓宽视野，这也是我一直觉得在可能情况下多学几门外语的原因。

回到编程上来，从最近学习数据结构和算法来说，我就发现如果只用Python来学数据结构和算法，比较难通过Python的实现来完全理解和掌握这些，这个和学习基础不一样，基础只要跟着一本好的资料敲代码就差不多了，但是算法需要从多个例子中总结其中的规律和实现方法。一个算法和数据结构在Python中可能就好几种实现，但是因为语言的限制不会有太大的差别，如果想对这个有更加深入的理解，从C语言、java的角度来实现就会对你理解这些更有帮助。从其他编程语言的角度来看你以前实现过的方法和函数会给你带来不一样的认识。

所以，从以前想单单把Python学好，现在开始学一些别的语言作为辅助。最近看了前端、java。

本来是希望在两周内把基本的数据结构和算法大致过一遍，从现在看就剩树和图有些问题，当然进度也在预期内，不过想学好算法并不是短期内能成功的事，后面就把数据结构和算法这块当做一个定期学习的任务。

现在开始做一些别的内容，因为最近看了前端嘛，想着就把web开发也学一下。那就从Django开始简单入门下。

学这块发现跟前面的基础和算法就区别挺大的了，首先一上来就是要创建虚拟环境。

然后又提出项目的概念，本来以前都是在jupyter notebook中单个文件写代码，现在开始要按项目来了。

说到虚拟环境就完全不理解，以前只听说过虚拟机，开发Python时不是安装了anaconda了集成开发环境了嘛，为什么还要虚拟环境呢，我从原来刚开始学编程时吃过各种环境变量、编译器、运行环境等问题的亏，以前为了准备这些东西都能把我好不容易积攒的学编程的乐趣给消耗殆尽，所以现在完全不纠结用什么编译器，文本编辑器等软件，这次遇到虚拟环境第一个想到的就是这到底是不是必须的，能不能不安装，你说要安装就安装总得给个理由吧，然后上网查，别人都只说创建虚拟环境用virtualenv，虚拟环境的作用是为了将新项目所需要的库与原来通用的库隔开。

反正都说好，具体哪里好也没说明白，然后看到步骤上多是Linux,或者Mac上的命令符，就想找个windows版本的，然后在b站找到视频看到视频下面有提到anaconda一嘴，发现好像他们讲的并不适合anaconda。所以还得找用anaconda创建虚拟环境的方法。

由于步骤网上都有，我只记录我自己认为对我和其他学习这块内容时有用的提示：

1. 如果你装了anaconda可以用anaconda Prompt创建虚拟环境，方法很简单，创建虚拟环境其实就像新建了一个文件夹一样，虚拟环境需要激活，激活：activate+虚拟环境名；
2. 在使用虚拟环境安装Django的过程中才发现pip和conda是有区别的，我用pip安装一遍发现虚拟环境文件下没有，还安装在原来文件下了，用conda安装才出现在虚拟环境文件下，具体的区别可以上网查一下，区别不大。因为我以前都是用pip这次突然发现区别值得记录一下。
3. 很多网上的或者书上的教程或问题解决方案随着时间的推移可能都不再合适，需要自己来辨别。就像我在创建Django项目时，按照书上的步骤`django-admin.py startproject learning_log .` 无法将项目创建到我想要的文件夹下，总是把文件创建到Django安装文件夹下，后面根据网上的步骤将二者结合，先在anaconda prompt中修改目录，然后再输入`django-admin startproject learning_log .`才在自己新建的文件夹下创建了项目。
4. 如果你跟着教程敲完代码后报错，排除了语法和自己输入错误后你可以勇于判断是教程的代码有问题，要么代码本身错了，要么是代码由于过时导致的错误。以前我总是怀疑是自己的问题，后面发现确实教程过时速度太快。所以我才一直想说不要只看别人的例子，要从例子中总结出自己的思路。

就像下面的问题，Django项目中让修改models.py文件

```Python
from django.db import models

# Create your models here.
class Topic(models.Model):
    #用户学习主题
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text

class Entry(models.Model):
    '''学到的有关某个主题的具体知识'''
    topic=models.ForeignKey(Topic)#这一行出错了
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='entries'
        
    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text[:50] + '...'

```

一般修改这个管理数据需要三步，第一步修改models.py，第二步执行命令python manage.py makemigrations app_name,在执行命令python manage.py migrate让Django迁移项目。但是这次在第二步时报错了，报错内容：

```
  File "E:\jupyter notebook\Django\project\learning_logs\models.py", line 27, in Entry
    topic = models.ForeignKey(Topic)
TypeError: __init__() missing 1 required positional argument: 'on_delete'
```

我检查了一遍代码发现和例子中的代码没有区别，那就应该是例子本身除了问题，然后上网查到将15行改为：

```
topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
```

在后面添加on_delete=models.CASCADE即可。原因是：在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错。老版本中models.CASCADE是默认值。这就是由于更新导致了教程出了问题。



在写models.py文件时遇到一个内部类的问题，第一次遇到所以记录一下，在定义一个类中还可以定义一个类class Meta，这个是给model定义元数据。元数据：不是一个字段的任何数据。感觉和自己理解的元数据不太一样。

常见属性有：

app_label:只有一种使用情况，就是你的模型类不再应用程序包下的models.py中，需要制定这个模型类是那个应用程序包的，看样子是可以跨文件使用的。

```Python
app_label='程序名'
```

再说一个现在遇到的：verbose_name_plural,这个选项制定模型的复数形式是什么：

```Python
verbose_name_plural='entries'
```

如果不提供这个属性，Django会使用verbose_name+'s'，也就是Entrys.



新建一个项目总是记不住步骤来回翻，把这个记录一下：

1. 打开anaconda prompt，启动虚拟环境：activate my_env(环境名)

2. 切换目录，找到你想创建项目的文件夹：cd E:\jupyter notebook\Django\pizzeria

3. 创建项目：`django-admin startproject learning_log .`learning_log是项目名，可以随便替换，后面空格后加一个'.'，这是必须的。

4. 创建数据库：`python manage.py migrate`，项目文件中新增一个db.sqlite3的文件。

5. 核实项目是否创建成功，启动服务器：`python manage.py runserver`,然后可以到URL http://http://127.0.0.1:8000/，打开查看是否成功了。在anaconda prompt按Ctrl+C或者关闭窗口可关闭服务器。

6. 创建应用程序：因为此时命令窗口已经运行服务器了，需要再打开一个anaconda prompt，重新走1,2两步到目录：`python manage.py startapp appname`，此时项目文件中会新增一个appname的文件夹，打开这个文件夹。

7. 定义模型：打开models.py从里面就可以定义想要的类了。这样就可以用到面向对象编程的知识了。

8. 激活模型：打开3中创建的项目名文件，找到settings.py，在INSTALLED_APPS的列表最后添加一个a应用程序名，就是6步中的appname.格式跟前面的需一致。

9. 需要让Django修改数据库，使其能够存储与创建模型相关的信息。即上面讲过的对appname调用makemigrations，在anaconda prompt中输入：`python manage.py makemigrations appname`,名利makemigrations让Django确定如何修改数据库，使其能够存储与我们定义新模型相关联的数据。

10. 应用迁移，让Django替我们修改数据库：`python manage.py migrate`

11. django管理网站

    - 创建超级用户：`python manage createsuperuser`，这里需要注意下，后面会让输入用户名，email，两遍密码。这两遍密码输入是没有反应的，我刚开始以为键盘出毛病了，检测下键盘没事，然后觉得可能命令窗口卡死了，重启还是这样，查了下发现这是正常现象，密码输入有显示星号的，有显示圆点的，这里就是什么都不显示也不反馈的，连输两遍如果对了就报对，错了就让你重输入。

    - 向管理员注册模型：在models.py所在目录中创建了一个名为admin.py的文件，打开修改，添加

      ```Python
      from appname.models import +7步中的类名
      
      admin.site.register(7步中的类名)
      ```

      这里我出了一个错误，上面一行用逗号将两个类名隔开，下面也在括号里这样做导致报错，下面应该将二者用两行写

      ```Python
      from django.contrib import admin
      
      # Register your models here.
      from pizzas.models import Pizza,Topping
      admin.site.register(Pizza,Topping)#上面可以写到一起，但是下面需要分开
      ```

      正确的应该是隔开的，这就是没动脑子靠记忆写的问题

      ```Python
      admin.site.register(Pizza)
      admin.site.register(Topping)
      ```

      修改这边是不需要走9和10两步的，只有修改models.py才需要走9和10两步。
    
    

最好的教程根本堆叠基本知识和例子，而是把自己解决问题的思路和学习的方法传递出去。对于我自己来说我希望的是我写的内容让我过段时间回过来再看是依然有效的，如果只是把例子写下来那是对我对大家都没什么用的。