import random
options=("rock","paper","scissors")
running=True
Pscore=0
Cscore=0
while running:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("enter a choice(rock,paper,scissors):")
        print(f"Player:{player}")
        print(f"Computer:{computer}")
        if player==computer:
            print("its a tie")
        elif player=="rock" and computer=="scissors":
            print("you win")
            Pscore+=1
        elif player=="paper" and computer=="rock":
            print("you win")
            Pscore+=1
        elif player=="scissors" and computer=="paper":
            print("you win")
            Pscore+=1
        else:
            print("you lose")
            Cscore+=1
        if not input("Play again?(yes/no):").lower()=="yes":
          running=False
print("Player:" ,Pscore ,"Computer:",Cscore)
print("Thanks for Playing!")