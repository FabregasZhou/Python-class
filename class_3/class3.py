age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

####################################

age = int(input('Please input your age:'))
if age >= 18:
    print('adult')
else:
    print('not an adult')

#####################################

names = ['Lynne', 'Joe', 'Stark']
for x in names:
    print(x)

####################################

for i in range(10):
    print(i)

######################################

n = 1
sum = 0
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)

######################################

x = []
for i in range(100):
    if i > 10:
        break
    elif i == 5:
        continue
    x.append(i)
print(x)

####################################

sum = 0
for i in range(1000):
    sum = sum + (i+1)

print(sum)

###################################

x1 = 0
x2 = 1

for i in range(20-2):
    y = x1 + x2
    x1 = x2
    x2 = y

print(y)

##################################
x1 = 0
x2 = 1

x = [x1,x2]

for i in range(20-2):
    y = x1 + x2
    x.append(y)
    x1 = x2
    x2 = y

print(x)