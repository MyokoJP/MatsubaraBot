import yaml
import discord
import random
import words
import datetime
from discord.ext import tasks
import xml.etree.ElementTree as ET
import re
import urllib.request
from bs4 import BeautifulSoup
import asyncio

client = discord.Client(intents=discord.Intents.all())
date = datetime.datetime.now()
Uho = 0
ooiCount = 0

##########################
DeveloperMode = "on"
##########################


if DeveloperMode == "off":
    Token = "MTA1MDc2MTEzNzM0MTMzNzY1MA.GrxePC.bV7fh8TmBphGADAPBW77ephV-ZibzPeM3jWX0E"
else:
    Token = "OTYwODgwNTk4MzY3NDczNzQ3.Gl0H4u.vWuPqoQrFvWPSvjzm3DVyAqEvpHqX8L51i_aPw"


def print_log():
    print(str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + str(date.hour) + ":" +
          str(date.minute) + ":" + str(date.second) + " INFO       " + "Message successfully replied.")


@client.event
async def on_ready():
    print('Logged in as', client.user, '!')
    print('BOT-ID   :', client.user.id)
    if DeveloperMode == "on":
        await client.change_presence(activity=discord.Game(name="b!help | ななパパを監視中"))
        print("確認：デベロッパーモードはONになっています")
    else:
        await client.change_presence(activity=discord.Game(name="b!help | ななパパを監視中"))
        print("確認：デベロッパーモードはOFFになっています")
    loop.start()


