# python自学日记16——调试(常见错误)

整理一套错误检查清单将在你未来编程时提供很大的助力。

## 1.语法错误

语法错误由python在将源代码翻译为字节的过程中产生。例如在def语句的末尾漏电冒号会产生一个冗余的错误信息：

```python
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()

def print_lyrics() #漏掉了冒号
    print('hello world')
```

报如下错误，SyntaxError语法错误的提示

```
  File "<ipython-input-1-ca5d3c6b426f>", line 6
    def print_lyrics()
                      ^
SyntaxError: invalid syntax
```

语法错误在知道怎么修改后往往都比较容易修正，但是，错误信息往往没有什么帮助，最常见的错误信息就是SyntaxError: invalid syntax（无效数据）和SyntaxError: invalid token（无效记号），都没什么信息量，只能自己找到相应的行检查。

需注意的是，语法错误虽然指出了出错的位置，但指出的位置并不一定就是发成错误的位置，有时候错误发生的位置是错误信息指明的位置之前，往往是前一行。

下面是一些可以避免最常见的语法错误的方法：

1. 确保你没有使用python关键字作为变量名称，例如class, del, from, not, while, as,global等，解释器通过关键字来识别程序的结构，不能用来做变量名称。
2. 检查在每一个符合语句的结尾，都有一个冒号，包括for，while, if和def语句。
3. 确保程序中每个字符串都有前后匹配的引号，自己可以试着看看少一个引号和没有引号报错的区别

```python
michael='Eric,the half a bee #少于个引号
print_twice(michael)
```

```
  File "<ipython-input-8-15d01e150a6d>", line 1
    michael='Eric,the half a bee
                                ^
SyntaxError: EOL while scanning string literal
```

