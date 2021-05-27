class Player(object):
  def __init__(self, name, score = 0):
    """Sets name, total, and round points"""
    self.name = str(name)
    self.totalPoints = score
    self.roundPoints = score
    print("Have fun " + self.name + "!")

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

  def __str__(self):
    """This returns the name, round points, and total points of the class"""
    return(self.name + " has " + str(self.roundPoints) + " this round and " + str(self.totalPoints) + " in total.")