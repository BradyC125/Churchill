import discord
import asyncio
import random
import logging
import gameClass
import runGame
from tokenHolder import *

client = discord.Client()

currentGames = {}

async def isAdmin(member):
  if member.server_permissions.manage_server or member.server_permissions.manage_messages:
    return True
  return False

async def endGame(cID):
  game = currentGames[cID]
  #End game

async def join(member, cID):
  if ((cID in currentGames) and (not currentGames[cID].gameStarted) and (not member in currentGames[cID].innedPlayerlist)):
    await client.send_message(currentGames[cID].gameChannel, "You've successfully joined the player list, {}".format(member.name))
    currentGames[cID].innedPlayerlist.append(member)
  
  elif not (cID in currentGames):
    currentGames[cID] = gameClass.GameInstance(client, client.get_channel(cID))
    await client.send_message(currentGames[cID].gameChannel, "You've successfully joined the player list, {}".format(member.name))
    currentGames[cID].innedPlayerlist.append(member)

  else:
    await client.send_message(currentGames[cID].gameChannel, "You're already on the player list, {}".format(member.name))

async def leave(member, cID):
  if ((cID in currentGames) and (not currentGames[cID].gameStarted) and member in currentGames[cID].innedPlayerlist):
    await client.send_message(currentGames[cID].gameChannel, "You've successfully left the player list, {}".format(member.name))
    currentGames[cID].innedPlayerlist.remove(member)

async def playerlist(member, cID):
  if (cID in currentGames):
    game = currentGames[cID]
    if len(game.innedPlayerlist) == 0:
      await client.send_message(game.gameChannel, "There are currently no players waiting to play")
    else:
      tempString = "Currently inned players: "
      for player in game.innedPlayerlist:
        tempString = tempString + "{}, ".format(player.name)
      while tempString.endswith(" ") or tempString.endswith(","):
        tempString = tempString[:len(tempString)-2]
      await client.send_message(game.gameChannel, tempString)
        

async def start(member, cID):
  minPlayers = 5 
  if not (cID in currentGames):
    return False
  
  game = currentGames[cID]
  if (len(game.innedPlayerlist) >= minPlayers and member in game.innedPlayerlist):
    runGame.main(game)
    
  elif member in game.innedPlayerlist:
    await client.send_message(game.gameChannel, "You need {} players to start a game, but you only have {}".format(minPlayers, len(game.innedPlayerlist)))

@client.event
async def on_message(message):
  command = message.content.lower().split(" ")[0]
  if command == "!join":
    await join(message.author, message.channel.id)
  elif command == "!leave":
    await leave(message.author, message.channel.id)
  elif command == "!playerlist":
    await playerlist(message.author, message.channel.id)
  elif command == "!start":
    await start(message.author, message.channel.id)
  elif command == "!endgame" and isAdmin(message.author):
    await endGame(message.channel.id)
  elif command == "!votecount" and message.channel.id in currentGames:
    await currentGames[message.channel.id].voteCount()
  
client.run(token)
