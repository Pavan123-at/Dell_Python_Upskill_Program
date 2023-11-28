import random
r= random.randint(1,100)

while r > 0:
   try:
      user_num = int(input("Guess the number between 1 to 100:"))
      if r == user_num:
         print("Correct")
         break
      elif r > user_num:
         print("Higher")
      else:
         print("Lower")
   except ValueError:
      print("Invalid input. Please enter a valid integer")
