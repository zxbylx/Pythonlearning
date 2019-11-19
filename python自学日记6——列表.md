# python自学日记6——列表

学习python时记录自己或观察别人从错误到正确的思路远比只看正确答案效果好——傅查理

## 1.编写一个函数，接收一个数字列表，并返回其累积和，例如[1,2,3]的累积和为[1,3,6]

看到求和想到前面用到的内置函数sum(t)，但是sum只说了是求列表内所有值的和，不知道能不能求部分和，所以需要做一下测试

```python
t=[1,2,3]
sum(t[:2])
```

返回值是3，表示可以用sum，然后得出如下代码：

```python
def cumulative_sum(t):
    res=[]
    for i in range(len(t)-1): #刚开始想着后面有i+1,以前这里都是需要减一的，但是忽略了":(i+1)"是不包括右侧的i+1的，所以不用减一
        res.append(sum(t[:(i+1)]))
    return res
t=[1,2,3]
cumulative_sum(t)
```

返回值是[1,3],所以把减一去掉就可以了

```python
def cumulative_sum(t):
    res=[]
    for i in range(len(t)):
        res.append(sum(t[:(i+1)]))
    return res
t=[1,2,3]
cumulative_sum(t)
```

这里有两点需要注意下，res后用append，我刚开始写成了res[i]=sum(t[:(i+1)])，这把字典和列表方法弄混，另外就是忘记了t[:(i+1)]中的“：”，也造成报错，需要注意下这些细节地方，这些bug是可以直接显示出来的，但是刚才那个减一是显示正常但是不符合预期结果，因为我们知道预期结果，所以才能检查出问题，如果不知道那就难了，写代码时还是需要提前想清楚。



**列表删除元素有三种方法，需注意三者区别和是否有返回值：**

1. t.pop()，pop修改列表，并返回被删除掉的值,默认删除最后一个
2. del t[i]，删除后不返回值，可以使用切片删除多个值
3. 如果你知道要删除的元素而不知道下标，可以使用remove，返回值是None



**对象和值：**

```python
a='banana'
b='banana'
a is b
```

输出是True

```python
c=[1,2,3]
d=[1,2,3]
c is d
```

 输出是False

前面a和b我们会说他们是相同的，在这个例子里python只建立了一个自发货车对象，而a和b都引用了它。

而后面两个我们可以说c和d是相等的，因为他们有相同的元素，但他们不是相同的。因为他们并不是同一个对象。**如果两个对象相同，则不然相等，如果相等，但不一定相同。注意区分相同和相等。**



**区分修改列表的操作和新建列表的操作十分重要**。例如append是修改列表，“+”则是新建列表。

```python
t1=[1,2]
t2=t1.append(3)
print(t1)
print(t2)
```

```
[1, 2, 3]
None #t2返回None说明t1.append(3)没有返回值
```

```python
t3=t1+[4]
print(t3)
```

```
[1, 2, 3, 4]
```

切片操作会新建一个列表

```python
def tail(t):
    return t[1:]
letters=['a','b','c']
rest=tail(letters)
print(rest)
```

```
['b', 'c']
```

## 2.编写一个函数is_anagram,接收两个字符串，当他们互为回文时返回True

给的提示是两个单词，如果重新排列其中一个的字母可以得到另一个则互为回文，这个提示我是看懂了，但是感觉不太对，上网查了下也只查了些诗中有互为回文的，但是那个写的是前面说的互为倒序的，那么就奇怪了，互为回文和互为倒序有什么区别，暂时先按照提示来写吧

```python
def is_anagram(word1,word2):
    if word1.sorted()==word2:
        return True
    return False
is_anagram('ab','ba')
```

```
AttributeError                            Traceback (most recent call last)
<ipython-input-72-85d6d5401dcc> in <module>
      4         return True
      5     return False
----> 6 is_anagram('ab','ba')

<ipython-input-72-85d6d5401dcc> in is_anagram(word1, word2)
      1 #练习：编写一个函数is_anagram,接收两个字符串，当它们互为回文时返回True
      2 def is_anagram(word1,word2):
----> 3     if word1.sorted()==word2:
      4         return True
      5     return False

AttributeError: 'str' object has no attribute 'sorted'
```

报错提示字符串不能使用sorted,可能是记错了，那用下sort试一下

```python
def is_anagram(word1,word2):
    if word1.sort()==word2:
        return True
    return False
is_anagram('ab','ba')
```

结果还是报同样的错误，然后才想起字符串是不能更改的，如果想排序看样子得先把字符串变成列表才行

```python
def is_anagram(word1,word2):
    if "".join(list(word1).sort())==word2 or "".join(list(word2).sort())==word1:
        return True
    return False
is_anagram('hello','ab')
```

