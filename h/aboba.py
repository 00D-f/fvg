import discord
import requests
import json
import math
from bs4 import BeautifulSoup


client = discord.Client()

wa = ['а чё', 'а чё)', 'а чё))', 'а чё)))', 'а че', 'а че', 'а че)', 'а че))', 'а че)))', 'а чё?']
wer = ['привет', 'здрасте', 'хай', 'прив', 'дароу', 'хэлоу', 'хелоу']
qwq = ['я тут', 'я пришел', 'я вернулся']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def on_member_join(aboba):
    for channel in aboba.guild.chanels:
        if channel.name == 'основной':
            await channel.send("добро посрать в" + {aboba.name})

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    arr = message.content.split(" ")
    if arr[0] == 'погода':
        r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={" ".join(arr[1:])}&appid=a6756a7aff9564a61122501b4ad92a9b')
        jsonData = json.loads(r.text)
        temp = math.floor(jsonData["main"]["temp"] - 273.15)
        await message.channel.send(F"{temp} C")

    if message.content == "скинь жопу":
        r = requests.get('https://dodopizza.ru/kurgan')
        bs = BeautifulSoup(r.text, "lxml")

        we = bs.find("section", attrs={"class":"sc-814yrq-2 brqcPI"})
        for child in we.children:
            title = child.find("h2", attrs={"class": "product-title"})

    if message.content.lower() == 'привет я артём':
        await message.channel.send('aHAAHAHAAH ты не лох')

    if message.content.lower() == ' ':
        await message.channel.send('...')

    if message.content.lower() == 'привет я степа':
        await message.channel.send('aHAAHAHAAH ты лох')

    if message.content.lower() == 'абоба':
        await message.channel.send('абиба')

    if message.content.lower() == 'ты тупой':
        await message.channel.send('охренел чтоли?')

        await message.channel.send('и ты')

    if message.content.lower() == 'че делаешь':
        await message.channel.send('фарширую пиццу ананасами')

    if message.content.lower() == 'Ой обновление ПО':
        await message.channel.send('эээ не уходи')

    for arr in wer:
        if message.content.lower() == arr:
            await message.channel.send('драсте')

    for arr in qwq:
        if message.content.lower() == arr:
            await message.channel.send('и че?')



client.run('ODI3NTA0Mzk1MTA5MDA3NDAw.YGb_hg.9FdHMe4hxtVSVf83Ffjzdl-wpAY')
