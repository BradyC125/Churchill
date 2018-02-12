import asyncio
import discord

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
  
  async def vote(self):
    client = self.client
    voteArray = {}
    votesCast = 0
    tempMessage = await client.send_message(self.gameChannel, "President {} has nominated {} for Chancellor. Please react to this message to vote.".format(self.president.name, self.nominatedPlayer.name))
    await client.add_reaction(tempMessage, '✔')
    await client.add_reaction(tempMessage, '❌')
    for player in self.innedPlayerlist:
      voteArray[player] = "Uncast"
    while not votesCast == len(voteArray):
      reaction = await client.wait_for_reaction(['✔','❌'],message = tempMessage)
      if reaction.user in self.innedPlayerlist:
        if reaction.emoji == '✔':
          castVote = "Yes"
        else:
          castVote = "No"
        if voteArray[reaction.user] == "Uncast":
          await client.send_message(self.gameChannel, "{} voted {}".format(reaction.user, castVote.lower()))
          voteArray[reaction.user] = castVote
          votesCast+=1
        elif not castVote == voteArray[reaction.user]:
          await client.send_message(self.gameChannel, "{} changed their vote to {}".format(reaction.user, castVote.lower()))
          voteArray[reaction.user] = castVote
    yes = 0
    no = 0
    for player in self.innedPlayerlist:
      if voteArray[player] == "Yes":
        yes+=1
      else:
        no+=1
    if not yes > no:
      await client.send_message(self.gameChannel, "The election failed.")
    return yes > no
      
  async def genPolicies(self):
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
            
  async def presPolicies(self):
    await self.client.send_message(self.president, ("You drew the following 3 policies:\n1: {}\n2: {}\n3: {}\nPlease select a policy to discard by saying "
                                                        "the number of the policy you'd like to remove").format(self.turnDeck[0],self.turnDeck[1],self.turnDeck[2]))
    def check(reply):
      bool1 = (reply.content[0] == "1" or reply.content[0] == "2" or reply.content[0] == "3")
      bool2 = reply.channel.is_private and reply.author==self.president
      return (bool1 and bool2)
    reply = await self.client.wait_for_message(check=check)
    await self.client.send_message(self.president, "You've passed the other 2 cards to the chancellor.")     
    if reply.content[0] == "1":
      self.turnDeck.pop(0)
    elif reply.content[0] == "2":
      self.turnDeck.pop(1)
    else:
      self.turnDeck.pop(2)
    
  async def chancellorPolicies(self):
    await self.client.send_message(self.chancellor, ("You were passed the following 2 policies:\n1: {}\n2: {}\nPlease choose a policy to enact by saying "
                                                         "the number of the policy you'd like to select").format(self.turnDeck[0],self.turnDeck[1]))
    def check(reply):
      bool1 = (reply.content[0] == "1" or reply.content[0] == "2" or (reply.content=="!veto" and self.vetoEnabled == True))
      bool2 = reply.channel.is_private and reply.author==self.chancellor
      return (bool1 and bool2)
    reply = await self.client.wait_for_message(check=check)
    if reply.content[0] == "1":
      self.enactedPolicy = self.turnDeck[0]
      await self.client.send_message(self.chancellor, "You've enacted a {} policy".format(self.enactedPolicy))
    elif reply.content[0] == "2":
      self.enactedPolicy = self.turnDeck[1]
      await self.client.send_message(self.chancellor, "You've enacted a {} policy".format(self.enactedPolicy))
    
  def addPolicy(self, policy): 
    if policy == "Fascist":
      self.fascistPolicies+=1
      self.fullDeck.pop(len(self.fullDeck)-1)
    else:
      self.liberalPolicies+=1
      self.fullDeck.pop(0)
    
  async def checkIfWon(self):
    onlyFascists = True
    tempBool = True
    for innedPlayer in self.innedPlayerlist:
      if not innedPlayer in self.fascists:
        onlyFascists = False
    if (self.facistPolicies == 6):
      await self.client.send_message(self.gameChannel, "The Fascists enacted 6 policies! They win!")
    elif(self.facistPolicies >= 3 and self.chancellor == self.hitler):
      await self.client.send_message(self.gameChannel, "The fascists elected Hitler as Chancellor! They win!")
    elif onlyFascists:
      await self.client.send_message(self.gameChannel, "The only living players are Fascists! They win!")
    elif (self.liberalPolicies == 5):
      await self.client.send_message(self.gameChannel, "The Liberals have enacted 6 policies! They win!")
    elif not (self.hitler in self.innedPlayerlist):
      await self.client.send_message(self.gameChannel, "The Liberals have killed Hitler! They win!")
    else:
      tempBool = False
    self.over = tempBool
    
  #Add Pres Powers
  
