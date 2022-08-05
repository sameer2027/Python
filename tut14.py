a = 18
n = 0  # no of guesses
v = 5   # no of guesses left
while n < 5:
    print("guess the no.")
    g = int(input())
    n = n + 1
    v = v - 1
    if g < a:
        print("the no guessed is less than actual")
        print("guesses left", v)
    elif g > a:
        print("the no guessed is greater than actual")
        print("guesses left", v)

    else:
        print("congrats same no")
        print("the no of guesses", n)
        print("guesses left", v)
        break
if v==0:
    print("sorry no more guesses left")