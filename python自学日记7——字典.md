# python自学日记7——字典

学会把复杂问题拆解成自己已经掌握的基础问题才是正确的学习之道——傅查理

# 1.编写一个函数，读入words.txt,并将它们作为键保存到一个字典中

后面还有使用in检查某单词是否在字典中，按说这个并不难，先读取单词表，然后通过将单词作为键，值用空字符就可以了，然后代码如下：

```python
def read_dict():
    fin=open('words.txt')
	words_dict={}
    for line in fin:
        word=line.split()
        words_dict[word]=''
    return words_dict
read_dict()
```

```
TypeError                                 Traceback (most recent call last)
<ipython-input-18-59d842fe37d6> in <module>
      7         words_dict[word]=''
      8     return words_dict
----> 9 read_dict()

<ipython-input-18-59d842fe37d6> in read_dict()
      5     for line in fin:
      6         word=line.split()
----> 7         words_dict[word]=''
      8     return words_dict
      9 read_dict()

TypeError: unhashable type: 'list'
```

但是报错了，具体原因也弄不清楚，只能先把循环单独拿出来比对一下

```python
fin=open('words.txt')
for line in fin:
    word=line.split()
    print(word)
```

```
['aa']
['aah']
['aahed']
['aahing']
['aahs']
['aal']
['aalii']
['aaliis']
['aals']
```

显示的是这样的，我记得前面读取的时候没有中括号，仔细看发现错在word=line.split(),split是做分割用的，本来这里应该用strip去空格的，只凭记忆写的记混了，然后改一下

```python
def read_dict():
    fin=open('words.txt')
	words_dict={}
    for line in fin:
        word=line.split()
        words_dict[word]=''
    return words_dict
read_dict()
```

这次显示就正常了，如果只到这没下面的检查单词是否在字典中这段代码是没有问题的，但是要检查一个单词是否在字典的键中就需要用到字典，而在函数中字典是局部引用，没法在别处使用的，所以当检查单词是否在字典中时会报错：words_dict没有被定义，所以需要把它放到函数外面，最终改成如下：

```python
fin=open('words.txt')
words_dict={}
def read_dict():
    
    for line in fin:
        word=line.strip()
        words_dict[word]=''
    return words_dict
read_dict()
'hello' in words_dict
```

代码是输出正常了，但是总觉得这个方法有点怪，也许会有更好的方法，后面找到再说。

## 2.使用字典作为计数器集合

```python
def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d
h=histogram('faljgaldkjalgkjeweraldfjsl')
print(h)
```

```
{'f': 2, 'a': 4, 'l': 5, 'j': 4, 'g': 2, 'd': 2, 'k': 2, 'e': 2, 'w': 1, 'r': 1, 's': 1}
```

这是比较常规的做法，字典有一个方法get，接收一个键和一个默认值，如果键出现在字典中，get返回对应的值，否则返回默认值，接下来用get来替代上面的代码

```python
def histogram(s):
    d=dict()
    for c in s:
        d[c]=int(d.get(c,'0'))+1 
    return d
h=histogram('faljgaldkjalgkjeweraldfjsl')
print(h)
```

get默认值设为0，如果c不在d，返回0，通过加1,d[c]=1,下次再检查这个值时，因为在d中会返回1，再通过加一变成2，这样就通过循环得出结果，省去了判断条件

## 3.反转字典

将原字典的值变为新字典的键，原字典的键变为新字典的值。

原来的方法还是通过键来做遍历，然后每次将对应的值去和新的字典中去比对，如果没有新增一个键值对，如果有了只在原来的值上增加一个新值

```python
def invert_dict(d):
    invert=dict()
    for key in d:
        val=d[key]
        if val not in invert:
            invert[val]=[key]
        else:
            invert[val].append(key)
    return invert
d=histogram('parrot')
print(d)
invert_dict(d)
```

```
{'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}
{1: ['p', 'a', 'o', 't'], 2: ['r']}
```

字典有个方法setdefault，通过这个方法将上面的函数写得更简洁些：

setdefault(key['default'])：如果字典存在键 key ，返回它的值。如果不存在，插入值为 default 的键 key ，并返回 default 。 default 默认为 None。

按照上面的描述需要先做几个实验，因为我们需要在空字典里新增键值对，需要用空字典测试一下setdefault方法

```python
a=dict()
a.setdefault('b',1)
```

返回值是1，print(a)返回是{'b': 1}，这样说如果字典里没有就会按照括号里的内容变成键值对放到字典里，再测试下

```python
a.setdefault('b',2)
print(a)
```

返回值还是{'b': 1}，这样基本上就懂了，如果已经存在返回还是1，我们需要在循环时如果键已经存在字典中需要增加键的值，那么刚开始设置为空字符，不过需要测试下类型：

