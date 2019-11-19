# python自学日记26——二叉树（中序遍历去括号）

## 1.解析树：中序遍历法去括号

将数学表达式表示成解析树

```python
from pythonds.basic import Stack
from pythonds.trees import BinaryTree

def buildParseTree(fpexp):
    fplist=fpexp.split()
    pStack=Stack()
    eTree=BinaryTree('')
    pStack.push(eTree)
    currentTree=eTree
    for i in fplist:
        if i=='(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree=currentTree.getLeftChild()
        elif i not in '+-*/)':
            currentTree.setRootVal(eval(i))
            parent=pStack.pop()
            currentTree=parent
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree=currentTree.getRightChild()
        elif i==')':
            currentTree=pStack.pop()
        else:
            raise ValueError('Unknown Operator:'+i)
    return eTree
parseTree=buildParseTree('( 3 + ( 4 * 5 ) )')
```

这个没什么问题，主要想记录的是后面的中序遍历法：

```python
def inorder(tree):
    if tree!=None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
inorder(parseTree)
```

这个将返回的是

3

+

4

*

5

修改上述使得能还原完全括号表达式

```python
def printexp(tree):
    sVal=''
    if tree:
        sVal='('+printexp(tree.getLeftChild())
        sVal=sVal+str(tree.getRootVal())
        sVal=sVal+printexp(tree.getRightChild())+')'
    return sVal
printexp(parseTree)
```

返回值：'((3)+((4)*(5)))'，这里面不必要的括号太多了，想着如何去掉，在添加左括号时想着如果没有右子树，那么就不用加括号，添加右括号时如果没有左括号就不用了

```python
def printexp(tree):
    sVal=''
    if tree:
        if tree.getRightChild()!=None:
            sVal='('+printexp(tree.getLeftChild())
        else:
            sVal=printexp(tree.getLeftChild())
        sVal=sVal+str(tree.getRootVal())
        if tree.getLeftChild()!=None:
            sVal=sVal+printexp(tree.getRightChild())+')'
        else:
            sVal=sVal+printexp(tree.getRightChild)
    return sVal
printexp(parseTree)
```

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-51-41c5c2f524fd> in <module>
     13             sVal=sVal+printexp(tree.getRightChild)
     14     return sVal
---> 15 printexp(parseTree)

<ipython-input-51-41c5c2f524fd> in printexp(tree)
      4     if tree:
      5         if tree.getRightChild()!=None:
----> 6             sVal='('+printexp(tree.getLeftChild())
      7         else:
      8             sVal=printexp(tree.getLeftChild())

<ipython-input-51-41c5c2f524fd> in printexp(tree)
     11             sVal=sVal+printexp(tree.getRightChild())+')'
     12         else:
---> 13             sVal=sVal+printexp(tree.getRightChild)
     14     return sVal
     15 printexp(parseTree)

<ipython-input-51-41c5c2f524fd> in printexp(tree)
      3     sVal=''
      4     if tree:
----> 5         if tree.getRightChild()!=None:
      6             sVal='('+printexp(tree.getLeftChild())
      7         else:

AttributeError: 'function' object has no attribute 'getRightChild'
```

后面想要不从根节点开始判断：

```python
def printexp(tree):
    sVal=''
    if tree.getRightChild():
        sVal='('+printexp(tree.getLeftChild())
        sVal=sVal+str(tree.getRootVal())
        sVal=sVal+printexp(tree.getRightChild())+')'
    else:
        sVal=printexp(tree.getLeftChild())
        sVal=sVal+str(tree.getRootVal())
        sVal=sVal+printexp(tree.getRightChild())
    return sVal
printexp(parseTree)
```

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-64-83baf66c77ef> in <module>
     10         sVal=sVal+printexp(tree.getRightChild())
     11     return sVal
---> 12 printexp(parseTree)

<ipython-input-64-83baf66c77ef> in printexp(tree)
      2     sVal=''
      3     if tree.getRightChild():
----> 4         sVal='('+printexp(tree.getLeftChild())
      5         sVal=sVal+str(tree.getRootVal())
      6         sVal=sVal+printexp(tree.getRightChild())+')'

<ipython-input-64-83baf66c77ef> in printexp(tree)
      6         sVal=sVal+printexp(tree.getRightChild())+')'
      7     else:
----> 8         sVal=printexp(tree.getLeftChild())
      9         sVal=sVal+str(tree.getRootVal())
     10         sVal=sVal+printexp(tree.getRightChild())

<ipython-input-64-83baf66c77ef> in printexp(tree)
      1 def printexp(tree):
      2     sVal=''
----> 3     if tree.getRightChild():
      4         sVal='('+printexp(tree.getLeftChild())
      5         sVal=sVal+str(tree.getRootVal())

AttributeError: 'NoneType' object has no attribute 'getRightChild'
```

