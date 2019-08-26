判断：

python中通过if...elif...else语句进行判断，基本语法如下：

    if x:
        ...
        ...
    elif y:
        ...
    else:
        ...
    
例中x、y应为布尔值。除了数值比较的结果以外，非零数值，非空list、tuple也可视为True

我们看下面的例子：

    age = 3
    if age >= 18:
        print('adult')
    elif age >= 6:
        print('teenager')
    else:
        print('kid')
    
运行该程序，会打印 kid

如果if后的语句的值是True，就执行if下缩进的语句，如果值为False，便去判断elif后的语句的布尔值，若还是False就执行else下缩进的语句。如果想在判断的某个分支中执行多个语句，只要保持缩进即可  
一个if后可以接多个elif

对上面代码进行拓展，现在我们希望让用户通过键盘输入年龄来判断其是否成年，代码如下：

    age = input('Please input your age:')
    if age >= 18:
        print('adult')
    else:
        print('not an adult')
    
试着运行下这段代码，会发现程序会报错  
TypeError: '>=' not supported between instances of 'str' and 'int'

这是因为通过input()接收到的变量都是字符串格式的而非数字，我们需要把age变量转换为数值才可进行数值的比较，这里通过int()函数即可实现，我们看一下修改后的代码：

    age = int(input('Please input your age:'))
    if age >= 18:
        print('adult')
    else:
        print('not an adult')

****
循环：

1. for...in...循环

for循环可以对list、tuple以及dict中的每一个元素进行操作，我们看下面的例子：

    names = ['Lynne', 'Joe', 'Stark']
    for x in names:
        print(x)

上面的例子会把names这个list中的每一个元素打印出来

如果我们想打印数字0-9，是不是得手写一个含数字1~99的list呢？答案是不用，python提供了range()函数，我们来看下下面的例子：

    for i in range(10):
        print(i)
    
不难看出，通过函数range(x)可以构建从0开始到小于x的最大整数的list

2. while循环

我们看下面的例子：

    n = 1
    sum = 0
    while n <= 100:
        sum = sum + n
        n = n + 1
    print(sum)

输出的结果就是1到100的和5050，通过这一例子不难理解，while循环的语法如下：

    while x:
        ...
        ...  
    
当x的值为True时执行while下的缩进语句

3. break & continue

通过break语句可以跳出循环，通过continue语句可以忽略此次循环中剩下没执行的语句，直接开始下次循环。通常我们将break、continue语句与if语句搭配使用，我们看下面的例子：

    x = []
    for i in range(100):
        if i > 10:
            break
        elif i == 5:
            continue
        x.append(i)
    print(x)

运行这段代码，理解break和continue的作用

有时候我们的程序写的有问题，可能会是循环的判断条件一直为True，导致程序卡死在循环中，我们称此时程序死循环了。但我们也可以利用死循环完成一些类似“中断”的操作，我们看下面的伪代码：

    while True:
        if 按钮被按下:
            break
        else:
            delay(50)
    点亮LED

如果程序意外进入了死循环或者其他卡死状况，请记得先点stop让程序停止运行，再仔细检查代码的逻辑错误

****
作业：

1. 使用for循环计算1~1000的和  
2. 计算斐波那契数列0,1,1,2,3,5,...的第20个数是多少
3. 创建一个list，存入斐波那契数列的前20个数