4. 如果你有三引号(单引号或双引号字符)多行字符，确保你正确结束了字符串。没有正确结束的字符串，会导致程序结尾处产生invalid token错误，或者它会将接下来的陈谷看做字符串的一部分，知道遇到下一个字符串为止。这种情况下可能都不会报错。
5. 没有关闭的开始符号——(，{或[——会让python继续解析下一行，并当做当前语句的一部分。通常来说，会在下一行立即产生一个错误。这种错误最常见的是多个嵌套时，有时候会数不过来，另外常见情况下是在一个括号中新增括号时容易漏掉。

```python
#在增加边长平方变量后依然返回成功，下面计算斜边长的平方
def hypotenuse(a,b):
    square_a=a**2
    square_b=b**2
    square_c=square_a+square_b
    print('斜边长的平方为：'+str(square_c)) #忽略了字符串必须和字符串之间用加号，直接用square_c，两个类型不一样不可用加号
    return 0
```

这种情况本来没有加str，后面需要转换为字符串时，容易在前面加str然后括号，到右侧添加括号时会出现你以为添加右侧括号了，实际上编辑器只是把光标移出括号的情况，需要再添加一次。

6. 检查在条件判断时将'=='写成'='的错误，这个是刚开始学python时经常出现的错误。
7. 检查缩进，不过这个选择一个合适的编辑器统一缩进一般不会出现问题。

**我一直修改，但没有什么区别**

这个我经常遇到，如果解释器报错的一个错误而你找不到，有可能是因为解释器和那你用的并不是同一套代码，检查你的编程环境，确保你正在编辑的代码和python运行的是同一个。出现这种问题有可能是以下原因：

1. 你修改了代码，但是解释器运行的还是你修改前的代码；如果不确定，可以在程序开头协商一个明显的错误，再运行一次，如果解释器没有发现这个错误，说明运行的不是新代码。
2. 你运行的是其他页面的代码，这种在pycharm这种编辑器中我遇到过，上面的运行会有运行文件提示，并不总是运行当前页面的代码。
3. 你编辑了代码，但是忘了报错了，有的编程环境会自动保存，有的不会，这个需注意下，最好找个自动保存的或者运行前会系统先保存再运行的。
4. 你修改了文件名，但代码中文件名没有改过来。
5. 如果你在编写一个模块，并使用import，请确保你的模块名称没有和python标准模块冲突，这个问题倒是不大，python命名空间决定一般先检查局部变量，再检查全局变量，最后检查内置变量。
6. 如果你在使用import来读入模块，请记得重载一个修改过的文件时，需要重启解释器或者使用reload。如果你重新导入这个模块，它并不会做任何事。同一个页面定义的类也是这样，修改就要重启编辑器。

如果你遇到困难被卡住，并弄不清楚是怎么回事，一个办法是重新以最简单的类似“hello world！”的程序开始，并确保你能让一个已知的程序运行，然后逐渐添加原先程序的部分到新程序中。

我自己看了下自己以前的语法错误：

```python
#使用for循环遍历字符串
index=0
for index<len(fruit):
    print(fruit[index])
    index+=1
```

```
  File "<ipython-input-2-f904b63b5686>", line 3
    for index<len(fruit):
             ^
SyntaxError: invalid syntax
```

这个是因为把for循环和while循环弄混了，for循环不能用条件判断的

```python
def qiuzhi(k):
    jieguo=(factorial(4k)*(1103+26390*k))/(factorial(k)**4*396**(4*k))
    while jieguo<1e-15:
        break
    jieguo=jieguo+(factorial(4(k+1))*(1103+26390*(k+1)))/(factorial(k+1)**4*396**(4*(k+1)))
    return jieguo
qiuzhi(0)
```

```
  File "<ipython-input-11-34f8f7a78fcc>", line 2
    jieguo=(factorial(4k)*(1103+26390*k))/(factorial(k)**4*396**(4*k))
                       ^
SyntaxError: invalid syntax
```

这个就比较典型了，我这不好的习惯想把所有内容写到一行里，导致代入数据结果正常显示，但是公式就是报错，最后也没找出错在哪，把这一整行分割赋值变量变成几行就没报错了，这个还容易忘了括号等问题。

# 2.运行时错误

### 2.1 我的程序什么都不做

这个问题最常见的原因是你的文件包含了各种函数和类的定义，但没有实际调用任何代码来启动执行。

比如写了一个函数，但是没有调用

```python
#用最简单的函数确定函数式子可行，然后下一步增加边长平方的变量
def hypotenuse(a,b):
    square_a=a**2
    square_b=b**2
    print(square_a)
    print(square_b)
    return 0
```

如果是运行上面代码是没有任何反应的，因为没有调用函数

```python
hypotenuse(3,4)
```

只有通过调用函数，才会有正常的返回值。、

如果你不确认程序中执行流程如何走向，可以在每个函数开头添加一个print语句，打印类似“进入函数foo”之类的输出，foo指得是函数名。

### 2.2 我的程序卡死了

如果一个程序突然停止看起来什么都没做，在jupyter notebook就是左侧一直显示星号，下面没有输出值，它就有可能卡死了。常见的原因是死循环和无限递归。

无限循环问题解决办法：

如果怀疑某个特别的循环，可以在循环开始前添加一个“进入xx循环”的print语句，在循环结尾处添加一个“退出xx循环”的print的语句。在运行程序如果只看到第一个没看到第二个证明进入死循环了。这其实是一个比较好的习惯，可以在每次写循环的时候都添加上。

如果你觉得有个无限循环但并不知道哪个循环导致了问题，可以在循环结尾处添加一个print语句，打印出循环条件中的变量值，以及条件的值。

```python
while x>0 and y<0:
    print('x:',x)
    print('y:',y)
    print('condition:',(x>0 and y<0))
```

现在当你再次运行程序时，正常情况是每次循环看到三次打印最后打印false，如果一直循环你可以从打印的值里找出问题。

无线递归问题解决办法：

大部分情况下，无限递归都会在程序运行一会儿后产生“Maximum recursion depth exceeded”的错误。可以先检查来保证有一个条件能导致函数或方法直接返回而不再继续递归调用。如果没有，那么你可能需要冲洗思考算法，并设定一个退出条件。

```python
def countdown(n):
    if n<=0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
        
countdown(3)
```

上面是一个简单的递归情况，直接返回的条件就是n<=0，检查你的递归中是否有这种类似的条件，没有的话就会产生无线递归的情况。

如果有这种条件，但还是报错，有可能是因为系统的默认递归次数太少，默认999次，可以自行修改一下，但是如果修改了还不行，可以在函数或方法的开头加一个print语句来打印参数，会看到每次函数调用都会打印几行输出，并能看到每次调用的参数，如果参数没有向触发直接返回的条件变化，大概也就发现问题所在了。

### 2.3常见运行时错误

**NameError:**

这种是我经常遇到的，打印错误单词，print写成了pirnt，有时候写快了就容易出这种错误，长单词少写个字母等。总之就是试图使用一个当前环境中不存在的变量。还有个要注意的是，函数内部的局部变量不能在定义他们的函数之外使用它们。



**TypeError:**

有三种可能的原因：

- 你在尝试错误地使用一个值。例如使用不是整数的值来索引字符串、列表或元组。

```python
a=[1,2,3,4]
a[1.1]
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-13dd0ca0e4b6> in <module>
      1 a=[1,2,3,4]
----> 2 a[1.1]

TypeError: list indices must be integers or slices, not float
```

- 格式符字符串中，内部的格式项和传入的参数不匹配。当格式项的树木不对或者转换的类型不对时都可能发生。

```python
'%d %d %d'%(1,2)#两边个数必须相等
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-c9066aaeeec0> in <module>
----> 1 '%d %d %d'%(1,2)

TypeError: not enough arguments for format string
```



```python
'%d'%'dollors'#类型也要一致
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-3e9f7bc91415> in <module>
----> 1 '%d'%'dollors'

TypeError: %d format: a number is required, not str
```

- 调用函数或方法时使用了错误数量的参数。对于方法来说，查看方法定义并检查第一个参数是否为self。接着查看方法调用；确保你实在正确类型的对象上调用方法，并正确提供了其他参数。

```python
#内置函数divmod接收两个参数，并返回两个值的元组，商和余数
t=(7,3)
divmod(t)#改成*t就可以了
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-13-4fed58f359b2> in <module>
      1 t=(7,3)
----> 2 divmod(t)

TypeError: divmod expected 2 arguments, got 1
```



```python
#练习：编写一个函数sumall，接收任意个数的参数并返回它们的和
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

sum只需要两个参数，这边却给了四个。

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

sum需要接收第一个参数是一个列表或元组等。

```python
def is_anagram(word1,word2):
    if "".join(list(word1).sort())==word2 or "".join(list(word2).sort())==word1:
        return True
    return False
is_anagram('hello','ab')
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-39-716276a7e28b> in <module>
      3         return True
      4     return False
----> 5 is_anagram('hello','ab')

<ipython-input-39-716276a7e28b> in is_anagram(word1, word2)
      1 def is_anagram(word1,word2):
----> 2     if "".join(list(word1).sort())==word2 or "".join(list(word2).sort())==word1:
      3         return True
      4     return False
      5 is_anagram('hello','ab')

TypeError: can only join an iterable
```

这里是因为sort()没返回值，是Nonetype，不符合join参数类型。



**KeyError:**

用一个字典不包括的键来查找字典的元素。

```python
items={'a':1,'b':2,'c':3}
items['d']
```

```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-2-d10caf65b3e6> in <module>
      1 items={'a':1,'b':2,'c':3}
----> 2 items['d']

KeyError: 'd'
```

显然这个报错并没有给出太多的信息，只能按照位置自己看一下了，想要找到问题所在得知道KeyError出现的原因是什么。



**AttributeError:**

在访问一个并不存在的属性或方法。检查拼写，可以使用dir函数来列出存在的属性。

```python
#练习：编写一个函数is_anagram,接收两个字符串，当它们互为回文时返回True
def is_anagram(word1,word2):
    if word1.sorted()==word2:
        return True
    return False
is_anagram('ab','ba')
```

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-37-85d6d5401dcc> in <module>
      4         return True
      5     return False
----> 6 is_anagram('ab','ba')

<ipython-input-37-85d6d5401dcc> in is_anagram(word1, word2)
      1 #练习：编写一个函数is_anagram,接收两个字符串，当它们互为回文时返回True
      2 def is_anagram(word1,word2):
----> 3     if word1.sorted()==word2:
      4         return True
      5     return False

AttributeError: 'str' object has no attribute 'sorted'
```

看到str没有sorted那改成sort(),结果还是相同错误。当时不知道这个类型错误的处理办法，只能瞎试了。

```python
t=[1,2,3]
t.find(1)
#想直接用用find方法，结果不行
```

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-56-36895259f80e> in <module>
      1 t=[1,2,3]
----> 2 t.find(1)
      3 #想直接用用find方法，结果不行

AttributeError: 'list' object has no attribute 'find'
```



```python
#练习：编写一个函数rotate_word，接收一个字符串以及一个整数作为参数，并返回一个新字符串，其中字母按照给定的整数值轮转位置
def rotate_word(word,num):
    new_word=''
    for letter in word:
        new_word.append(chr(ord(letter)+num))
    return new_word
rotate_word('a',1)
```

```
---------------------------------------------------------------------------
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

如果AttributeError指明一个对象是Nonetype，则意味着它是None.这种问题的一个常见原因是忘记返回或用print替代了返回。如果函数执行语句到结尾都没有遇到return语句，那么它会返回None。另一个常见的原因是使用了一个返回None的列表方法作为结果，比如sort。所以注意print和return的区别，以及注意一个方法是否有返回值是比较重要的事。



**IndexError:**

在访问列表、字符串或元组时使用的索引大于它的长度减一。在错误发生前一行，添加一个print语句展示索引的值和数组的长度。数组长度是否正确，索引大小是否正确。

```python
a=[1,2,3,4]
a[4]
```

```
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-4-46bc376b5cb2> in <module>
      1 a=[1,2,3,4]
----> 2 a[4]

IndexError: list index out of range
```

更容易出错的情况是在`for i in range(len(list)):`这种情况时，有时候需要减一，有时候不需要减一，这个需要根据循环里的内容做判断，容易出错。

## 3.语义错误

语义错误是正常返回值但是和预期不一样的错误。从某种角度来说，语义错误更难调试。因为解释器并不提供任何错信息，只有你自己知道程序到底应该怎么做。

解决语义错误的第一步是在程序文本和你看到的程序行为之间建立一个连接。你需要对程序实际在做什么有一个假设。让这件事变得很难的原因是计算机运行得太快。

在合适的位置插入print语句依然是最简单有效的检查问题的方法

你应该问自己如下几个问题：

- 程序中有没有地方你期望它去做而实际上没有发生的？找到运行那段功能的代码，并确保它确实如你所期望的那样运行了。
- 有没有一些不应该发生的事情？找到程序中运行了某种不该出现的功能的代码。
- 有没有一段代码产生的效果和你所期望的不一致？确保你完全明白这段代码，特别是当它牵涉到其他python模块的函数或方法的调用时。阅读你调用到的函数的文档。使用简单的测试用例测试它们并检查结果。

为了能够编程，你需要对程序如何工作，有一个思维模型。如果编写出一段和你预料不一样的代码，常常问题不是在程序本身，而是在你的思维模型上。

修正你的思维模型的最佳方法是将程序划分成不同部分（通常是函数和方法）并独立测试每一部分。一旦找到你的模型和真实世界的偏差，就能够解决问题了。

当然，在开发程序时，你应当分组件进行构建和测试。如果发现一个问题，应当只需要检查一小部分新的不确认是否正确的代码。

编写复杂表达式也有可能出问题，难读，难调试。另一个问题是求值的顺序可能和你期望的也不一样。将复杂表达式拆分成一系列复制到临时变量的语句，常常是好主意。

```python
def estimate_pi():
    def factorial(n):
        if n==0:
            return 1
        else:
            recurse=factorial(n-1)
            result=n*recurse
            return result
    a=0
    k=0
    while (factorial(4k)*(1103+26390*k))/(factorial(k)**4*396**(4*k))>=1e-15:
        a+=(factorial(4k)*(1103+26390*k))/factorial(k)**4*396**(4*k)
        k=k+1
    return a
    daoshu=2*math.sqrt(2)/9801*a
    pi=1/daoshu
    return pi
estimate_pi()
```

```
  File "<ipython-input-7-c6198d4f4c13>", line 11
    while (factorial(4k)*(1103+26390*k))/(factorial(k)**4*396**(4*k))>=1e-15:
                      ^
SyntaxError: invalid syntax
```

拆分了好几次代码，这个复杂公式总是出错，后来把公式拆了就没问题了

```python
import math
def factorial(n):
    if n==0:
        return 1
    else:
        recurse=factorial(n-1)
        result=n*recurse
        return result
def estimate_pi():
    total=0
    k=0
    factor=2*math.sqrt(2)/9801
    while True:
        num=factorial(4*k)*(1103+26390*k)
        den=factorial(k)**4*396**(4*k)
        term=factor*num/den
        total+=term
        if abs(term)<1e-15:
            break
        k+=1
        return 1/total
print(estimate_pi())
        
```

有时候自己实在想不出来了，可以暂时离开电脑休息下，也许过段时间就找到问题所在了。

实在找不到错误需要别人帮助的情况也是存在的，这时请确保你已经准备好了。你的程序应当尽量简单，而你应当使用最小的输入来复现错误。你应当在合适的地方放好了print语句(并且他们的输出应当容易理解)，你应当足够理解这个问题，因此能够简明扼要的描述它。

当你找人帮忙时，请确保给他们需要的信息：

- 如果有错误信息，它是什么，它代表了程序的哪部分？
- 在这个错误发生前，你做的最后一件事是什么？你写的最后一段代码是什么？失败的心测试用例是什么？
- 至今为止你做了哪些尝试，并从中得到了什么？

我们的目标不只是让程序正确运行，目标是学会如何让程序正确运行。