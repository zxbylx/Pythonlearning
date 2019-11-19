# python自学日记21——数据结构与算法(5)

## 1.队列：模拟打印任务

**代码一变长就容易出现写错的地方，最好还是进行增量开发，写一段测一下，在关键节点写print语句，省的全写完报错再找起来也麻烦。**

由于模拟情况内容较多，本着抽象思维只提取对问题有用的信息，简要的说一下避免后面读不懂问题

实验室每小时有10个学生，一个小时内每个人都打印2次，即每小时有20个打印任务，每个打印任务打印页数在1到20页不等

打印机一台，可设置每分钟高质量打印5页或者低质量打印10页

应该如何设置打印机速度？计算平均等待时长和1小时候剩余任务数量。

需要先计算出每一秒创建打印任务的概率：3600秒内创建20个打印任务，相当于180秒创建一个，那么每一秒创建打印任务的概率是1/180.我们可以针对这个设置一个1-180的随机数，随机到某个值时创建一个打印任务。

```python
import random
def newPrintTask():
    num=random.randrange(1,181) #randrange(start,end)创建二者范围内的随机整数
    if num==180:
        return True
    else:
        return False
```

根据情况需要为打印机和打印任务创建类，还需要创建一个等待打印任务的队列。

按照时间顺序模拟程序运行，将一小时分成3600秒，逐秒遍历

1. 在每一秒需要判断是否有新任务创建，如果有放到待打印队列中并且生成一个时间戳；判断打印机是否空闲，如果空闲且队列不空从队列中取出一个任务到打印机执行，同时生成一个时间，减去添加进待打印队列的时间就是等待时间；
2. 添加进打印机执行时需要统计执行时间倒计时，根据执行速度和页数可以求出一共需要多少秒，从一开始就倒计时，倒计时为0时，打印机变为空闲，然后走上一步判断队列是否为空，是否要添加新的打印任务。
3. 当模拟完成时，统计每个任务的平均等待时间，以及看队列中还剩几个待打印任务。

```python
class Printer:  #创建打印机的类
    def __init__(self,ppm):
        self.pagerate=ppm #打印速度
        self.currentTask=None #当前任务数量
        self.timeRemaining=0 #执行任务倒计时
    def tick(self): #任务执行伴随着时间倒计时不断变小
        if self.currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
#             if self.timeRemaining<=0:
            self.currentTask=None
    def busy(self): #判断打印机是否空闲
        if self.currentTask!=None:
            return True
        else:
            return False
    def startNext(self,newtask): #开始执行新任务并计算任务总用时
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages()*60/self.pagerate
```

这里由于疏忽在tick方法中没有对倒计时是否小于等于0进行判断就直接将当前任务变成None了，导致的结果就是输出结果显示等待打印时间为0，剩余任务也是0，测试好好多地方，最后才找到问题所在，将判断条件添加上就显示正常了

创建task对象

```python
import random
class Task:
    def __init__(self,time):
        self.timestamp=time #创建任务时的时间戳
        self.pages=random.randrange(1,21)#任务页数从1到20页随机产生
        
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self,currenttime):  #等待时间是进入打印机时间-创建任务时的时间
        return currenttime - self.timestamp
```

主程序

```python
from pythonds.basic import Queue

def simulation(numSeconds,pagesPerMinute):#第一个参数是模拟总时长，第二个参数是打印机速度
    labprinter=Printer(pagesPerMinute) #创建打印机对象
    printQueue=Queue()
    waitingtimes=[] #创建一个等待时间列表，为最后计算平均等待时间用
    
    for currentSecond in range(numSeconds):#从开始遍历模拟时间内的每一秒
        if newPrintTask():
            task=Task(currentSecond) #有新任务创建时间戳
            printQueue.enqueue(task) 
#             print(task.timestamp)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask=printQueue.dequeue()
#             print(nexttask.waitTime(currentSecond))
            waitingtimes.append(nexttask.waitTime(currentSecond))
#             print(waitingtimes)
            labprinter.startNext(nexttask)
        labprinter.tick()
    averageWait=sum(waitingtimes)/len(waitingtimes)
    print('Average wait %6.2f secs %3d tasks remaining.'%(averageWait,printQueue.size()))
for i in range(10):
    simulation(3600,10)
```

