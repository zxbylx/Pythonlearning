# python自学日记5——文字游戏

学习python时记录自己或观察别人从错误到正确的思路远比只看正确答案效果好——傅查理

# 1.判断单词中是否有字母“e"

写一个函数has_no_e,当给定的单词不包含字母‘e'时，返回True

刚开始我写的是这样的：

```python
def has_no_e(word):
    for letter in word:
        if letter=='e':
            return False
    	return True
has_no_e('tdy')
```

但是总是跟预想的结果不一样，单词有‘e'时也返回True,所以添加一个print想看看情况：

```python
def has_no_e(word):
    for letter in word:
        if letter=='e':
            print(letter)
            return False
        return True
has_no_e('hello')
```

但是也没效果，print貌似也没生效，这时有点怀疑打印问题了

```python
def has_no_e(word):
    for letter in word:
        print(letter)
has_no_e('hello')
```

但是这个打印时没有问题了，所以想把判断条件单独拿出来试一下：

```python
word='hello'
for letter in word:
    if letter=='e':
        return False
    else:
        return True
```

```
  File "<ipython-input-14-bb84b00c1080>", line 4
    return False
    ^
SyntaxError: 'return' outside function
```

这个报了一个语法错误，上网查了下，**原因是return在函数之外没有任何意义**，后面想把return改成break，但是break在多层循环中只能打断一层，无法跳出循环，既然拆出来没解决，只能从最初的代码找原因，**后面发现return True在循环里了，放到循环外应该就可以了**，然后试了下

```python
def has_no_e(word):
    for letter in word:
        if letter=='e'or letter=='E':
            return False
    return True
has_no_e('tdy')
```

返回正常，这样就可以了，后面有补充了对'E'的筛查。

## 2.读入words.txt,打印出不含'e'的单词，并计算这种单词在整个单词表中的百分比

words.txt可在http://thinkpython.com/code/words.txt中下载,这个结合上面的代码首先打印出这些单词，然后计算打印单词数量和单词总数，再求百分比，先计算打印单词数量如下

```python
def has_no_e(word):
    for letter in word:
        if letter=='e'or letter=='E':
            return False
    print(word)
    return True
fin=open('words.txt')
count=0
sum=0
for line in fin:
    word=line.strip()
    has_no_e(word)
    count+=1
    sum+=1
print(count)
```

单词打印倒是对的，但是sum和count是一样的，这时我想的是先求一下单词总数是多少，看看哪个出错了

```python
fin=open('words.txt')
count=0
for line in fin:
    count+=1
print(count)
```

发现结果和上面是一样，那么上面得出的是单词总数，说明自己对循环不够熟悉，以为前面加了个条件就是计算条件的数量了。但是加了个函数不知道怎么统计函数里的单词数量，所以想着不用函数，如下

```python
fin=open('words.txt')
sum=0
count=0
for line in fin:
    for letter in word:
        if letter=='e':
            continue
    	print(word)
    	count+=1
    sum+=1
print(sum)
print(count)
```

但是打印出来全是最后一个字母，数字统计的也有问题，后面想这个逻辑还是对的，把判断加到原来代码的函数上试试；

```python
def has_no_e(word):
    for letter in word:
        if letter=='e'or letter=='E':
            return False
    return True
fin=open('words.txt')
sum=0
count=0
for line in fin:
    word=line.strip()
    if has_no_e(word): #返回True时才走下面的逻辑，这样统计的就不是全部的单词了
        print(word)
        count+=1
    sum+=1
print(count)
print(sum)
print(count/sum)
```

这样结果是对的了，但是得出的是小数，需要把小数转换为百分比

```python
a=count/sum
b='%.2f%%'%(a*100)#将小数转换为百分比且保留两位小数
print(b)
```

# 3.编写一个函数is_abecedarian，如果单词中的字母是按照字母表顺序排列的（两个重复也OK），则返回True

看到这个让我想起在前面做过一个字符串比较的题，题目中说字符串也是可以通过运算符比较大小的，大写字母小于小写字母，同类字母按照字母表排序前面的小于后面的，然后根据这个写出如下代码：

```python
def is_abecedarian(word):
    for i in range(0,len(word)-1): #此处注意是len(word)-1,因为下面有word[i+1]，如果不减一后面会造成下标超出范围的情况
        if word[i]>word[i+1]:
            return False
    return True
is_abecedarian('Aabbcee')
```

