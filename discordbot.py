import discord
from discord.ext import commands
import os
import random
import glob

TOKEN = "OTY4MTIyODA0MjY2NDkxOTA0.YmaQnw.covHjTTIONxLFEWhWCD-Tp4MQrw"

client = discord.Client()

@client.event
async def on_message(message):   

    if message.author.bot:
        return

    if message.content == "$help":
        await message.channel.send("$pixと入力するとランダムな画像を送信します\n$clipと入力するとランダムな動画を送信します\n$tofuxicと入力するとtofuをいじめることができます\n$kill CENSLOEDと入力することで殺せます。")

    if message.content == "無名ちゃん":
        await message.channel.send("https://twitter.com/XzLib?s=20&t=X0-9hXmgcBtz11beTyXBmg")  

    if message.content == "$killcount":
        global nigga
        nigga = 0
        await message.channel.send("killcountを設定しました。") 
        
    if message.content == "$kill CENSOLED":
        await message.channel.send("Censoledを殺しました") 
        nigga += 1
        await message.channel.send("今まで殺したCensoledの数は" + str(nigga) + "匹です。") 
    
    for i in range(15):
     if message.content == "$hicensoled":
         await message.channel.send("<@533547797060780052>")

    for i in range(15):
     if message.content == "$tofuxic":
        await message.channel.send("<@688668113297997846>")

    for i in range(15):
     if message.content == "$encha":
         await message.channel.send("<@759753838734868570>enchant!?!?!?!")  

    for i in range(15):
     if message.content == "$風間いろは":
         await message.channel.send("<@657528099310796820>")   

    for i in range(15):
     if message.content == "$なおみ":
         await message.channel.send("<@715154836445724734>")         

    if message.content == "$yue":
         await message.channel.send("https://streamable.com/ahmxij")       

    if message.content == "$terada":
        await message.channel.send(file=discord.File("terada.jpg"))  

    if message.content == "$elf":
        await message.channel.send(file=discord.File("elf.png"))      

    if message.content == '$pix':
            file = glob.glob('./pix/*')
            file2 = random.choice(file)
            file3 = discord.File(file2, filename=file2)
            await message.channel.send(file=file3)   

    if message.content == "$Valo Custom":
        maps = ["ACENT", "SPLIT", "BIND", "ICEBOX", "BREEZE", "FRACTURE", "HAVEN"]
        out = random.choice(maps)
        await message.channel.send(out)        

    if message.content == '$clip':
            file = glob.glob('./clip/*')
            file2 = random.choice(file)
            file3 = discord.File(file2, filename=file2)
            await message.channel.send(file=file3)  

    if message.content == '$差別':
      embed = discord.Embed(title="NIGGA!",description="黒人死ね！！！！！")
      await message.channel.send(embed=embed)      
                            
client.run('OTY4MTIyODA0MjY2NDkxOTA0.YmaQnw.covHjTTIONxLFEWhWCD-Tp4MQrw')
