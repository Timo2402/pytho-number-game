import random

answer = random.randrange(1,10)
attempt = 0
while attempt < 3:   
    number = int(input("enter your guess!!"))
    if  0 < number <= 10:
        attempt += 1
        if number == answer:
            print("Wow correct you won🥇🥇")
            break
        elif number != answer and attempt<3:
            print ("incorrect")
        else:
            print(f"Sorry you lost the game⚠️, correct answer is {answer}.")
    else:
        print("Enter valid number between 1-10")
        


    
