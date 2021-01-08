# Remove duplicates Performance test
import timeit

setup10000 = '''
import numpy as np
items = np.random.choice(30, 100, replace=True)
'''

# 1.
list_filter_code = '''
filtered_items = []

for item in items:
    if item not in filtered_items:
        filtered_items.append(item)
'''

# 2.
set_filter_code = '''
filtered_items = list(set(items))
'''

# 3.
dict_filter_code = '''
filtered_items = list(dict(zip(items, [None]*len(items))).keys())
'''

time1 = timeit.timeit(list_filter_code, setup=setup10000)
time2 = timeit.timeit(dict_filter_code, setup=setup10000)
time3 = timeit.timeit(set_filter_code, setup=setup10000)


print("Time taken for list filter: {time}".format(time=time1))
print("Time taken for dict filter: {time}".format(time=time2))
print("Time taken for set  filter: {time}".format(time=time3))

# Time taken for list filter: 58.0322898
# Time taken for dict filter: 30.996039699999997
# Time taken for set  filter: 26.12637389999999



# Lists => mutable
# Tuples => Immutable