我的想法是先把字符串变成列表，然后排序，后面在用“”.join把分开的字母重新拼在一起，结果报错如下：

```
<ipython-input-74-716276a7e28b> in is_anagram(word1, word2)
      1 def is_anagram(word1,word2):
----> 2     if "".join(list(word1).sort())==word2 or "".join(list(word2).sort())==word1:
      3         return True
      4     return False
      5 is_anagram('hello','ab')

TypeError: can only join an iterable
```

有个怀疑是sort()没返回值，然后尝试了下确实没有，那用sorted(t)试了下有返回值，然后把代码改成下面这样：

```python
def is_anagram(word1,word2):
    if "".join(sorted(list(word1)))==word2 or "".join(sorted(list(word2)))==word1:
        return True
    return False
is_anagram('hello','ello')
```

这次就正常了，还是如前面讲的，注意有没有返回值很重要。

## 3.生日悖论

编写一个函数has_duplicates接收一个列表，当其中任何一个元素出现多于一次时，返回True.它不应当修改原始列表

首先想到的就是对列表中每个元素数一下个数，当任何一个超过1时返回True

```python
def has_duplicates(t):
    for s in t:
        if t.count(s)>1:
            return True 
    return False
t=[1,3,2]
has_duplicates(t)
```

当然如果是自己之前不知道count（我也是上网查了用法），可以用笨办法，首先排序，然后挨个判断相邻元素是否相同

```python
def has_duplicates1(t):
    new_t=t[:] #生成新的列表
    new_t.sort() #因为这个会修改列表，不会生成新的列表
    for i in range(len(new_t)-1):
        if new_t[i]==new_t[i+1]:
            return True
    return False
t=[1,3,3]
has_duplicates1(t)
```

如果你们班有23个学生，那么其中有两人生日相同的几率有多大？可以使用random模块中的randint生成随机整数

去查了下官方文档，知道了randint的用法，一次只能生成一个随机数，那么想生成23个就需要用到循环，下面还需要计算概率需要调用，所以生成一个函数

```python
def random_birt(students):
    t=[]
    for i in range(students):
        t.append(random.randint(1,366))
    return t
# random_birt(23)
        
def count_match(students,numbers):
    t=random_birt(students) #应该放到循环里，否则只生成一个随机列表，结果都是一样的
    count=0
    for i in range(numbers):
        if has_duplicates(t):
            count+=1
    return count
count_match(23,1000)
```

返回值时1000，一想就不对，发现随机列表没有放到循环里，放到循环里后如下

```python
def random_birt(students):
    t=[]
    for i in range(students):
        t.append(random.randint(1,366)) #一年按365天算，所以生成随机数范围是1到365
    return t
# random_birt(23)
        
def count_match(students,numbers):
    
    count=0
    for i in range(numbers):
        t=random_birt(students)
        if has_duplicates(t):
            count+=1
    return count
count_match(23,1000)
```

返回值494，说明1000次中有494次出现两个人生日相同。概率接近50%

## 4.编写一个函数bisect,接收一个排好序的列表，以及一个目标值，当目标值在列表之中，返回其下标，否则None

想直接用find方法，试了下发现list是不能用find的，然后通过循环一个个比对了

```python
def bisect(t,target):
    for i in range(len(t)):
        if t[i]==target:
            return i
    return None
t=[1,2,3,4,5,6]
bisect(t,5)
```

上述方法是将列表中所有的元素拿出来与目标一一比对，但是这有个问题就是如果列表很长就会造成速度比较慢，因此我们可以用二分查找（需要列表是有序的），bisect模块（可见官方文档）用于二分查找：

```python
import bisect
def find_lt(a,x):
    i=bisect.bisect_left(a,x) #bisect.bisect_left(a, x, lo=0, hi=len(a))，在a中找到x合适的插入点，使得x左侧都小于x,右侧大于等于x	
    if i != len(a) and a[i]==x:
        return i
    return None
t=read_words()
find_lt(t,'hello')
```

二分查找大大降低了查找速度，如果单词列表有113809个，按照第一种方法就要查找相应次数，按照第二种大概17步就可以找到。

## 5.读取文件words.txt生成一个列表

```python
import time
def read_words():
    fin=open('words.txt')
    t=[]
    for line in fin:
        word=line.strip()
        t.append(word)
    return t
start_time=time.time()
t=read_words()
elapsed_time=time.time()-start_time
print(len(t))
print(t[:10])
print(elapsed_time)
```

## 6.编写一个程序找到单词表中互为倒序的单词对

