import discord
import asyncio
import random
import logging
import gameClass

async def threeFailures(game):
  #TODO

async def main(game):
  numOfPlayers = len(game.innedPlayerlist)
  if numOfPlayers > 8:
    game.addRoles(3)
  elif numOfPlayers > 6:
    game.addRoles(2)
  else:
    game.addRoles(1)
  
  await game.sendRolePMs()
  
  game.presidentCounter = random.randrange(0,game.numOfPlayers)
  
  while not game.over:
    await game.genPolicies()
    playerElected = False
    failedElections = 0
    while not playerElected:
      await game.assignPres()
      await game.nomination()
      playerElected = await game.vote()
      if not playerElected:
        if failedElections == 2:
          await threeFailures(game)
        else:
          failedElections += 1
          game.presidentCounter += 1
    game.chancellor = game.nominatedPlayer
    game.nominatedPlayer = False
    await game.checkIfWon()
    if not game.over:
      await game.client.send_message(game.gameChannel, ("The vote succeeded! President {} and Chancellor {} "
                                                        "are now choosing policies.").format(game.president.name, game.chancellor.name))
      game.lastChancellor = game.president
      game.lastPresident = game.chancellor
      await game.presPolicies()
      await game.chancellorPolicies()
      await game.addPolicy(game.enactedPolicy)
      game.presidentCounter += 1
      await game.checkIfWon()
