# python自学日记12——类和函数

有时候把一个问题弄得更难（或者更通用）反而会让它变得更简单（因为会有更少的特殊情况以及更少的出错机会）。

## 1.编写一个print_time函数，接收一个时间对象作为形参并以“时：分：秒”的格式打印它。

要演示这个问题，需要先把时间对象写出来，首先定义一个类,然后实例化生成一个时间对象

```python
class Time(object):
    '''
    Represents the time of day.
    attributes:hour,minute,second
    '''
time=Time()
time.hour=1
time.minute=9
time.second=30
```

这个相对简单一些，不过为了打印出来美观一些，需要对呈现结果做一些处理，格式操作符'%.2d'可以以最少两个字符打印一个整数，如果需要会在前缀添加0

```python
def print_time(t):
    h='%.2d'%t.hour
    m='%.2d'%t.minute
    s='%.2d'%t.second
    return h+':'+m+':'+s
#     print(h+':'+m+':'+s)
print_time(time)
```

本来我是用print打印的，但是由于后面的练习需要这个函数的输出值，所以后面改成了return，这点其实已经好几次出现了，一定要记得print打印出来后type类型是Nonetype，需要用到值时改成return，注意二者区别。

## 2.编写一个布尔函数is_after,接收两个时间对象，t1和t2，并若t1在t2后面则返回True，否则返回False

这次我做了一个挑战，就是不用if语句。让我想起以前有个例子中通过操作符来替代if语句的判断情况，所以我最初代码如下

```python
time2=Time()#因为要比较需要两个参数，所以新建一个对象
time2.hour=2
time2.minute=23
time2.second=1
def is_after(t1,t2):
    return t1>t2
is_after(time,time2)
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-20b0e959ab71> in <module>
      6 def is_after(t1,t2):
      7     return t1>t2
----> 8 is_after(time,time2)
      9 

<ipython-input-8-20b0e959ab71> in is_after(t1, t2)
      5 time2.second=1
      6 def is_after(t1,t2):
----> 7     return t1>t2
      8 is_after(time,time2)
      9 

TypeError: '>' not supported between instances of 'Time' and 'Time'
```

但是报错了，提示类之间不支持'>'这个操作，我想是不是可以用前者减后者大于0来替代：

```python
time2=Time()
time2.hour=2
time2.minute=23
time2.second=1
def is_after(t1,t2):
    return t1-t2>0
is_after(time,time2)
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-d902a560f822> in <module>
      6 def is_after(t1,t2):
      7     return t1-t2>0
----> 8 is_after(time,time2)
      9 

<ipython-input-9-d902a560f822> in is_after(t1, t2)
      5 time2.second=1
      6 def is_after(t1,t2):
----> 7     return t1-t2>0
      8 is_after(time,time2)
      9 

TypeError: unsupported operand type(s) for -: 'Time' and 'Time'
```

显然我没有抓住错误的重点，重点是Time这个类，我比较的是两个类的对象，发现比较错值了，应该比较的是前一个练习中返回的那个时间，所以将代码改成下面：

```python
time2=Time()
time2.hour=2
time2.minute=23
time2.second=1
def is_after(t1,t2):
    return print_time(t1)>print_time(t2) #如果前者大于后者返回True，否则返回False，这样可以替代判断语句
is_after(time,time2)
```



今天在求两个时间之间的间隔时刚开始是使用借位实现的减法，后面发现如果先把时间对象转换成整数，求完差值或和再转换成时间时会更简单。

先写两个函数，一个是将时间转换为整数秒，然后另一个是将秒转换为时间。

```python
def time_to_int(time):
    minutes=time.hour*60+time.minute
    seconds=minutes*60+time.second
    return seconds
```

```python
def int_to_time(seconds):
    time=Time()
    minutes,time.second=divmod(seconds,60)#divmod函数将第一个参数除以第二个参数并以元组形式返回商和余数
    time.hour,time.minute=divmod(minutes,60)
    return time
```

写完我们需要做一个简单的测试，测试上面两个函数时正确的

```python
time_to_int(int_to_time(100))==100
```

返回值是True，证明上面的函数是正确的，当对时间求和时可以简单的写成：

```python
def add_time(t1,t2):
    seconds=time_to_int(t1)+time_to_int(t2)
    return int_to_time(seconds)
```

**有时候把一个问题弄得更难（或者更通用）反而会让它变得更简单（因为会有更少的特殊情况以及更少的出错机会）。**



**调试建议：在调试时学到一个新概念，不变式**

个事件对象当minute和second的值在0到60（包含0不包含60）之间，以及hour是正值时，是合法的，这些需求称为不变式，因为它们应当总是为真。

这给我们做调试提供了方向
编写代码来检查不变式可以帮助你探测错误并找寻它们的根源，例如下面

```python
def valid_time(time):
    if time.hour<0 or time.minute<0 or time.second<0:
        return False
    if time.minute>=60 or time.second>=60:
        return False
    return True
```

先通过不变式写出一个函数，接在在每个函数开头可以通过不变式检查函数，确保它们是有效的。

```python
#接收每个函数的开头，可以检查参数，确保它们是有效的
def add_time(t1,t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    seconds=time_to_int(t1)+time_to_int(t2)
    return int_to_time(seconds)
```

