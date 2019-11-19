# python自学日记8——元组

遇到一个问题时抓取里面的关键信息并将这些关键信息转化为你已经掌握的函数方法才是解决未知问题之道。

## 1.编写一个函数sumall，接收任意个数的参数并返回它们的和

提示写了sum(1,2,3)会报错：sum expected at most 2 arguments,got 3

接受多个参数我知道需要用到元组，但是我不知道哪里，所以先写成这样：

```python
def sumall(t):
    return sum(*t)
t=(1,2,3,4)
sumall(t)
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-232d6a4d3dd5> in <module>
      3     return sum(*t)
      4 t=(1,2,3,4)
----> 5 sumall(t)

<ipython-input-16-232d6a4d3dd5> in sumall(t)
      1 #练习：编写一个函数sumall，接收任意个数的参数并返回它们的和
      2 def sumall(t):
----> 3     return sum(*t)
      4 t=(1,2,3,4)
      5 sumall(t)

TypeError: sum expected at most 2 arguments, got 4
```

报错和提示差不多，那先解决sum问题

```python
sum(1,2)
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-17-a91f35d5101e> in <module>
----> 1 sum(1,2)

TypeError: 'int' object is not iterable
```

遇到错误一般首先都是复制这个去搜索，但是有时候搜到的和想要的不一样时，可以去看下官方文档，有时候官方文档解释比较清楚，参数代表什么，举个例子什么的。但sum解释的不够清楚，尤其是iterable代表了什么不清楚，这时搜索python sum，很多网友会在网上将一些函数、方法自己解释一遍，方便其他人学习，我找到菜鸟教程里面解释的比较清楚，写到iterable是可迭代对象，如列表、元组、集合。这个我就清楚了，第二个参数是用来和iterable的和相加的，默认0，选填。

```python
def sumall(*args):
    return sum(args)
sumall(1,2,3)
```

*args可以传递多个参数，并且函数会收集所有参数到一个元组上，这样sum(args)实际上调用的就是元组。

## 2.对一个单词列表按照单词长度降序排序，单词长度相等的随机排序

提示：参考random模块的random函数

看到排序首先想到什么可以排序，列表。按照长度排序需要先求出每个单词的长度，需要用到循环遍历单词表。然后先按长度排序，长度相等的按随机排序，这个涉及了多级排序，我去官方文档查了多级排序，虽然是可以指定几个排序条件，但是都是通用一个排序标准，要么降序，要么升序。我本以为可以只用两个长度和单词，对长度用降序排序，对单词用随机排序，但是没有随机排序这一说。查看了random函数时生成随机数，这让我想到可以在长度和单词之间插入一个随机值，然后再统一降序排序，就可以实现单词随机排序了。

```python
def sort_by_length(words):
    t=[]
    for word in words:
        t.append((len(word),word))
    t.sort(reverse=True)
    
    res=[]
    for length,word in t:
        res.append(word)
    return res
words=('ab','bcd','ac')
sort_by_length(words)
```

这个是按长度排序的例子，所以我们要做的只是在长度和单词之间插入一个随机值即可，但是生成随机值的位置要注意，不能在循环外面，这样从头到尾只生成了一个随机值，必须在循环里，每次生成不一样的随机值才能达到效果

```python
import random
def sort_by_length(words):
    t=[]
    for word in words:
        rand=random.random() #在循环里生成随机值
        t.append((len(word),rand,word)) #随机值夹在长度和单词中间
    t.sort(reverse=True)
    
    res=[]
    for length,rand,word in t:
        res.append(word)
    return res
words=('ab','bcd','ac','bc','cd','ae','ba')
sort_by_length(words)
```

```
['bcd', 'ba', 'cd', 'ab', 'bc', 'ac', 'ae']
```

这个问题给我的启示是，有些效果在代码中实现起来可能没有直接的方法按照描述的方式实现，当然我们首先是想着找到最直接的方法，就比如如果能对两个维度进行不一样的排序方式且有随机排序这一说，我们自然应该用最直接的方法，但是如果没有，我们就应该要学会使用变通的方法，抓住关键词，就比如这个里面的随机，然后去看官方文档或网上搜索与随机有关的函数、方法等，看看有没有别的方法解决这个问题。

