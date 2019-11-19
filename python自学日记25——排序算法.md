# python自学日记25——排序算法

## 1.冒泡排序

冒泡排序是比较相邻的元素，将不合顺序的交换。每一轮遍历都将下一个最大值放到正确的位置上。

```python
def bubbleSort(alist):

    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum): 
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
#             temp=alist[i]
#             alist[i]=alist[i+1]
#             alist[i+1]=temp
    return alist
bubbleSort([1,3,4,2,5])
```

这是正确的代码，两两替换这个可以从临时变量替换改成直接一行交替位置替换。我刚开始看这个代码不知道为什么用两个循环，觉得应该以一个也可以。所以就去掉了一个替换成下面的：

```python
def bubbleSort(alist):
    for i in range(len(alist)-1):
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum): #本来以为前两行没什么用，但替换掉以后发现我的代码只排了一次
#两次循环的意义在于进行多次排序
        if alist[i]>alist[i+1]:
            alist[i],alist[i+1]=alist[i+1],alist[i]

    return alist
bubbleSort([1,3,4,2,5])
```

输出结果是[1,3,2,4,5]，这样才看出为什么要用双循环，否则只遍历一遍。应该是要遍历n-1遍才行的。

冒泡排序通常被认为是效率最低的排序算法，因为交换次数太多。但对于只需要遍历几次的列表，冒泡排序可以根据一轮遍历中没有发生元素交换提前判定列表为有序并结束排序过程。

```python
def shortBubbleSort(alist):
    exchanges=True
    passnum=len(alist)-1
    while passnum>0 and exchanges:
        exchanges=False  #循环中先将交换设为False
        for i in range(passnum):
            if alist[i]>alist[i+1]: #只有出现前面比后面值大时才将交换改为True,否则退出循环
                exchanges=True
                alist[i],alist[i+1]=alist[i+1],alist[i]
        passnum=passnum-1
    return alist
shortBubbleSort([23,4,3,4,1,5])
```

## 2.快速排序

快速排序的思路就是从列表中任选一个值，然后将小于这个值的元素放在这个值的左边，大于这个值的元素放到这个值的右边。然后对左半部分和有半部分再进行递归调用。

听起来还是挺简单的，但是为什么代码看着那么复杂呢？

```python
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint=partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
def partition(alist,first,last):
    pivotvalue=alist[first] #取第一个值为基准值
    leftmark=first+1
    rightmark=last
    done=False
    while not done:
        while leftmark<=rightmark and alist[leftmark]<=pivotvalue:
            leftmark=leftmark+1
        while alist[rightmark]>=pivotvalue and rightmark>=leftmark:
            rightmark=rightmark-1
        if rightmark<leftmark:
            done=True
        else:
            temp=alist[leftmark]
            alist[leftmark]=alist[rightmark]
            alist[rightmark]=temp
    temp=alist[first]
    alist[first]=alist[rightmark]
    alist[rightmark]=temp
    return rightmark
b=[54,26,93,17,77,31,44,55,20]
quickSort(b)
print(b)
```

这个代码的方法是取第一个值为基准值，然后将剩余数从左右两边往中间遍历，左边遇到比基准值大的停住，右边遇到比基准值小的停住，然后交换这两个值的位置。然后再继续往中间遍历，直到右边值遍历到左边值左边时，那么此时右边值所在的位置和基准值对调。这时就完成了第一次分割。然后对左右两边列表进行递归调用。

看着就挺复杂的，我也见过另外一个讲快速排序的，易读易懂，就是不知道时间复杂度是不是一样。

```python
def quicksort(array):
    if len(array)<2:
        #base case,array with 0 or 1 element are already sorted
        return array
    else:
        #recursive case
        pivot=array[0]
        #sub-array of all the elements less than the pivot
        less=[i for i in array[1:] if i <=pivot]
        #sub-array of all the elements greater than the pivot
        greater=[i for i in array[1:] if i >pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
print(quicksort([2,5,1,4,3]))
```

这段代码读起来就很容易懂了。通过列表生成式和循环遍历，然后将左右两个列表放在基准值列表左右两侧。然后进行递归调用。

快速排序基准值选的好坏直接影响时间复杂度，如果每次都能使左右两边数量相等或差1，那么时间复杂度为：O(nlogn),如果每次都有一边没有元素，那么就会变成：
$$
O(n^2)
$$
加上递归的开销，比冒泡算法还差。

