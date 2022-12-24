import discord
import random
import words
import datetime
client = discord.Client(intents=discord.Intents.all())
date = datetime.datetime.now()
Uho = 0

Token = "MTA1MDc2MTEzNzM0MTMzNzY1MA.GrxePC.bV7fh8TmBphGADAPBW77ephV-ZibzPeM3jWX0E"
# Token = "OTYwODgwNTk4MzY3NDczNzQ3.Gl0H4u.vWuPqoQrFvWPSvjzm3DVyAqEvpHqX8L51i_aPw"
Switch = "on"


@client.event
async def on_ready():
    print('Logged in as', client.user, '!')
    print('BOT-ID   :', client.user.id)


@client.event
async def on_message(message):
    if message.author.bot:
        return

    global Switch
    global date
    global Uho

    if message.content == "b!on":
        if Switch == "on":
            await message.channel.send('既に返信機能がオンになっています。')
            return
        else:
            Switch = "on"
            await message.channel.send('返信機能をオンにしました。')
            return

    elif message.content == "b!off":
        if Switch == "off":
            await message.channel.send('既に返信機能がオフになっています。')
            return
        else:
            Switch = "off"
            await message.channel.send('返信機能をオフにしました。')
            return

    elif Switch == "on" and message.channel.id == 1050771659285610566:
        if Uho == 1:
            await message.channel.send("ぶrrrrrrrrrr")
            return
        elif message.content == "うほっ" or message.content == "うほ":
            Uho += 1

        random_message = random.choice(words.matsubara)
        await message.channel.send(random_message)
        print(str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + str(date.hour) + ":" +
              str(date.minute) + ":" + str(date.second) + " BOT       " + "メッセージを正常に返信しました。")

client.run(Token)
