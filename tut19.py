x = 89


def harry():
    x = 20

    def rohan():
        global x
        x = x+6
        print(x)
    print("before calling rohan() :",x)
    rohan()
    print("after calling rohan() : ",x)


harry()
print(x)-

'''l=10
def func1():
    m=8
    global l
    l=5

    print(l,m)
func1()
print(l)'''

