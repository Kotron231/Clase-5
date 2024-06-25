import discord
from discord.ext import commands
import os, random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
  print(f'Ha iniciado sesión como {bot.user}')
@bot.command()
async def meme(ctx):
  try:
    images = os.listdir('MEMES')
    if images:
      img_name = random.choice(images)
      with open(f'MEMES/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    else:
      await ctx.send("¡No se encontraron memes en la carpeta 'imagenes'!")
  except FileNotFoundError:
    await ctx.send("¡No se encontraron memes en la carpeta 'imagenes'!")
bot.run('TU TOKEN')
