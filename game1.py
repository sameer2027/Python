import random
lst = ["snake", "water", "gun"]
comp_score = 0
your_score = 0
i = 1
while i <= 10:
    print("match no : ", i)
    comp_choice = random.choice(lst)
    your_choice = int(input("enter 1 for snake\nenter 2 for water\nenter 3 for gun\n"))
    if your_choice == 1 and comp_choice == "water" or your_choice == 2 and comp_choice == "gun" or your_choice == 3 \
            and comp_choice == "snake":
        print("computer choose :", comp_choice)
        print("you wins this match")
        your_score = your_score + 1
        print("your score is : ", your_score)
        print(" computer score is : ", comp_score)
    elif your_choice == 1 and comp_choice == "snake" or your_choice == 2 and comp_choice == "water" or your_choice == 3\
            and comp_choice == "gun":
        print("computer choose :", comp_choice)
        print("its a tie")
        print("your score is : ", your_score)
        print(" computer score is : ", comp_score)
    else:
        print("computer choose :", comp_choice)
        print("computer wins this match ")
        comp_score = comp_score + 1
        print("your score is : ", your_score)
        print(" computer score is : ", comp_score)
    i = i + 1
print("the ten match series is over ")
if your_score > comp_score:
    print(" you won the series")
    print("your score was : ", your_score)
    print(" computer score was : ", comp_score)
elif your_score == comp_score:
    print("series got tie")
    print("your score was : ", your_score)
    print(" computer score was : ", comp_score)
else:
    print("computer won the series ")
    print("your score was : ", your_score)
    print(" computer score was : ", comp_score)

