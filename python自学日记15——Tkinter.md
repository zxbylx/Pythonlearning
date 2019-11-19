# python自学日记15——Tkinter

调试建议：

GUI编程的挑战之一是哟啊记录哪些事情是在GUI正在构建时发生的，哪些事情是在之后用户行为的响应中发生的。

例如，当设置回调时，一个常见的错误是没有传入函数的引用，而是直接调用它：

```python
def the_callback():
    print('Called.')

g.bu(text='This is wrong!',command=the_callback())
```

如果运行这段代码，会发现它立即就调用了the_callback，然后才创建按钮。当你按下按钮时，什么都不会发生。因为the_callback的返回值是None（print虽然打印了值，但这不是返回值，这里需要注意，return才有返回值）。通常不应该在设置GUI时调用一个回调函数，它只应该在之后响应用户事件时被调用。

修改上面代码不在运行时就调用，改为响应用户事件时调用，需要把the_callback后面的()给去掉

```python
def the_callback():
    print('Called.')

g.bu(text='This is wrong!',command=the_callback)#去掉括号后就变成了响应事件后调用
```



GUI编程的另一个挑战是你无法控制程序执行的流程。程序中那部分会被先执行，完全由用户决定，这意味着你需要设计程序以能够正确处理任意顺序的事件。

例如下面练习

创建一个画布和按钮。当用户按下按钮时，它应在画布上绘制一个圆；添加一个输入框和按钮，按下第二个按钮，读取输入框中的一个颜色名称，并使用哪个颜色填充圆圈，需要处理未创建圆用户修改颜色的情况

我刚开始写的是这样

```python
from swampy.Gui import *
b=Gui()
b.title('19-2')
def make_circle():
    global item #忽略应该把函数内的变量改成全局变量
    item=canvas.circle([50,50],100,fill='red')
def change_color():
    item.config(fill=entry.get())
canvas=b.ca(width=500,height=500)
canvas.config(bg='white')
button=b.bu(text='画圆',command=make_circle)
entry=b.en()

button2=b.bu(text='改变颜色',command=change_color)
b.mainloop()
```

刚开始还没有把item定义成全局变量，导致执行第二步修改颜色时就报错，这其实有点忘了，对局部变量和全局变量没有形成这个意识，后面改成全局变量后正常流程是没事了，但是如果用户在没有创建圆时就点击改变颜色的按钮还是会报错，所以针对各种不同的情况都需要做处理，所以需要做一个判断

```python
b=Gui()
b.title('19-3')
canvas=b.ca(width=500,height=500,bg='white')
circle=None #先定义圆时None
def callback1():
    global circle
    circle=canvas.circle([0,0],100)
def callback2():
    if circle==None: #在没有创建圆点击改变颜色按钮什么也不返回
        return
    color=entry.get()
    circle.config(fill=color)

button1=b.bu('画圆',command=callback1)
button2=b.bu('改变颜色',command=callback2)
entry=b.en()
b.mainloop()
```

增加这一步判断就少了报错的情况，本来还应该针对用户填写颜色单词出错时进行异常捕捉，但是报错类型“_tkinter.TclError”这种以前也没遇到过，不知道怎么写，后面知道了之后再说。



当部件的树木增加后考虑所有可能的时间序列就变得更加困难。管理这种复杂度的办法之一就是将系统的状态封装为一个对象并考虑以下问题，首先要搞清楚什么是状态，什么是事件，事件伴随着用户的行为，事件分割不同的状态：

1. 有哪些可能的状态，在上面的圆圈的例子中，我们可以考虑两个状态，用户创建一个圆圈前和后。
2. 在每个状态中可能发生哪些事件，在这个例子中，用户可以按下任何一个按钮，或者退出。
3. 对每个状态-事件对，期望的输出是什么？因为有两个状态和两个按钮，因此有四个状态-事件对需要考虑
4. 由什么导致一个状态到另一个状态？在这个例子中，当用户创建第一个圆圈时，状态转换。

定义并检验一些在任何事件序列下都保持的不变量会很有用。