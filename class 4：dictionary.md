dictionary：

假如说我们定义了一个人，需要描述ta的性别、身高、年龄、身材等特征，此时dictionary是一个不错的选择。我们看下面的例子：

    Joe = {'gender': 'male', 'stature': 180, 'age': 22, 'fat': False}
    
上面这句代码建立了一个名为Joe的字典，字典中含有四对key-value对，每对key-value间用逗号隔开。我们对这个dict进行下面的操作：

    print(Joe['fat'])
    Joe['handsome'] = True
    print(Joe)
    print('grade' in Joe)
    print(Joe.get('gender'))
    print(Joe.get('grade', -1))
    print(Joe.pop('fat'))
    print(Joe)
    
运行上面代码，尝试理解下每一句语句的作用：

Joe['fat']返回名为'fat'的key对应的value，如果没有这个key，则程序报错；  
执行Joe['handsome'] = True时，会先检查字典Joe中是否有'handsome'这个key，有的话直接修改他的value为True，没有的话则在这个dict中添加这对key-value；  
'grade' in Joe返回的布尔型变量表示名为'grade'的key是否在字典Joe中；  
Joe.get('gender')在'gender'不存在时和'gender' in Joe是等价的，都返回False，但'gender'存在时返回其对应的value；  
get()方法可以指定key不存在时返回的值，Joe.get('grade', -1)指定了'grade'不存在时返回值-1；  
Joe.pop('fat')返回'fat'对应的value，并将这一对key-value从dict中删除

接下来我们看一下实际应用中dictionary的两个常用调用方法：

    Joe = {'gender': 'male', 'stature': 180, 'age': 22, 'fat': False}
    for n in Joe:
        print(n)
    for n, m in Joe.items():
        print(n + ':' + str(m))
        
第一个for循环在每一次循环时把Joe的一个key赋值给n，第二个for循环在每次循环时将一个key赋值给n，并将其对应的value赋值给m

****
作业：

写一个记录一个学生成绩的脚本

基本功能：  
1. 用户输入课程名和成绩，将其记录到一个dict中
2. 用户可以删除或修改某一课程的成绩
3. 计算平均成绩
