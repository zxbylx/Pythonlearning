# python自学日记24——数据结构与算法(8)

## 1.递归问题：汉诺塔

今天还是继续研究递归问题，汉诺塔如下图，规则小盘子不能在大盘子上面，目的是在三个柱子之间来回换直到把所有盘子移动到另一根柱子上。

![点击查看源网页](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1572795960611&di=28b6899959fd9961a6cf65996abc52aa&imgtype=0&src=http%3A%2F%2Fpic4.58cdn.com.cn%2Fzhuanzh%2Fn_v2bce81a882de74ce1b3aff979f137d8d9.jpg%3Fw%3D750%26h%3D0)

递归的思路是先找到基本情况，只有一个的时候，从A直接移动到B即可，两个时先把一个移动到C,然后把底部的移动到B，再把C上的移动到B即可。这就是基本情况

- 先借助B将高度为height-1的盘子移动到C
- 然后将最后一个盘子移动到B
- 借助A将高度为height-1的盘子移动到终点柱子。

```python
def moveTower(height,fromPole,toPole,withPole):
    if height>=1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)#需要注意这个函数的位置
        moveTower(height-1,withPole,toPole,fromPole)
#         moveDisk(fromPole,toPole)#本来想测试下这个位置看看行不行，但发现结果是错的
def moveDisk(fp,tp):
    print('move disk from %s to %s\n'%(fp,tp))
moveTower(2,'A','B','C')
```

返回值：

```
move disk from A to C

move disk from A to B

move disk from C to B

```

递归确实从表面上看比较不容易理解，我试着换了下打印的位置，就发现结果是不对的。我一直在想一个问题，看待递归问题到底需不需要把递归的所有过程想清楚了，一直想把这个问题想明白，但是很多递归问题自己确实很难把递归的每一步具体是怎么变化的难梳理清楚。也许应该注重的是递归的思路，而不是递归的过程。

## 2.动态规划：用递归解决找零钱问题

随机说出一个钱数，如何用最少的硬币来找零。目前国内硬币有1角，5角和1元。如果是3.7元，那么最少的是6个，3个1元，1个5角，2个1角。

最少的情况是一枚硬币，即找零的金额在1角、5角和1元之间。如果不在这个范围内择优多种选择：1枚1角的硬币机加上找零金额减去1角后所需的硬币；1枚5角的硬币加上找零金额减去5角后的所需硬币；1枚1元的硬币加上找零金额减去1元后所需的硬币。

```python
def recMC(coinValueList,change):
    minCoins=change #先定义一个最大的硬币数
    if change in coinValueList: #如果找零金额在硬币列表中
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:#这里没有直接用for i in coinValueList是为了刨除比找零金额大的硬币
            numCoins=1+recMC(coinValueList,change-i)
            if numCoins<minCoins:
                minCoins=numCoins
        return minCoins
recMC([1,5,10],63) #以1角为基准
```

这个递归能解决问题，但是效率很低，因为会出现重复情况。调用递归的次数过多，需要把重复的情况去掉。减少计算量的关键在于记住已有的结果。

```python
def recDC(coinValueList,change,knownResults):#定义的是大写的K，下面是小写
    minCoins=change
    if change in coinValueList:
        knownResults[change]=1
        return 1
    elif knownResults[change]>0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <=change]:
            numCoin=1+recDC(coinValueList,change-i,knownResults)
            if numCoins<minCoins:
                minCoins=numCoins
                knownResults[change]=minCoins
    return minCoins
recDC([1,5,10],63,[0]*63)
```

这里传入三个参数，第三个参数是个列表，为了记录已有的结果。关键点我刚开始不理解的是elif这一段，我刚开始想既然上面已经判断过找零在硬币列表里了，那么knownResults[change]>0的情况不是重复了嘛，除了等于1还能等于什么。这里就又忘记了递归调用的问题，每次调用参数不一样，虽然最开始的不可能出现大于0的情况了，但是在后面减掉某个硬币时就有可能出现了。所以我刚开始去掉了elif这一段，发现和上面一样变得很慢了。这段才是为了记住结果而存在的判断。

但是这个而有一个问题，那就是会报错：list index out of change.原因是第三个参数列表长度如果和change金额一样，那么列表下标旧的改成change-1或者将第三个参数再加上1即可，比change数大1位。

```python
def recDC(coinValueList,change,knownResults):
    minCoins=change
    if change in coinValueList:
        knownResults[change]=1
        return 1
    elif knownResults[change]>0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <=change]:
            numCoins=1+recDC(coinValueList,change-i,knownResults)
            if numCoins<minCoins:
                minCoins=numCoins
                knownResults[change]=minCoins
#     print(knownResults)
    return minCoins
recDC([1,5,10],63,[0]*64)
```

这个是通过记住结果来解决找零问题，下面是动态规划解决找零问题：动态规划算法会从1角找零开始，然后系统的一直计算到所需的找零金额。这样做可以保证在每一步都已经知道任何小于当前值的找零金额所需要的最少硬币数。

```python
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount=cents
        newCoin=1
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
                newCoin=j
        minCoins[cents]=coinCount #记录每一个零钱所需要的最少硬币数
        coinsUsed[cents]=newCoin #记录这个零钱最后一个硬币的金额
    return minCoins[change]#返回所需最少硬币数量
def printCoins(coinsUsed,change):#记录需要的是哪几个硬币
    coin=change
    while coin>0:
        thisCoin=coinsUsed[coin]
        print(thisCoin)
        coin=coin-thisCoin
```

```python
c1=[1,5,10,21,25]
coinsUsed=[0]*64
coinCount=[0]*64
dpMakeChange(c1,63,coinCount,coinsUsed)
printCoins(coinsUsed,63)
```

返回值是：21,21,21

如果打印coinsUsed，会打印出每个零钱对应的所需硬币的数量。这里有个需要说的是，打印的是每个零钱对应位置显示的最后一个硬币。