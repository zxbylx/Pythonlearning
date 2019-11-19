# Python自学日记30——1000行代码入门JavaScript

发现真的如学习外语一样，只有在学习第二种语言的时候你的母语才会更进一步。就像学JavaScript时看到两个问题：

如果在定义变量时不指定数据类型它要怎么知道数据的类型？

看到定义变量时一次了解了Python、C和JavaScript三种语言定义变量的方式，C是需要指定数据类型的，Python和JavaScript是不需要的。设定数据的值时，即已自动暗示了数据类型。例如，如果变量值为17，它的类型就是数字，如果改成“sixteen”这个变量类型就自动转换为字符串。

既然Python和JavaScript能自动处理数据类型，为什么还需要学习数据类型的相关内容呢？

因为现实中有很多无法依赖自动处理类型的情况。假设有个数字存储为文本类型，你突然想把这个数字用于数学运算，这时就需要把文本转换为数字类型；还有在alert里列出数字，数据类型也同样需要先转换为文本。

记录要点：

1. JavaScript不允许读/写用户硬盘上的文件
2. JavaScript的交互性完全发生在浏览器里，不需要载入新页面，因而减低了数据与服务器间非必要的来回传送。
3. JavaScript中定义变量前需要用var，定义常量用const，Python中不需要在定义变量前加关键字，Python也无法定义常量。目前主要是用全部大写约定俗成的表示常量，但是还是可以改的。后来Python通过自定义常量类来实现定义常量。
4. 创建常量时必须初始化，也就是为其赋值；
5. NaN表示非数字，也用于支出某段数据不是数字（当它期待中应当是数字时）。

以下代码需分段，基本上我都将不同部分用行隔开了：

