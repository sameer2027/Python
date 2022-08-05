def func(normal, *args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(normal)
    for i in args:
        print(i, end=" ")
    print("")
    for rno, student in kwargs.items():
        print(f"rno {rno} is present ie {student}")


name = ["harry", "carry", "cherry", "sameer"]
XII = {"1": "harry", "2": "carry", "3": "cherry"}

n = "i am a normal argument"
func(n, *name, **XII)
