import random 
import time
print("__Welcome to rock paper scissors___")
print("This is a battle  between computer and computer")
score=0
random.seed("rock")
computer_score=0
while True:
    #rps means rock paper scissors
    input("Enter any key to continue")
    rps=random.choice(["rock","paper","scissors"])
    if rps not in ("rock","paper","scissors"):
        print("Invalid input")
        continue
    if rps=="end":
        break
    time.sleep(1)
    computer_rps=random.choice(["rock","paper","scissors"])
    if rps==computer_rps:
        print(">>>It's a tie")
        continue
    if computer_rps=="rock" and rps=="paper":
        print(">>computer 1 won")
        score+=1
    elif computer_rps=="paper" and rps=="scissors" :
        print(">>computer 1 won")
        score+=1
    elif computer_rps=="scissors" and rps=="rock":
        print(">>computer 1 won")
        score+=1
    else:
        print(">>computer 2 won")
        computer_score+=1
    if score==6:
        print("computer 1have defeated computer 2!!")
        break
    elif computer_score==6:
        print("computer 2 has defeated computer 1!!")
        break