# python自学日记4-字符串

## 1.for循环

使用for循环遍历字符

由于好久没用for循环了，有点生疏，竟然写成了下面代码

```python
fruit='banana'
len(fruit)
index=0
for index<len(fruit):
    print(fruit[index])
    index+=1
```

File "<ipython-input-2-f904b63b5686>", line 3
    for index<len(fruit):
             ^
SyntaxError: invalid syntax

报错是肯定的了，这是把for循环和while循环杂糅了，还是应该注意下for循环和while循环的区别

```python
fruit='banana'
len(fruit)
index=0
while index<len(fruit):
    print(fruit[index])
    index+=1
```

这个是能正常打印的，但是while确实不适合做遍历循环，用for会更简单一些

```python
for char in fruit:
    print(char)
```

## 2.字符串方法

这里记录两个replace和strip

```python
#str.replace(old,new[,count]) []表示里面的是可选,count,表示只替换前count次出现
word='banana'
word.replace('na','se')
word.replace('na','se',1)#只替换了第一个na
```

```python
#str.strip([chars]) 默认移除前后的空格，输入chars则移除chars
'   hello   '.strip()
'www.example.com'.strip('cmowz.')
```

```python
#strip从开头和结尾分别向中间筛选，遇到第一个非chars则停止
a='#.......section 3.2.1 issue #32.......'
a.strip('.#!')#从此结果看出，中间的 .和#都没有被移除，因为前面都有不是chars的部分 
```

输出结果是：'section 3.2.1 issue #32'

## 3.比较两个单词，如果互为倒序则返回True

```python
def is_reverse(word1,word2):
    if len(word1)!=len(word2):
        return False
    i=0
    j=len(word2)-1 #注意需要减一，否则会超出下标范围
    while j>=0: #注意要大于等于0，而不是大于0,否则会少比较一个
        if word1[i]!=word2[j]:
            return False
        i+=1
        j-=1
    return True
is_reverse('stp','pots')
```

## 4.以前写过一个回文的函数比较麻烦，这次通过[::-1]来测试单词是不是回文会简单很多

```python
def is_palindrome(word):
    if word==word[::-1]:
        return True
    return False
is_palindrome('helleh')
```

题目中有些用一行把这个函数写出来，说到一行我首先想到就是用lambda函数，思来想去写出了如下代码：

```python
is_palindrome=lambda word:(True if word==word[::1],False)
is_palindrome('hello')
```

```
  File "<ipython-input-55-363d8c65fb6a>", line 2
    is_palindrome=lambda word:(True if word==word[::1],False)
                                                      ^
SyntaxError: invalid syntax
```

结果就报错了嘛，上网查了下lambda是不能用if语句的，后面有机会详细补充下lambda的用法以及其和def函数的区别

## 5.练习：ROT13字符串轮转加密

编写一个函数rotate_word，接收一个字符串以及一个整数作为参数，并返回一个新字符串，其中字母按照给定的整数值轮转位置，'A'移动3个位置是'D'，'Z'移动1个位置是'A'.

```python
def rotate_word(word,num):
    new_word=''
    for letter in word:
        new_word.append(chr(ord(letter)+num))
    return new_word
rotate_word('a',1)
```

```
AttributeError                            Traceback (most recent call last)
<ipython-input-64-4664c16d8869> in <module>
      5         new_word.append(chr(ord(letter)+num))
      6     return new_word
----> 7 rotate_word('a',1)

<ipython-input-64-4664c16d8869> in rotate_word(word, num)
      3     new_word=''
      4     for letter in word:
----> 5         new_word.append(chr(ord(letter)+num))
      6     return new_word
      7 rotate_word('a',1)

AttributeError: 'str' object has no attribute 'append'
```

第一次直接写成上面，报错提示str是不能用append的，所以改成'+'

```python
def rotate_word(word,num):
    new_word=''
    for letter in word:
        new_word=new_word+(chr(ord(letter)+num))#这个位置改动
    return new_word
rotate_word('Z',1)
```

但是输出结果预期是'A'，但显示的是'['，这显然是对Unicode不熟悉，以及对题目没有把握好，首先我测了下'a'和'A'的Unicode值，为了能使Z加1变成A，需要经过一些计算，先把一个字母减掉初始值，如果是大写的减A的值，然后加要移动的值，再加26，然后对26取余，得出来的余数再加初始值就得到最终字母的Unicode了，然后再转换为字母即可，这里有个注意的地方，大写对应初始是A，小写对应初始是a。

```python
def rotate_word(word,num):
    new_word=''
    for letter in word:
        if letter.isupper():
            start=ord('A')#ord函数将字母转换为Unicode点的整数
        elif letter.islower():
            start=ord('a')
        #chr函数将数值编码转换为字符
        new_word=new_word+(chr((ord(letter)-start+num+26)%26+start))
    return new_word
rotate_word('melon',-10)
```

我这有个不好的毛病就是习惯把一系列运算写到一行，拆解一下或许更容易看

下面是答案的代码

```python
import string


def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
	print(rotate_word('cheer',7))
```

答案用了两个函数，而且都写好了文档字符串，显得比较容易读，以后也应该学着写文档字符串。