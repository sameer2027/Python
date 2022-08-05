'''n = int(input("enter the no of rows :"))
k = int(input("enter 0 for ascend and 1 for decsend : "))
if k==0:
    for i in range(1, n+1):
       print("*"*i)
elif k==1:
      for i in range(n, 0, -1):
           print("*"*i)'''
'''n = int(input("enter the no of rows :"))
for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end =" ")
    print("")'''
'''n = int(input("enter the no of rows :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i ,end =" ")
    print("")'''
n = int(input("enter the no of rows :"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i, end = " ")
    print("")
