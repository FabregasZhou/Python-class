grades = {}

def handle_end():
    print()
    print('#####################################')
    print()

while True:
    print('1.输入/修改成绩')
    print('2.删除成绩')
    print('3.查看平均成绩')
    print('4.查看成绩表')
    print('0.退出程序')

    command = input('请输入要进行的操作编号，按回车确定：')

    if command == '1':
        name = input('请输入课程名：')
        grade = input('请输入成绩：')

        grades[name] = int(grade)

        handle_end()
    elif command == '2':
        name = input('请输入要删除的课程名：')

        if name in grades:
            grades.pop(name)
            print('删除成功！')
        else:
            print('没有该课的成绩！')

        handle_end()
    elif command == '3':
        ave = 0
        n = 0

        for name, grade in grades.items():
            ave = ave + grade
            n = n + 1

        if n == 0:
            print('还没有录入成绩！')
        else:
            ave = ave / n
            print('平均成绩为：' + str(ave))

        handle_end()
    elif command == '4':
        ave = 0
        n = 0

        for name, grade in grades.items():
            print(name + ':' + grade)

            ave = ave + grade
            n = n + 1

        if n == 0:
            print('还没有录入成绩！')
        else:
            ave = ave / n
            print('平均成绩为：' + str(ave))

        handle_end()
    elif command == '0':
        print('正在退出，感谢使用！')
        break
    else:
        print('请输入正确的操作编号！')

        handle_end()