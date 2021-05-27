import time

class Computer(object):
  def __init__(self, name, score = 0):
    """Sets name, total, and round points"""
    self.name = str(name)
    self.totalPoints = score
    self.roundPoints = score
    self.probability = 1
    print("This computer is hard mode be careful!\n")

  def getTotal(self):
    """Returns the total points"""
    return(self.totalPoints)

  def getRound(self):
    """Returns the round points"""
    return(self.roundPoints)

  def getName(self):
    """Returns the name assigned to the class at creation"""
    return(self.name)

  def updateScore(self, change):
    """Adds to the round score"""
    self.roundPoints += change

  def resetRound(self):
    """Resets the round score if the got a 1 on either die"""
    self.roundPoints = 0

  def resetTotal(self):
    """Resets the total score if they were super greedy and rolled snake eyes"""
    self.totalPoints = 0

  def updateTotal(self):
    """Updates the total points by adding the round points to previous total points"""
    self.totalPoints += self.roundPoints
    #self.roundPoints = 0

  def resetProb(self):
    """This resets the probablility like it is the first roll"""
    self.probability = 0.695

  def calcProb(self):
    """This multiplies the probability by the probability of a single roll not having two 1's"""
    self.probability *= 0.695

  def takeChance(self):
    """This is a function that calls the other functions and decides wether to run the roll depending on if it has to many points that round or if it gets to low of a probability"""
    self.calcProb()
    print("Calculating ...\n")
    time.sleep(0.5)
    if self.roundPoints >= 20:
      flag = "n"
    elif self.probability < 0.3:
      flag = "n"
    else:
      flag = "y"
    return(flag)


  def __str__(self):
    """This returns the name, round points, and total points of the class"""
    return(self.name + " has " + str(self.roundPoints) + " this round and " + str(self.totalPoints) + " in total.")