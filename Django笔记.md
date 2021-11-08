# Django笔记

##### 1.设置时区

在settings里设置

```
TIME_ZONE = 'Asia/Shanghai'
```

但是经过测试不足以修改前端或数据库存储的时间，还需要修改

```
USE_TZ = False
```

此时调用时间为中国时间。源码

```python
def now():
    """
    Return an aware or naive datetime.datetime, depending on settings.USE_TZ.
    """
    if settings.USE_TZ:
        # timeit shows that datetime.now(tz=utc) is 24% slower
        return datetime.utcnow().replace(tzinfo=utc)
    else:
        return datetime.now()
```

##### 2.改变模型需要3步：

编辑model.py文件，改变模型

运行python manage.py makemigrations 为模型的改变生成迁移文件

运行python manage.py migrate 来应用数据库迁移。

##### 3.{% static %}模板标签在静态文件中不可用

`{% static %}` 模板标签在静态文件（例如样式表）中是不可用的，因为它们不是由 Django 生成的。你仍需要使用 *相对路径* 的方式在你的静态文件之间互相引用。这样之后，你就可以任意改变 `STATIC_URL`（由 :ttag:`static` 模板标签用于生成 URL），而无需修改大量的静态文件。