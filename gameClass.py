class GameInstance:
  def __init__(self, client, channel):
    self.channel = channel
    self.client = client
    self.presidentCounter = 0
    self.facistPolicies = 0
    self.liberalPolicies = 0
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
  
  async def sendRolePMs(game):
    client = game.client
    for player in game.innedPlayerlist:
      if player == game.hitler:
        if fascists.lenght == 1:
          await client.send_message(player, "You're Hitler. Your teammate is {}".format(game.facists[0].name))
        else:
          await client.send_message(player, "You're Hitler. Because you have more than one teammate, you don't get to know who they are")
      elif player in game.fascists:
        if game.fascists.length == 1:
          await client.send_message(player, "You're a facist. Hitler is {}".format(game.hitler.name))
        elif game.facists.lenght == 2:
          if game.facists[0] == player:
            await client.send_message(player, "You're a facist. Hitler is {} and your teammate is {}".format(game.hitler.name, game.facists[1].name))
          else:
            await client.send_message(player, "You're a facist. Hitler is {} and your teammate is {}".format(game.hitler.name, game.facists[0].name))
        else:
          if game.facists[0] == player:
            await client.send_message(player, "You're a facist. Hitler is {} and your teammates are {} and {}".format(game.hitler.name, game.facists[1].name, game.facists[2].name))
          elif game.facists[1] == player:
            await client.send_message(player, "You're a facist. Hitler is {} and your teammates are {} and {}".format(game.hitler.name, game.facists[0].name, game.facists[2].name))
          else:
            await client.send_message(player, "You're a facist. Hitler is {} and your teammates are {} and {}".format(game.hitler.name, game.facists[1].name, game.facists[0].name))
      else:
        await client.send_message(player, "You're a liberal")
  
  def assignPres(self):
    self.president = self.innedPlayerlist[self.presidentCounter%self.numOfPlayers]
    
  async def nominations(self):
    client = self.client
    self.gameChannel
    playerNominated = False
      warningGiven = False
      while not playerNominated:
        nominationMessage = await client.wait_for_message(author=self.president, channel=self.gameChannel)
        try:
          self.nominatedPlayer = nominationMessage.mentions[0]
          if self.nominatedPlayer in self.innedPlayerlist:
            if (self.nominatedPlayer != self.lastChancellor) and (self.nominatedPlayer != self.lastPresident):
              playerNominated = True
              await client.send_message(self.gameChannel, ("President {} has nominated {} for Chancellor. Please react to this message "
                                                           "to vote.").format(self.president.name, self.nominatedPlayer.name))
              #Add reactions
              awat
            else:
              self.nominatedPlayer = False
              await client.send_message(self.gameChannel, "I'm sorry, but your nominee was term limited! Please nominate someone else.")
          else:
            self.nominatedPlayer = False
            await client.send_message(self.gameChannel, "You didn't enter a valid nomination message!")
        except IndexError:
          if not warningGiven:
            await client.send_message(self.gameChannel, "Please mention the person you're nominating like this: `@user`")
            warningGiven = True
  
  def countVote(self):
    #TODO
    
  def vote(self): 
    #Invoke self.countVote()
    #TODO
    
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
    #TODO
    
  def chancellorPolicies(self):
    #TODO
    
  def addPolicy(self): 
    #Change self.fullDeck
    #TODO
    
  def checkIfWon(self):
    #TODO
    
  #Add Pres Powers
  
