# python自学日记11——类和对象

## 1.编写一个函数move_rectangle,接受一个Rectangle对象和两个值，dx,dy。它应当通过添加dx到corner的x坐标和添加dy到corner的y坐标来改换矩形的位置

因为这个练习涉及了很多前面的例子和练习，如果不写出来可能看不懂，所以把需要涉及的内容先写出来。

首先我们定义一个类型叫做类：

```python
class Point(object):
    '''Represents a point in 2-D space.'''
print(Point)
```

```
<class '__main__.Point'>
```

然后我们建一个矩形的类：

```python
class Rectangle(object):
    '''Represents a rectangle
    attributes:width,height,corner.
    '''
box=Rectangle()
box.width=100.0 #矩形宽度
box.height=200.0 #矩形高度
box.corner=Point() #corner是Point的一个对象，用来指定左下角的定点
box.corner.x=0
box.corner.y=0
```

然后然后下面是练习的代码，这个函数相对容易，有三个形参，一个是对象，另外两个值作用在corner坐标上，结果如下

```python
def move_rectangle(rect,dx,dy):
    rect.corner.x+=dx
    rect.corner.y+=dy
move_rectangle(box,10,20)
print_point(box.corner)
```

```
(10,20)
```



对象是可以复制的，我们可以使用copy模块对对象进行复制，不过复制分为浅复制copy和深复制deepcopy

```python
import copy
box2=copy.copy(box)
box2 is box
#box2 == box #也会返回False因为==对于实例来说的默认行为和is是相同的
```

```
False
```

```python
box2.corner is box.corner #这表明copy复制对象本身但不复制内嵌的Point对象，称为浅复制
```

```
True
```

下面是深复制例子

```python
box3=copy.deepcopy(box)#与浅复制相对，deepcopy深复制复制对象和内嵌的对象，甚至他们引用的对象以此类推，就是全复制了
box3.corner is box.corner 
```

```
False
```

以上所有的举例和练习都是为了让下面的联系好理解

## 2.编写move_rectangle的一个版本，它会新建并返回一个Rectangle对象，而不是直接修改就有的对象

分解这个问题，不直接修改对象移动首先就需要复制矩形，不能用浅复制的原因是虽然矩形被复制了，但是他们共用一个corner，所以实际上导致原矩形被移动了，所以需要用深复制，不过需要得出一个新对象，我想可不可以用四个参数，第二个参数作为复制第一个参数，不过需要先做一个简要的实验；

```python
def a(rect,rect1):
    rect1=copy.copy(rect)
a(box,box1)
```

```
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-33-550f2a30860b> in <module>
      1 def a(rect,rect1):
      2     rect1=copy.copy(rect)
----> 3 a(box,box1)

NameError: name 'box1' is not defined
```

所以使用四个参数的方法有点问题，如果这个参数之前未被定义会报错，所以只能用三个参数，后面想在函数中复制对象，并将此赋值给一个全局对象，后面发现如果使用了return就不需要使用全局对象了

```python
import copy
def move_rectangle_copy(rect,dx,dy):
    #global rect1
    rect1=copy.deepcopy(rect)
    rect1.corner.x+=dx
    rect1.corner.y+=dy
    return rect1
move_rectangle(box,10,20)
print_point(rect1.corner)
```

结果倒是对了，不过貌似还可以用之前学过的问题识别方法将上面的代码简化，复制对象后面的可以用前面的函数替代：

```python
import copy
def move_rectangle_copy(rect,dx,dy):
    rect1=copy.deepcopy(rect)
    move_rectangle(rect1,dx,dy)
    return rect1
move_rectangle(box,10,20)
print_point(rect1.corner)
```

这样代码会稍微精简一些。