'''print("enter the max rows of the pattern")
n = int(input())
print("enter 1 for increasing pattern and 0 for decreasing pattern")
c = bool(input())
i = 0
a = "*"
if c == 0:
    c = True
elif c == 1:
    c = False
else:
    print("enter only either 0 or 1")
while c == 0:
    i = i + 1
    if i <= n:
        print(i*a)
    else:
        break
 while c== 1:
     print(n*a)'''
a = "*"
i = 0


def f1(n):
    while i < n:
        i = i + 1
        print(i*a)
    return i*a


def f2(m):
    while m > 0:
        print(m*a)
        m = m - 1
    return m*a


print("enter the max rows of the pattern")
n = int(input())
print("enter 0 for increasing pattern and 1 for decreasing pattern")
c = int(input())
if c == 0:
    print(f1(n))
elif c == 1:
    print(f2(n))










