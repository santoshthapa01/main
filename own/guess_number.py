import random
computer = random.randint(1,20)
attempt = 3
while (attempt>0):
    try:
        user = int(input("Enter your choice: "))
        if computer == user:
            print(f"You guessed right. The number is {computer}")
            break
        if user >=0 or user < 20:
            print("Please choose number only between 1-20")
        else:
            attempt -= 1
            if(attempt==0):
                print(f"You guessed wrong. The right one is {computer}")
            if(user < computer):
                print(f"You have {attempt} life remainig choose higher then {user}.")
            if(user > computer):
                print(f"You have {attempt} life remaining please choose less then {user}.")  
        
        
    except ValueError:
        print("Invalid number.")





