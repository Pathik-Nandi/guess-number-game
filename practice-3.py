#_____________________guessing the number----------------------

number_of_guess= 1
print("you can guess 9 times\n -------------------------")
while number_of_guess<9:
    try:
        guess_no=int(input("Enter the guessing number: "))
        if guess_no>30:
            print("Hey user, please guess any number in between 30")
            break
        if guess_no==10:
            print(guess_no,"you are win")
            break
        elif guess_no>15:
            print(guess_no, "This number is too high")
        elif guess_no>10:
            print(guess_no,"this number is  high")
        elif guess_no<5:
            print(guess_no,"This number is very low")
        elif guess_no<10:
            print(guess_no,"This number is low")
        else:
            print("invalid")
    except Exception as e:
        print(e)
    number_of_guess=number_of_guess+1


if number_of_guess==9:
    print("game over")
