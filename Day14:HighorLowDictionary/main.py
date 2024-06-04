import os
import random
import art 
from game_data import data  


import os
import random
import art 
from game_data import data  



def choose_persons():
  '''This function is used to choose a random dictionaries'''
  random_fame_person = random.randint(0, len(data) - 1)
  person_1 = data[random_fame_person]
  return person_1

def guess_who(p1, p2):
  '''This function is used to return two dictionaries depending on the input, must have
  two dictionaries to choose from'''
  guess = input("Who do you think has more followers: 'A' or 'B'\n")
  chosen_person = {}
  other_person = {}

  if guess == 'A':
    chosen_person = p1
    other_person = p2
  if guess == 'B':
    chosen_person = p2
    other_person = p1
  return chosen_person, other_person

print(art.logo)
play_again = True
while(play_again):
  correct = True
  score = 0
  person1 = choose_persons()
  while(correct):
    person2 = choose_persons()
    while(person2 == person1):
      person2 = choose_persons()
    print(f"{person1['name']}, a {person1['description']} from {person1['country']} \n{art.vs}\n{person2['name']}, a {person2['description']} from {person2['country']}\n")
    chosen_person, other_person = guess_who(person1, person2)
  
    print(f"You chose {chosen_person['name']} with {chosen_person['follower_count']}")
    print(f"the other choice was {other_person['name']} with {other_person['follower_count']}")
  
    if chosen_person["follower_count"] > other_person["follower_count"]:
      print("Correct")
      os.system("clear")
      score += 1
      print(f"Your score is {score}")
      person1 = person2
    else:
      os.system("clear")
      print("Wrong")
      correct = False
  print(f"Your final score was {score}\n")
  again = input("Do you want to play again: 'y' or 'n'\n")
  if again == 'n':
    print("Thank you for playing higher or lower by Bcodes!")
    play_again = False
  else:
    os.system("clear")
