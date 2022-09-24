import discord
from discord.ui import Button,View
from discord.ext import commands
from discord.utils import get
import asyncio
import os
bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())


@bot.event
async def on_ready():
    print("준비 완료!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("무엇이든 물어보세요!"))
@bot.command(name="대화시작하기")
async def on_message(ctx):
    ch2 = bot.get_channel(994941257916887121)
    author_name = ctx.message.author.name
    embed2 = discord.Embed(title="대화를 시작했습니다",description=(author_name), color=0xf9ff84)
    await ch2.send(embed=embed2)
    await ctx.author.send ("물어볼 수 있는 명령어를 알려 드리겠습니다!")
    await ctx.author.send ("!를 이용하여 명령어를 사용 할 수 있습니다!")
    await ctx.author.send ("너무 명령어를 많이 사용하면 봇과 대화가 1일 불가합니다")
    await ctx.author.send ("명령어 목록 : !안녕, !너의 정보를 알려줘, !명령어 목록")
@bot.command(name="안녕")
async def on_message(ctx):
    ch1 = bot.get_channel(994941257916887121)
    author_name = ctx.message.author.name
    embed1 = discord.Embed(title="안녕이 작동됨",description=(author_name), color=0xf9ff84)
    await ch1.send(embed=embed1)
    await ctx.author.send ("안녕! 나는 무물봇이야 나한테 무엇이든 물어봐!^^")
    await ctx.author.send ("나를 사용하려면 !를 사용해봐!")
@bot.command(name="너의정보를알려줘")
async def on_message(ctx):
    ch3 = bot.get_channel(994941257916887121)
    author_name = ctx.message.author.name
    embed3 = discord.Embed(title="너의정보를알려줘 작동됨",description=(author_name), color=0xf9ff84)
    await ch3.send(embed=embed3)
    await ctx.author.send ("나는 무엇이든 알려주는 무물봇이야 나에 대해 다시 설명해줄까?")
@bot.command(name="명령어목록")
async def on_message(ctx):
    ch4 = bot.get_channel(994941257916887121)
    author_name = ctx.message.author.name
    embed4 = discord.Embed(title="명령어목록이 작동됨",description=(author_name), color=0xf9ff84)
    await ch4.send(embed=embed4)
    await ctx.author.send ("명령어 목록 : !안녕, !너의정보를알려줘, !명령어목록")
@bot.command(name="출석체크")
async def on_messange(ctx):
    chl = bot.get_channel(994941257916887121)
    author_name = ctx.message.author.name
    await ctx.message.author.send ("출석체크가 완료 되었습니다!")
    embedl = discord.Embed(title="출석체크 됨",description=(author_name), color=0xf9ff84)
    await chl.send(embed=embedl)
acsses_token = os.environ["BOT_TOKEN"]
bot.run(acsses_token)