互为倒序的意思是“ad"和”da“这样就是，所以刚开始想着从头开始循环，检查每个单词的倒序单词是否在单词表中即可，然后代码如下：

```python
def remove_dumplicates(t): #为了去重，不过在验证主程序是否可行前还没调用函数
    new_t=[]
    for i in range(len(t)):
        if t[i] not in new_t:
            new_t.append(t[i])
    return new_t
# t=[1,[1,2],[2,1]]
# remove_dumplicates(t)
def daoxu():
    a=[]
    t=read_words()
    for s in t:
        if s[::-1] in t:
            a.append(sorted([s,s[::-1]]))
    return a
daoxu()
```

一直用挨个查找的方法用习惯了，上来随手就写成这样，运行的时候发现忽略了运行时间了。十万个单词，每个单词反向然后再查找一遍，具体时间就算不过来了，挺长的，所以需要用到二分查找，改成如下

```python
import bisect
def remove_dumplicates(t): #去重列表中重复的元素
    new_t=[]
    for i in range(len(t)):
        if t[i] not in new_t:
            new_t.append(t[i])
    return new_t

def find_lt(a,x): #二分查找
    i=bisect.bisect_left(a,x)
    if i != len(a) and a[i]==x:
        return True
    return None
def daoxu():
    a=[]
    t=read_words() #用到上面生成字母表的列表
    for s in t:
        if find_lt(t,s[::-1])==True and s!=s[::-1]:
            a.append(sorted([s,s[::-1]]))
    return remove_dumplicates(a)
daoxu()
```

得出的反向对需要两两不能相同，所以s!=s[::-1],然后再去重，最后就得出所要的结果了。

## 7.编写一个程序找到单词表中所有互锁的单词

互锁：两个单词，从每个单词中交错去除一个字母可以组成一个新的单词，我们称之为互锁，例如shoe和code可以互锁为schooled

我的思路是将单词表中的每个单词根据下标的奇偶分别拆分成两个单词，然后查找这两个单词是否都在单词表中，如果在就是互锁，不在就不是，但是在将一个单词拆分时遇到了问题：

```python
for i in range(len('hello')):
    s1=[]
    s2=[]
    if i%2!=0:
        s1.append(['hello'[i]])
    elif i%2==0:
        s2.append('hello'[i])
print(s1,s2)
```

返回不符合预期，后面发现是s1和s2放到循环中了，应该放在外面。

```python
s1=[]
s2=[]
for i in range(len('hello')):
    
    if i%2!=0:
        s1.append('hello'[i])
    elif i%2==0:
        s2.append('hello'[i])
print(s1,s2)
```

这样就分成了两个列表了，然后通过join将列表拼接成单词

```python
def husuo():
#     a=[]
    t=read_words() #获取单词表
    for s in t:
        s1=[]
        s2=[]
        for i in range(len(s)):
            
            if i%2!=0: #奇数下标
                s1.append(s[i]) #将所有奇数下标组成一个列表
            elif i%2==0: #偶数下标
                s2.append(s[i]) #将所有偶数下标组成一个列表
        word1=''.join(s1)  #将列表拼接成字符串
        word2=''.join(s2)
        if find_lt(t,word1) and find_lt(t,word2): #查找两个单词同时在单词表中的情况
            print(word1+'   '+word2 +'     '+s)
#     return a
husuo()
```

这个问题我想的是两两组成词再查找运算量太大，而且麻烦，反向思考将单词拆分，然后查找就好一些。另外就是大问题要学会拆解成小问题，如前面两步就是看能不能自己把一个单词拆分成奇偶列表。

三互锁单词按照上面的逻辑稍微改一下就行了：

```python
def husuo():
#     a=[]
    t=read_words()
    for s in t:
        s1=[]
        s2=[]
        s3=[]
        for i in range(len(s)):
            
            if i%3==0:
                s1.append(s[i])
            elif i%3==1:
                s2.append(s[i])
            else:
                s3.append(s[i])
        word1=''.join(s1)
        word2=''.join(s2)
        word3=''.join(s3)
        if find_lt(t,word1) and find_lt(t,word2) and find_lt(t,word3):
            print(word1+'   '+word2 +'     '+word3+'      '+s)
#     return a
husuo()
```

下面是答案代码：

```python
from inlist import *


def interlock(word_list, word):
    """Checks whether a word can be split into two interlocked words.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
        

def interlock_general(word_list, word, n=3):
    """Checks whether a word can be split into n interlocked words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])


#    for word in word_list:
#        if interlock_general(word_list, word, 3):
#            print (word, word[0::3], word[1::3], word[2::3])
```

我发现在将一个一个单词拆分这块自己做得复杂了，用切片更简单一些，下次得注意下。