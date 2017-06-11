# List Comprehension

# Using List Comprhension and a cartesian product 
colors = ['black', 'white']
sizes = ['s', 'm', 'l']
tshirts = [(color, size)  for color in colors for size in sizes]
# print the nested list
for color in colors:
    for size in sizes:
        print((color, size))







"""
theList = ['a', 'b', 'c']
print(theList)

compList = [chars for chars in theList]
print(compList)

upperList = [chars.upper() for chars in theList]
print(upperList)
"""