```javascript
<script>
        // 1.变量基础
        prompt('请输入你的年龄'); //输入框
        alert('计算的结果是'); //警示框
        console.log('我是程序员能看到的'); //浏览器控制台打印输出信息

        var age;
        age = 18;
        console.log(age)

        var myname = 'zhao';
        console.log(myname);

        var myname = 'zhaoxinbo';
        var address = '火影村';
        var age = 18;
        console.log(myname, address, age);

        var myname = prompt('请输入你的名字');
        alert('您的名字是' + myname);

        var age = 18,
            address = '火影村',
            name = 'he咯'; //一次声明多个变量用逗号隔开

        var sex;
        console.log(sex); //显示undefined，因为程序不知道声明了什么默认undefined

        var apple1 = '青苹果',
            apple2 = '红苹果';
        var temp;
        temp = apple1;
        apple1 = apple2;
        apple2 = temp;
        // 无法使用apple1,apple2=apple2,apple1;这种在Python中直接可以替换的语句
        console.log(apple1)
        console.log(apple2)



        // 2.数据类型
        var num = 10; //num就是数字型，根据后面赋值来决定前面变量的类型
        var num1 = 010; //八进制 0-7 数字前面加0表示八进制
        console.log(num1); //程序显示默认转换为十进制，显示8
        var num2 = 0x23; //0x表示十六进制
        console.log(num2);
        console.log(Number.MAX_VALUE); //数字型的最大值
        console.log(Number.MAX_VALUE * 2); //Infinity无穷大
        console.log(-Number.MAX_VALUE * 2); //-Infinity无穷小
        console.log(Number.MIN_VALUE); //数字型的最小值
        console.log('sdf' - 3); //NaN在预期是数字但并不是数字时显示，非数字

        console.log(isNaN(12)); //isNaN判断是否为非数字

        var str1 = "hello,my'dfds'd/naffa" //转译用反斜杠\
        var str1 = "hello,my'dfds'd\naffa" //转译用反斜杠\
        console.log(str1);

        var str = 'my name is andy';
        console.log(str.length); //length字符串长度

        console.log('hello' + 18); //字符串拼接，只要其中有一个字符串，+号都表示字符串拼接，无论后面是字符串、数字或布尔型
        console.log('hello' + true);
        console.log('hello' + 'true');

        var age = prompt('请输入您的年龄');
        alert('您的年龄是' + age + '岁！');

        var flag = true;
        var flag1 = false;
        console.log(flag + 1); //true参与加法当1来看
        console.log(flag1 + 1); //false参与加法当0来看

        var num = 19;
        console.log(typeof(num)); //typeof判断数据类型并返回数据类型值
        console.log(typeof num); //两种方式貌似都行，那用下面的吧

        var num = 1;
        console.log(num.toString()); //转换为字符串
        console.log(typeof num.toString());
        console.log(String(num)); //转换为字符串
        console.log(typeof String(num));
        console.log(num + ''); //直接用加号和空字符串，就直接转换为字符串，字符串拼接法

        var age = prompt('请输入您的年龄'); //prompt获取值是字符串类型
        console.log(parseInt(age)); //parseInt()转换为整型，舍去小数
        console.log(parseInt('3.94'));
        console.log(parseInt('120px'));
        console.log(parseInt('rem120px')); //第一个不是数字则返回NaN
        console.log(parseFloat('3.14')); //parseFloat转换为浮点型
        console.log(Number('23')); //返回23
        console.log(Number('23.3')); //返回23.3
        console.log(Number('23.3px')); //无法去掉px返回NaN

        // #案例：弹出一个输入框，输入出生年份后，能计算出我们的年龄
        var birthYear = prompt('请输入您的出生年份：');
        var age = 2019 - birthYear; //prompt获取值是字符串，但是前面是数字和减号，可以将这个字符串转换为数字进行运算，除加号外，减号、乘号和除号都可以将字符串转化为数字
        alert('您的年龄是' + age + '岁!');

        // #案例：两个输入值相加
        var num1 = prompt('请输入第一个值：');
        var num2 = prompt('请输入第二个值：');
        var num3 = parseFloat(num1) + parseFloat(num2);
        alert('两个值的和是：' + num3);

        console.log(Boolean(''));
        console.log(Boolean(0));
        console.log(Boolean(NaN));
        console.log(Boolean(undefined));
        console.log(Boolean(null)); //除了这上面五个返回false，其他都返回true

        // #案例：获取用户的姓名，年龄，性别并打印出来
        var yname = prompt('请输入您的姓名：');
        var age = prompt('请输入您的年龄：');
        var gender = prompt('请输入您的性别：');
        alert('姓名:' + yname + '\n' + '年龄:' + age + '\n性别:' + gender);


        // 3.运算符
        console.log(1 + 2);
        console.log(0.1 + 0.2); //浮点数运算会有精度问题，尽量不要直接对浮点数进行运算，另外也不要直接判断两个浮点数是否相等

        var num = 1;
        ++num; //效果和num=num+1是一样的,前置自增运算符，先加1后返回值
        console.log(num);
        var age = 10;
        // age++; //单独使用时类似于++age和age=age+1
        console.log(age++ + 10); //返回20，后置自增先返回原值，再加1，也就是先返回原值10，加上10后得到20，这时age再加1，age变为11
        console.log(age);

        var e = 10;
        var f = e++ + ++e; //1.e++=10,返回e=11,后面++e是在e=11基础上进行，所以++e=12,二者相加返回22，这个刚开始没做对，注意
        console.log(f);

        console.log(18 == 18);
        console.log(18 == '18'); //==默认会转换数据类型，所以返回true，只要求值一样即可，不要求数据类型
        console.log(18 === 18); //true
        console.log(18 === '18'); //返回false，三个等号表示全等，需要值和数据类型都一样才返回true
        console.log(18 != '18'); //false
        console.log(18 !== '18'); //true

        console.log(3 > 5 && 3 > 2); //&&逻辑与，and,但是不能使用and代替
        console.log(3 > 5 || 3 > 2); //||逻辑或，or，但是不能用or代替
        console.log(!(3 > 5)); //!表示非，not,也不能被替代

        // #短路运算（逻辑中断）：当有多个表达式(值)时，左边的表达式可以确定结果时，就不再继续预算右边的表达式的值
        // 1. 逻辑与： 表达式1 && 表达式2
        // 如果第一个表达式的值为真， 则返回表达式2
        // 如果第一个表达式的值为假， 则返回表达式1
        console.log(123 && 456); //123为真，返回456
        console.log(0 && 123); //0为假，返回0
        console.log(0 && 1 + 2 && 456 * 34); //不管式子多少个，只要第一个为假，就返回第一个值
        console.log(1 && 0 && 4 * 4); //不管式子多少个，返回第一个遇到的为假的值，如果没有，则返回最后一个
        console.log(1 && 2 > 1 && 4 * 4); //不管式子多少个，返回第一个遇到的为假的值，如果没有，则返回最后一个,返回16
        console.log(1 && 2 < 1 && 4 * 4); //不管式子多少个，返回第一个遇到的为假的值，如果没有，则返回最后一个,返回2<1的值false

        // 2. 逻辑或：如果表达式1为真，返回表达式1，如果表达式1为假，返回表达式2；通用的讲，返回第一个遇到的真表达式的值，如果没有则返回最后一个值
        console.log(123 || 456); //123
        console.log(0 || 456); //456
        console.log(0 || '' || null || NaN); //NaN

        // 逻辑中断导致结果发生变化，逻辑中断很重要，会影响程序运行结果、、、、、、！@
        // var num = 0;
        console.log(123 || num++); //123
        console.log(num); //由于前面第一个值为真，直接返回导致后面就没有运算，所以num还是0

        // 运算符优先级：
        //     1. 小括号
        //     2. 一元运算符(++, --, !)： 即只需要一个变量即可的
        //     3. 算数运算符(先 * /%后+-)
        //     4. 关系运算符： > , >= , < , <=
        //     5. 相等运算符： == ， != , === , !==
        //     6. 逻辑运算符： 先 && 后 ||
        //     7. 赋值运算符： =
        //     8. 逗号运算符：,
        console.log(4 >= 6 || '人' != '阿凡达' && !(12 * 2 == 144) && true); //true
        var num = 10;
        console.log(5 == num / 2 && (2 + 2 * num).toString() === '22'); //true


        // 4.分支语句
        var age = prompt('请输入您的年龄：');
        if (parseInt(age) >= 18) {
            alert('允许进入网吧！');
        } else {
            alert('未成年人不允许进入网吧！');
        }

        判断是否为闰年
        var year = prompt('请输入年份：');
        if (year % 4 == 0 && parseInt(year) % 100 != 0 || parseInt(year) % 400 == 0) { //%可以把year转换为数字类型，不用再自己转
            alert(year + '年是闰年！');
        } else {
            alert(year + '年是平年！');
        }

        判断是否中奖
        var input = prompt('请输入您的姓名：');
        if (input == '刘德华') {
            alert('您中奖5元！');
        } else {
            alert('您未中奖！');
        }

        成绩判断级别
        var score = prompt('请输入您的分数：');
        if (score >= 90) {
            alert('A');
        } else if (parseInt(score) >= 80 && parseInt(score) < 90) {
            alert('B');
        } else if (parseInt(score) >= 70 && parseInt(score) < 80) {
            alert('C');
        } else if (parseInt(score) >= 60 && parseInt(score) < 70) {
            alert('D');
        } else {
            alert('E');
        }

        // 三元表达式:简化版的if，else
        // 语法结构：条件表达式? 表达式1:表达式2
        // 如果条件为真，返回表达式1，条件为假，返回表达式2
        var num = 10;
        var result = num > 5 ? '是的' : '不是的';
        console.log(result);
        if (num > 5) {
            result = '是的';
        } else {
            result = '不是的';
        }

        var num = prompt('请输入数字：');
        var result = num < 10 ? '0' + num : num;
        alert(result);

        // switch语句，适用于表达式为固定值
        switch (2) {
            case 1:
                console.log('这是1');
                break
            case 2:
                console.log('这是2');
                break
            case 3:
                console.log('这是3');
                break
            default:
                console.log('没有结果！');
        }

        // 表达式的值必须和case后面的值全等时才可以，值和类型都一样
        var num = 3;
        switch (num) {
            case 1:
                console.log(1);
                break;
            case 3:
                console.log(3);
                break;
            default:
                break;
        }
        // switch和if else if比较：switch进行条件判断后直接执行到程序的条件语句，效率更高，感觉是用了字典这种哈希算法，if语句需要一个个遍历条件，像列表遍历，相对慢，所以条减少时用if，条件多时用switch。不过if写起来相对简单。


        // 5.循环语句
        for (var num = 1; num <= 100; num++) {
            console.log('你好！' + num);

        }
        var num = 0;
        for (var i = 1; i <= 100; i++) {
            num += i;
            // console.log(num);

        }
        var average = num / 100;
        console.log(average);

        var even = 0;
        var odd = 0;
        for (var i = 1; i <= 100; i++) {
            if (i % 2 == 0) {
                even += i
            } else {
                odd += i
            }
        }
        console.log(even);
        console.log(odd);

        var num = prompt('请输入班级人数：');
        var sum = 0;
        for (i = 1; i <= num; i++) {
            var score = prompt('请输入第' + i + '个学生的成绩：');
            sum += parseFloat(score);
        }
        var average = sum / num;
        alert('班级平均分为：' + average);

        for (i = 1; i <= 5; i++) {
            var a = '';
            for (j = 1; j <= 5; j++) {
                a = a + '☆'

            }
            console.log(a);

        }

        // 打印倒三角个星星
        var a = '';
        for (i = 1; i <= 5; i++) {

            for (j = i; j <= 5; j++) {
                a = a + '☆'
            }
            a = a + '\n'
        }
        console.log(a);

        // 九九乘法表
        var mlt = '';
        for (i = 1; i <= 9; i++) {
            for (j = 1; j <= i; j++) {
                mlt = mlt + j + '*' + i + '=' + j * i + '\t';
            }
            mlt = mlt + '\n';
        }
        console.log(mlt);

        var num = 1;
        while (num <= 100) {
            console.log('hello,world!');
            num++;
        }

        var love = prompt('请输入：');
        while (love != '我爱你') {
            love = prompt('请输入：');
        }
        alert('我也爱你');

        // do while,//先写循环体再写判断条件
        var i = 1;
        do {
            console.log('hello');
            i++;
        } while (i <= 100);

        for (var i = 1; i <= 5; i++) {
            if (i == 3) {
                continue;
            }
            console.log('我正在吃第' + i + '个包子！');

        }

        var sum = 0;
        for (i = 1; i <= 100; i++) {
            if (i % 7 == 0) {
                continue;
            }
            sum += i;
        }
        console.log(sum);

        for (var i = 1; i <= 5; i++) {
            if (i == 3) {
                break;
            }
            console.log('我正在吃第' + i + '个包子！');
        }



        // 6.数组
        var arr = new Array(); //创建数组
        var arr1 = [1, 2, 'hello', true];
        // console.log(arr1);
        // console.log(arr1[0]);
        // console.log(arr1[1]);
        // console.log(arr1[2]);
        // console.log(arr1[3]);
        // console.log(arr1[4]); //由于没有下标4，返回undefined，Python中就直接报错了
        for (i = 0; i < arr1.length; i++) {
            console.log(arr1[i]);

        }

        // 求数组中的最大值
        var arr1 = [2, 7, 23, 45, 34, 23, 12, 100];
        var max = arr1[0]; //不能将max取0，如果列表中都是负数就不对了，取第一个值就不会出错
        for (i = 1; i < arr1.length; i++) {
            if (max < arr1[i]) {
                max = arr1[i];
            }
        }
        console.log(max);

        // 数组扩容
        var arr1 = [1, 2, 3];
        // arr1.length = 5; //这种扩容方法在Python中是不行的，新增的默认是undefined
        console.log(arr1);
        arr1[6] = 4; //这种直接超过索引上限添加新值的方法Python也不允许，这个还真是灵活，中间用empty填充
        console.log(arr1);

        var arr1 = [];
        for (i = 1; i <= 10; i++) {
            arr1[i - 1] = i;
            // arr1 += [i]; //这种方法不行
        }
        console.log(arr1);

        // 将下列数组中大于10的数字放到一个新的数组中
        // 方法1：需要一个计数器
        var arr1 = [1, 2, 23, 12, 3, 56];
        var arr2 = [];
        var num = 0;
        for (i = 0; i < arr1.length; i++) {
            if (arr1[i] > 10) {
                arr2[num] = arr1[i];
                num++;
            }
        }
        console.log(arr2);

        // 方法2：应用arr2的长度代替计数器
        var arr1 = [1, 2, 23, 12, 3, 56];
        var arr2 = [];
        for (i = 0; i < arr1.length; i++) {
            if (arr1[i] > 10) {
                arr2[arr2.length] = arr1[i];
            }
        }
        console.log(arr2);

        // 颠倒数组,javascript没法用arr[1:]这种切片，所以a[::-1]这种简单的颠倒方法用不了
        var arr1 = ['a', 'b', 'c'];
        var arr2 = [];
        for (i = arr1.length - 1; i >= 0; i--) {
            arr2[arr2.length] = arr1[i];
        }
        console.log(arr2);

        // 冒泡排序
        var arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1];
        for (i = 0; i < arr1.length - 1; i++) { //外层循环管趟数
            for (j = 0; j < arr1.length - 1 - i; j++) { //内层循环管每趟交换次数
                if (arr1[j] > arr1[j + 1]) {
                    var temp;
                    temp = arr1[j];
                    arr1[j] = arr1[j + 1];
                    arr1[j + 1] = temp;
                }
            }
        }
        console.log(arr1);
        // 方法2
        var arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1];
        for (i = arr1.length - 1; i > 0; i--) { //将递增改为递减循环
            for (j = 0; j < i; j++) {
                if (arr1[j] > arr1[j + 1]) {
                    var temp;
                    temp = arr1[j];
                    arr1[j] = arr1[j + 1];
                    arr1[j + 1] = temp;
                }
            }
        }
        console.log(arr1);



        // 7.函数
        // 1-100的累加和
        function sum_n(start, end = 100) {
            var sum = 0;
            for (i = start; i <= end; i++) {
                sum += i;
            }
            console.log(sum);

        }
        sum_n(1); //如果实参个数超过形参个数，取到形参个数为止，不报错
        //如果形参个数多于实参个数，多余的形参被定义为undefined，如果按照目前的加法返回NaN

        // 返回值
        function sayHi() {
            return 'hi';
        }
        console.log(sayHi());

        function sum_n(start, end = 100) {
            var sum = 0;
            for (i = start; i <= end; i++) {
                sum += i;
            }
            return sum;

        }
        console.log(sum_n(1, 100));

        // 利用函数求两个数的最大值
        function max(num1, num2) {
            return num1 > num2 ? num1 : num2;
        }
        console.log(max(1, 2));

        function print(num1, num2) {
            return num1, num2; //return只返回一个值，如果多个值逗号隔开，返回最后一个
        }
        console.log(print(1, 2));

        function fn() {
            console.log(arguments); //在不知道有多少个实参时，可以用arguments替代；里面存储了所有传过来的实参，得到的是一个伪数组
            console.log(arguments[2]);
            console.log(arguments.length);
        }
        fn(1, 2, 3);
        //伪数组：并不是真正意义上的数组
        //1.具有数组的length属性
        //2.按照索引方式存储的
        //3.没有真正数组的一些方法，如pop(),push()等

        // 利用函数求任意个数的最大值
        function getMax() {
            var max = arguments[0];
            for (i = 1; i < arguments.length; i++) {
                if (max < arguments[i]) {
                    max = arguments[i];
                }
            }
            return max;
        }
        console.log(getMax(1, 2, 3));

        // 练习：利用函数把翻转数组封装起来
        function reverse(alist) {
            var new_alist = [];
            for (i = alist.length - 1; i >= 0; i--) {
                new_alist[new_alist.length] = alist[i];
            }
            return console.log(new_alist);

        }
        reverse([1, 2, 3, 5]);

        // 函数表达式(匿名函数)：声明函数
        // var 变量名=function(){};
        var fun = function(aru) {
            console.log('我是函数表达式');
            console.log(aru);

        }
        fun('hello'); //fun是变量名，这个函数没有函数名，可以把函数表达式看做是声明变量，只不过值是个函数而已
        //函数表达式也可以传递参数



        // 8.作用域
        // 全局变量：1.在全局作用域下声明的变量；2.在函数内部没有声明直接赋值的变量，相当于在函数内部去掉var等于Python里的global；
        function fun() {
            var num1 = 10; //局部变量
            num2 = 20; //全局变量
        }
        fun(); //要想使得num2成为全局变量的前提是调用函数，没有调用就会报错；
        // console.log(num1);//会报错
        console.log(num2);
        //局部变量：在函数内部声明的变量，形参也是局部变量
        //1.全局变量只有在浏览器关闭的时候才会销毁，比较占内存资源；局部变量在程序执行完毕就会销毁，减少资源占用

        // 作用域链：内部函数访问外部函数的变量，采取的是链式查找决定取哪个值，称作作用域链：就近原则
        function f1() {
            var num = 123;

            function f2() {
                console.log(num);

            }
            f2();
        }
        var num = 456;
        f1(); //返回的是123，不是456



        // 9. 预解析
        // js引擎运行js分为两步：预解析，代码执行
        // (1)预解析：js引擎会把js里所有的var还有function提升到当前作用域的最前面进行预解析
        // (2)代码执行，按照代码书写顺序从上往下执行
        // 预解析分为变量预解析(变量提升)和函数预解析(函数提升)
        // 变量提升：把所有的变量声明提升到当前作用域最前面，不提升赋值操作；
        console.log(num); //返回undefined而不报错的原因
        var num = 1;
        //上面两行代码顺序由于预解析，如下：
        var num; //预解析提升声明变量到当前作用域的最前面，不提升赋值操作；
        console.log(num); //由于变量被声明了，但是没有赋值所以是undefined
        num = 1; //赋值操作根据顺序最后执行
        //函数提升，把所有的函数声明提升到当前作用域的最前面
        fn();

        function fn() {
            console.log(11);
        }
        // 但是函数调用必须在函数表达式后面，函数表达式是赋值类的，只能把声明变量提升到最前面

        // 练习：预解析1
        var a = 18;
        f1();

        function f1() {
            var b = 9;
            console.log(a);
            console.log(b);
            var a = '123';
        }
        // 上面代码执行顺序如下：
        var a;

        function f1() {
            var b;
            var a;
            b = 9;
            console.log(a); //undefined
            console.log(b); //9
            a = '123';
        }
        a = 18;
        f1();

        // 练习：预解析2
        f1();
        console.log(c);
        console.log(b);
        console.log(a);

        function f1() {
            var a = b = c = 9; //相当于var a=9;b=9;c=9;b和c之前没有var，相当于全局变量了
            console.log(a);
            console.log(b);
            console.log(c);

        }
        // 上面代码预解析后的顺序为：
        function f1() {
            var a;
            a = 9;
            b = 9;
            c = 9; //b和c前没有var,当全局变量看
            console.log(a);
            console.log(b);
            console.log(c);

        }
        f1();
        console.log(c);
        console.log(b);
        console.log(a);



        // 10.对象
        // 对象是由属性和事物组成的。属性：事物的特征，在对象中用属性来表示（常用名词）；方法：事物的行为，在对象中用方法表示（常用动词）；
        var obj = {}; //利用字面量创建一个空的对象
        var obj = {
            uname: '张三丰',
            age: 18,
            sex: '男',
            sayHi: function() { //方法后面跟匿名函数
                console.log('hi');

            }
        }
        console.log(obj.uname); //调用属性的方法1
        console.log(obj['age']); //调用属性的方法2
        obj.sayHi(); //调用方法

        var obj = new Object(); //利用new object创建对象
        obj.uname = '张三丰';
        obj.age = 18;
        obj.sex = '男';
        obj.sayHi = function() {
            console.log('hi');

        }

        //利用构造函数创建对象，感觉就是Python中的类
        //构造函数首字母大写，调用函数时必须前面加new
        //构造函数不需要return就可以返回结果
        function Star(uname, age, sex) {
            this.name = uname;
            this.age = age;
            this.sex = sex;
            this.sing = function(sang) {
                console.log(sang);

            }
        }
        var ldh = new Star('刘德华', 18, '男'); //调用函数返回的是对象
        console.log(ldh.name);
        console.log(ldh['sex']);
        ldh.sing('冰雨');
        // console.log(ldh.sing);//由于方法里已经使用了log所以这里不需要了
        var zxy = new Star('张学友', 20, '男');
        console.log(zxy.name);
        zxy.sing('祝福');

        // 遍历对象
        var obj = {
            uname: '张三丰',
            age: 18,
            sex: '男',
            sayHi: function() { //方法后面跟匿名函数
                console.log('hi');

            }
        }
        for (var k in obj) {
            console.log(k);
            console.log(obj[k]);
        }



        // 11.内置对象
        console.log(Math.PI);
        console.log(Math.max(1, 2, 3));
        console.log(Math.floor(1.9)); //1,向下取整
        console.log(Math.ceil(1.2)); //2,向上取整
        console.log(Math.round(1.4)); //1,四舍五入
        console.log(Math.round(1.5)); //2,四舍五入，其他数字都是四舍五入，但是.5往大了取
        console.log(Math.round(-1.5)); //往大了取返回-1
        console.log(Math.round(-1.6)); //-2
        console.log(Math.random()); //[0,1)之间的随机小数
        // 取两个数之间的随机整数，包含两个数
        function getRandom(max, min) {
            return Math.floor(Math.random() * (max - min + 1)) + min; //因为向下取整，所以要加1
        }
        console.log(getRandom(1, 10));

        // 随机点名
        var arr = ['bob', 'mary', 'john', 'king', 'miss'];
        console.log(arr[getRandom(0, arr.length - 1)]);

        // 猜数字游戏
        function getRandom(max, min) {
            return Math.floor(Math.random() * (max - min + 1)) + min; //因为向下取整，所以要加1
        }
        var random = getRandom(1, 10);
        while (num != random) { //true使得条件总是真，如果没有退出条件就是死循环
            var num = prompt('请输入一个1-10之间的数字:');
            if (num > random) {
                alert('你猜大了');
            } else if (num < random) {
                alert('你猜小了');
            } else {
                alert('你猜对了');
                break;
            }
        }


        // 练习：封装自己的数学对象，包含PI和最大值最小值
        var MyMath = {
            PI: 3.1415926,
            max: function() { //这里不改把arguments当做形参
                var max = arguments[0];
                for (i = 1; i < arguments.length; i++) {
                    if (max < arguments[i]) {
                        max = arguments[i];
                    }
                }
                return max;
            },
            min: function() {
                var min = arguments[0];
                for (i = 1; i < arguments.length; i++) {
                    if (min > arguments[i]) {
                        min = arguments[i];
                    }
                }
                return min;
            }
        }
        console.log(MyMath.PI);
        console.log(MyMath.max(1, 2, 3));
        console.log(MyMath.min(1, 2, 3));

        Date()
        var date1 = new Date(2019, 10, 1);
        console.log(date1); //返回的是11月，而不是10月,因为月份从0开始（0-11）
        var date2 = new Date('2019-11-12 11:39:21');
        console.log(date2);
        var date = new Date();
        console.log(date);
        console.log(date.getFullYear());
        console.log(date.getMonth() + 1);
        console.log(date.getDate());
        console.log(date.getHours());
        console.log(date.getMinutes());
        console.log(date.getSeconds());
        console.log(date.getDay()); //周一返回1，周六返回6，周日返回0
        //写一个2019年11月12日 星期三格式
        var year = date.getFullYear();
        var month = date.getMonth() + 1;
        var day = date.getDate();
        var arr = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
        var week = date.getDay();
        console.log('今天是：' + year + '年' + month + '月' + day + '日 ' + arr[week]);

        function getTimer() {
            var time = new Date();
            var h = time.getHours();
            h = h < 10 ? '0' + h : h;
            var m = time.getMinutes();
            m = m < 10 ? '0' + m : m;
            var s = time.getSeconds();
            s = s < 10 ? '0' + s : s;
            return h + ':' + m + ':' + s;
        }
        console.log(getTimer());

        //获取时间戳
        var date = new Date();
        console.log(date.valueOf()); //获取现在距离1970.1.1的总的毫秒数
        console.log(date.getTime());
        var date1 = +new Date(); //+new Date()返回总的毫秒数
        console.log(date1);
        //H5新增写法
        console.log(Date.now());


        // 练习：倒计时
        function countDown() {
            var deadline = prompt('请以"2019-01-01 00:00:00"格式输入截止时间:');
            var date = new Date(deadline);
            deadtime = date.getTime();
            var now = +new Date();
            while (deadtime > now) {
                leftSeconds = (deadtime - now) / 1000; //毫秒数需要除以1000
                d = parseInt(leftSeconds / 60 / 60 / 24);
                d = d < 10 ? '0' + d : d;
                h = parseInt(leftSeconds / 60 / 60 % 24);
                h = h < 10 ? '0' + h : h;
                m = parseInt(leftSeconds / 60 % 60);
                m = m < 10 ? '0' + m : m;
                s = parseInt(leftSeconds % 60);
                s = s < 10 ? '0' + s : s;
                return alert(d + ':' + h + ':' + m + ':' + s);
            }
        }
        countDown();

        var arr = [1, 2, 3];
        var arr1 = new Array(2); //其中的2表示数组长度为2，里面有两个空的元素
        var arr2 = new Array(2, 3); //[2,3]
        console.log(arr1);
        // 检测是否为数组
        var arr = [];
        var obj = {};
        console.log(arr instanceof Array);
        console.log(obj instanceof Array);
        console.log(Array.isArray(arr)); //h5新增，ie9以上版本才支持
        console.log(Array.isArray(obj));

        // 添加数组
        var arr = [1, 2, 3];
        console.log(arr.push(4, 'pin')); //返回新数组的长度
        console.log(arr);
        console.log(arr.unshift('helo')); //在数组前面添加元素,返回新数组的长度
        console.log(arr);
        //删除元素，pop和Python效果一样
        console.log(arr.pop());
        //shift 删除第一个元素
        console.log(arr.shift());

        //数组排序
        var arr = [1, 2, 3];
        arr.reverse(); //翻转数组
        console.log(arr);
        var arr1 = [1, 2, 4, 3, 13];
        // arr1.sort(); //[1,13,2,4,3]，先排十位，有点问题啊
        arr1.sort(function(a, b) {
            return a - b; //升序的顺序排列
            // return b-a; //降序排列
        })
        console.log(arr1);

        // 返回数组元素索引号方法
        var arr = ['red', 'blue', 'black', 'pink', 'blue'];
        console.log(arr.indexOf('blue')); //indexof找第一个元素的下标，找不到返回-1
        console.log(arr.indexOf('blue', 2)); //从2位置开始查找
        console.log(arr.lastIndexOf('blue')); //从后找第一个元素的下标，找不到返回-1，上面返回1，这个返回4

        //数组去重
        var arr = ['c', 'a', 'z', 'a', 'x', 'a', 'x', 'c', 'b'];

        function unique(arr) {
            var newarr = [];
            for (i = 0; i < arr.length; i++) {
                if (newarr.indexOf(arr[i]) == -1) {
                    newarr.push(arr[i]);
                }
            }
            return newarr;
        }
        console.log(unique(arr));

        // 数组转换为字符串
        var arr = [1, 2, 3];
        console.log(arr.toString());
        console.log(arr.join()); //默认以逗号分隔
        console.log(arr.join('-')); //默认以逗号分隔

        //基本包装类型：把简单数据类型包装为复杂数据类型
        var str = 'blue';
        console.log(str.length);
        // (1)把简单数据类型包装为复杂数据类型；
        var temp = new String('blue');
        // (2)把临时变量的值给str
        str = temp;
        // (3)销毁临时变量
        temp = null;

        // 练习：查找字母出现的位置和次数
        var str = "dafadfsdfdfsfsfsdfasassd";
        var index = str.indexOf('s'); //Of,o没有大写报错
        var count = 0;
        while (index != -1) {
            console.log(index);
            count += 1;
            index = str.indexOf('s', index + 1);
        }
        console.log(count);

        //根据位置返回对应字符
        var str = 'helo';
        console.log(str[2]); //返回l
        console.log(str.charAt(2)); //返回l
        console.log(str.charCodeAt(2)); //返回相应索引号的字符ASCII值，目的，判断用户按下了哪个键

        // 练习：返回字符串中出现字符出现做多次数的字符和对应次数；
        var str = 'dafadfsdfdfsfsfsdfasassd';
        var o = {};
        for (var i = 0; i < str.length; i++) {
            var chars = str.charAt(i);
            if (o[chars]) {
                o[chars]++;
            } else {
                o[chars] = 1;
            }
        }
        var max = 0;
        var ch = '';
        for (var k in o) {
            if (o[k] > max) {
                max = o[k];
                ch = k;
            }
        }
        console.log(max);
        console.log(ch);

        //拼接字符串
        var str = 'zhao';
        console.log(str.concat(' xinbo'));
        //截取字符串
        var str1 = '改革春风吹满地';
        console.log(str1.substr(2, 2)); //第一个参数是下标位置，第二个数个数，返回“春风”，从2开始取2个字符

        //替换字符串
        var str = 'dafsdafsadfsfsfsd';
        console.log(str.replace('s', '*')); //只替换查到的第一个
        // 全部替换用循环
        while (str.indexOf('s') !== -1) {
            str = str.replace('s', '*');
        }
        console.log(str);

        //字符串转换为数组，和Python一样，先split分割
        var str2 = 'red,blue,pink';
        console.log(str2.split(',')); //以为是默认空格，结果测试下不是，没有默认，不加参数不分割
        var str3 = 'red blue pink';
        console.log(str2.split()); //["red,blue,pink"]
    </script>
```

