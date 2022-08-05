list1 = [["harry",1],["larry",2],["carry",6],["marrie",8]]
print(list1)
#for name in list1:
 #   print(name)
dict1 = dict(list1)
print(dict1)
for name,no in dict1.items():
    print(name,no,end=" ")
print("\n")
items=["harry","cherry",3,4,5,88,66,6]
for item in items:
    if str(item).isnumeric() and item >= 6:
        print(item)
    else:
        print("popat")
