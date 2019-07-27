names = ['Joe', 'Lynne', 'Bob']

print(names)

print('The length of the list is', len(names))

print(names[0])

print(names[-1])

###################################
names = ['Joe', 'Lynne']
print(names)

names.append('Bob')
print(names)

the_last_name = names.pop()
print('The last name of the list is', the_last_name)
print(names)

names[0] = 'Zhou'
print(names)

names.insert(1, 'Joe')
print(names)

the_first_name = names.pop(0)
print('The first name of the list is', the_first_name)
print(names)

##################################
names = ('Joe', 'Lynne', 'Bob')

print(names)

print('The length of the tuple is', len(names))

print(names[0])

print(names[-1])

###################################
emotion = ['happy', 'sad', 'angry']
print(emotion)

emotion.insert(1, 'bored')
print(emotion)

x = emotion.pop(2)
print(x)
print(emotion)

emotion[2] = 'unhappy'
print(emotion)

n = len(emotion)
print('The length of the list is', n)
print(emotion)