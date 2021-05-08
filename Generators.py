
xss = [1,2,3,4,5]

# As a list
def sqr_list(xs):
    results = []
    for i in xs:
        results.append(i*i)
    return results

# List Comprehension
sqr = [x*x for x in xss]
sqr = sqr_list(xss)
print(sqr)


# Generators
def sqr_gen(xs):
    for i in xs:
        yield i * i

sqrg = sqr_gen(xss)
print(sqrg)

# List Comprehension Generators
sqrg = (x*x for x in xss)
print(next(sqrg))

# for x in sqrg:
#     print(x)


# Performance
# https://www.youtube.com/watch?v=bD05uGo_sVI