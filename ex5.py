def gettime():
    import datetime
    return datetime.datetime.now()


def logg(k):
    if k == 1:
        c = int(input("enter 1 for food 2 for exercise :"))
        if c == 1:
            food = input("enter diet :")
            f = open("harry_food.txt", "a")
            f.write(str(gettime()) + " : ")
            f.write(food)
            f.close()
        elif c == 2:
            exercise = input("enter exercise :")
            f = open("harry_ex.txt", "a")
            f.write(str(gettime()) + " : ")
            f.write(exercise)
            f.close()
    elif k == 2:
        c = int(input("enter 1 for food 2 for exercise :"))
        if c == 1:
            food = input("enter diet :")
            f = open("rohan_food.txt", "a")
            f.write(str(gettime()) + " : ")
            f.write(food)
            f.close()
        elif c == 2:
            exercise = input("enter exercise :")
            f = open("rohan_ex.txt", "a")
            f.write(str(gettime()) + " : ")
            f.write(exercise)
            f.close()
    elif k == 3:
        c = int(input("enter 1 for food 2 for exercise :"))
        if c == 1:
            food = input("enter diet :")
            f = open("hamid_food.txt", "a")
            f.write(str(gettime()) + " : ")
            f.write(food)
            f.close()
        elif c == 2:
            exercise = input("enter exercise :")
            f = open("hamid_ex.txt", "a")
            f.write(str(gettime()) + " : ")
            f.write(exercise)
            f.close()
    else:
        print("wrong input please enter only 1,2,3")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for food 2 for exercise :"))
        if c == 1:
            f = open("harry_food.txt")
            print(f.read())
        elif c == 2:
            f = open("harry_ex.txt")
            print(f.read())
            f.close()
    elif k == 2:
        c = int(input("enter 1 for food 2 for exercise :"))
        if c == 1:
            f = open("rohan_food.txt")
            print(f.read())
        elif c == 2:
            f = open("rohan_ex.txt")
            print(f.read())
            f.close()
    elif k == 3:
        c = int(input("enter 1 for food 2 for exercise :"))
        if c == 1:
            f = open("hamid_food.txt")
            print(f.read())
            f.close()
        elif c == 2:
            f = open("hamid_ex.txt")
            print(f.read())
            f.close()
    else:
        print("wrong input please enter only 1,2,3")


print(" HEALTH MANAGEMENT SYSTEM ")
a = int(input("enter 1 to log the data or press 2 to retrievew the data "))
if a == 1:
    b = int(input("enter \n1 for HARRY\n2 for ROHAN\n3 for HAMID\n"))
    logg(b)
elif a == 2:
    b = int(input("enter \n1 for HARRY\n2 for ROHAN\n3 for HAMID\n"))
    retrieve(b)
else:
    print("you used neither logg the data nor to retrieve the data")

