import discord
from discord.ext import commands
import requests
import my_secrets  #archivo con nuestro token 
# import base
import bingo


#vamos a crear un intents, con esto le diremos a discord que queremos acceder a diverentes eventos dentro dentro de su api
intents = discord.Intents.default()
intents.message_content = True  #Y activamos la opcion para leer el contenido de los mensajes

#Declaramos el bot y le damos un prefijo al que responder
bot = commands.Bot(command_prefix='$', intents=intents)

#Creamos la parida para el juego de Bingo
partida = bingo.partida_Bingo()

@bot.command()
async def test(ctx, *args):
    respuesta = ' '.join(args)
    await ctx.send(respuesta)

# @bot.command()
#async def temp(ctx):
#    temp = base.OptenerTemp()
#    await ctx.send(f"la temperatura de mañana sera de {temp}")

@bot.event
async def on_ready():
    print(f"Preparado para empezar {bot.user}")

@bot.command()
async def crear_bingo(ctx):
    partida.CrearBingo()
    await ctx.send("Creada la partida con exito")

@bot.command()
async def crear_Carta_Jugador(ctx):
    if partida.activa:
        nuevo_jugador = bingo.jugador(ctx.author)
        carta = nuevo_jugador.pedirCarta()
        partida.jugadores.append(nuevo_jugador)
        await ctx.send(f"{ctx.author.mention}, aquí tienes tu cartón: {carta}")
    else: 
        await ctx.send("No hay ninguna partida en proceso.")

@bot.command()
async def jugadores(ctx):
    if not partida.jugadores:
        await ctx.send("Aún no hay ningún jugador apuntado.")
    else:
        lista_nombres = [j.nombre for j in partida.obtener_jugadores]
        await ctx.send(f"Jugadores en la partida: {', '.join(lista_nombres)}")

@bot.command()
async def bola(ctx):
    resultado = partida.sacar_Bola()
    await ctx.send('La bola sole del bombo y es... ' + resultado)


def comprobar_numeros(valor):
    partida


#Aqui se tierne que instalar el requests porque sino el programa no va a funcionar
bot.run(my_secrets.Bot_TOKEN)


