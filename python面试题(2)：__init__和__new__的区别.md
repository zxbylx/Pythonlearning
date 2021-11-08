# python面试题(2)：`__init__`和`__new__`的区别

python中的`__init__`并不是真正意义上的构造函数，它只是在实例创建好后进行初始化

真正创建实例的是`__new__`方法，主要作用有两个：

第一个是在内存中为对象分配空间

第二个是返回对象的引用

所以如果重写了new方法就需要加上下面这行代码返回对象的引用

```
return super().__new__(cls)
```



1.`__new__`才是真正的构造函数，`__init__`不是构造函数

主要区别在于：`__new__`是用来创造一个类的实例的(constructor)，而`__init__`是用来初始化一个实例的(initializer)。



##### python中新类和旧类

python中类分为新类和旧类，旧类是python3之前的类，旧类并不是默认继承object类，而是继承type类。

以object为基类可以使得所定义的类具有新类所对应的方法(methods)和属性(properties)。



`**__new__`和`__init__`参数不同**

**`__new__`第一个参数是cls，而`__init__`第一个参数是self。这是因为我们调用`__new__`的时候，该类的实例还不存在（也就是self所引用的对象还不存在），所以需要接受一个类作为参数，从而产生一个实例。而当我们在调用`__init__`的时候，实例已经存在，因此`__init__`接收self作为第一个参数并对该实例进行必要的初始化操作。这也意味着`__init__`是在`__new__`之后被调用的。**



##### python旧类中的`__new__`和`__init__`

python旧类中实际上没有`__new__`方法，因为旧类中`__init__`实际上起构造器的作用，所以如果我们定义如此旧类：

```python
#在python2中，如果在python3新类中会被调用
class oldStyleClass:
    def __new__(cls):
        print('__new__ is called')  #这一行在创建实例的时候不会被调用
oldStyleClass()
```

输出结果

```
<__main__.oldStyleClass instance at 0x0000000002639F08>
```

可见创建及初始化对象过程中并没有调用`__new__`方法，实际上除非显示调用`oldStyleClass.__new__(oldStyleClass)`，该类中的`__new__`方法中的内容永远不会被调用。因为旧类构造实例并不会调用`__new__`方法。

但如果我们重载`__init__`方法：

```python
class oldStyleClass:
    def __init__(self):
        print('__init__ is called')
oldStyleClass()
```

输出结果

```
__init__ is called
<__main__.oldStyleClass instance at 0x00000000026C9F08>
```

如果在__init__中加上return语句，将会导致报错，TypeError: __init__() should return None, not 'int'。

这意味着对于python的旧类而言，无法控制__init__函数的返回值。

##### python新类中的`__new__`和`__init__`

python的新类中允许用户重载__new__和__init__方法，且这两个方法具有不同的作用。__new__作为构造器，起创建一个类实例的作用，而`__init__`作为初始器，起初始化一个已被创建的实例的作用。

```python
class newStyleClass:
    def __new__(cls):
        print('__new__ is called')
#         return super(newStyleClass, cls).__new__(cls)  #python2用法
        return super().__new__(cls)    #python3用法,super()用于调用父类的一个方法，在这里就是调用                                        #object类的__new__(cls)方法。
    def __init__(self):
        print('__init__ is called')
        print('self is:', self)
        
newStyleClass()
```

结果如下：

```
__new__ is called
__init__ is called
self is: <__main__.newStyleClass object at 0x000001E89C6C3D88>
<__main__.newStyleClass at 0x1e89c6c3d88>
```

创建类实例的过程中`__new__`和`__init__`被调用的顺序从上面的输出结果也可以看出，`__new__`函数先被调用，构造了一个newStyleClass的实例，接着`__init__`函数在`__new__`函数返回一个实例的时候被调用，并且这个实例作为self参数被传入`__init__`函数。

需要注意的是，如果`__new__`函数返回一个已经存在的实例（不论是哪个类），`__init__`不会被调用.

```python
obj = 12
class returnExistedObj:
    def __new__(cls):
        print('__new__ is called')
        return obj
    
    def __init__(self):
        print('__init__ is called')
        
returnExistedObj()
```

