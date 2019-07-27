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
