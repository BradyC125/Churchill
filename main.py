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
    currentGames[cID].innedPlayerlist.append(member)
  
  elif not (cID in currentGames):
    currentGames[cID] = gameClass.GameInstance(client, client.get_channel(cID))

async def leave(member, cID):
  if ((cID in currentGames) and (not currentGames[cID].gameStarted) and member in currentGames[cID].innedPlayerlist):
    currentGames[cID].innedPlayerlist.remove(member)

async def start(member, cID):
  if not (cID in currentGames):
    return False
  
  game = currentGames[cID]
  if (game.innedPlayerlist.length >= minPlayers and member in game.innedPlayerlist):
    runGame.main(game)
    
  elif game.innedPlayerlist < minPlayers:
    await client.send_message(game.channel, "You need {} players to start a game, but you only have {}".format(minPlayers, game.innedPlayerlist.length))

@client.event
async def on_message(message):
  command = message.content.lower().split(" ")[0]
  if command == "!join":
    await join(message.author, message.channel.id)
    await client.send_message(message.channel, "You've successfully joined the player list, {}".format(message.author.name))
  elif command == "!leave":
    await leave(message.author, message.channel.id)
  elif command == "!start":
    await start(message.author, message.channel.id)
  elif command == "!endgame" and isAdmin(message.author):
    await endGame(message.channel.id)
  elif command == "!votecount" and message.channel.id in currentGames:
    await currentGames[message.channel.id].voteCount()
  
client.run(token)