三数取中法，在列表头元素，中间元素与尾元素中取中间值。

```python
import numpy as np
def quicksort(array):
    if len(array)<2:
        #base case,array with 0 or 1 element are already sorted
        return array
    else:
        a=[array[0],array[-1],array[len(array)//2]]

        #recursive case
        pivot=np.median(a)
#         print(pivot)
        #sub-array of all the elements less than the pivot
        less=[i for i in array[1:] if i <=pivot]
        #sub-array of all the elements greater than the pivot
        greater=[i for i in array[1:] if i >pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
print(quicksort([2,5,1,4,3]))
```

刚开始我想取中值应该需要numpy，然后将这个写进去结果返回[1 , 2.0 , 3 , 3.0 , 4]，发现5没啦，还多了个3.0什么的。

然后用print语句打印了a和pivot，让我发现可能是因为如果array元素个数少于3个时会出现三个值有重复现象，会不会是这个问题，然后就添加判断：

```python
import numpy as np
def quicksort(array):
    if len(array)<2:
        #base case,array with 0 or 1 element are already sorted
        return array
    elif len(array)==2:
        pivot=array[0]
        less=[i for i in array[1:] if i <=pivot]
        #sub-array of all the elements greater than the pivot
        greater=[i for i in array[1:] if i >pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
    else:
        a=[array[0],array[-1],array[len(array)//2]]
        print(a)
        #recursive case
        pivot=np.median(a)
        print(pivot)
        #sub-array of all the elements less than the pivot
        less=[i for i in array[1:] if i <=pivot]
        #sub-array of all the elements greater than the pivot
        greater=[i for i in array[1:] if i >pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
print(quicksort([2,5,1,4,3]))
```

这次还是报错，感觉错的更离谱了

```
[2, 3, 1]
2.0
[5, 3, 4]
4.0
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-28-f433c447a382> in <module>
     21         greater=[i for i in array[1:] if i >pivot]
     22         quicksort(less)+[pivot]+quicksort(greater)
---> 23 print(quicksort([2,5,1,4,3]))

<ipython-input-28-f433c447a382> in quicksort(array)
     20         #sub-array of all the elements greater than the pivot
     21         greater=[i for i in array[1:] if i >pivot]
---> 22         quicksort(less)+[pivot]+quicksort(greater)
     23 print(quicksort([2,5,1,4,3]))

<ipython-input-28-f433c447a382> in quicksort(array)
     20         #sub-array of all the elements greater than the pivot
     21         greater=[i for i in array[1:] if i >pivot]
---> 22         quicksort(less)+[pivot]+quicksort(greater)
     23 print(quicksort([2,5,1,4,3]))

TypeError: unsupported operand type(s) for +: 'NoneType' and 'list'

```

后面想想如果少于3个又不是求平均值，不会改变数值大小，所以不是个数的问题。出现浮点数是不是浮点数的问题呢，然后又在求中值前加了int，结果还是不行。再仔细看代码发现逻辑问题出现在后面的代码上，如果中值是在中间值或者最后一个值时，遍历还是从array[1:]，这是按照选第一个值的逻辑，所以需要根据值的位置变化进行逻辑上的变化。

如果根据值的位置进行后面逻辑的变化发现代码会变得很复杂，我想过判断时将小于等于改为小于，遍历从array[1:]改为array[:]，但是这个有个问题如果出现多个相同值时会出现少数的情况。然后又开始想如果出现多个相同值怎么办。总之觉得越来越复杂，后面发现如果不改变后面逻辑转而去改变前面，将中值和首位的值进行替换，那么后面的内容就不需要改动了。

```python
def quicksort(array):
    if len(array)<2:
        #base case,array with 0 or 1 element are already sorted
        return array
    else:
        if array[0]>=array[len(array)//2] and array[len(array)//2]>=array[-1]:
            array[0],array[len(array)//2]=array[len(array)//2],array[0]
        elif array[-1]<=array[len(array)//2] and array[0]<=array[-1]:
            array[0],array[-1]=array[-1],array[0]
#         else:
#             array[0]=array[0]
        
        #recursive case
        pivot=array[0]
        #sub-array of all the elements less than the pivot
        less=[i for i in array[1:] if i <=pivot]
        #sub-array of all the elements greater than the pivot
        greater=[i for i in array[1:] if i >pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
print(quicksort([2,5,1,7,4,3,6]))
```

这样，如果中值在中间或者尾部，那么都和首位的值进行替换就解决了。