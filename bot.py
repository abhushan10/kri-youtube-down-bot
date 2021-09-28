from discord.ext import commands
import discord
from discord.ext import commands, tasks
from random import choice
import pafy
import requests

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!',help_command=None)

#====ON_READY====#
@bot.event
async def on_ready():
    change_status.start()   # starting task.Loop
    print('[+] I AM READY ! ')

@bot.command()
async def video(ctx,*,url):
    await ctx.reply(f'> ** [+] We are Processing Video **')
    video = pafy.new(url)
    best = video.getbest()
    await ctx.send(f'> ** [+] Finished Processing Video **')
    playurl = best.url
    shorting_site = requests.get("http://tinyurl.com/" + "api-create.php?url=" + playurl)
    shorted_url = shorting_site.text
    await ctx.reply(f'> ** Download Your Video HERE: <{shorted_url}> **')

@bot.command()
async def music(ctx,*,url):
    await ctx.reply(f'> ** [+] We are Processing Audio **')
    video = pafy.new(url)
    best = video.getbestaudio()
    await ctx.send(f'> ** [+] Finished Processing Audio **')
    playurl = best.url
    shorting_site = requests.get("http://tinyurl.com/" + "api-create.php?url=" + playurl)
    shorted_url = shorting_site.text
    await ctx.reply(f'> ** Download Your Music HERE: <{shorted_url}> **')


@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description="> ** Prefix ===> '!' ** \n > ** !music ===> Download Audio of Youtube Video ** \n > **!video ===> Download Video of Youtube **", color=0xdf4e4e)
    embed.add_field(name="** Usuage **", value="** !music `YOUTUBE_URL_HERE` ** \n ** !video `YOUTUBE_URL_HERE` **", inline=True)
    await ctx.send(embed=embed)














#=====CHANGING STATUS EVERY 10 SEC ==========#
@tasks.loop(seconds=10)
async def change_status():
    status_change= ['Chilling Music! | .help','Abhushan | .help', 'Eating Brain | .help','Naughty Boy! | .help']
    await bot.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game(choice(status_change)))
bot.run('ODkyMzA2Mzk3NDExMjc4ODk4.YVK_Fw.pM9J1jnhp3WY1Lb2sDHURRIOpo8')
