# python自学日记22——数据结构与算法(6)

## 1.用队列解决在超市等待结账问题（自编）

假设一家超市只有一个收银台，收银台每分钟可结算20件商品，每天高峰期1小时结算人流量可达200人，每人购买商品数量在1-30件不等，客户平均等待时间

每小时结算人流达200人，即每18秒创建一个待结算任务，每秒生成待结算人物的概率是1/18.设定一个随机数，如果数字等于18，则创建一个待结算任务

```python
import random
def new_task():
    num=random.randrange(1,19)
    if num==18:
        return True
    else:
        return False
```

然后需要创建一个收银台的类和任务队列

```python
import random
from pythonds.basic import Queue
class CheckStand:
    def __init__(self,cpm):
        self.cpm=cpm
        self.currentTask=None
        self.timeRemaining=0
    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False
    def tick(self):
        if self.currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
#                 self.currentTask==None #问题所在，用了两个等号，该用一个的
                self.currentTask=None
    def startNext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getChecks()*60/self.cpm #忘记使用getChecks了
        

class Task:
    def __init__(self,time):
        self.timestamp=time
        self.checks=random.randrange(1,31)
    def getStamp(self):
        return self.timestamp
    def getChecks(self):
        return self.checks
    def waitTime(self,currenttime):
        return currenttime-self.timestamp

#主程序
def check_simulation(numSeconds,checksPerMinute):
    checkstander=CheckStand(checksPerMinute)
    checkqueue=Queue()
    waitingtimes=[]
    
    for currentSecond in range(numSeconds):
        if new_task():
            task=Task(currentSecond)
#             print(task.getStamp())
            checkqueue.enqueue(task)
        if (not checkstander.busy()) and (not checkqueue.isEmpty()):
#             print('开始执行新任务')
            nexttask=checkqueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            checkstander.startNext(nexttask)
        checkstander.tick()
#     averageWait=sum(waitingtimes)/len(waitingtimes)
    averageWait=len(waitingtimes)
    print('平均等待 %6.2f secs %3d 任务还在等待中'%(averageWait,checkqueue.size()))
for i in range(10):
    check_simulation(3600,20)
```

```
平均等待  73.00 secs 139 任务还在等待中
平均等待  76.00 secs  91 任务还在等待中
平均等待  79.00 secs 103 任务还在等待中
平均等待  80.00 secs 144 任务还在等待中
平均等待  77.00 secs 119 任务还在等待中
平均等待  77.00 secs 143 任务还在等待中
平均等待  86.00 secs 114 任务还在等待中
平均等待  85.00 secs 121 任务还在等待中
平均等待  81.00 secs 114 任务还在等待中
平均等待  70.00 secs 139 任务还在等待中
```

其实这个问题跟昨天写的“python自学日记21——数据结构与算法(5)”是类似问题，代码基本上就是一样的，但是重新写一遍还是会出一些问题，发现问题并解决问题才是自己重新编了一个题目并重新写一遍的目的。如果没有这一遍会给自己一种会了的错觉，写完之后发现其实对这类问题的解决还不够熟悉。

新问题的出现让自己对这个问题认识会更加深一些，出现的问题标在代码中了，第一个会导致从始至终只有一个任务在执行。最后结果就是平均等待时间是0秒，但是还剩好多任务在等待中。第二个就报错明显了，没有获得商品数无法和整数相乘。

这只是初步问题，后面可以延伸下需要一分钟处理多少商品，或者应该同时放置多少个收银台等问题。

