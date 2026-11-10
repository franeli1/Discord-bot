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

#Message to know if the bot is onLine
@bot.event
async def on_ready():
    print(f"Preparado para empezar {bot.user}")

#Command for create the game.
@bot.command()
async def crear_bingo(ctx):

    partida.CrearBingo()

    await ctx.send("🎱 Partida creada. Usad `$crear_Carta_Jugador` para pedir cartón "
                   "y `$bola` para sacar la primera bola.")

#Command to finish the game 
@bot.command()
async def terminar_bingo(ctx):

    if not partida.activa:
        await ctx.send("No hay ninguna partida en curso.")
        return
    
    partida.TerminarBingo()
    await ctx.send("La partida a terminado.")

#User command for create the card
@bot.command()
async def crear_Carta_Jugador(ctx):

    if not partida.activa: 
        await ctx.send("No hay ninguna partida en proceso.")
        return
    
    if partida.numeros_salidos:
        await ctx.send("No puedes entrar en una partida en curso espera a la siguiente.")
        return
    
    nuevo = partida.unirse(ctx.author)

    if nuevo is None:
        await ctx.send(f"{ctx.author.mention}, ya tienes el carton. Puedes verlo con `$carton`.")
        return

    ctx.send(f"{ctx.author.mention}, aquí tienes tu cartón:\n{nuevo.pedirCarta()}")


@bot.command()
async def carton(ctx):
    user = partida.jugadores.get(ctx.author.id)
    if not partida.activa or user is None:
        await ctx.send("No tienes un carton para esta partida")
        return
    await ctx.send(f"{ctx.author.mention}, tu cartón ( * = ya ha salido): \n" f"{user.pedirCarta(partida.numeros_salidos)}")    

@bot.command()
async def jugadores(ctx):
    if not partida.obtener_jugadores:
        await ctx.send("Aún no hay ningún jugador apuntado.")
    else:
        lista_nombres = [j.nombre for j in partida.obtener_jugadores]
        await ctx.send(f"Jugadores en la partida: {', '.join(lista_nombres)}")
@bot.command(name="linea")
async def cantar_linea(ctx):
    j = partida.jugadores.get(ctx.author.id)
    if not partida.activa or j is None:
        await ctx.send("No estás jugando en esta partida.")
        return
    if partida.linea_cantada:
        await ctx.send("La línea ya ha sido cantada.")
        return
 
    if j.tiene_linea(partida.numeros_salidos):
        partida.linea_cantada = True
        await ctx.send(f"🎉 ¡**LÍNEA** para {ctx.author.mention}! Seguimos hasta el bingo.")
    else:
        await ctx.send(f"{ctx.author.mention}, ¡no tienes línea todavía!")
 
 
@bot.command(name="bingo")
async def cantar_bingo(ctx):
    j = partida.jugadores.get(ctx.author.id)
    if not partida.activa or j is None:
        await ctx.send("No estás jugando en esta partida.")
        return
 
    if j.tiene_bingo(partida.numeros_salidos):
        await ctx.send(f"🏆 ¡**BINGO** para {ctx.author.mention}! ¡Enhorabuena, has ganado!")
        partida.TerminarBingo()
    else:
        await ctx.send(f"{ctx.author.mention}, ¡tu cartón no está completo!")

@bot.command()
async def bola(ctx):
    if not partida.activa:
        await ctx.send("No hay ninguna partida en proceso.")
        return
    if not partida.jugadores:
        await ctx.send("Todavía no hay jugadores. Pedid cartón con `$crear_Carta_Jugador`.")
        return
 
    resultado = partida.sacar_Bola()
    if resultado is None:
        partida.TerminarBingo()
        await ctx.send("¡Se han acabado las bolas! La partida termina sin ganador.")
        return
 
    salidos = ', '.join(str(n) for n in partida.numeros_salidos)
    await ctx.send(f"La bola sale del bombo y es... **{resultado}**\n" f"Números salidos: {salidos}")


#Aqui se tierne que instalar el requests porque sino el programa no va a funcionar
bot.run(my_secrets.Bot_TOKEN)


