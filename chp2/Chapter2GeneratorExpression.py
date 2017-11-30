"""Using a generator expression (genexp)
the advantage to the genexp is that each item in
the list is not assigned a place in memory (2 lists)
Useful for creating output that does not need to be stored
in memory
"""

colors = ['black', 'white']
sizes = ['s', 'm', 'l']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)