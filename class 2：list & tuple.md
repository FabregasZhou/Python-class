list：  

list是一个可改变的有序集合，用中括号[]括起，元素间用逗号隔开。我们看下面的例子：

names = ['Joe', 'Lynne', 'Bob']  
print(names)  
print(len(names))  
print(names[0])  
print(names[-1])

这里建立了一个名为names的list，里面三个元素为字符串'Joe','Lynne'和'Bob'。可以通过print()函数打印list。  
len()函数会返回list内的元素个数  
list内元素是有序的，从编号0开始，假如共有n个元素，编号就是0,1,...,n-1。通过names[x]调用编号为x的元素的值。  
同时我们也可以倒着数，names[-1]表示取列表names的最后一个元素的值

上面的例子只体现出了list的有序集合这一特点，那么可改变这一特点体现在何处呢？我们看一看下面的例子：

names = ['Joe', 'Lynne']  
names.append('Bob')  
the_last_name = names.pop()  
names[0] = 'Zhou'  
names.insert(1, 'Joe')  
the_first_name = names.pop(0)

在每一句代码后加上一句print(name)以查看每次操作后的效果。  
append()函数用于在list的末尾添加新元素，pop(x)函数用于删除并返回list编号为x的元素，缺省时作用于list最末尾的元素  
insert(n,x)函数用于在编号为n的位置插入元素x，原先的元素编号顺延  
对list对应编号的元素重新赋值即可修改list

list的长度可以为0，即一个空列表[]。

list内的元素可以为list，即list可以嵌套list

****
tuple：

tuple是不可改变的有序集合，用小括号()括起，元素间用逗号隔开。我们看下面的例子：

names = ('Joe', 'Lynne', 'Bob')  
print(names)  
print(len(names))  
print(names[0])  
print(names[-1])

这里和list完全一样，只是tuple是用小括号括起，而list是用中括号括起。

tuple是不可改变的集合，所以没有pop()、append()等函数

当tuple只有一个元素时，如只含数字1，应该写成(1,)的形式，如果写成(1)系统会认为括号为普通的括号而非tuple的标志，会误认为是数字1而不是tuple

****
作业：

完成下面操作：  
1.创建一个list，内有元素'happy','sad','angry'  
2.在'happy'后插入'bored'  
3.删除元素'sad'  
4.将元素'angry'修改为'unhappy'  
5.打印list的长度
