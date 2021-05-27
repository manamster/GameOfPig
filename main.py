import Die_Class
import playerClass
import computerPlayer
import time

#This is the block that lets the players set their name and choose wether the 2nd player should be a computer or not.
player1 = playerClass.Player(input("What is the name of the first player?\n"))
compPlayerFlag = input("Would you like to play against a computer? (y/n)").lower()
if compPlayerFlag == "n":
  player2 = playerClass.Player(input("What is the name of the second player?\n"))
else:
  player2 = computerPlayer.Computer("Computer Man")
#Flag to decide if a while loop for the main game is going to run
scoreFlag = 0
#Sets the current player and starts the main game while loop
currentPlayer = player1
while scoreFlag == 0:
  #Sets a flag for another while loop and prints the current player name and score
  flag = "y"
  print(currentPlayer)
  print()
  while flag != "n":
    #Checks to see if the currentPlayer has less than the score needed to win the game. If the do it does the game logic. Else causes the win message to go and it ends the game.
    if currentPlayer.getTotal() < 50:
      #Rolls the dice
      d1 = Die_Class.Die(6)
      d2 = Die_Class.Die(6)
      num1 = d1.roll()
      num2 = d2.roll()
      sumNums = num1 + num2
      print("Roll: Die 1     Die 2")
      print("{:>11}{:>6}".format(num1, num2))
      print()
      #Pauses inbetween the roll and the player input to prevent the game from going to fast
      time.sleep(0.5)
      #This decides if the player has lost any points or gained any
      if num1 == 1 and num2 == 1:
        print("Hmm thats some really bad luck ... sucks for you :(\n")
        currentPlayer.resetTotal()
        currentPlayer.resetRound()
        flag = "n"
      elif num1 == 1 or num2 == 1:
        print("Oh you were greedy and lost your points this round :O who would have known.\n")
        currentPlayer.resetRound()
        flag = "n"
      else:
        print("Oh you actually won points ... thats surprising.\n")
        currentPlayer.updateScore(sumNums)
        print(currentPlayer)
      #this if statement decides if it is a computer to roll again or if it is a player to ask them to roll again. This also updates each points category and for the computer it resets the probability
      if flag != "n":
        if compPlayerFlag != "n" and currentPlayer == player2:
          flag = currentPlayer.takeChance()
          if flag == "y":
            print("\"I have calculated that I am gonna roll again\" - Computer Man\n")
          else:
            print("\"Its too dangerous for me to roll again so I aint gonna.\" - Computer Man\n")
            currentPlayer.updateTotal()
            currentPlayer.resetRound()
            currentPlayer.resetProb()
        else:
          flag = input("Would you like to roll again?(y/n)\n")
          if flag == "n":
            currentPlayer.updateTotal()
            currentPlayer.resetRound()
      else:
        #This happens if the player or computer got any 1's and it switches to the next player
        if compPlayerFlag != "n" and currentPlayer == player2:
          pass
        else:
          input("Press enter to switch to the next player.\n")
    else:
      #This is the win statement that happens if the player has more than 50 points total
      if compPlayerFlag != "n" and currentPlayer == player2:
        print(currentPlayer.getName() + " has won. Dang you are unlucky!\n")
      else:
        print(currentPlayer.getName() + " has won. Good Job!")
      scoreFlag = 1
      flag = "n"
  #This switches the players
  if currentPlayer == player1:
    currentPlayer = player2
  else:
    currentPlayer = player1