# python自学日记17——数据结构和算法(1)

## 1.解压可迭代对象赋值给多个变量

如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

python的星号表达式可以解决这个问题：

```python
def drop_fisrt_last(grades):
    first,*middle,last=grades
    return avg(middle)
grades=[12,21,21,34,23,45,65,76,45,345,645,45,34,3,56,456,76,5,45,34,7,55,656,34,55,5,345,45,345,65]
drop_fisrt_last(grades)
```

```
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-15-e57a599665f6> in <module>
      6     return avg(middle)
      7 grades=[12,21,21,34,23,45,65,76,45,345,645,45,34,3,56,456,76,5,45,34,7,55,656,34,55,5,345,45,345,65]
----> 8 drop_fisrt_last(grades)

<ipython-input-15-e57a599665f6> in drop_fisrt_last(grades)
      4 def drop_fisrt_last(grades):
      5     first,*middle,last=grades
----> 6     return avg(middle)
      7 grades=[12,21,21,34,23,45,65,76,45,345,645,45,34,3,56,456,76,5,45,34,7,55,656,34,55,5,345,45,345,65]
      8 drop_fisrt_last(grades)

NameError: name 'avg' is not defined
```

结果报错了，例子中的avg并没有提前做定义，所以才报NameError，这时我想求平均值函数应该import math模块就可以了，然后再前面输入上述代码发现math里并没有avg，还是报同样的错误，然后无去搜索了下这个错误发现avg函数需要自己先写出来，然后我就在想难道python没有自带的求平均值的内置函数吗？查到用numpy的mean可以，但是这个不适合求列表的平均值，后面在标准库里查到统计模块statistics里的mean可以，然后试了下确实可以

```python
from statistics import *
def drop_fisrt_last(grades):
    first,*middle,last=grades
    return mean(middle)
grades=[12,21,21,34,23,45,65,76,45,345,645,45,34,3,56,456,76,5,45,34,7,55,656,34,55,5,345,45,345,65]
drop_fisrt_last(grades)
```

另一种方法就是先自己定义一个avg函数

```python
def avg(x):
    return sum(x)/len(x)
def drop_fisrt_last(grades):
    first,*middle,last=grades
    return avg(middle)
grades=[12,21,21,34,23,45,65,76,45,345,645,45,34,3,56,456,76,5,45,34,7,55,656,34,55,5,345,45,345,65]
drop_fisrt_last(grades)
```



**阶段过渡的资料收集怪圈**

昨天算是一个入门阶段的结束，整理完了以前的出错情况（可以看python自学日记16——调试），每当到一个阶段结束和新的阶段开始的过度时期就会有点资料慌，想找各种资料，接下来想着继续学python的话就要从数据结构算法、web开发、数据科学等方向挑方向，这时总觉得自己手上的资料不够，其实每个方向都有书籍和视频，但是总是担心这些资料质量不够好，想着再多找一些。

于是今天下午去了图书馆，想再借几本书，如果实在找不到就从网上买几本，结果图书馆网上显示有的书到馆内怎么都找不到，不过还是带回来几本。心理稍微踏实一点，其实自己清楚，如果你确定能找到最优质的资料那你可以尽情的去找，如果不确定那就应该不要陷入资料收集怪圈里，导致最后收集了一大堆杂七杂八的资料最后哪一个也没有认真学完，其实挑一两个受到任何的资料从头到尾学完肯定比到处找资料东学一点西学一点效果好的。但理性有时候总是比不过感性。

今天也没好好好学，就看了一点，明天开始进入下一阶段，这个阶段就会多方向交替进行。

后面有时间把自己找的这些资料、网站、视频的链接整理一下，自己可能用不到这些，但是如果能给别人在学习python的道路上提供一些帮助也是很好的。