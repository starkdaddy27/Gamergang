# Import the random module
import random
 
# Computer chooses a random number between 1 and 1000
target = random.randint(1, 1000)
 
retries = 0
 
while(True):
   
  # Taking user choice
  choice = int(input("Enter your choice: "))
  retries += 1
 
  # Wrong guess
  if target != choice:
     
    print("Wrong Guess!! Try Again")
     
    # Hint
    if target < choice:
      print("The required number lies between 0 and {}".format(choice))
    else:
      print("The required number lies between {} and 1000".format(choice))
   
  # Correct choice
  else:
    print("You guessed the correct number after {} retries".format(retries))
    # User guessed the correct value
    # So let's end the infinite loop
    break;
