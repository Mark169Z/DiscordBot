from discord.ext import commands
import discord
from discord.ext.commands import bot
import youtube_dl

class Music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="join")
    async def join(self,ctx):
        channel = ctx.author.voice.channel
        if channel == None:
            await ctx.send("You are not in a channel")
        if ctx.voice_client == None :
            await channel.connect()
        else:
            await bot.voice_client.move_to(channel)

    @commands.command(name="dc")
    async def disconnect(self,ctx):
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name="p")
    async def play(self,ctx,url):
        try:
            ctx.voice_client.stop()
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
            YDL_OPTIONS = {'format':'bestaudio'}
            vc = ctx.voice_client
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url,download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                vc.play(source)
        except:
            await ctx.send("Error")

    @commands.command(name="pause")
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused!")
    
    @commands.command(name="resume")
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resuming")
def setup(bot):
    bot.add_cog(Music(bot))