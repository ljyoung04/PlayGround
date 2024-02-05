#Simple up&down game
import random

print("="*33)
print(" " * 9 +"Up & Down Game")
print(" The Answer is between 1 and 100")
print("="*33)

attempt = 1

ans = 10

while True:
    print("What is your answer? : ",end="")
    user_input = int(input())
    if user_input == ans :
        print("Correct!!")
        print(f"You tried {attempt} times!")
        break
    elif user_input > ans:
        print("Down!")
        attempt += 1
    else:
        print("Up!")
        attempt += 1
