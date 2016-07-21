value = 2
guess = input("Guess my favorite value!")
While value != int(guess): 
    if value < int(guess): 
      print("Your guess was too high! Sadness!")
      guess = input("try again: ")
  else value > int(guess):
     print("Your guess was too low! dawn of saddness")
      guess = input("try again: ")
if value == int(guess):
      print("You got it right! Awesome foddie")
      print("Game Over!!! See Ya next time buddy!")