```python
type(a.setdefault('a',''))
```

返回值是str，那么就再测试下用list能不能将空字符串转换为列表

```python
list(a.setdefault('a',''))
```

返回值是[]，那么就可以写代码了

```python
def invert_dict(d):
    invert=dict()
    for key in d:
        val=d[key]
        invert[val]=list(invert.setdefault(val,'')).append(key)
    return invert
d=histogram('parrot')
invert_dict(d)
```

```
TypeError                                 Traceback (most recent call last)
<ipython-input-116-5d92649dd8a4> in <module>
      7     return invert
      8 d=histogram('parrot')
----> 9 invert_dict(d)

<ipython-input-116-5d92649dd8a4> in invert_dict(d)
      4     for key in d:
      5         val=d[key]
----> 6         invert[val]=list(invert.setdefault(val,'')).append(key)
      7     return invert
      8 d=histogram('parrot')

TypeError: 'NoneType' object is not iterable
```

上网查了下报错原因说一般发生在将None赋给多个值时，还是需要先拆解成小代码块检查

```python
b=dict()
b['a']=list(b.setdefault('a','')).append('hello')
print(b)
```

返回值是{'a': None}，本来预期是后面变成hello结果用append没有效果，换“+”试试

```python
b=dict()
b['a']=list(b.setdefault('a',''))+['hello']
print(b)
```

```
{'a': ['hello']}
```

这次返回值倒是正常了，上面报错看出是用append键的值都是None才报错的，下面将append改成“+”

```python
def invert_dict(d):
    invert=dict()
    for key in d:
        val=d[key]
        invert[val]=list(invert.setdefault(val,''))+[key]
    return invert
d=histogram('parrot')
invert_dict(d)
```

这次返回结果是正常的了。

看了答案代码如下

```python
def invert_dict(d):
    """Inverts a dictionary, returning a map from val to a list of keys.

    If the mapping key->val appears in d, then in the new dictionary
    val maps to a list that includes key.

    d: dict

    Returns: dict
    """
    inverse = {}
    for key, val in d.items():
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, z=1)
    inverse = invert_dict(d)
#     for val, keys in inverse.items():
#         print( val, keys)
    print(inverse)
```

发现了几个问题，首先我不知道字典可以用for key, val in d.items(),这样可以节省一些代码，dict.items(返回的对象是一个动态试图，当字典变是，视图也会变。

另外答案用的是inverse.setdefault(val, []).append(key)，而不是用将值赋给value，就说明我对这个setdefault并没有完全理解，另外我也发现了一个问题，我用的是' ',答案用的是[],倒是省了再转化成list了。还一个让我更清楚的是有返回值和没有返回值的情况，例如

```python
[1,2]+[3]
```

返回值是[1,2,3]

但是用[1,2].append('3')，返回值是None,这也就说明了为什么会在前面报上面的错误。

## 4.编写一个程序，读入单词表，并找到所有轮转对。

轮转对：两个单词，如果可以使用轮转操作将一个转换为另一个，则成为轮转对。例如ad轮转一步变为be。

遇到一个大的问题没头绪首先要想一下能将这个问题分解成哪些已经做过的，读入单词表这个以前做过了，轮转操作在ROT13那个练习中也做过了。那么大体思路就是读入单词表，用遍历方式将每个单词轮转1到25步，因为26步是本身，然后将轮转后的单词查看是否在单词表中，如果在就打印出来这两个词就可以了。

```python
import bisect
def rotate_word(word,num): #轮转单词
    new_word=''
    for letter in word:
        if letter.isupper():
            start=ord('A')
        elif letter.islower():
            start=ord('a')
        
        new_word=new_word+(chr((ord(letter)-start+num+26)%26+start))
    return new_word
# rotate_word('melon',-10)
def find_lt(a,x): #查找单词是否在单词表中
    i=bisect.bisect_left(a,x)
    if i != len(a) and a[i]==x:
        return True
    return None
def read_words(): #读取单词表
    fin=open('words.txt')
    t=[]
    for line in fin:
        word=line.strip()
        t.append(word)
    return t
def sdf():
    t=read_words()
    for s in t:
        for i in range(1,26):
            new_words=rotate_word(s,i)
            if find_lt(t,new_words):
                print(s,i,new_words)
sdf()    
```

总结：注意一个方法或函数最后是有返回值还是没返回值的情况。

从今天看出有些时候会发现答案给的代码中会有一些内置函数或方法使得编程变得很简单，这当然很好，所以应该多多阅读标准库。但是在不知道这个的情况下也能做出来也非常好。就像刚开始学英语时，比较好的练习方式是用已掌握的一些简单词汇能把一些你没遇到的复杂事物或情况描述出来。所以一是要多多掌握简便的方法，也要学着把复杂问题转换成自己已经掌握的方法来解决。