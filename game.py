import random
print("Welcome to the game of rock paper and scissors")
print("Select your choice ",
"\nrock = 1",
"\npaper = 2",
"\nscissors =3")

Choice = int(input("Choose your move : "))
rock = 1
paper = 2
scissors = 3 
opponent = random.randint(1,3)
if Choice == 1:
    choice = "rock"
elif Choice == 2:
    choice = "paper"
elif Choice == 3:
    choice = "scissors"

if opponent == 1:
    opp_choice = "rock"
elif opponent == 2:
    opp_choice = "paper"
elif opponent == 3:
    opp_choice = "scissors"

print(f"You has choosen {choice}")
print(f"Computer has choosen {opp_choice}")

if Choice == 1 and opponent == 1:
    print("it's a tie")

elif Choice == 1 and opponent == 2:
    print("You loose")

elif Choice == 1 and opponent == 3:
    print("You win")

elif Choice == 2 and opponent == 1:
    print("You win")

elif Choice == 2 and opponent == 2:
    print("it's a tie")

elif Choice == 2 and opponent == 3:
    print("you loose")

elif Choice == 3 and opponent == 1:
    print("You loose")

elif Choice == 3 and opponent == 2:
    print("You win")

elif Choice == 3 and opponent == 3:
    print("it's a tie")

else:
    print("please select a valid input")
 


   