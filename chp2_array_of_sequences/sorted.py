fruits = ['grape', 'banana', 'cherry', 'raspberry']
print(sorted(fruits))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print('To change the fruits list to a new list...')
fruits.sort()
print(fruits) 
