a = [[1, 5], [0, 4], [3, 2]]
##a.sort(reverse=True)
a.sort(key=lambda x: x[1])
print(a)