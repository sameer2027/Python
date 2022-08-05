from functools import reduce
list1 = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x**2, list1)))
print(list(filter(lambda x: x > 2, list1)))
print(reduce(lambda x, y: x*y, list1))


def square(a):
    return a*a


def cube(a):
    return a*a*a


func = [square, cube]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)



