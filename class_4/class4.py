Joe = {'gender': 'male', 'stature': 180, 'age': 22, 'fat': False}

print(Joe['fat'])
Joe['handsome'] = True
print(Joe)
print('grade' in Joe)
print(Joe.get('gender'))
print(Joe.get('grade', -1))
print(Joe.pop('fat'))
print(Joe)

########################################

Joe = {'gender': 'male', 'stature': 180, 'age': 22, 'fat': False}

for n in Joe:
    print(n)

for n, m in Joe.items():
    print(n + ':' + str(m))
