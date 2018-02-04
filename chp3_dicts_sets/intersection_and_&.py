# creating a merged set using &
list1 = ['red', 'white', 'blue']
list2 = ['purple', 'blue', 'pink', 'orange', 'green', 'white']
merge = (set(list1) & set(list2)) 
print(f'Merged sets: {merge}')

# using the .intersection
merge = (set(list1).intersection(list2))  
print(f'Merged sets with intersect: {merge}')