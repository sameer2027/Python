def func1(a, b):
    print("hello you are in function 1", a+b)
def func2(a, b):
    """""This is a function which will calculate average of two nos.
    this will not work for three nos """
    average = (a+b)/2
    return average
v = func1(5,7)
print(v)
print(func2(5,7))
print(func2.__doc__)