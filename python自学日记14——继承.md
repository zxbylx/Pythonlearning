# python自学日记14——继承（扑克牌）

随时提醒自己是否抓住了问题的关键对于解决问题的有很大的帮助。

## 1.用类来定义一副扑克牌

本次定义扑克牌排除大小王，只针对其他的52张牌，共有4个花色，每种花色13张。如果我们想定义一个新对象来表示卡牌，则其属性显然应该是rank(大小)和suit(花色)。但属性值就不那么直观了。我们模仿Unicode给字母、汉字等字符通过数字编码的形式使用证书来给大小和花色编码。

花色编码：

草花：0，方片：1，红桃：2，黑桃：3

数字编码：

按数字来一一对应，其中：Jack:11,Queen:12,King:13

```python
class Card(object):
    '''Represents a standard playing card.'''
    def __init__(self,suit=0,rank=2):
        self.suit=suit
        self.rank=rank
    #为了将Card对象打印成人们阅读的形式，需要将整数编码映射成对应的大小和花色
    #rank_names的第一个元素是None，因为没有大小为0的牌，让None占据一个位置就可以使编码数字和卡牌大小对应是更整齐一点，例如下标2到字符串'2'这样。
    suit_names=['Clubs','Diamonds','Hearts','Spades']
    rank_names=[None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    #__str__在打印时将编码和卡牌一一对应起来
    def __str__(self):
        return '%s of %s'%(Card.rank_names[self.rank],Card.suit_names[self.suit])
```

对比卡牌：比较大小时内置有比较操作符(<,>,=等)，但是对于我们定义的类型来说，不能直接比较，需要用到“python自学日记13——类和方法”中的重载操作符来实现。

例子中介绍的是用`__cmp__`接收两个形参，self和other，当第一个对象大的时候返回正数，第二个大时返回负数，相等时返回0.

卡牌比较涉及两个属性大小和花色，我们决定花色大于大小，剩下的按照编码大小来比较。

```python
class Card(object):
    ... #表示上面有代码省略
    def __str__(self):
        return '%s of %s'%(Card.rank_names[self.rank],Card.suit_names[self.suit])
    def __cmp__(self,other):
        #检查花色
        if self.suit>other.suit:
            return 1
        if self.suit<other.suit:
            return -1
        
        #花色相同，检查大小
        if self.rank>other.rank:
            return 1
        if self.rank<other.rank:
            return -1
        
        #大小相同，平局
        return 0
```

按照这个代码当我们比较两个卡牌时

```python
queen_of_diamonds=Card(1,12)
card1=Card(2,11)
print(card1)
#对比卡牌
queen_of_diamonds.__cmp__(card1)
```

返回值时正常的，例子中还提出用内置函数cmp对卡牌进行比较，但尝试了一下发现不行，通过网上查询发现cmp在python3中被取消了，不过找到了替代模块operator，但是发现这个将比较拆的更细了，无法很简单的实现上述同时比较大、小和等于的情况，就暂时没替换。但是这个确实为下面的练习埋下了问题。

## 2.定义牌组

通过上面对卡牌的定义，我们接下来利用card属性创建牌组，首先创建牌组Deck：

```python
import random
class Deck(object):
    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(1,14): #从1开始是为了排除None字符
                card=Card(suit,rank)
                self.cards.append(card)
    #打印牌组
    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card)) #str会对每个卡牌对象调用__str__方法并返回字符串表达形式
        return '\n'.join(res)
    #发牌
    def pop_card(self):
        return self.cards.pop() #pop每次从列表最后删除一个值并返回这个值
    #添加一个卡牌
    def add_card(self,card):
        self.cards.append(card)
    #洗牌，random.shuffle将序列随机打乱顺序
    def shuffle(self):
        random.shuffle(self.cards)
```

我们使用嵌套循环，外层0到3是遍历花色，内层循环从1到13遍历卡牌大小，每次迭代使用当前花色和大小创建一个卡牌并添加到self.cards列表中。

后面还涉及了发牌、添加牌、洗牌等过程，这些都直接在上述代码中呈现。

```python
deck=Deck()
print(deck)
deck.shuffle()
print(deck)
```

通过上述代码已经将卡牌顺序打乱。

## 3.编写一个Deck的方法sort,使用列表方法sort对一个Deck中的卡牌进行排序。

刚开始我想的比较简单，就是定义一个sort方法，然后用sort()就可以了

```python
class Deck(object):
    ...
    def shuffle(self):
        random.shuffle(self.cards)
    #使用sort对Deck中的卡牌进行排序
    def sort(self):
        self.cards.sort()
```

然后验证下结果

```python
deck.sort()
print(deck)
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-8232c32b8e57> in <module>
----> 1 deck.sort()
      2 print(deck)

<ipython-input-6-827beb81f51a> in sort(self)
     28     #练习：编写一个Deck方法sort，使用列表方法sort来对一个Deck中的卡牌进行排序
     29     def sort(self):
---> 30         self.cards.sort()

TypeError: '<' not supported between instances of 'Card' and 'Card'
```