根据这个函数和前面写过的代码可计算出words.txt单词表中符合此规则的单词总数

```python
fin=open('words.txt')
count=0
sum=0
for line in fin:
    word=line.strip()
    if is_abecedarian(word):
        print(word)
        count+=1
    sum+=1
print(count)
print(sum)
a=count/sum
b='%.2f%%'%(a*100)
print(b)
```

在113809个单词中符合的有596个，占比0.52%。

看了答案后有三种方法如下：

```python
#for循环法，不过与我的略有不同
def is_abecedarian1(word):
    previous=word[0]
    for c in word:
        if c<previous:
            return False
        previous=c
    return True
```

```python
#递归方法
def is_abecedarian2(word):
    if len(word)<=1:
        return True
    if word[0]>word[1]:
        return False
    return is_abecedarian2(word[1:])
is_abecedarian2('aello')
```

```python
#while循环
def is_abecedarian3(word):
    i=0
    while i<len(word)-1:
        if word[i+1]<word[i]:
            return False
        i+=1
    return True
is_abecedarian3('aello')
```



调试建议：

在所有包含'e'的单词中，你应当测试以'e'开始的单词，也应当测试以其结尾的单词，以及其在单词中部的情况。应当测试长单词、短单词及非常短的单词，比如空字符串。空字符串是特殊情形的一个例子，特殊情况往往不那么明显，但又常常隐藏着错误。

注意：你可能发现一种类型的错误（不应该包含但被却被包含的单词），但对另一种情况（应当包含但没包含的单词）则不能发现。

程序测试可以用来显示bug的存在，但无法显示它们的缺席。



今天学到一个新的解决问题的方法：问题识别

解决问题的一种方式，把问题表述为已经解决的某个问题的特例。



## 4.练习：汽车里程表共6位，初始情况，后四位是回文，行使一公里后后五位是回文，再过一公里，中间四位是回文，再过一公里，6位数是回文，求初始值，通过[::-1]来测试一个单词是不是回文

刚开始按照字符串切片和对题目的条件设置得出如下代码：

```python
def is_palindrome(word):
    if word==word[::-1]:
        return True
    return False
def chushizhi():
    for mile in range(1000000):
        if len(str(mile))!=6:
            return False 
        if is_palindrome(str(mile)[2:]) and is_palindrome(str(mile+1)[1:]) and is_palindrome(str(mile+2)[1:5]) and is_palindrome(str(mile+3)):
            print(mile)
    return False
chushizhi()  
```

这个返回是False,因为知道肯定有结果，所以知道这肯定有问题，但是这个以后要注意，以后如果不知道预期结果，那么就检查不出bug来了。第一想法就是先减少判断条件看看情况，如下代码：

```python
def is_palindrome(word):
    if word==word[::-1]:
        return True
    return False
def chushizhi():
    for mile in range(1000000):
        if len(str(mile))!=6:
            return False #因为return后都不执行，所以后面的代码由于这个return变得无效了
        if is_palindrome(str(mile)[2:]):#减少这里的判断条件
            print(mile)
    return False
chushizhi()  
```

结果还是和上面一样，再仔细看上面判断条件发现，如果mile从0到1000000，那么前面遇到一个字符长度不等于6时直接返回False,所以是因为前面的判断条件后的return导致后面的代码无法执行导致的，所以改成下面的代码：

```python
def is_palindrome(word):
    if word==word[::-1]:
        return True
    return False
def chushizhi():
    for mile in range(1000000):
        if len(str(mile))==6 and is_palindrome(str(mile)[2:]) and is_palindrome(str(mile+1)[1:]) and is_palindrome(str(mile+2)[1:5]) and is_palindrome(str(mile+3)):
            print(mile)
chushizhi()
```

返回结果198888和199999，测试了下是对的。但是总有个疑问，汽车里程刚开始不是从100000开始的，而是从000000开始的，那么从000000到100000之间是否有符合这个的呢，先看了下答案怎么写的；