输出结果

```
__new__ is called
12
```



如果`__new__`函数中不返回任何对象，则`__init__`函数也不会调用。

```python
class notReturnObj:
    def __new__(cls):
        print('__new__ is called')
        
    def __init__(self):
        print('__init__ is called')
        
notReturnObj()
```

输出结果

```
__new__ is called
```

可见如果`__new__`函数不返回对象的话，不会有任何对象被创建，`__init__`函数也不会被调用来初始化对象。

如果`__new__`函数返回一个别的类的实例，`__init__`函数也不会被调用。

```python
class sample:
    def __str__(self):
        print('sample')
        
class example:
    def __new__(cls):
        print('__new__ is called')
        return sample()
    def __init__(self):
        print('__init__ is called')
        
example()
```

输出结果

```
__new__ is called
<__main__.sample at 0x1e89d616908>
```



### 总结

|            | `__new__`                                                    | `__init__`                                                   |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 调用时间   | 创建对象实例前                                               | 创建对象实例后                                               |
| 第一个参数 | cls，因为还没有实例，需要传入cls创建实例,此参数在实例化时由python解释器自动提供 | self(`__new__`方法的返回对象），实例已经创建，传入self初始化实例 |
| 作用       | 在内存中为对象创建内存空间，返回对象实例                     | 初始化对象实例                                               |
| 返回值     | 对象实例                                                     | None，且不能有返回值，有就报错                               |
| 旧类       | 没有`__new__`方法                                            | `__init__`充当构造器                                         |
| 类型       | 静态方法                                                     | 实例方法                                                     |

只有在`__new__`创建的是当前类的实例，才会调用当前类的`__init__`方法，就像前面所看到的，如果`__new__`方法创建的是别的类的实例，或其他对象，那么`__init__`方法不会被调用.



##### 补充内容

###### `__new__`的作用

依照python官方文档的说法，__new__方法主要是当你继承一些不可变class时（比如int, str, tuple)，提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass.

首先看一下第一个功能，具体可以用int来作为一个例子：

假如我们需要一个永远都是正数的整数类型，通过集成int，我们可以通过重载__new__方法得到想要的结果

```python
class PositiveInteger(int):
    def __new__(cls, value):
        return super().__new__(cls, abs(value))
    
a = PositiveInteger(-3)
print(a)
```

输出结果是3.证明重载`__new__`方法实现了需求的功能。



###### 用__new__方法实现单例模式

什么是单例模式：简单来说就是一个类只能创建一个实例的设计模式。

意图：保证一个类只有一个实例，并提供一个访问它的全局放完点。

使用场景：当你想控制实例数目，节省系统资源的时候。

如何实现：判断系统是否有这个单例，如果有则返回，没有则创建。

关键代码：构造函数是私有的。

```python
class singleClass:
    def __new__(cls):
    	#关键步骤，如果判断当前类没有instance属性，则创建一个实例，如果已经有了则返回已创建的实例
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
a = singleClass()
b = singleClass()
a.attr = 'value1'
print(a)
print(b)
print(b.attr)
a is b
```

输出结果

```
<__main__.singleClass object at 0x000001E89DE74DC8>
<__main__.singleClass object at 0x000001E89DE74DC8>
value1
True
```

从结果可以看出a.attr值与b.attr值相同，a is b返回的是true，也就是说他们共用一个实例。

###### 静态方法与实例方法

1.静态方法属于整个类所有，因此调用它不需要实例化，可以直接调用(类.静态方法()), 实例方法必须先实例化，创建一个对象，才能进行调用(对象.实例方法())

2.静态方法只能访问静态成员，不能访问实例成员，而实例方法可以访问静态成员和实例成员

3.在程序运行期间，静态方法是一直存放在内存中，因此调用速度快，但是却占用内存，实例方法是使用完成后由回收机制自动进行回收，下次再使用必须再实例化。

4.一般来说，公共的函数、经常调用的可以写成静态方法，比如数据连接等。

https://blog.csdn.net/lihao21/article/details/79762681

https://zhuanlan.zhihu.com/p/40162669