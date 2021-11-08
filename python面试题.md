# python面试题(1)

### 1.一行代码实现1-100之和

```python
sum(range(1, 100))
```

提到python求和肯定就是sum()函数了，首先我们得知道sum函数的用法。

##### sum()

语法：

```python
sum(iterable[, start])
```

参数：

iterable：可迭代对象，如列表、元组、集合、range。iterable的项官方文档中写的是**通常为数字**，后面遇到再说。

start：指定相加的参数（必须是数字类型），如果没有，默认0.这个参数是初始值，作用就是从这个初始值开始，不停的加第一个参数迭代出来的数字。

通过help查看sum的具体信息，发现3.7版本和3.8版本的内容是不一样的

python3.7

```python
>>>help(sum)
Help on built-in function sum in module builtins:

sum(iterable, start=0, /)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
```

python3.8

```python
>>> help(sum)
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.

```

这两个表达式中区别在于start=0和"/"的位置，要理解二者区别就需要知道"/"在这里是什么意思。这就需要说到函数的参数问题了。

```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

默认情况下，函数的参数传递形式可以是位置参数或是显示的关键字参数。为了确保可读性和运行效率，所以做了限制允许参数传递形式的做法。

斜杠前面的是仅限位置参数的，斜杠和星号中间的可以是位置参数，也可以是关键字参数，星号后面的是仅限关键字参数的。斜杠和星号是可选的，没定义则参数可以按位置也可以按关键字传递。

所以在python3.7中，如果你用关键字传递start会报错

```python
sum(range(1, 101), start=1)
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-17-96c0e320ac0a> in <module>
----> 1 sum(range(1, 101), start=1)

TypeError: sum() takes no keyword arguments
```

但是python3.8对sum()做了调整，使得start可以以关键字形式传递了

```
PS C:\Users\48967> python
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> sum([1, 2, 3], start=2)
8
```

sum其他用法：

```python
a = range(1,11)
b = range(1,10)
c =  sum([item for item in a if item in b])
print(c)
```

剩下的还有两个需要理解的，一个是可迭代对象，一个是range()函数。

##### 可迭代对象

这个我收集总结了下可迭代对象、迭代器和生成器的对比，可以看这篇文章，链接如下：

https://zhuanlan.zhihu.com/p/165251712

##### range()方法

在python2中，range()返回的是一个列表，python3为了节省空间，返回的是一个可迭代对象。所以打印时不会打印列表

```
>>> print(range(1, 10))
range(1, 10)
```

###### 函数语法

```python
range(stop)
range(start, stop[, step])
```

- start没有时默认为0，start和stop必须为整数类型
- range是包含start但是不包含stop
- step没有整数要求，默认是1，可以做小数，如果start比stop大，step必须指定且需要是负数，否则无效
- 它是不可变的序列类型，可以进行判断元素、查找元素、切片等操作，但不能修改
- 是可迭代对象，却不是迭代器

```python
>>>list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 2))
[0, 2, 4, 6, 8]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
#start大，stop小没指定step无效
>>> list(range(1, 0))
[]
#序列操作
>>> a = range(1, 10)
>>> a[1]
2
>>> a[0] = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'range' object does not support item assignment
#不是迭代器
>>> hasattr(range(3), '__iter__')
True
>>> hasattr(range(3), '__next__')
False
>>> hasattr(iter(range(3)), '__next__')
True
```

在 for-循环 遍历时，可迭代对象与迭代器的性能是一样的，即它们都是惰性求值的，在空间复杂度与时间复杂度上并无差异。我曾概括过两者的差别是“一同两不同”：相同的是都可惰性迭代，不同的是可迭代对象不支持自遍历（即next()方法），而迭代器本身不支持切片（即**getitem**() 方法）。



在找可迭代对象、迭代器和生成器资料的过程中看到一篇博客感觉挺不错的，讲range的，推荐一下。

python|range函数用法完全解读。

https://www.jianshu.com/p/e639605cd6c3