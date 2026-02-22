import discord
from discord.ext import commands
import requests
import my_secrets  #archivo con nuestro token 
import base


#vamos a crear un intents, con esto le diremos a discord que queremos acceder a diverentes eventos dentro dentro de su api
intents = discord.Intents.default()
intents.message_content = True  #Y activamos la opcion para leer el contenido de los mensajes

#Declaramos el bot y le damos un prefijo al que responder
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx, *args):
    respuesta = ' '.join(args)
    await ctx.send(respuesta)

@bot.command()
async def temp(ctx):
    temp = base.OptenerTemp()
    await ctx.send(f"la temperatura de mañana sera de {temp}")

@bot.event
async def on_ready():
    print(f"Preparado para empezar {bot.user}")

#Aqui se tierne que instalar el requests porque sino el programa no va a funcionar
bot.run(my_secrets.Bot_TOKEN)


