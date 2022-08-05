#list1 = ["sameer", "harry", "carry", "cherry", "marry"]
#r = enumerate(list1)
#print(list(r))
#for index, val in enumerate(list1):
 #   print(val)
list2 = ["lays", "kurkure", "frooti", "snacks"]
for index, item in enumerate(list2):
    if index % 2 == 0:
        print(f"jarvis please buy {item}")