```python
def has_palindrome(i, start, len):
    """Returns True if the integer i, when written as a string,
    contains a palindrome with length (len), starting at index (start).
    """
    s = str(i)[start:start+len]
    return s[::-1] == s
    

def check(i):
    """Checks whether the integer (i) has the properties described
    in the puzzler.
    """
    return (has_palindrome(i, 2, 4)   and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))


def check_all():
    """Enumerates the six-digit numbers and prints any that satisfy the
    requirements of the puzzler"""

    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


check_all()
```

结果和我的一样，而且从代码看来答案代码也没有考虑十万以前的数字。

我决定自己写一下，将上面代码改成下面的样子：

```python
def is_palindrome(word):
    if word==word[::-1]:
        return True
    return False
def chushizhi():
    for mile in range(1000000):
        a=len(str(mile))
        if a<6 and is_palindrome(str(mile).zfill(6)) and is_palindrome(str(mile+1).zfill(6)) and is_palindrome(str(mile+2).zfill(6)) and is_palindrome(str(mile+3).zfill(6)):
            print(mile)
        elif len(str(mile))==6 and is_palindrome(str(mile)[2:]) and is_palindrome(str(mile+1)[1:]) and is_palindrome(str(mile+2)[1:5]) and is_palindrome(str(mile+3)):
            print(mile)
chushizhi()
```

加了一个判断，当小于6位数时，通过字符串方法zfill，在前面用0补齐，不过得出的结果还是一样的，但是感觉这样会更严谨一些。

## 5.#练习：我和母亲年龄的两位数互为倒数，至今已经发生过6次，它可能总共发生8次，我现在多大

提示：可能会发现字符串方法zfill有用

根据这个提示说明我年龄小于10的时候也有互为倒数的情况发生，需要做个分析，互为倒数用到一个前面写过的函数is_reverse，然后判断条件是年龄互为倒数且我的年龄小于母亲的年龄，得出如下代码：

```python
def is_reverse(word1,word2):
    if len(word1)!=len(word2):
        return False
    i=0
    j=len(word2)-1
    while j>=0:
        if word1[i]!=word2[j]:
            return False
        i=i+1
        j=j-1
    return True
def age_me():
    for mo_age in range(10,100):
        for age in range(100):
            if len(str(age))<2 and is_reverse(str(age).zfill(2),str(mo_age)) and age<mo_age:
                print(age,mo_age,mo_age-age)
            if is_reverse(str(age),str(mo_age)) and age<mo_age :
                print(age,mo_age,mo_age-age)
     return a
age_me()
```

得出了很多个符合条件的数字对，但是这个无法直观看出哪个符合，所以需要计算二者差值，差值数量为8的数值对的第六组是现在的年龄：

```python
def is_reverse(word1,word2):
    if len(word1)!=len(word2):
        return False
    i=0
    j=len(word2)-1
    while j>=0:
        if word1[i]!=word2[j]:
            return False
        i=i+1
        j=j-1
    return True
def all_list(arr): #统计列表中每个元素出现的次数
    result={}
    for i in set(arr):
        result[i]=arr.count(i)
    return result
def age_me():
    a=[]
    for mo_age in range(10,100):
        for age in range(100):
            if len(str(age))<2 and is_reverse(str(age).zfill(2),str(mo_age)) and age<mo_age:
                print(age,mo_age,mo_age-age)
                a.append(mo_age-age)
            if is_reverse(str(age),str(mo_age)) and age<mo_age :
                print(age,mo_age,mo_age-age)
                a.append(mo_age-age)
    return all_list(a)
age_me() 
```

然后得出了差值为18时共出现了8次，从上开始数第六次是57和75，所以我现在年龄时57岁。

下面是答案的代码：

```python
def str_fill(i, len):
    """return the integer (i) written as a string with at least
    (len) digits"""
    return str(i).zfill(len)


def are_reversed(i, j):
    """ return True if the integers i and j, written as strings,
    are the reverse of each other"""
    return str_fill(i,2) == str_fill(j,2)[::-1]


def num_instances(diff, flag=False):
    """returns the number of times the mother and daughter have
    pallindromic ages in their lives, given the difference in age.
    If flag==True, prints the details."""
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """enumerate the possible differences in age between mother
    and daughter, and for each difference, count the number of times
    over their lives they will have ages that are the reverse of
    each other."""
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1

print('diff  #instances')
check_diffs()

# print
print('daughter  mother')
num_instances(18, True)
```

