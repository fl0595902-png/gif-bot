import discord
from discord.ext import commands
from PIL import Image
import requests
from io import BytesIO
import os

TOKEN = os.getenv("TOKEN")

bot.run(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot listo como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 😎")

@bot.command()
async def gif(ctx):
    if not ctx.message.reference:
        await ctx.send("Respondé a una imagen con !gif")
        return

    ref_msg = await ctx.channel.fetch_message(
        ctx.message.reference.message_id
    )

    if not ref_msg.attachments:
        await ctx.send("Ese mensaje no tiene imagen.")
        return

    image_url = ref_msg.attachments[0].url
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content)).convert("RGB")

    gif_path = "output.gif"
    img.save(gif_path, format="GIF")

    await ctx.send(file=discord.File(gif_path, filename="convertido.gif"))

bot.run(TOKEN)