
from art import logo
import random
from replit import clear

def random_number():
  num = random.randint(1,100)
  return num

def enter_number():
  entered_number = int(input("Enter the number you haved guessed between 1 and 100 : "))
  return entered_number

def option():
  difficulty = input("Enter the difficulty at which you want to play : Easy or Hard :-  ").lower()

  return difficulty

def game():
  clear()
  print(logo)
  guess_number = random_number() 
  level = option()
  khela_hobe= True
  

  if level == 'easy':
    number_of_turns = 10
  else:
    number_of_turns = 5

  while khela_hobe==True and number_of_turns>0:
    number_entered = enter_number()
    if number_entered>guess_number and number_of_turns>0:
     print(f"The number you have entered is higher than the guess number. Try Again!! ")
     number_of_turns-=1
     print(f"You have {number_of_turns} turns left....")

    elif number_entered< guess_number and number_of_turns>0:
     print("The number you have entered is lower than the guess number. Try Again!! ")
     number_of_turns-=1
     print(f"You have {number_of_turns} turns left....")

    else:
     print(f"Congratulation!!! You have entered the right number... The number was {guess_number}")
     khela_hobe= False
    
  if number_of_turns == 0:
      print(f"You have exhausted all your guesses... The correct number or guess was {guess_number}")

gg= True
while gg==True:
  game()
  again = input("Do you want to try again : yes or no :- ").lower()
  
  if again =='no':
    gg= False
    clear()
    print(logo)
    print("GoodBye....Be sure to come back and try again")
  
  elif again != 'yes' or again != 'no':
    gg= False
    clear()
    print("You have enetered the wrong option hence you were logged out....")

