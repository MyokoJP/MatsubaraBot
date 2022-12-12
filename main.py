#settings
Matsubara = [
    "おぉい",
    "おおぅい",
    "おうい",
    "おいっ",
    "私は学生時代野球でメンタルも体も鍛えられましたから",
    "なるほどぉ〜？",
    "面白い話をしれ！！！！！！しろ！！",
    "あ、うーす",
    "戦国時代にならないでくださいよ",
    "それが戦争になるんです！",
    "思います！！！！！！",
    "洪水！",
    "授業５分のばしますよ？",
    "静かなる土地、うるせぇよ！",
    "うほっ、ああすみません",
    "やめろよ",
    "分国法だよ",
    "僕を退職させないでくださいよ",
    "このままだと僕暴れますよ？",
    "おいぶっ飛ばすぞ",
    "はいしーし？",
    "はいとんとんとん？",
    "君だああああああ！",
    "もう3日は授業しないよ？だって授業3日後だもん",
    "あーなるほどぉ？",
    "どんどん埋められる！？！？",
    "話を聞いてないのは誰かな？君だあああああああ！",
    "きみだぁっ！",
    "なんだとぉ〜¿",
    "倒されちゃった‼︎‼︎",
    "ごみばこにねっ、うん、い、一時保管しただけですから",
    "ま、まあ踏みますよ、ボク信者ですからﾄﾞﾔｧ(?!)",
    "ｱ…ｵﾝ..ﾀｼｶﾆ..ｿﾚﾓｿｿﾃﾞｽn….a",
    "あ、ああぉはよぉぅ",
    "ぁ、じゃぁつぎわ〜青沼選手ぅﾃﾞｽｶﾈ",
    "お、おうい君だよぅ",
    "ﾋﾞｼｯ"
]
Token = "MTA1MDc2MTEzNzM0MTMzNzY1MA.GrxePC.bV7fh8TmBphGADAPBW77ephV-ZibzPeM3jWX0E"
Switch = "on"
#-------

import discord
import random
client = discord.Client(intents=discord.Intents.all())


# Botが起動したときに実行
@client.event
async def on_ready():
    print('Logged in as', client.user, '!')
    print('BOT-ID   :', client.user.id)


# メッセージを受信するごとに実行
@client.event
async def on_message(message):
    if message.author.bot:
        return

    global Switch
    global Matsubara
    global random_message

    if message.content == "b!on":
        if Switch == "on":
            await message.channel.send('既に返信機能がオンになっています。')
        else:
            Switch = "on"
            await message.channel.send('返信機能をオンにしました。')

    elif message.content == "b!off":
        if Switch == "off":
            await message.channel.send('既に返信機能がオフになっています。')
        else:
            Switch = "off"
            await message.channel.send('返信機能をオフにしました。')

    elif Switch == "on" and message.channel.id == 1050771659285610566:
            random_message = random.choice(Matsubara)
            await message.channel.send(random_message)



client.run(Token)