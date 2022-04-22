import discord
import random

def checkPun(m,f):

    with open(f,"r") as file:
        puns = file.readlines().split()

    for p in puns:
        if p in m:
            return p

    return False

def pickPun(pun):
    f = pun +".txt"
    with open(f, "r") as file:
        puns = file.readlines().split(",")
    
    return puns[random.randint(0,len(puns)-1)]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Its fine now, why? For I am here! {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    pun = checkPun(message.content,"punlist.txt")
    if pun != False:
        await message.channel.send(pickPun(pun))


client.run('your token here')
