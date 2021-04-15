import random

jackpot=random.randint(0,51)

score= 100
gameend=True

print("Here are rules:\n1.Guess the number chosen between 1 and 50\n2.If Your difference is less than or equal to 20, little is used\n3.Otherwise too is used\n\nHAVE FUN\n")

guess=int(input("Give your guess:"))

while score>0:
    if guess!=jackpot:
        score-=10
        diff=guess-jackpot
        if abs(diff)>20:
            if diff>0:
                guess=int(input("You are too ahead mate! \nTry again:"))
            else:
                guess=int(input("You are too behind mate! \nTry again:"))
        elif abs(diff)<=20 :
            if diff>0:
                guess=int(input("You are little ahead mate! \nTry again:"))
            else:
                guess=int(input("You are little behind mate! \nTry again:"))
    elif guess==jackpot:
        gameend=False
        print("\n\nHurrah!! You won with a score of %d"%score)
        break
    
if gameend:
    print("You lose, Loser!!")