报错显示Card对象不支持'<'，我刚开始想我不是已经使用了重载操作符了嘛，应该不会出现这种情况，想着可能是sort默认的降序排序没有使用重载操作符方法，是不是可以将`__cmp__`作为参数传入sort()方法里，然后查了下sort内的参数性质，然后试了下，不行，我想是不是没带上Card对象，带上`Card.__cmp__`试了下还是不行，那我想的是既然这样就不用sort好了

我后面用了快速排序算法，但是报错结果和最开始的差不多也是'<'不适用列表类型之类的，然后想想要不用cmp在python3中的替代方法吧，上网查了下operator，`__lt__`对应小于，既然上面一直报错'<'不适用，那用lt试一下看看

```python
class Card(object):
    ... #表示上面有代码省略
    def __str__(self):
        return '%s of %s'%(Card.rank_names[self.rank],Card.suit_names[self.suit])
    def __lt__(self,other):#用__lt__替换__cmp__
        #检查花色
        if self.suit>other.suit:
            return 1
        if self.suit<other.suit:
            return -1
        
        #花色相同，检查大小
        if self.rank>other.rank:
            return 1
        if self.rank<other.rank:
            return -1
        
        #大小相同，平局
        return 0
```

运行结果倒是不报错了，也打印了52张牌，但是并没有按照顺序排列。不过这算是一个好兆头，说明离结果更近了，然后来来回回替换了好几次发现都不行，有点崩溃了，用搜索引擎先搜了sort的用法，然后搜了“重载操作符+排序”，各种未果之后，决定还是直接找网上看看有么有人做过这个问题的，先通过百度搜了下练习答案，没有；然后通过谷歌搜，倒是搜到GitHub上有书中其他章节的答案了，但是没有这个的，然后在GitHub上搜英文书名找到了答案，发现结果离我确实比较近了，我用`__lt__`替换了`__cmp__`，但是没有修改下面的代码，修改了下面代码就可以了

```python
class Card(object):
    ... #表示上面有代码省略
    def __str__(self):
        return '%s of %s'%(Card.rank_names[self.rank],Card.suit_names[self.suit])
    def __lt__(self, other):
        """Compares this card to other, first by suit, then rank.
        returns: boolean
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
```

分别将卡牌转变成元组，然后进行比较。

为了解决这个问题我试了很多方法也浪费了很多的时间，发现其实刚开始思路是对的，但是一直没做出来并且浪费很多时间的原因是没有抓住问题的本质以及对知识点sort排序和重载操作符也没有完全掌握。

其实这个问题最开始报的错是最关键的，但是我没有重视起来，我用快速排序算法替换sort还是报同样的错误是因为排序的关键就是能比较大小，否则就无法排序，所以能否比较大小就是问题的关键，剩下的就是如何通过重载操作符来实现比较大小，`__cmp__`已经在python3中取消了，不过正常情况下取消一个必然会有替代方案，只需要好好研究这个替代方案即可，我最后是用替代方案试过，但是只改了头，没有该其他代码，应该把替代的例子好好研究下，看看替代的方法是如何使用的方能解决这个问题。

当然花费很多时间并不是完全没有用，这个问题让我对重载操作符和sort排序的理解更深入了，而且知道解决一个问题就要抓住问题的核心，使用搜索引擎时记得百度、谷歌、必应等都试一遍，在python2还没有完全停止使用时注意python2和python3的区别。

## 4.继承：是一种能够定义一个新类对现有某个类稍作修改的语言特性

新建一个子类表示一副“手牌”

```python
class Hand(Deck):
    '''Represents a hand of playing cards'''
    def __init__(self,label=''):
        self.cards=[]
        self.label=label
      #这是move_cards在子类里的测试，表示在父类和子类中都适用
#     def move_cards(self,deck,num):
#         for i in range(num):
#             self.add_card(deck.pop_card())
```

我们可以用pop_card和add_card来出牌，并将这个封装成一个方法move_cards到Deck里，下面是Deck的最终版本

```python
import random
#定义牌组
class Deck(object):
    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(1,14):
                card=Card(suit,rank)
                self.cards.append(card)
    
    #打印牌组
    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    #发牌
    def pop_card(self):
        return self.cards.pop()
    #添加一个卡牌
    def add_card(self,card):
        self.cards.append(card)
    #洗牌，random.shuffle将序列随机打乱顺序
    def shuffle(self):
        random.shuffle(self.cards)
    #练习：编写一个Deck方法sort，使用列表方法sort来对一个Deck中的卡牌进行排序
    def sort(self):
        self.cards.sort()
    #将继承后面代码封装起来成为一个方法move_cards，放到Deck中
    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())
    #练习：编写一个Deck方法deal_hand，接受两个形参，手牌的数量和每副手牌的牌数。它会根据形参创建新的Hand对象，按照每副手牌的拍数出牌，并返回一个Hand对象的列表
    def deal_hands(self,num_hand,num_card):
        hand_list=[]
        for i in range(num_hand):
            hand_i=Hand()
            self.move_cards(hand_i,num_card)
            hand_list.append(hand_i)
            print(hand_i)
        return hand_list
```

