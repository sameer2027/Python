f = open("harry2.txt")
f.seek(100)
print(f.tell())
print(f.readline())
f.seek(0)
print(f.tell())
print(f.readline())
print(f.tell())
f.close()
with open("harry2.txt") as f:
    print(f.read())