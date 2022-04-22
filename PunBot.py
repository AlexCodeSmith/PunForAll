import discord
import random

def getPuns(f):
    plist=[]
    puns = []
    c = 0
    with open(f) as file:
        for line in file:
            line = line.strip() #get rid of newline
            plist.append(line.split(';')) #split the pun type from list and add it to plist
            split = plist[c][1].split(',') #split the comma separated puns 
            plist[c].remove(plist[c][1]) #remove them from plist
            plist[c] += split #join plist with the now split puns
            puns.append(plist[c][0]) #add the pun type to puns 
            c+=1 #increment c                    
    return plist,puns

def checkPun(m,puns):
    for p in puns:
        if p.lower() in m.lower(): #check if the pun word is in the message
             return p
    return False


def pickPun(plist,p):
    for puns in plist:
        if puns[0] == p:
            return puns[random.randint(1,len(puns[0]))]

plist, puns = getPuns("punlist.txt")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Its fine now, why? For puns are here!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    pun = checkPun(message.content,'punlist.txt')
    if pun != False and random.randint(0,3) == 3:
        await message.channel.send(pickPun(pun))


client.run('your token here')