模拟10次，在1小时内，设置打印机速度为每分钟打印10页，结果显示

```
Average wait   5.50 secs   0 tasks remaining.
Average wait  21.05 secs   0 tasks remaining.
Average wait  12.67 secs   0 tasks remaining.
Average wait  11.28 secs   0 tasks remaining.
Average wait  10.69 secs   0 tasks remaining.
Average wait  27.78 secs   0 tasks remaining.
Average wait  16.19 secs   0 tasks remaining.
Average wait  13.55 secs   0 tasks remaining.
Average wait   0.15 secs   0 tasks remaining.
Average wait  20.21 secs   0 tasks remaining.
```

设置10页平均等待时长从0.15秒到27秒，且都打印完成了。

如果设置成每分钟5页：

```python
for i in range(10):
    simulation(3600,5)
```

结果如下：

```
Average wait 117.40 secs   2 tasks remaining.
Average wait  17.54 secs   0 tasks remaining.
Average wait  61.00 secs   0 tasks remaining.
Average wait  72.54 secs   0 tasks remaining.
Average wait 125.67 secs   4 tasks remaining.
Average wait 102.42 secs   4 tasks remaining.
Average wait 180.50 secs   6 tasks remaining.
Average wait  62.68 secs   1 tasks remaining.
Average wait 136.84 secs   0 tasks remaining.
Average wait  69.32 secs   0 tasks remaining.
```

平均等待时长从17秒到180秒，而且10次中有5次没有打印完。通过这个大致就可以看出应该怎么设置。

这个从自己的错误导致产生错误显示等待0秒，没有剩余任务，通过print语句找了好久都没找到，然后去对例子代码，看了两遍也没看出什么问题，觉得可能是代码本身有问题，看了视频发现人家也按照代码来但是也能显示正常，我就想着把代码一行行复制，然后一行行比对，最终发现问题所在。这给我的启示有两点，一是自己眼睛有时会出现这种情况以为自己看的很仔细了但是还是会漏掉或看错信息，另一个就是如果不是因为自己在没有完全理解这个问题之前就按照例子代码敲了一遍（没过脑子），也不至于出了问题找半天找不到原因所在，如果是自己写的代码出问题找到原因的思路会更清晰一点。以后不要在没看清问题就先敲代码。

## 2.结合从中序表达式转换到后序表达式以及计算后序表达式的算法，直接实现对中序表达式的计算

中序表达式就是我们常见的四则运算表达式：`1+2*3` 或者`2+3*(1+2)`

由于中序表达式对于我们人来说知道先乘除后加减遇到括号先算括号里的规则，但是对计算机来说很难算，因为计算机是从左到右遍历，所以为了方便计算机计算，需要将中序表达式转换为后序表达式

`1+2*3` 对应的后序表达式是：1 2 3 * +；当计算机从左开始遍历后序表达式时，遇到数字就放到一个栈里，遇到运算符就从栈里提出两个数字进行计算，然后把结果放回到栈里，如此循环最后得出计算结果

`2+3*(1+2)`对应的后序表达式是：2 3 1 2 + * +；转换规则我在代码里写一下

中序转后序：

```python
from pythonds.basic import Stack
def infixToPostfix1(infixexpr):
    prec={}
    prec['*']=3 #我们需要先定义四则运算的运算符先后运算级别，方便计算机识别
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    
    opStack=Stack() #新建一个栈存储运算符
    postfixList=[] #列表存储数字和运算符
    try:
        tokenList=infixexpr.split() #要求字符串每个字符都必须以空格隔开，方便遍历
        for token in tokenList:
            if token.isnumeric(): #.isnumeric判断token是不是数字，注意后面有()，不写没效果
                postfixList.append(token)
            elif token=='(':
                opStack.push(token) #把(添加到栈里
            elif token==')': #遇到)时，就将栈里的运算符添加到列表后面，直到遇到(为止
                topToken=opStack.pop()
                while topToken!='(':
                    postfixList.append(topToken)
                    topToken=opStack.pop()
            else:
                while (not opStack.isEmpty()) and (prec[opStack.peek()]>=prec[token]): #当遇到新运算符且栈里的运算符级别比当前高或相等时
                    postfixList.append(opStack.pop())#先把栈里的运算符取出来添加到列表中
                opStack.push(token) #然后把当前运算符添加到栈中
        while not opStack.isEmpty():#遍历完如果栈里还有运算符就逐个添加到列表末尾
            postfixList.append(opStack.pop())
        return ' '.join(postfixList) #最后再用空格把列表里的元素连接起来就是后序表达式
    except:
        return '表达式不符合要求'
```