@client.event
async def on_message(message):
    if message.author.bot:
        return
    global date
    global Uho
    global ooiCount

    if message.content.startswith("b!"):
        command = message.content.split()[0].replace('b!', '')
        if command == "":
            embed = discord.Embed(
                title="エラー",
                color=discord.Colour.from_rgb(224, 0, 0),
                description="引数がありません。b!のあとに正しいコマンドを入力して下さい。\n詳しくは`b!help`をご覧下さい。"
            )
            await message.reply(embed=embed)
            return
        else:
            if command == "set":
                arg1 = message.content.split()[1]
                if arg1 == "reply":
                    arg2 = message.content.split()[2]
                    if arg2 == "add":
                        if not message.author.guild_permissions.administrator:
                            embed = discord.Embed(
                                title="エラー",
                                color=discord.Colour.from_rgb(224, 0, 0),
                                description="このコマンドを実行する権限がありません。"
                            )
                            await message.reply(embed=embed)
                            return
                        if message.channel_mentions:
                            channel_mention = message.channel_mentions[0]
                            channel_id = channel_mention.id
                            with open('settings.yml', 'r') as fr:
                                yml = yaml.load(fr, Loader=yaml.Loader)

                                if channel_id in yml["c"]:
                                    if yml["c"][channel_id] is True:
                                        await message.reply("既に追加されています。", mention_author=False)
                                        return
                                    else:
                                        yml["c"][channel_id] = True
                                        with open('settings.yml', 'w') as fw:
                                            yaml.dump(yml, fw, default_flow_style=False)
                                        await message.reply("IDを追加しました。", mention_author=False)
                                        return
                                else:
                                    yml["c"][channel_id] = True
                                    with open('settings.yml', 'w') as fw:
                                        yaml.dump(yml, fw, default_flow_style=False)
                                    await message.reply("IDを追加しました。", mention_author=False)
                                    return
                        else:
                            embed = discord.Embed(
                                title="エラー",
                                color=discord.Colour.from_rgb(224, 0, 0),
                                description="チャンネルが入力されていないか、正しく設定されていません。詳しくは`b!help`をご覧ください。"
                            )
                            await message.reply(embed=embed)
                            return
                    elif arg2 == "del":
                        if not message.author.guild_permissions.administrator:
                            embed = discord.Embed(
                                title="エラー",
                                color=discord.Colour.from_rgb(224, 0, 0),
                                description="このコマンドを実行する権限がありません。"
                            )
                            await message.reply(embed=embed)
                            return
                        if message.channel_mentions:
                            channel_mention = message.channel_mentions[0]
                            channel_id = channel_mention.id
                            with open('settings.yml', 'r') as fr:
                                yml = yaml.load(fr, Loader=yaml.Loader)
                                if channel_id in yml["c"]:
                                    if yml["c"][channel_id] is False:
                                        await message.reply("既に削除されています。", mention_author=False)
                                        return
                                    else:
                                        yml["c"][channel_id] = False
                                        with open('settings.yml', 'w') as fw:
                                            yaml.dump(yml, fw, default_flow_style=False)
                                        await message.reply("IDを削除しました。", mention_author=False)
                                        return
                                else:
                                    yml["c"][channel_id] = False
                                    with open('settings.yml', 'w') as fw:
                                        yaml.dump(yml, fw, default_flow_style=False)
                                    await message.reply("設定されていません。既に削除されています。", mention_author=False)
                                    return
                        else:
                            embed = discord.Embed(
                                title="エラー",
                                color=discord.Colour.from_rgb(224, 0, 0),
                                description="チャンネルが入力されていないか、正しく設定されていません。詳しくは`b!help`をご覧ください。"
                            )
                            await message.reply(embed=embed)
                            return
                    else:
                        embed = discord.Embed(
                            title="エラー",
                            color=discord.Colour.from_rgb(224, 0, 0),
                            description="引数2が正しく設定されていません。詳しくは`b!help`をご覧ください。"
                        )
                        await message.reply(embed=embed)
                        return
                elif arg1 == "788":
                    arg2 = message.content.split()[2]
                    if arg2 == "add":
                        if not message.author.guild_permissions.administrator:
                            embed = discord.Embed(
                                title="エラー",
                                color=discord.Colour.from_rgb(224, 0, 0),
                                description="このコマンドを実行する権限がありません。"
                            )
                            await message.reply(embed=embed)
                            return
                        if message.channel_mentions:
                            channel_mention = message.channel_mentions[0]
                            channel_id = channel_mention.id
                            with open('settings.yml', 'r') as fr:
                                yml = yaml.load(fr, Loader=yaml.Loader)

                                if channel_id in yml["n"]:
                                    if yml["n"][channel_id] is True:
                                        await message.reply("既に追加されています。", mention_author=False)
                                        return
                                    else:
                                        yml["n"][channel_id] = True
                                        with open('settings.yml', 'w') as fw:
                                            yaml.dump(yml, fw, default_flow_style=False)
                                        await message.reply("IDを追加しました。", mention_author=False)
                                        return
                                else:
                                    yml["n"][channel_id] = True
                                    with open('settings.yml', 'w') as fw:
                                        yaml.dump(yml, fw, default_flow_style=False)
                                    await message.reply("IDを追加しました。", mention_author=False)
                                    return
                        else:
                            embed = discord.Embed(
                                title="エラー",
                                color=discord.Colour.from_rgb(224, 0, 0),
                                description="チャンネルが入力されていないか、正しく設定されていません。詳しくは`b!help`をご覧ください。"
                            )
                            await message.reply(embed=embed)
                            return
                    if arg2 == "del":
                        if not message.author.guild_permissions.administrator:
                            embed = discord.Embed(
                                title="エラー",
                                color=discord.Colour.from_rgb(224, 0, 0),
                                description="このコマンドを実行する権限がありません。"
                            )
                            await message.reply(embed=embed)
                            return
                        if message.channel_mentions:
                            channel_mention = message.channel_mentions[0]
                            channel_id = channel_mention.id
                            with open('settings.yml', 'r') as fr:
                                yml = yaml.load(fr, Loader=yaml.Loader)
                                if channel_id in yml["n"]:
                                    if yml["n"][channel_id] is False:
                                        await message.reply("既に削除されています。", mention_author=False)
                                        return
                                    else:
                                        yml["n"][channel_id] = False
                                        with open('settings.yml', 'w') as fw:
                                            yaml.dump(yml, fw, default_flow_style=False)
                                        await message.reply("IDを削除しました。", mention_author=False)
                                        return
                                else:
                                    yml["n"][channel_id] = False
                                    with open('settings.yml', 'w') as fw:
                                        yaml.dump(yml, fw, default_flow_style=False)
                                    await message.reply("既に削除されています。", mention_author=False)
                                    return
                        else:
                            embed = discord.Embed(
                                title="エラー",
                                color=discord.Colour.from_rgb(224, 0, 0),
                                description="チャンネルが入力されていないか、正しく設定されていません。詳しくは`b!help`をご覧ください。"
                            )
                            await message.reply(embed=embed)
                            return
                else:
                    embed = discord.Embed(
                        title="エラー",
                        color=discord.Colour.from_rgb(224, 0, 0),
                        description="引数1が正しく設定されていません。詳しくは`b!help`をご覧ください。"
                    )
                    await message.reply(embed=embed)
                    return

            if command == "on":
                server_id = message.guild.id
                with open('settings.yml', 'r') as fr:
                    yml = yaml.load(fr, Loader=yaml.Loader)
                    if server_id in yml["s"]:
                        if yml["s"][server_id] is True:
                            await message.channel.send("僕起きてますよ？")
                            return
                        else:
                            with open('settings.yml', 'w') as fw:
                                yml["s"][server_id] = True
                                yaml.dump(yml, fw, default_flow_style=False)
                                await message.channel.send("ばらちゃんが起きた！みんな優しくね‼︎")
                                return
                    else:
                        with open('settings.yml', 'w') as fw:
                            yml["s"][server_id] = True
                            yaml.dump(yml, fw, default_flow_style=False)
                        await message.channel.send("僕起きてますよ？")
                        return

            elif command == "off":
                server_id = message.guild.id
                with open('settings.yml', 'r') as fr:
                    yml = yaml.load(fr, Loader=yaml.Loader)
                    if server_id in yml["s"]:
                        if yml["s"][server_id] is False:
                            await message.channel.send("バラちゃん寝てるから静かに〜!!")
                            return
                        else:
                            with open('settings.yml', 'w') as fw:
                                yml["s"][server_id] = False
                                yaml.dump(yml, fw, default_flow_style=False)
                                await message.channel.send("あぁおやすみなさい")
                                return
                    else:
                        with open('settings.yml', 'w') as fw:
                            yml["s"][server_id] = False
                            yaml.dump(yml, fw, default_flow_style=False)
                        await message.channel.send("あぁおやすみなさい")
                        return

            elif command == "help":
                embed = discord.Embed(
                    title="ヘルプ［b!help］",
                    color=discord.Colour.from_rgb(255, 247, 0),
                    description="**❓コマンド一覧**\n```b!help\nヘルプを表示します\n\nb!on\nサーバーのメッセージ返信機能をオンにします" +
                                "\n\nb!off\nサーバーのメッセージ返信機能をオフにします\n\nb!set <reply|788> <add|del> #ch_id*\n" +
                                "送信や返信の対象を追加します（管理者のみ）。ななぱぱ通知送信の対象を追加するには第1引数に788、返信のチャンネルの対象を追加するには第1引数にreplyと入力します。" +
                                "また追加するときは第2引数にadd、削除するときは第2引数にdelを入力します（例は下）。```*#ch_idにはチャンネルをメンションします。\n" +
                                "(例：b!set reply <#1050771659285610566>)\n\n**📝ななパパ更新通知について**\nこの更新の通知については，Amebaブログの" +
                                "RSS機能を使っています。そのため、通知が少し遅れる可能性があります。また、レート制限回避のため更新の検知を1分に1回にしています。そのためこれについても、" +
                                "通知が多少遅れる可能性があります。\n\n**💬返信機能について**\nランダムに返信される機能は`b!add`で送信されるチャンネルの対象を追加できます。" +
                                "また、全てのチャンネルにおいて自動に返信する場合があります。"
                )
                await message.reply(embed=embed, mention_author=False)
                return
            else:
                embed = discord.Embed(
                    title="エラー",
                    color=discord.Colour.from_rgb(224, 0, 0),
                    description="引数が無効です。b!のあとに正しい文字を入力して下さい。\n詳しくは`b!help`をご覧下さい。"
                )
                await message.reply(embed=embed)
                return

    if ("そうだよ" in message.content or "そーだよ" in message.content or "そぅだよ" in message.content or
        "そおだよ" in message.content or "そーーだよ" in message.content or "そおおだよ" in message.content or
            "そーーーだよ" in message.content or "そおおおだよ" in message.content):
        if ooiCount != 0:
            ooiCount += 1
            if ooiCount == 10:
                await message.channel.send("おおいいつまでやるんだよ")
                return
            elif ooiCount == 12:
                await message.channel.send("15回…っていつまでやるの、！")
                ooiCount = 0
                return
            else:
                await message.channel.send(str(ooiCount) + "回目")
                return
        if random.randrange(100) < 30:
            ooiCount += 1
            await message.channel.send(str(ooiCount) + "回目")
            return
        else:
            await message.reply("そうだよってやめろよ😠", mention_author=False)
        return
    ooiCount = 0

    if ("そうたよ" in message.content or "そーたよ" in message.content or "そぅたよ" in message.content or
        "そおたよ" in message.content or "そーーたよ" in message.content or "そおおたよ" in message.content or
            "そーーーたよ" in message.content or "そおおおたよ" in message.content):
        if random.randrange(100) < 2:
            msg = await message.channel.send("そうたよ（便乗）")
            async with message.channel.typing():
                await asyncio.sleep(10)
                await msg.edit("そうたよ（焦）")
        return
    if ("おおい" in message.content or "おいい" in message.content or "おいっ" in message.content or
        "ぉおい" in message.content or "おぉい" in message.content or "ぉおぃ" in message.content or
        "おぉぃ" in message.content or "ぉいぃ" in message.content or "ぉぃい" in message.content or
        "おい" in message.content or "おぃ" in message.content or "ぉい" in message.content or
        "ぉぃ" in message.content or "おいつ" in message.content or "おぃつ" in message.content or
        "ぉいつ" in message.content or "ぉぃつ" in message.content or "おうい" in message.content or
        "おうぃ" in message.content or "おぅい" in message.content or "ぉうい" in message.content or
        "ぉぅい" in message.content or "おぅぃ" in message.content or "ぉうぃ" in message.content or
        "ぉぅぃ" in message.content or "おいい" in message.content or "ぉいい" in message.content or
        "おぃい" in message.content or "おいぃ" in message.content or "ぉぃい" in message.content or
        "おぃぃ" in message.content or "ぉいぃ" in message.content or "ぉぃぃ" in message.content or
        "ooi" in message.content or "oi" in message.content or "oii" in message.content or
            "oooi" in message.content):
        if random.randrange(100) < 1:
            await message.channel.send("あおい")
            return
        ooi = ["おおい", "おいい", "おいっ", "ぉおい", "おぉい", "ぉおぃ", "おぉぃ", "ぉいぃ", "ぉぃい", "おい", "おぃ", "ぉい", "ぉぃ"]
        random_message = random.choice(ooi)
        await message.channel.send(random_message)
        print_log()
        return

    if ("なるほど" in message.content or "なる" in message.content or message.content.endswith("だよ") or
        message.content.endswith("ちゃった") or message.content.endswith("てくる") or message.content.endswith("るよ") or
            message.content.endswith("した") or message.content.endswith("った") or message.content.endswith("みた")):
        if random.randrange(100) < 40:
            msg = await message.channel.send("なるほどぉ～？（便乗）")
            if random.randrange(100) < 2:
                await asyncio.sleep(3)
                await msg.edit("そうかなぁ～？（懐疑心）")
            return

    if "だる" in message.content or "だある" in message.content or "daru" in message.content.casefold():
        emoji = "<:daru:1075407121274900550>"
        await message.add_reaction(emoji)
        print(str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + str(date.hour) + ":" +
              str(date.minute) + ":" + str(date.second) + " INFO       " + "Reaction successfully added.")
        return

    # ここから特定のチャンネルのみ起動
    with open('settings.yml', 'r') as fr:
        yml = yaml.load(fr, Loader=yaml.Loader)
        server_id = message.guild.id
        channel_id = message.channel.id
        if server_id not in yml:
            with open('settings.yml', 'w') as fw:
                yml["s"][server_id] = True
                yaml.dump(yml, fw, default_flow_style=False)
        else:
            if yml[server_id] is False:
                return
        if channel_id not in yml["c"]:
            return
        if yml["c"][channel_id] is False:
            return

    if "うほっ" in message.content or "うほ" in message.content or "ウホ" in message.content or "ウホッ" in message.content:
        if random.randrange(100) < 10:
            message.channel.send("ばrrrrrら")
            return
        uho = ["うほっ", "うほ", "ウホ", "ウホッ"]
        random_message = random.choice(uho)
        await message.channel.send(random_message)
        print_log()
        return
    if ("前田" in message.content or "まえだ" in message.content or "maeda" in message.content or
            "MAEDA" in message.content):
        if random.randrange(100) < 2:
            await message.channel.send(file=discord.File("daru.png"))
            return
        maeda = ["うほっ", "おいぶっ飛ばすぞ", "はいむぅし", "だrrrrr"]
        random_message = random.choice(maeda)
        await message.channel.send(random_message)
        print_log()
        return
    if ("清正" in message.content or "きよまさ" in message.content or "kiyomasa" in message.content or
            "KIYOMASA" in message.content or "キヨまさ" in message.content):
        if random.randrange(100) < 40:
            await message.channel.send("清正くんは年明けてから全然部活きてませんねえ～")
            return
        kiyomasa = ["はいむぅし", "なるほどぉ?？"]
        random_message = random.choice(kiyomasa)
        await message.channel.send(random_message)
        print_log()
        return
    random_message = random.choice(words.matsubara)
    await message.channel.send(random_message)
    print_log()
    return


