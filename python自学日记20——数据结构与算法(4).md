# python自学日记20——数据结构与算法(4)

## 1.用python实现栈

栈是一种后进先出的线性有序集合，每当python需要实现像栈这样的抽象数据结构时，就可以创建类。我看到后进先出就想到了沃尔玛这种大型仓库的进库出库顺序有的是后进先出。还有一摞书放和拿都是从顶部。

可以用列表来实现栈，最符合的情况是把列表的尾部当做栈的顶部处理，这样添加、删除元素都是比较简单的，代码如下：

```python
class Stack():
    def __init__(self):
        self.items=[]
    def isEmpty(self): #检查栈是否为空
        return self.items==[]
    def push(self,item): #添加元素到栈顶端
        self.items.append(item)
    def pop(self): #从顶端删除元素
        return self.items.pop()
    def peek(self): #返回顶端元素不修改栈
        return self.items[len(self.items)-1]
    def size(self):#返回栈的长度
        return len(self.items)
```

这个相对简单，后面有想着做一个把列表头部当做栈顶部处理的情况：

```python
class Stack1():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def pop(self):
        return self.items.pop(0)
    def push(self,item):
        self.items[0].insert(item)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
```

有点不确定的是插入到列表下标为0元素的方法，就按照自己理解写成上面这样了，果然测试了一下报错了

```python
a=Stack1()
a.push(1)
len(a)
```

```
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-12-3efcebe6c123> in <module>
      1 a=Stack1()
----> 2 a.push(1)
      3 len(a)

<ipython-input-10-ac44917fde2a> in push(self, item)
      8         return self.items.pop(0)
      9     def push(self,item):
---> 10         self.items[0].insert(item)
     11     def peek(self):
     12         return self.items[0]

IndexError: list index out of range
```

后面查了下insert插入的方法，`list.insert(index,obj)`，该方法没有返回值。

```python
class Stack1():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def pop(self):
        return self.items.pop(0)
    def push(self,item):
        self.items.insert(0,item)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
```

改完后测试了下结果就正常了。这给我的提醒就是有些时候你以为你看会了只是你看懂或听懂的错觉，要检查自己是不是真的会了，还是需要自己动手尝试一遍（不要照抄），需要自己思考着做。

**改变抽象数据类型的实现却保留其逻辑特征，这种能力体现了抽象思想。**

上述两种方法都能实现栈，但根据“python自学日记19——数据结构与算法(3)”中提到的列表中append和pop()的时间复杂度都是O(1)，这意味着不论栈有多少个元素，第一种实现push和pop操作都会在恒定时间完成。第二种测受制于栈中元素个数。因为insert(0)和pop(0)时间复杂度都是O(n)。所以应该选择第一种。

## 2.匹配括号

编程中如果遇到多个括号嵌套情况容易出现最后括号不匹配的情况，要么括号右边部分多一个要么少一个。我们用栈可以检测括号的匹配情况

括号匹配：((()))()

括号不匹配：(())) 右括号多一个

思路是从左侧开始一个个遍历，如果是左括号就放入栈中，如果是右括号就到栈里去匹配顶部的括号是不是左括号，如果是就删除顶部左括号，进入下一个循环。如果不是就返回False。

```python
from pythonds.basic import Stack #pythonds需要自己安装
def parChecker(symbolString):
    s=Stack()
    balanced=True #先设定balance为True,作为后面循环判断条件
    index=0
    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol=="(": #如果是‘(’就添加到栈中
            s.push(symbol)
        else:
            if s.isEmpty(): #不是情况先检查栈是不是为空，如果是修改balance为False，接下来就无法循环了，其实可以不用balance，不过前期是个能比较易读的方式
                balanced=False
            else:
                s.pop()
        index+=1
    if balanced and s.isEmpty():
        return True
    else:
        return False
```

我修改不用balanced的情况：

```python
from pythonds.basic import Stack
def parChecker1(symbolString):
    s=Stack()
    index=0
    while index<len(symbolString):
        symbol=symbolString[index]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.isEmpty(): #如果出现')'但是栈为空可以直接报错
                return False
            else:
                s.pop()
        index+=1
    return True  #循环如果能结束肯定是匹配好了可以直接返回True
```

测试是注意特殊情况，比如空字符串。

延伸情况：匹配普通符号，如方括号和花括号等多个括号嵌套的情况

匹配情况：{[()]}