刚开始我从判断大写字母改成判断数字时写的是`if token.isnumeric:`导致参数是什么样，返回的就还是什么样，没有任何变化，方法后面必须带括号这个需要记得，避免漏掉。

```python
infixToPostfix1('1 + 2 * 3')
```

```
输出是：'1 2 3 * +'
```

计算后序表达式；

```python
from pythonds.basic import Stack
def postfixEval(postfixExpr):
    operandStack=Stack() #新建一个栈存放数字
    try:
        tokenList=postfixExpr.split() #空格隔开方便遍历
        for token in tokenList:
            if token.isnumeric():
#             if token in '0123456789': 本来例子中是这样但是这个只能处理0-9的运算
                operandStack.push(int(token)) #遇到数字就转换成整数，或许浮点数会更好，不过目前不能判断浮点数后面找到好的方法可以试一下，否则计算机无法计算小数也是问题
            else:
                operand2=operandStack.pop()#遇到运算符从栈中提取两个数进行计算
                operand1=operandStack.pop()#注意二者顺序不能颠倒，否则减法和除法出错
                result=doMath(token,operand1,operand2)
                operandStack.push(result)
        return operandStack.pop()
    except:
        return '参数不符合要求'
def doMath(op,op1,op2):
    if op=='*':
        return op1*op2
    elif op=='/':
        return op1/op2
    elif op=='+':
        return op1+op2
    else:
        return op1-op2
```

下面根据上面两个算法写出直接计算中序表达式的代码，由于中序转后序，后序计算用了两次遍历，直接计算一次遍历就可以了，用到两个栈，一个存储数字，一个存储运算符，结合点就在于中序转后序代码里每当添加运算符到列表时那段代码改成提取数字栈中两个数与本来要添加到列表的运算符进行计算即可完成。

```python
from pythonds.basic import Stack
def jisuan(zhongxu):
    prec={}
    prec['*']=3
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    
    opStack=Stack()
    operandStack=Stack()
    tokenList=zhongxu.split()
    for token in tokenList:
        if token.isnumeric():
#         if token in '0123456789':
            operandStack.push(int(token))
        elif token=='(':
            opStack.push(token)
        elif token==')':
            topToken=opStack.pop()
            while topToken!='(':
                operand2=operandStack.pop()
                operand1=operandStack.pop()
#                 result=doMath(token,operand1,operand2)#遇到括号就报错原因是这一行误将topToken写成token了
                result=doMath(topToken,operand1,operand2)
                operandStack.push(result)
                topToken=opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()]>=prec[token]):
                operand2=operandStack.pop()
                operand1=operandStack.pop()
                result=doMath(opStack.pop(),operand1,operand2)
                operandStack.push(result)
            opStack.push(token)
            
    while not opStack.isEmpty():
        operand2=operandStack.pop()
        operand1=operandStack.pop()
        result=doMath(opStack.pop(),operand1,operand2)
        operandStack.push(result)
    return operandStack.pop()
def doMath(op,op1,op2):
    if op=='*':
        return op1*op2
    elif op=='/':
        return op1/op2
    elif op=='+':
        return op1+op2
    else:
        return op1-op2 
```

刚开始由于写错一行代码，出现的结果是表达式里没有括号时计算结果是正常的，有括号就返回0，然后从括号位置找到了原因。

处理这个的方法就是要找到两个算法重叠的部分，遍历两次可以精简，前面用列表存数字后面用栈存数字可以直接用一个栈处理即可。二者连接的部分就是前面是添加运算符到列表，后面是遇到运算符就从栈里取两个数字进行计算。结合这三点可以将这个问题写出来。

代码一变长就容易出现写错的地方，最好还是进行增量开发，写一段测一下，在关键节点写print语句，省的全写完报错再找起来也麻烦。