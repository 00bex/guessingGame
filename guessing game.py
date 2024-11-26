import random

def getUserGuess():
   numberToGuess = random.randint(1,50)
   attempts = 0
   maxAttempts = 5
   print("Welcome to Emmanuel's guessing Game")
   print("Between 1 - 50, guess the right number. You got 5 trials")
   
   while attempts < maxAttempts:
      guess = int(input("Enter your guess 1-50:"))
      #print(numberToGuess)
      maxAttempts-=1
      if guess < numberToGuess:
         print("Low! Try again.")
      elif guess > numberToGuess:
         print("High! Try again.")
      else:
         print(f"Good job! {numberToGuess} is correct !")
         break
      
   else:
      print(f"Oops you ran out of attempts.The number was {numberToGuess}.")

getUserGuess()
