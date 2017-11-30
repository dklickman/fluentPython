# insort(seq, item) inserts item into seq to keep seq in ascending order as sorting is very expensive
import bisect
import random

SIZE = 7 
random.seed(1729)
my_list = list()
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
  