现实情况在并不会有提示这一说，学会抓住关键信息是我们应该掌握的能力。

## 3.编写一个函数most_frequent,接收一个字符串并按照频率的降序打印字母

首先找其中的关键词，字符串、频率、降序。给字符串中每个字母进行频率技术在“python自学日记7——字典”中已经讲过了，排序在刚才也掌握了，那么这个题只需要将这两个结合一下就出来了。

```python
d=dict() #因为下面函数要用，所以把它单独放出来作为全局变量
def histogram(s):#使用字典作为计数器集合
    
    for c in s:
        d[c]=int(d.get(c,'0'))+1
    return d

def most_frequent(a):
    histogram(a)
    c=[]
    for key,val in d.items():
        c.append((val,key)) #将键和值颠倒放入列表中方便下面按照值的大小排序
        c.sort(reverse=True)
    res=[]
    for val,key in c:
        res.append(key)
    print(res)
most_frequent('adffdadfafasdfafdafadf')
```

```
['f', 'a', 'd', 's']
```

返回值符合预期，证明这个方法是对的。

读入单词表，并将单词表中字母按照出现频率降序排列，这个刚开始觉得挺简单的，然后代码如下：

```python
d=dict()
def histogram(s):
    
    for c in s:
        d[c]=int(d.get(c,'0'))+1
    return d

def most_frequent(a):
    histogram(a)
    c=[]
    for key,val in d.items():
        c.append((val,key))
    c.sort(reverse=True)
    res=[]
    for val,key in c:
        res.append(key)
    print(res)
# most_frequent('adffdadfafasdfafdafadf')
fin=open('words.txt').read()    
t=most_frequent(fin)
for x in t:
    print(x)
```

```
['\n', 'e', 's', 'i', 'a', 'r', 'n', 't', 'o', 'l', 'd', 'c', 'u', 'g', 'p', 'm', 'h', 'b', 'y', 'f', 'k', 'v', 'w', 'z', 'x', 'j', 'q']
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-48-23f2f0423937> in <module>
     22 # a=print(t)
     23 # type(a)
---> 24 for x in a:
     25     print(x)
     26 # def read_file(filename):

TypeError: 'NoneType' object is not iterable
```

发现错误以后，刚开始以为是列表最前面的'\n'导致的错误，就想用切片把第一个'\n'给去掉：

```python
fin=open('words.txt').read()    
t=most_frequent(fin)[1:]
for x in t:
    print(x)
```

结果还是报同样的错误，那就说明不是这个问题，我想能不能从源头上就把'\n'给去掉，然后能去也比较麻烦，而且答案里也没从文件里把'\n'去掉也做出来了。所以我从上面开始找到第哪里可能出错了，最后发现一个问题，那就是如果将print(res)改成return res时就显示正常了

```python
d=dict()
def histogram(s):
    
    for c in s:
        d[c]=int(d.get(c,'0'))+1
    return d

def most_frequent(a):
    histogram(a)
    c=[]
    for key,val in d.items():
        c.append((val,key))
    c.sort(reverse=True)
    res=[]
    for val,key in c:
        res.append(key)
    #print(res)
    return res
# most_frequent('adffdadfafasdfafdafadf')
fin=open('words.txt').read()    
t=most_frequent(fin)
for x in t:
    print(x)
```

```
e
s
i
...
q
```

不过这个打印的结果是竖着的，我刚开始还以为是列表形状的原因，但是竖着的列表和横着的列表明明是一样的，这时想起来，既然问题出在最后的列表上，那么分成两种情况分别看下最终结果t的类型，结果在前面是print(res)时，t的类型是Nonetype,用return res时，t的类型是list，这才找到了原因。

**所以，要注意区分print 和 return，虽然返回结果看上去经常是一样的，但是它们的类型是不一样的，需要养成一个习惯经常用type测试一下各种返回值的类型。**

