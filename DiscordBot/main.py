import discord
from discord.ext import commands
import asyncio
import os 
import random
import youtube_dl
import pafy

Token = 'NzQ1MjQwOTIwNTk2OTM4ODcz.Xzu5sQ.kgIqRYobEfgpKyRY7Id7rAeVtsM'

client = commands.Bot(command_prefix = '|')

loop = False

@client.event
async def on_ready():
    print(f'{client.user} has arrived!!!')

@client.command()
async def ping(ctx):
    await ctx.send(f'I **Muto Yugi** has {round(client.latency*100)}ms')

@client.command()
async def clear(ctx, amount = 4):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'My dark magician has eliminated {amount} messages')
    await ctx.send('https://tenor.com/view/darkmagician-yugioh-yugi-gif-7750682')
    await asyncio.sleep(4)
    await ctx.channel.purge(limit=2)

@client.command()
async def move(ctx, member : discord.Member, channel : discord.VoiceChannel):
    await member.move_to(channel)
    await ctx.send(f'You activated my trap card {member}, my **mirror force** sent you to **{channel}**')
    await ctx.send('https://tenor.com/view/yugioh-yugi-gif-17998675')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=3)

@client.command()
async def ger(ctx,member : discord.Member, channel1 : discord.VoiceChannel , channel2 : discord.VoiceChannel , amount = 2):
    global loop
    await ctx.send(f'You will never reach the truth **{member}**')
    await ctx.send('https://tenor.com/view/jojos-bizarre-adventure-anime-windy-stare-looking-gif-17841830')
    loop = True
    while amount>=0 and loop :
        await member.move_to(channel1)
        await asyncio.sleep(1)
        await member.move_to(channel2)
        await asyncio.sleep(1)
        amount-=1
    loop = False
    await ctx.channel.purge(limit=3)

@client.command()
async def loopstopper(ctx): 
    global loop
    loop = False
    await ctx.send('Tomare!!!')
    await ctx.send('https://tenor.com/view/zawarudo-starplatinum-power-gif-14840872')


@client.command()
async def dc(ctx,member : discord.Member) :
    await member.move_to(None)

@client.command()
async def dcloop(ctx,member : discord.Member, amount = 2):
    global loop
    await ctx.send(f'You will never reach the truth **{member}**')
    await ctx.send('https://tenor.com/view/jojos-bizarre-adventure-anime-windy-stare-looking-gif-17841830')
    loop = True
    while amount>=0 and loop :
        await member.move_to(None)
        await asyncio.sleep(1)
        amount-=1
    loop = False
    await ctx.channel.purge(limit=3)


@client.command()
async def inv(ctx):
    await ctx.send('**Use this Link below to summon me**')
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=745240920596938873&permissions=8&scope=bot')

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


client.run(Token)