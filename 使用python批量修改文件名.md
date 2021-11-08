# 使用python批量修改文件名

在工作中有时候会遇到多个文件名格式不对的情况，需要一一修改，例如从test1.py，test2.py，...，testn.py改为test_1.py，test_2.py，...，test_n.py的情况，如果文件数量少手动改改就算了，但是文件多的话，就不想手动改了，我现在本着重复的事情尽量用代码实现，就想着肯定可以通过python来批量修改的，然后就开始分析：

1. 要批量修改文件名，首先得获取所有的文件名
2. 批量替换少部分文件名需要把想要的部分提取出来，然后拼接成新的文件名
3. 实行文件名替换

按照这3步，首先要获取所有的文件名，用到os.listdir()方法，不传参数是获取当前文件路径下的所有文件和文件夹列表

```python
import os

print(os.listdir())

```

输出结果：

```
D:\GitHub\auto-repeat\.venv\Scripts\python.exe D:/GitHub/auto-repeat/replace_filename/main.py
['main.py', 'test1.py', 'test2.py', 'test3.py', '__init__.py']
```

本来我想的操作是通过for循环提出出带test的文件，然后通过“.”把testn和后面的py分开，然后用切片把test和后面的数字分开，最后再通过拼接字符的形式改为test_n.py的新文件名形式，但是今天写的时候突然想到另一个方法，那就是用想要替换的字符把文件名切开，然后通过用join方法用替换后的字符“test_n”将切开的列表拼接起来，这样比较简单

```python
import os

print(os.listdir())
file_list = os.listdir()
for file in file_list:
    if 'test' in file:
        print(file.split('test'))
        new_file = 'test_'.join(file.split('test'))
        print(new_file)
```

输出结果：

```
D:\GitHub\auto-repeat\.venv\Scripts\python.exe D:/GitHub/auto-repeat/replace_filename/main.py
['main.py', 'test1.py', 'test2.py', 'test3.py', '__init__.py']
['', '1.py']
test_1.py
['', '2.py']
test_2.py
['', '3.py']
test_3.py

Process finished with exit code 0
```

可以看到替换后的文件名已经被赋值到new_file变量了，剩余最后一步就是替换文件名，用os.rename()方法将旧文件名和新文件名作为参数传递进去就可以了。

最终代码如下：

```python
import os

# 获取当前文件夹下的所有文件和文件夹列表
file_list = os.listdir()
for file in file_list:
    if 'test' in file:
        # 用test_替换test
        new_file = 'test_'.join(file.split('test'))
        # 文件名替换
        os.rename(file, new_file)
```

### 扩展：

有时修改还需要筛选只修改文件

就用到os.path.isfile(file)

还有可能需要判断文件后缀

file.endswith('.py')

