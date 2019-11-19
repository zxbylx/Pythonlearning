# python自学日记23——数据结构与算法(7)

## 1.用递归方法将整数转换成2-16位进制的字符串

将十进制转换成其他进制这个问题在“python自学日记20——数据结构与算法(4)”中已经用栈解决过了，当时遇到了一些问题，循环处理、通用化等，最后写出的代码如下：

```python
from pythonds.basic import Stack
def divideBy(decNumber,dec):
    digits='0123456789ABCDEF' #先把十六进制的所有字符放到一个字符串中
    s=Stack()
    while decNumber>0:
        a=decNumber%dec
        s.push(a)
        decNumber=decNumber//dec
    b=''
    while not s.isEmpty(): 
        b=b+digits[s.pop()] #用余数作为字符串的下标找到对应的字符
    return b
divideBy(138,16)
```

是先将整数除以进制数得到的余数一个个压入栈中，后面在一个个取出来的过程。这个问题用递归解决代码会更精简一些

```python
def toStr(n,base):
    convertString='0123456789ABCDEF'
    if n<base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base]
toStr(10,2)
```

递归就是将问题不断地分成更小的子问题，直到子问题可以用普通的方法解决。说通俗一点就是一个会调用自己的函数。用现实中的例子来讲就比如我们肯定听过“从前有座山，山上有座庙，庙里有个老和尚在给小和尚讲故事，讲的是什么呢？从前有座山，山上有座庙，庙里有个老和尚在给小和尚讲故事，讲的是什么呢？从前有座山......”如果顺着这个讲可以一直讲下去，但是递归是用来解决问题的，无限递归肯定不是我们所希望的，所以就引出递归三原则：

1. 算法必须有基本情况，也就是有一个退出递归的条件；
2. 递归算法必须改变其状态并向基本情况靠近；改变状态通常意味着代表问题的数据以某种方式变得更小；
3. 递归算法必须递归地调用自己。

## 2.递归可视化：绘制分形树

python中提供了turtle模块，可以通过前后左右移动加上转弯等操作绘制图案。分形树就是用这个模块来画。

分形树代码看着很简单，但是是递归里花费我很久还没有完全弄懂的一个问题。先上代码

```python
def tree(branchLen,t):
    if branchLen>5:
        t.forward(branchLen)#先向前移动，画树干
        t.right(20)
        tree(branchLen-15,t)#再画右分支，递归调用自己
        t.left(40)
        tree(branchLen-15,t)#然后画左分支，递归调用自己
        t.right(20)
        t.backward(branchLen) #最后倒回到节点处
from turtle import *
t=Turtle()
myWin=t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(110,t)
myWin.exitonclick()
```

这段代码主要就是上面的这个函数，难点在于递归会导致多层嵌套，然后顺序容易乱，然后想看看具体每一步是怎么执行的，我就在每一步操作上都添加了print语句，如下：

```python
def tree(branchLen,t):
    if branchLen>5:
        t.forward(branchLen)
        print('向前%d'%branchLen)
        t.right(20)
        print('右转20度')
        tree(branchLen-15,t)
        print('向前%d'%(branchLen-15))
        t.left(40)
        print('左转40度')
        tree(branchLen-15,t)
        print('向前%d'%(branchLen-15))
        t.right(20)
        print('右转20度')
        
        t.backward(branchLen) #究竟是怎么转向左边的还没有看懂
        print('倒退%d'%branchLen)
from turtle import *
t=Turtle()
myWin=t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(75,t)
myWin.exitonclick()
```

这样确实把每一步打印出来了，但是还是挺难看懂的。然后上网查了下递归画分形树，多数人都是把代码写出来了，但是并没有讲为什么是这样。这个问题我觉得挺典型的，因为一个函数里涉及多个递归情况。向左和向右、后退等，这个需要区分层的关系、以及顺序的关系。

比如这个函数在符合条件下会先把向右拐和右拐下面的前进给执行完，后面再执行向左拐和后退等问题。但是当向左拐、后退时，由于进入了上一层，这时的参数大小回到上一层的参数大小。层级会影响参数大小这个问题是理解递归的一个关键。

**递归限定了函数所用变量的作用域。尽管反复调用相同的函数，但每次调用都会为函数的局部变量创建新的作用域。**