import timeit

setup_str = '''
items = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
'''

# 1. Loop
loop_code = '''
s = []
for item in items:
    s.append(item)
'''


# 2. List Comprehension
lst_comp_code = '''
s = [item for item in items]
'''

time1 = timeit.timeit(loop_code, setup=setup_str)
time2 = timeit.timeit(lst_comp_code, setup=setup_str)

print("Time taken for loop: {time}".format(time=time1))
print("Time taken for list_comp: {time}".format(time=time2))

# List comprehension optimised by python
# Time taken for loop: 2.971493
# Time taken for list_comp: 1.8658072000000003