@tasks.loop(seconds=60)
# ななパパチェック
async def loop():
    with open('rss20.xml', 'r', encoding='utf-8') as fr:
        titlel = ET.parse(fr).getroot()[0][6][0].text
        with urllib.request.urlopen("http://rssblog.ameba.jp/nanasora-sg3/rss20.xml") as fo:
            tree = ET.parse(fo)
            root = tree.getroot()
            title = root[0][6][0].text

            if titlel != title:
                print(str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + str(date.hour) + ":" +
                      str(date.minute) + ":" + str(date.second) + " INFO       " + "Blog updates detected.")
                html = root[0][6][1].text
                link = root[0][6][2].text
                soup = BeautifulSoup(html, 'lxml')
                imgs = soup.find_all('img', src=re.compile('^https://stat.ameba.jp/user_images/'))
                count = 0
                for img in imgs:
                    if count == 1:
                        break
                    src = img['src']
                    count += 1
                soup = BeautifulSoup(html, 'html.parser')
                inner = soup.get_text()
                urllib.request.urlretrieve("http://rssblog.ameba.jp/nanasora-sg3/rss20.xml", "rss20.xml")
                embed = discord.Embed(
                    title=title,
                    color=discord.Colour.from_rgb(0, 192, 235),
                    description=inner[:30] + "...\n[【続きを見る】](" + link + ")",
                    url=link
                )
                embed.set_author(name="ななパパ更新通知", icon_url="https://www.myoko.xyz/header_bk.png")
                embed.set_image(url=src)
                embed.set_footer(text="by <:ameba:1081490390454116362>ななパパの徒然日記 (*´д`*)もへぇ～♡")
                with open('settings.yml', 'r') as f:
                    yml = yaml.load(f, Loader=yaml.Loader)
                    channels = yml["n"]
                    true_keys = [key for key, value in channels.items() if value]
                for i in true_keys:
                    channel = client.get_channel(i)
                    await channel.send(embed=embed)
            else:
                if DeveloperMode == "on":
                    print(str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + str(date.hour) + ":" +
                          str(date.minute) + ":" + str(date.second) + " INFO       " +
                          "Checked the blog for updates, but they were not done.")


client.run(Token)
