print("enter the first no.")
n1= int(input())
print("enter the second no.")
n2=int(input())
print("enter the operation you want to do *,/,+,-")
op = input()

if op == "*":
     if n1 == 45 and n2 == 3 or n1 == 3 and n2 == 45:
        print("the product is : 555")
     else:
        print("the product is : ", n1*n2)
if op == "/":
    if n1 == 56 and n2 == 6:
        print("the division is : 4.0")
    else:
        print("the division is : ", n1/n2)
if op == "+":
    if n1 == 56 and n2 == 9 or n1 == 9 and n2 == 56:
        print("the sum is : 77")
    else:
        print("the sum is : ", n1+n2)
