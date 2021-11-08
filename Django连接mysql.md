# Django连接mysql

##### 1.在虚拟环境中安装pymysql库

Django项目默认使用mysqldb模块进行和mysql数据库之间的交互操作，但是mysqldb模块对于python3.4以上的版本支持还不够完善，所以我们要使用替代方案
 通过pymysql模块完成和数据库之间的交互过程

我使用的是pipenv创建的虚拟环境，所以用

```
pipenv install pymysql
```

##### 2.在项目主目录下的__init__文件中添加下面代码

```python
import pymysql

#这一句很重要，不然会报错django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3，里面的数字可能会跟着具体版本号编号
pymysql.version_info = (1,3,13, 'final', 0)
pymysql.install_as_MySQLdb()
```

##### 3.在settings文件中设置数据库连接

```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 连接mysql
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',  #需要提前创建
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
```

##### 4.创建模型类

在任意app目录下的models文件中

```python
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

##### 5.将创建好的模型类映射到数据库

直接在命令行输入

```
python manage.py makemigrations
或
python manage.py makemigrations app_name
```

会创建一个如下的数据库表

```
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```

可以指定项目中的app的名字，也可以不指定，不指定则映射项目中全部app的表模型

运行此命令可以在app内的migrations文件夹下生成迁移记录文件

##### 6.将映射的数据表真正的在数据库中创建对应的表

运行下面命令

```
python manage.py migrate
或
python manage.py migrate app_name
```

然后就可以到mysql中对应数据库中看到生成的表了。

表的名字会以appname_person出现。