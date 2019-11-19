# python自学日记13——类和方法

## 1.操作符重载

通过定义其他的特殊方法，你可以为用户定义类型的各种操作符制定行为。例如，如果你为Time类定义一个__add__方法，则可在时间对象上使用+操作符

```python
class Time(object):
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def time_to_int(time):
        minutes=time.hour*60+time.minute
        seconds=minutes*60+time.second
        return seconds
    def increment(self,seconds):
        seconds+=self.time_to_int()
        return int_to_time(seconds)
    def print_time(time):
        print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))
    def is_after(self,other):
        return self.time_to_int()>other.time_to_int()
    def __str__(self):
        return '%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second)
    def __add__(self,other):
        seconds=self.time_to_int()+other.time_to_int()
        return int_to_time(seconds)
```

#当你对时间对象应用+操作符时，python会调用add，当你打印结果时，python会调用str
#修改操作符的行为以便它能够作用于用户定义的类型，这个过程叫做操作符重载

```python
start=Time(9,45)
duration=Time(1,35)
print(start+duration)
```

本来两个时间对象是不可以相加的，但是通过定义了add方法，则可以实现两个时间对象相加。

## 2.基于类型的分发

为Point对象编写一个add方法，可以接受一个对象或者元组，如果第二个操作对象是一个Point方法，则方法应该返回一个新的Point对象，其x坐标是两个操作对象的x坐标的和，y坐标也类似。

如果迭戈操作对象是一个元组，方法则将第一个元素和x坐标相加，将第二个元素和y相加，并返回一个包含相加结果的心Point对象。

首先需要判断传入的第二个参数的类型与第一个参数类型是否一致，这里需要用到内置函数isinstance，接收一个值和一个类对象（当然也可以换成列表、元组等），如果类型相同则返回True，否则返回False.

然后为每一种情况设置一个方法实现上述效果。

```python
class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print_point(p):
        print('(%g,%g)'%(p.x,p.y))
    def __str__(self):
        return '(%g,%g)'%(self.x,self.y)
    def increment(self,other):
        return (self.x+other[0]),(self.y+other[1])
    def __add__(self,other):
        if isinstance(other,Point):
            return self.add_point(other)
        else:
            return increment(self,other)#这里写错了，应该写成return self.increment(other)
    def add_point(self,other):
        return (self.x+other.x),(self.y+other.y)
```

```python
blank=Point(1,2)
white=Point(2,3)
print(blank+white)
```

返回(3,5)结果是对的，返回试一下元组

```python
print(blank+(2,3))
```

```
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-78-873124d5c067> in <module>
----> 1 print(blank+(2,3))

<ipython-input-74-241285b4e395> in __add__(self, other)
     14             return self.add_point(other)
     15         else:
---> 16             return increment(self,other)
     17     def add_point(self,other):
     18         return (self.x+other.x),(self.y+other.y)

NameError: name 'increment' is not defined
```

报错显示increment没有被定义，去类里面看了下发现在第二种情况的代码写错了，应该用方法而不是函数，将代码修改后

```python
class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print_point(p):
        print('(%g,%g)'%(p.x,p.y))
    def __str__(self):
        return '(%g,%g)'%(self.x,self.y)
    def increment(self,other):
        return (self.x+other[0]),(self.y+other[1])
    def __add__(self,other):
        if isinstance(other,Point):
            return self.add_point(other)
        else:
            return self.increment(other)
    def add_point(self,other):
        return (self.x+other.x),(self.y+other.y)
```

然后还是报同样的错误，按说明明已经修改成功了，应该返回正确的值，但还是报错，这就说到修改class类时需要重启服务器的问题了，判断标准是我把这段代码复制到另一个页面时是正常返回值，在本页面就一直报错，所以重启了jupyter notebook后就显示正常了。我记得在哪里看到修改class是需要重启服务器的。

## 3.编写一个叫做Kangaroo的类，有如下方法

1. 一个`__init__`方法，将属性pouch_contents(口袋中的东西)初始化一个空列表
2. 一个put_in_pouch方法接收任何类型的对象，并将它添加到pouch_contents中
3. 一个`__str__`方法，返回Kangaroo对象以及口袋中的内容的字符串表达形式。

创建两个Kangaroo对象，将它们赋值给kanga和roo，并将roo添加到kanga的口袋中。

```python
class Kangaroo(object):
    def __init__(self,pouch_contents=[]):
        self.pouch_contents=pouch_contents
    def put_in_pouch(self,a):
        self.pouch_contents.append(a)
    def __str__(self):
        return '%s'%self.pouch_contents
```

```python
kanga=Kangaroo([1])
roo=Kangaroo([2])
kanga.put_in_pouch(roo)
print(kanga)
```

这是我看到这个问题想到并写出的代码，但是这个里面有个小的问题，初始化时pouch_contents=[]不具有扩展性，如果修改类的话原来写的都会跟着变，所以在查看答案代码中它有把第一个方法做了下调整：

```python
class Kangaroo(object):
    def __init__(self, contents=None):
        if contents == None:
            contents = []
        self.pouch_contents = contents
    def put_in_pouch(self,a):
        self.pouch_contents.append(a)
    def __str__(self):
        return '%s'%self.pouch_contents
```

将contents带一个默认值，如果不传参数时就按默认值处理，如果传入参数可以按传入参数处理，扩展性会好一些。

然后答案代码将第三个方法也有处理，不过和我的不一样

```python
class Kangaroo(object):
    def __init__(self, contents=None):
        if contents == None:
            contents = []
        self.pouch_contents = contents
    def put_in_pouch(self,a):
        self.pouch_contents.append(a)
    def __str__(self):
        """return a string representation of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)
```

我基本上能理解这个方法，就是对`object.__str__(self)`有点疑问，暂时还无法理解，上网查了下发现涉及了一些继承的问题，放在后面学了继承之后再回来看看这个问题。