import time
initial = time.time()
for i in range(500):
    print("hello world")
print("time taken by for loop is", time.time() - initial, "seconds")
print(time.asctime())
print(time.localtime())
k = 0
initial2 = time.time()
while k < 3:
    print("hello")
    time.sleep(2)
    k += 1

print("time taken by while loop is", time.time() - initial2, "seconds")
