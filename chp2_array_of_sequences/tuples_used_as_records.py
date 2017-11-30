"""
Tuples stored as records in a positional construct Pg 29
"""
lax_coords = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s %s' % passport)

for country, _ in traveler_ids:
    print(country)
    
# line 8, the 2 positional % % are inturpreted as the field values in the tup

# tuple packing / unpacking example AKA parallel assignment
lax_coords2 = (33.9425,-118.408056)
latitude, longitude = lax_coords2
print(latitude)
print(longitude)

# more parallel assignment *works on the command line* 
theTups = (0, 1, 2, 3, 4, 5)
a, b, *rest = theTups
print(a, b, rest)