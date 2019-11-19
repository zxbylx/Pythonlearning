# python自学日记2——函数调试

将一个大程序分解为小函数，自然而然地引入了调试的检查点，如果一个函数不能正常工作，可以考虑3种可能性。

1. 函数获得的实参有问题，某个前置条件没有达到
2. 函数本身有问题，某个后置条件没有达到
3. 函数的返回值有问题，或者使用的方式不正确

要排除第一种可能，可以在函数开始的地方加上print语句，显示实参的值（以及它们的类型）。或者可以添加代码来显式的检查前置条件。
如果实参看起来没有错，在每个return语句前添加print语句，显示返回值。如果有可能手动检查返回值。考虑使用更容易检验结果的实参来调用函数。
如果函数看起来正常，检查调用它的代码，确保返回值被正确使用（或者确实被使用了）。

用python编写Ackermann函数如下：

```python
def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
```

传入实参ack(3,4)时，返回值为125，是正常的
传入试产ack(13,4)时，报错显示如下
RecursionError: maximum recursion depth exceeded in comparison
报错原因：
python默认的递归深度是有限的（默认是1000），因此当递归深度超过999时，就会引发这样的异常。
修改递归深度方法：

```python
import sys
sys.setrecursionlimit(100000) #例如这里设置为十万
```

这个值的大小取决于你自己，最好适中即可，执行完递归再降低，毕竟递归深度太大，如果是其他未知操作引起，可能UI造成内存溢出。

回文是一个正向和你想拼写都相同的单词，比如“noon”，和“redivider”。递归的说，如果一个单词第一个和最后一个字母相同，并且中间是一个回文，则这个单词是回文
下面函数接收一个字符串形参并返回第一个，最后一个一级中间的字母：

```python
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1,-1]
```

刚开始我是这么调用的：middle(ab)
报错返回：name 'ab' is not defined
原因是字符串形参，应该传入一个字符串实参，然后改成这样：
middle('hello')，报错如下
string indices must be integers
这个错误意思是字符串的下标一定要是整数，还以为自己对字符串切片下标的记忆出了问题，然后尝试其他函数
first('hello')这个函数调用返回是正常的'h'，调用last('hello')返回也是正常的，那排除字符串下标的问题那么就是middle这个函数本身有问题
仔细看了下，原来return返回的word[1,-1]这里有错误，应该改成word[1:-1]这样就问题解决了。
编写一个函数is_palindrome,接收一个字符串形参，并当它是回文的时候返回True,否则返回False.
我的代码是这样的：

```python
def is_palindrome(word):
    if len(word)<=1:
        return True
    elif first(word)==last(word):
        if len(middle(word))<=1:
            return True
        else:
            is_palindrome(middle(word))
    return False
is_palindrome('hdedh')
```

结果按说返回是True,结果却是错的。
我初始逻辑是按照正向逻辑，先判断word长度，然后判断首字母和末尾字母是否相同，相同取中间字母，然后判断中间字母长度，然后把中间字母重新代回到is_palindrome(word)，就是不知道错哪了，望看到此知道如何改的回复一下，谢谢。

看了答案后感觉这个用逆向逻辑判断会更好一些：

```python
def is_palindrome(word):
    if len(word)<=1:
        return True
    if first(word)!=last(word):
        return False
    return is_palindrome(middle(word))
is_palindrome('hded')
```

求两个数的最大公约数，用辗转相除法：
错误代码：

```python
def gcd(a,b):
    if a=0 or b=0:    #当时想把基础情况先写出来，其中一个为0时，最大公约数为另一个值
        return a
    if a%b==0:     #如果较大的数除以较小的数余数为0，则最大公约数为较小的数
        return b
    else:
        gcd(a,b)=gcd(b,a%b)    #如果无法整除，则把较小的数和余数重新代入函数中
gcd(5,0)
```

正确思路：
1.首先判断a和b是否为0，如果为0，则最大公约数为另一个值
2.然后让a%b取余数，如果等于0，则最大公约数为b
3.如果不等于，则把b和a%b的余数代入函数中重复此过程

```python
def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    elif a%b==0:
        print(b)
    else:
        gcd(b,a%b)
gcd(0,40)
gcd(5,10)
```

看了一些别人的代码，有的用到了循环，有的需要判断a和b的大小，这些都不是必要的。但他们多数都忽略了0值，如果`b==0`，且不做前面的守卫代码，就会报错。
注意事项：
a==0,不能用a=0,刚开始这个地方出错了
另外print(b）正常显示，return b在gcd(10,5)这种一次整除情况下能显示输出结果，在无法整除的例如gcd(3,4)这种则不显示结果，要注意print和return的区别。

后来发现其实不用判断a是不是等于0，只需要判断b就可以了，a等于0的情况在下面包含着。所以修改了一下代码如下：

```python
def gcd1(a,b):
    if b==0:
        return a
    elif a%b!=0:
        gcd(b,a%b)
    return b
gcd(10,0)
```

这样代码更精简，而且也不用纠结return b还是print(b)的问题了。



另一种思路用辗转相减法求最大公约数：
1.用循环判断

```python
def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
gcd(13,40)
```

当a=b时则任取一个值为最大公约数
如果a不等于b，则用较大值减较小值，直到二者相等位置

2.##相减法求两数最大公约数

```python
def getGreatdivisor(a,b):
    if a>b:#默认b较大得数，否则两数交换位置
        a,b=b,a
    if b-a==a:
        print("最大公约数为",a)
    else:
        getGreatdivisor(b-a,a)
        
a=int(input("first:"))
b=int(input("second:"))
getGreatdivisor(a,b)
```

