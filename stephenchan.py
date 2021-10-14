import discord
from discord.ext import commands
import random
import time
ram = random.randint(500, 9999)
bot = commands.Bot("!")

@bot.event
async def on_ready():
    print('estou aqui')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "!thread" in message.content:
        await message.delete()
    else:
        await message.delete()
    await bot.process_commands(message)
    
@bot.command(name="thread")
async def criar_thread(ctx, msg=None):
    resposta = f"""
anonymous - no.{ram}

```
{msg}
```

> crie um topico para responder esse fio
"""
    await ctx.send(resposta)

bot.run("ODk4MjMxMjY2NjY5OTA3OTg4.YWhNDg.7AMnMtw6Cog3yspjkKZ0IWP_O70")