## 5.下面是扑克牌中可能的手牌，按照牌值大小增序排列。

对子、两对、三条、顺子、同花（五张花色一样）、满堂红（三张牌大小相同，另外两张相同）、四条（四张牌大小相同）、同花顺。

添加方法has_pair,has_twopair等，他们根据手牌是否达到相对应的条件来返回True或False,代码需对任意数量的手牌都适用

编写一个函数classify(分类)，它可以弄清楚一副手牌中最大的组合，并设置label属性。

编写一个函数，对一副手牌洗牌，将其分成不同手牌，对手牌进行分类，并记录每种分类出现的次数。

打印各种分类及它们的概率。

由于涉及了类很多东西不想重复写了，这次就全写到一起了，在写顺子时有点不知道怎么写，也是纠结时间比较久的，这个值得记录一下写顺子的方法，后面应该用得到。

```python
class PokerHand(Hand):
    #按照从最大同花顺到对子降序写这个列表，当classify方法识别出一个就直接返回，就可以解决返回最大的组合问题了
    all_labels=['straight_flush','four_of_a_kind','fullhouse','flush','straight','twopair','pair']

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    #练习：添加判断手牌中是否有对子的方法
    def rank_hist(self):#需要先将卡牌按照大小计数
        self.ranks={}
        for card in self.cards:
            self.ranks[card.rank]=self.ranks.get(card.rank,0)+1
    def has_pair(self):
        '''Return True if the hand has a pair,False otherwise'''
        self.rank_hist()
        for val in self.ranks.values():
            if val>=2:
                return True
        return False
    #添加判断手牌中是否有两个对子的方法
    def has_twopair(self):
        self.rank_hist()
        count=0
        for val in self.ranks.values():
            if val==2:
                count+=1
            if val==4:
                count+=2
        if count>=2:
            return True
        return False
    #添加判断手牌中是否有满堂红的方法（针对5张牌）
    def has_fullhouse(self):
        self.rank_hist()
        if len(self.ranks)!=2:
            return False
        for val in self.ranks.values():
            if val==3 or val==2:
                return True
            return False
    #添加判断手牌中是否有四条的方法
    def has_four_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val==4:
                return True
        return False
    #添加判断手牌中是否有顺子的方法
    def has_straight(self):
        self.rank_hist()
        ranks=self.ranks.copy()
        ranks[14]=ranks.get(1,0)
        
        return self.in_a_row(ranks,5)
    def in_a_row(self,ranks,n):
        count=0
        for i in range(1,15):
            if ranks.get(i,0):
                count+=1
                if count==5:
                    return True
            else:
                count=0
        return False
    
    #添加判断手牌中是否有同花顺的方法
    def has_straight_flush(self):
        self.rank_hist()
        self.suit_hist()
        if self.has_flush() and self.has_straight():
            return True
        return False
    #练习：编写一个函数classify(分类)，它可以弄清楚一副手牌中出现的最大的组合，并设置label属性
    def classify(self):
        self.rank_hist()
        self.suit_hist()
        self.labels=[]
        for label in PokerHand.all_labels:
            f=getattr(self,'has_'+label)
            if f():
                self.labels.append(label)
                return self.labels[0] #从列表中识别出来的第一个组合就返回，那么就返回的肯定是最大的组合了

if __name__ == '__main__':
    # make a deck
#     deck = Deck()
#     deck.shuffle()

#     # deal the cards and classify the hands
#     for i in range(7):
#         hand = PokerHand()
#         deck.move_cards(hand, 7)
# #         hand.sort()
# #         print(hand)
# #         print(hand.has_flush())
# #         print(hand.has_pair())
# #         print(hand.has_twopair())
# #         print(hand.has_fullhouse())
# #         print(hand.has_four_of_a_kind())
# #         print(hand.has_straight())
# #         print(hand.has_straight_flush())
#         print(hand.classify())
#         print('')
    t=[]
    n=1000
    for i in range(n):
        
        deck=Deck()
        deck.shuffle()
        
        for j in range(10):
            hand=PokerHand()
            deck.move_cards(hand,5)
            t.append(hand.classify())
#     return t
    times={}
    for s in t:
        times[s]=times.get(s,0)+1
#     return times
    for key,val in times.items():
        val='%.2f%%'%(float(val/(n*10))*100)
        print(key,val)
#             print(hand.classify())
#             print('')
```

