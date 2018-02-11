class GameInstance:
  def __init__(self, client, channel):
    self.channel = channel
    self.client = client
    self.presidentCounter = 0
    self.facistPolicies = 0
    self.liberalPolicies = 0
    self.playerElected = False
    self.voteOutcome = False
    self.nominatedPlayer = False
    self.president = False
    self.chancellor = False
    self.hitler = False
    self.enactedPolicy = False
    self.vetoEnabled = False
    self.unanimousVeto = False
    self.lastChancellor = False
    self.lastPresident = False
    self.peekEnabled = False
    self.voteArray = {}
    self.turnDeck = []
    self.fascists = []
    self.fullDeck = ["Fascist","Fascist","Fascist","Fascist","Fascist","Fascist","Fascist","Fascist","Fascist","Fascist","Fascist",
                     "Liberal","Liberal","Liberal","Liberal","Liberal","Liberal"]
    self.policyDeck = self.fullDeck
    
  def addFascist(self):
    newFascist = self.innedPlayerlist[random.randrange(1,self.numOfPlayers)]
    if newFascist in self.fascists:
      self.addFascist()
    else:
      self.fascists.append(newFascist)
        
  def addHitler(self):
    self.hitler = self.innedPlayerlist[random.randrange(1,self.numOfPlayers)]
    if self.hitler in self.fascists:
      self.addHitler()
  
  def assignRoles(self, numOfFascists):
    for x in range(0, numOfFacists):
      self.addFascist()
    self.addHitler()
  
  def assignPres(self):
    self.president = self.innedPlayerlist[self.presidentCounter%self.numOfPlayers]
    
  def nominations(self):
    \\TODO
  
  def countVote(self):
    \\TODO
    
  def vote(self): 
    \\Invoke self.countVote()
    \\TODO
    
  def genPolicies(self):
    if len(self.policyDeck) > 3:
      i = 0
      while i < 3:
        chosenPolicy = random.randrange(0,len(self.policyDeck))
        self.turnDeck.append(self.policyDeck.pop(chosenPolicy))
        i = i + 1
    elif len(self.policyDeck) == 3:
      self.turnDeck = list(self.policyDeck)
      self.policyDeck = self.fullDeck
    else:
      self.policyDeck = self.fullDeck
      await self.genPolicies()
            
  def presPolicies(self):
    \\TODO
    
  def chancellorPolicies(self):
    \\TODO
    
  def addPolicy(self): 
    \\Change self.fullDeck
    \\TODO
    
  def checkIfWon(self):
    \\TODO
    
  \\Add Pres Powers
  
