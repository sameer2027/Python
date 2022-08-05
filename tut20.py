'''n = int(input("enter the no :"))
j = 1
i = 1
while i <= n:
    j = j * i
    i = i + 1
print(j)'''


'''def fact(m):
    if m == 0 or m == 1:
        return 1
    else:
        a = m * fact(m-1)
        return a

n = int(input("enter the no : "))
print("the factorial is : ", fact(n))'''

'''n = int(input("enter the no : "))
for i in range(1,11):
    print(n, "*", i, "=", n*i)'''


def fabon(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fabon(n-1)+fabon(n-2)


m = int(input("enter the term you want to find : "))
print("the term in the series is :", fabon(m))










