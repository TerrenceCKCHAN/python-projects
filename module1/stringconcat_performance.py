import timeit

# Illustrates the performance of string concat

setup_str = '''
items = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
'''

# 1. Non pythonic way
strconcat_code = '''
s = ""
for item in items:
    s += item
'''


# 2. Pythonic way
join_code = '''
s = "".join(items)
'''

time1 = timeit.timeit(strconcat_code, setup=setup_str)
time2 = timeit.timeit(join_code, setup=setup_str)

print("Time taken for string concat: {time}".format(time=time1))
print("Time taken for join method: {time}".format(time=time2))


# Results:
# Time taken for string concat: 2.1991514999999997
# Time taken for join method: 0.36590529999999966

# Python string is immutable: 
# concatenation generates a new string instead of modifying existing one in place