结果还是报错

```python
def printexp(tree):
    sVal=''
    if tree:
        if type(tree.getRightChild())!='NoneType':
            sVal='('+printexp(tree.getLeftChild())
        else:
            sVal=printexp(tree.getLeftChild())
        sVal=sVal+str(tree.getRootVal())
        if type(tree.getLeftChild())!='NoneType':
            sVal=sVal+printexp(tree.getRightChild())+')'
        else:
            sVal=sVal+printexp(tree.getRightChild)
    return sVal
printexp(parseTree)
```

如果子节点没有就不用加括号，然后返回的结果还是一样的'((3)*((4)+(5)))'，我看这段代码以为我添加括号的地方写错了位置，我其实都有点放弃这个问题了，想着以后如果能想出来再说，结果误打误撞发现了转机

```python
def printexp(tree):
    sVal=''
    if tree:
        if type(tree.getRightChild())!='NoneType':
            sVal=printexp(tree.getLeftChild())
        else:
            sVal='('+printexp(tree.getLeftChild())
        sVal=sVal+str(tree.getRootVal())
        if type(tree.getLeftChild())!='NoneType':
            sVal=sVal+printexp(tree.getRightChild())
        else:
            sVal=sVal+printexp(tree.getRightChild)+')'
    return sVal
printexp(parseTree)
```

将添加括号的位置放到else里来后发现返回值是3+4*5，我还以为成功了呢，结果将公式替换为

```python
parseTree=buildParseTree('( 3 * ( 4 + 5 ) )')
```

返回的结果是3*4+5，那么就说明代码还是有问题，然后又想应该是同时有左子树和右子树时才加括号，代码修改如下：

```python
def printexp(tree):
    sVal=''
    if tree:
        if str(type(tree.getLeftChild()))!='NoneType' and str(type(tree.getRightChild()))!='NoneType':
            sVal='('+printexp(tree.getLeftChild())
            sVal=sVal+str(tree.getRootVal())
            sVal=sVal+printexp(tree.getRightChild())+')'
        else:
            sVal=printexp(tree.getLeftChild())
            sVal=sVal+str(tree.getRootVal())
            sVal=sVal+printexp(tree.getRightChild())

    return sVal
printexp(parseTree)
```

因为type类型是NoneType，想着是不是需要改成字符串和后面的才有比较性，后来发现用str改后返回值是"`<class 'pythonds.trees.binaryTree.BinaryTree'>`"，还是不行。最后发现也许是自己想的过于复杂了，下午的思路还是影响自己，晚上过了这么久后发现好像换个思路应该可以

```python
def printexp(tree):
    sVal=''
    if tree:
        if tree.getLeftChild() and tree.getRightChild():
            sVal='('+printexp(tree.getLeftChild())
            sVal=sVal+str(tree.getRootVal())
            sVal=sVal+printexp(tree.getRightChild())+')'
        else:
            sVal=printexp(tree.getLeftChild())
            sVal=sVal+str(tree.getRootVal())
            sVal=sVal+printexp(tree.getRightChild())

    return sVal
printexp(parseTree)
```

返回值就正常了：（3*（4+5）），这样看确实如“python自学日记16——调试（常见错误）”中所说，遇到问题实在做不出来可以过段时间再想，也许就做出来了。

本来想把这个问题写出来问下大家的，结果自己写着写着就找到解决方案了。

## 2.cannot import name 'BinaryHeap' from 'pythonds.trees' 

这次说一个bug，在导入二叉堆的时候发现:

```python
from pythonds.trees import BinaryHeap
```

会报错：

```
ImportError:cannot import name 'BinaryHeap' from 'pythonds.trees' (D:\anaconda\lib\site-packages\pythonds\trees\__init__.py)
```

遇到这种错误第一想法就是搜索引擎查一下，发现没找到合适的答案，涉及导入模块一般要么pip 安装一下，但是这个跟以往的有点区别，以往都是报错没有xx模块，但是这个还给出了路径，我就想着去这个路径里看看，发现没有BinaryHeap,但是有BinHeap,看到这就明白是改版了，换成新的名称了。后面可以记住如果再遇到有提供路径的，可以去路径里查看下原因。