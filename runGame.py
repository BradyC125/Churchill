import discord
import asyncio
import random
import logging
import gameClass

async def threeFailures(game):
  print("Debug")
  #TODO

async def main(game):
  game.gameStarted = True
  
  numOfPlayers = len(game.innedPlayerlist)
  if numOfPlayers > 8:
    game.assignRoles(3)
  elif numOfPlayers > 6:
    game.assignRoles(2)
  else:
    game.assignRoles(1)
  
  await game.sendRolePMs()
  
  game.presidentCounter = random.randrange(0,game.numOfPlayers)
  
  while not game.over:
    await game.genPolicies()
    print("genPolicy complete in channel {} ({})".format(game.gameChannel.name, game.gameChannel.server.name))
    playerElected = False
    failedElections = 0
    while not playerElected:
      await game.assignPres()
      print("assignPres complete in channel {} ({})".format(game.gameChannel.name, game.gameChannel.server.name))
      await game.nomination()
      print("nomination complete in channel {} ({})".format(game.gameChannel.name, game.gameChannel.server.name))
      playerElected = await game.vote()
      print("vote complete in channel {} ({})".format(game.gameChannel.name, game.gameChannel.server.name))
      if not playerElected:
        if failedElections == 2:
          await threeFailures(game)
        else:
          failedElections += 1
          game.presidentCounter += 1
    game.chancellor = game.nominatedPlayer
    game.nominatedPlayer = False
    await game.checkIfWon()
    print("checkIfWon complete in channel {} ({})".format(game.gameChannel.name, game.gameChannel.server.name))
    if not game.over:
      await game.client.send_message(game.gameChannel, ("The vote succeeded! President {} and Chancellor {} "
                                                        "are now choosing policies.").format(game.president.name, game.chancellor.name))
      game.lastChancellor = game.president
      game.lastPresident = game.chancellor
      await game.presPolicies()
      print("presPolicies complete in channel {} ({})".format(game.gameChannel.name, game.gameChannel.server.name))
      enactedPolicy = await game.chancellorPolicies()
      print("chancellorPolicies complete in channel {} ({})".format(game.gameChannel.name, game.gameChannel.server.name))
      await game.addPolicy(enactedPolicy)
      print("addPolicy complete in channel {} ({})".format(game.gameChannel.name, game.gameChannel.server.name))
      game.presidentCounter += 1
      await game.checkIfWon()
