import discord
import asyncio
import random
import logging
import gameClass

async def threeFailures(game):
  #TODO
  
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

async def main(game):
  numOfPlayers = len(game.innedPlayerlist)
  if numOfPlayers > 8:
    game.addRoles(3)
  elif numOfPlayers > 6:
    game.addRoles(2)
  else:
    game.addRoles(1)
  
  await sendRolePMs(game)
  
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
