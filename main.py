import discord
import os
import requests
import json
import random
import sad_words
import encouragement
import tip
from keep_alive import keep_alive

client = discord.Client()


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
	  return

  msg = message.content

  if msg.startswith('*hello'):
	  await message.channel.send('Hello!'+message.author.mention)
	  await message.channel.send(file=discord.File('joey.jpg'))

  if msg.startswith('*inspire'):
	  quote = get_quote()
	  await message.channel.send(quote)

  if any(word in msg for word in sad_words.words):
	  await message.channel.send(random.choice(encouragement.encouragements))
  
  if msg.startswith('*tips'):
	  await message.channel.send(random.choice(tip.tips))
  
  if msg.startswith('*helpline'):
    await message.channel.send(file=discord.File('help1.jpg'))
    await message.channel.send(file=discord.File('help2.jpg'))
    await message.channel.send(file=discord.File('help3.jpg'))
    await message.channel.send(file=discord.File('help4.jpg'))
    await message.channel.send(file=discord.File('help5.jpg'))
    await message.channel.send(file=discord.File('help6.jpg'))
  
  if msg.startswith('*links'):
    await message.channel.send('https://themindclan.com/')
    await message.channel.send('Affordable mental health resources in India: https://docs.google.com/spreadsheets/d/10Ht1QnCZYoLdblCOIr05qF4tpfyuq_uXQ_dq3yjLueM/htmlview#gid=381934799')
    await message.channel.send('List of mental health practitioners at nominal fee/free: https://docs.google.com/document/d/1uEeTDdu58z8nVLbBG8o1qY2xbOhlb9TRVx5COnw2ZiQ/mobilebasic')
    await message.channel.send('Low cost support circles (Therapize): https://instagram.com/p/COAj6iMJtgz/')

keep_alive()
client.run(os.environ['token'])