不匹配请：{[(()] 少一个右侧花括号

这个我最初的思路是建三个栈分别进行匹配，在循环中进行判断，这样能解决但是代码感觉比较复杂，冗余，如果扩展代码会显得更多。后面发现有比较好的且扩展性好的方法

```python
from pythonds.basic import Stack
def parChecker(symbolString):
    s=Stack()
    balanced=True
    index=0
    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol in '([{': #先检测是否在字符串范围内
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top=s.pop()
                if not match(top,symbol): #匹配栈顶部的括号和遍历中的括号是否匹配
                    balanced=False
        index+=1
    if balanced and s.isEmpty():
        return True
    else:
        return False
def match(open,close):
    opens="([{"
    closer=")]}"
    return opens.index(open)==closer.index(close) #这里用到index方法，学过忘了还是不够熟悉
```

`str.index(str,beg=0,end=len(string))`检测字符串中是否包含被检测字符串，还可以指定检测开始结束范围，如果包含返回开始的索引值，否则抛出异常。这端代码通过match函数匹配的好处是易扩展，不管后面添加单引号匹配、双引号匹配或其他的，都不需要再增加代码行数了。

学过一遍的知识还是需要多练习，否则忘了和没学过差不多。另外要整理不同的知识点的使用频率，使用频率高的优先练习。

## 3.将十进制转换为二进制数

利用一种叫做“除以2”算法，除以2算法假设待处理整数大于0，将十进制数循环不停的除以2，取的余数按照顺序依次为二进制数从小到大的位数（即从右到左）。然后利用栈存储这些最后用空字符把这些数字依次连接起来。

```python
from pythonds.basic import Stack
def divideBy2(decNumber):
    s=Stack()
    while decNumber//2!=0:
        a=decNumber%2
        s.push(a)
        decNumber=decNumber//2
    s.push(1)
    b=''
    for i in len(s):
        b=b+s.pop()
    return b
divideBy2(12)
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-37-80b644294f33> in <module>
     12         b=b+s.pop()
     13     return b
---> 14 divideBy2(12)

<ipython-input-37-80b644294f33> in divideBy2(decNumber)
      9     s.push(1)
     10     b=''
---> 11     for i in len(s):
     12         b=b+s.pop()
     13     return b

TypeError: object of type 'Stack' has no len()
```

结果报错，类对象不能用len，那就用条件循环判断，判断栈不为空时取顶部值添加到字符串右侧。

```python
from pythonds.basic import Stack
def divideBy2(decNumber):
    s=Stack()
    while decNumber//2!=0: #显然这个条件不具有通用性，只适合二进制
        a=decNumber%2
        s.push(a)
        decNumber=decNumber//2
    s.push(1) #最后用s.push(1)是因为最后一位肯定是1//2结果是0，没有添加到栈里
    b=''
    while not s.isEmpty(): #不应该用if而是用while
        b=b+str(s.pop())
    return b
divideBy2(11)
```

刚开始用的是if，看到结果发现不对，后面又改成了while。

下面将十进制数改成任意进制的数，通过将上面代码修改一下使其具有通用性，这样需要在函数中传入两个参数，不过发现了一个问题就是上面函数除了二进制之外其他进制根本无法使用，主要是由于第一个while循环的条件所致，刚开始没注意直接写的如下：

```python
from pythonds.basic import Stack
def divideBy(decNumber,dec):
    s=Stack()
    while decNumber//dec!=0: 
        a=decNumber%dec
        s.push(a)
        decNumber=decNumber//dec
    s.push(1)
    b=''
    while not s.isEmpty():
        b=b+str(s.pop())
    return b
divideBy(138,8)
```

138对应的八进制数是212，按照这段代码输出的是112，因为s.push(1)把最左边的给限定死了，这个在二进制里符合是由于二进制只有0和1，但八进制除了0和1之外还有2-7，这些是无法满足的，所以需要修改一下条件：

```python
from pythonds.basic import Stack
def divideBy(decNumber,dec):
    s=Stack()
    while decNumber>0: #将条件改为大于0，这样就无需在最后手动添加到栈了
        a=decNumber%dec
        s.push(a)
        decNumber=decNumber//dec
    b=''
    while not s.isEmpty(): 
        b=b+str(s.pop())
    return b
divideBy(138,8)
```

本来以为这样就算结束了，但是想到十六进制的数字（主要是这个不常用到），忽略了这一点，尝试用这段代码改十进制为十六进制，发现divideBy(138,16)输出结果是“810”，这比原来值看着还大，所以这个还需要改动一下，将十六进制的“ABCDEF”添加进来：

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

这个给我的提示是写代码时注意扩展性或者说通用性，但具体也要看情况，有时候为了扩展性需要舍弃一些东西，比如速度、性能或者增加空间占比，但是看二者孰轻孰重了。

