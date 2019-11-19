# python自学日记10——文件

让自己尽量暴露在错误之中是成长的一个比较快的方式，发下错误就证明你要习得新知识点了。

## 1.写一个函数sed，接收如下参数，一个模式字符串，一个替换用字符串，以及两个文件名；读取第一个文件，并将内容写入第二个如果文件中任何地方出现了模式字符串，它应该被替换

如果在过程中遇到错误，你的程序应当能捕获异常，打印一个错误，并退出。

首先要抓取关键信息，一个函数四个形参，两个字符串，两个文件名；读取文件、写入文件、替换文字，捕获异常。

先将这个拆解成最简单的，读取和写入，因为前面已经分别练习过读取文件和写入文件，分解出来的任务就是要组合这两个小的知识点，将已经掌握的小知识点组合的过程是对小知识点的练习也能形成新的知识点。

```python
def sed(file1,file2):
    
    fin=open(file1,'r') 
    fout=open(file2,'w')
    fout.write(fin)
sed('words.txt','hello.txt')
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-31-f986a2d23114> in <module>
      6 
      7 #         print('Something went wrong')
----> 8 sed('words.txt','hello.txt')

<ipython-input-31-f986a2d23114> in sed(file1, file2)
      3     fin=open(file1,'r')
      4     fout=open(file2,'w')
----> 5     fout.write(fin)
      6 
      7 #         print('Something went wrong')

TypeError: write() argument must be str, not _io.TextIOWrapper
```

看来用open(filename,'r')形式读取的文件内容格式是_io.TextIOWrapper，且这个是无法直接写入另一个文件的，所以我改成open(filename).read()，这个打印到新文件中是正常的

```python
def sed(file1,file2):
    
    fin=open(file1).read()
    fout=open(file2,'w')
    fout.write(fin)
    file1.close()
    file2.colse()
sed('words.txt','hello1.txt')
```

打印正常后我想着应该把两个文件给关掉，保持一个好的习惯，但是报错了

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-35-440dad7d9561> in <module>
      8 
      9 #         print('Something went wrong')
---> 10 sed('words.txt','hello1.txt')

<ipython-input-35-440dad7d9561> in sed(file1, file2)
      4     fout=open(file2,'w')
      5     fout.write(fin)
----> 6     file1.close()
      7     file2.colse()
      8 

AttributeError: 'str' object has no attribute 'close'
```

也就是说传入的形参文件名只有在具体方法或函数中才有用，否则就是一个字符串，字符串肯定是不能关闭的。然后看了前面练习过程中用到的是fout.close()，那就跟着学一下

```python
def sed(file1,file2):
    
    fin=open(file1).read()
    fout=open(file2,'w')
    fout.write(fin)
    fin.close()
    fout.colse()
sed('words.txt','hello1.txt')
```

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-49-b453bf941c2a> in <module>
      8 
      9 #         print('Something went wrong')
---> 10 sed('words.txt','hello1.txt')

<ipython-input-49-b453bf941c2a> in sed(file1, file2)
      4     fout=open(file2,'w')
      5     fout.write(fin)
----> 6     fin.close()
      7     fout.colse()
      8 

AttributeError: 'str' object has no attribute 'close'
```

这就问题大了，用open(filename).read()把fin的格式变成了字符串，导致了无法close，那先注释掉这一行看看行不行

```python
def sed(file1,file2):
    
    fin=open(file1).read()
    fout=open(file2,'w')
    fout.write(fin)
#     fin.close()
    fout.colse()
    
sed('words.txt','hello1.txt')
```

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-50-ec090cd36d61> in <module>
      7     fout.colse()
      8 
----> 9 sed('words.txt','hello1.txt')

<ipython-input-50-ec090cd36d61> in sed(file1, file2)
      5     fout.write(fin)
      6 #     fin.close()
----> 7     fout.colse()
      8 
      9 sed('words.txt','hello1.txt')

AttributeError: '_io.TextIOWrapper' object has no attribute 'colse'
```

结果fout直接写入的文件格式也是_io.TextIOWrapper，也无法关闭。这就成难题了，我看前面直接写入一行字符串是可以关闭的，那也许是需要一行行读取，一行行写入，如果这样可以关闭，那还得解决一个问题，读取的文件怎么关闭，需要再做一个测试

```python
fin=open('a.txt','r')
print(fin)
fin.close()
```

```
<_io.TextIOWrapper name='a.txt' mode='r' encoding='cp936'>
```

没有报错，证明关闭文件成功，现在需要的是把文件一行行读取，一行行写入

```python
def sed(file1,file2):
    fin=open(file1,'r')
    fout=open(file2,'w')
    for line in fin:
        fout.write(line)
    fin.close()
    fout.close()
sed('a.txt','e.txt')
```

没有报错，去检查了下e.txt发现也把a.txt中的内容全部写入进去了。证明这一步算是成功了，那么接下来就是处理替换的问题了，替换利用前面的格式操作符试一下，我首先在需要读入的文件中某些行添加了'%s'

```python
def sed(typstr,restr,file1,file2):
    fin=open(file1,'r')
    fout=open(file2,'w')
    for line in fin:
        line=line%restr
        fout.write(line)
    fin.close()
    fout.close()
sed('%s','zhao','a.txt','g.txt')
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-60-c745fd95f732> in <module>
     10 #     except:
     11 #         print('Something went wrong')
---> 12 sed('m','zhao','a.txt','g.txt')

<ipython-input-60-c745fd95f732> in sed(typstr, restr, file1, file2)
      4     fout=open(file2,'w')
      5     for line in fin:
----> 6         line=line%restr
      7         fout.write(line)
      8     fin.close()

TypeError: not all arguments converted during string formatting
```

这个错误表明前面%和后面的参数数量不对应，我检查了下文件a.txt，发现原因是有些行加入了一个'%s'，有些行是没有的，这就表明如果一行中格式操作符和后面的替换字符数量不一样就报错，所以我在每一行都加入了一个'%s'，然后就没有报错了。但是这里我突然想到一个问题，格式操作符的局限是不能替换别的内容，还得要求数量一致，文件内容大的话其实不好处理。所以我修改了函数第一个参数改为'm'，想看下能不能替换掉，发现还是替换掉文件中的'%s'，这也就是说明按照我目前的写法，sed函数第一个参数是无效的，因为有格式操作符的原因，直接替换了文件中的格式操作符。

所以，我决定用之前学过的replace替换，然后把捕获异常try，except加上。

```python
def sed(typstr,restr,file1,file2):
    try:
        fin=open(file1,'r')
        fout=open(file2,'w')
        for line in fin:
            line=line.replace(typstr,restr) #用restr替换typstr
            fout.write(line)
        fin.close()
        fout.close()
    except:
        print('Something went wrong')
sed('m','zhao','a.txt','g.txt')
```

没有报错，检查了下g.txt发现文件中的m都被替换掉了，且不受数量限制。大功告成。

关于捕获异常的用法我需要讲一下，我其实刚开始写代码就把捕获异常这块内容写进去了，直接报错'Something went wrong'，捕获异常有好处，但是在练习时这个有点麻烦，我还得把这块代码去掉，然后再运行一遍才知道哪里出错了，所以在练习时可以先不用这个，我觉得在实际开发中有大量代码时这个报错可能让你找到哪里出错了，当然如果有可能出现无线递归或循环报错时，那个地方加捕获异常是非常好的。否则，**让自己尽量暴露在错误之中是成长的一个比较快的方式，发下错误就证明你要习得新知识点了。**



文件处理中有遇到一个管道问题，不过介绍不多，后续有时间再学习。