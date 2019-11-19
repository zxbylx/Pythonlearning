# python自学日记9——选择数据结构

## 1.编写一个程序从文件中读入一个单词列表，并打印出所有是回文的单词集合

这次的回文和以前理解的回文不一样，例子如下：

['deltas','desalt','lasted','salted','slated','staled']

['retainers','ternaries']

只要都是相同字母组成的单词都算在回文的单词集合中

按照抓取关键信息转化成自己已经掌握的方法原则，我有两个大致方向，一个是挨个读取每个单词，把单词用前面所说的字母词频计数器分解单词，如果词频计数相同的放到一个集合中；另一个方向是将26个字母通过排列组合方式组成各个单词然后去单词表中比对，显然第二个方法违反了最初的原则，因为这个并没有在我目前的掌握之中，而且特复杂，计算量大。

但是后面发现还有更简单的方法，就是利用已经掌握的排序功能，将每个单词的字母分拆并排序，如果结果相同的放到一个集合里。

```python
def paixu_pinjie(word):
    t=list(word)
    t.sort()
    a=''.join(t)
    return a

fin=open('words.txt')
d=dict()
for line in fin:
    word=line.strip()
    b=paixu_pinjie(word)
    if b not in d:
        d[b]=word
    else:
        d[b].append(word)
return d

for key,val in d.items():
    if len(val)>1:
        print(val)
```

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-14-c76bff3c7e52> in async-def-wrapper()
     17 return d
     18 
---> 19 for key,val in d.items():
     20     if len(val)>1:
     21         print(val)

AttributeError: 'str' object has no attribute 'append'
```

这里发现问题在d[b]=word上，word是字符串，所以不能使用append，如果想在后面添加单词编程单词集合，需要将word变成列表：

```python
def paixu_pinjie(word):
    t=list(word)
    t.sort()
    a=''.join(t)
    return a

fin=open('words.txt')
d=dict()
for line in fin:
    word=line.strip()
    b=paixu_pinjie(word)
    if b not in d:
        d[b]=[word]
    else:
        d[b].append(word)
return d

for key,val in d.items():
    if len(val)>1:
        print(val)
```

这样倒是不报错了，但是发现输出结果里有一个单词的集合，显然最后的for循环后面的代码没生效，发现是因为for上面的return导致的，按说return只能在函数里使用，现在有两个解决方案，一个是把这个return删除，另一个是把上面的写成一个函数。

```python
def paixu_pinjie(word):
    t=list(word)
    t.sort()
    a=''.join(t)
    return a

def all_anagrams(filename):
    fin=open(filename)
    d=dict()
    for line in fin:
        word=line.strip().lower()
        b=paixu_pinjie(word)
        if b not in d:
            d[b]=[word]
        else:
            d[b].append(word)
    return d
def print_anagram_set(d):
    for key,val in d.items():
        if len(val)>1:
            print(val)

d=all_anagrams('words.txt')
print_anagram_set(d)
```

将上面代码改成了函数，另外在word=line.strip()后面加上了.lower()，需要将大写字母变成小写字母。决定是否将一段代码写成函数的原则是，这段代码是否会被重复使用，还有这段代码是否可以单独拆出来不用。

修改前面问题的程序，按照集合内单词数量倒序打印。

```python
def print_anagram_sets_in_order(d):
    t=list() #建一个空列表储存数据
    for key,val in d.items():
        if len(val)>1:
            t.append((len(val),val))
    t.sort(reverse=True) #排序
    #按倒序打印
    for x in t:
        print(x)
print_anagram_sets_in_order(d)
```

因为后面需要重新使用上面的部分代码，所以需要将其中一部分转换为函数，否则就得重新写一遍。

## 2.编写一个choose_from_hist,接受一个直方图作为参数，并从直方图中，按照频率大小，成比例的随机返回一个值

直方图在“python自学日记7——字典”中有写过，通过这个也想起有人问过一个关于什么是好的python学习资料的问题，我决定一个好的学习资料其中有一点就是能把前后的知识点通过练习题的方式串起来。其他的再单独找时间一起说一下。

直方图函数早已经写过了，剩下的就是根据概率随机取值了。从官方文档中看到random中有choices是符合这个要求，其中有个关键参数weights是可以在列表中根据weights后面的列表中每个数占总数的概率取值的，具体到本例中，直方图会得出一个字典，包含没给字母和对应字母出现的词频，我们可以将字典中键和值分成两个列表，键的列表作为随机取值的列表，值的列表则赋值给weights作为前面取值的概率，得出如下代码

```python
def histogram(s):
    d=dict()
    for c in s:
        d[c]=int(d.get(c,'0'))+1  #get可接收一个键和默认值，如果字典中有这个键，返回键对应值，否则返回默认值
    return d
def choose_from_hist(s):
    d=histogram(s) #在直方图函数结果基础上又运行了一次函数
    a=[] 
    b=[]
    for key,val in d.items():
        a.append(key)
        b.append(val)
    print(a) #键的列表
    print(b) #值的列表
    return random.choices(a,weights=b,k=20)
h=histogram('aaaaaabb')        
choose_from_hist(h)
```

```
['a', 'b']
[1, 1]
```

结果返回值中值列表本来应该是[6,2]结果是[1,1]，查看原因是发现，直方图函数运行了两次，也就是已经传入了直方图函数作为参数，有运行了一次直方图函数。所以去掉函数内运行直方图代码即可

```python
def histogram(s):
    d=dict()
    for c in s:
        d[c]=int(d.get(c,'0'))+1
    return d


def choose_from_hist(s):
    a=[]
    b=[]
    for key,val in d.items():
        a.append(key)
        b.append(val)
    print(a)
    print(b)
    return random.choices(a,weights=b,k=5) #k是一次去k个随机数
h=histogram('aaaaaabb')        
choose_from_hist(h)
```

```
['a', 'b']
[6, 2]
```

Out[85]:

```
['a', 'a', 'a', 'a', 'b']
```

