"""
Instances of a class that is built with namedtuple are light on resources
because the field names are stored in the class, using less memory
"""
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = (City('Tokyo', 'JP', 36.933, (33.689722, 139.691667)))
print(tokyo)

print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.61, 77.20899))
delhi = City._make(delhi_data) # allows a named tuple to be made 
print(delhi._asdict())

for k, v in delhi._asdict().items():
    print('{} : {}'.format(k, v))