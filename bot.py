import discord

from discord.ext import commands

client = commands.Bot(command_prefix='>')

@client.command()
async def ping(ctx):
    await ctx.send('pong')
    

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'hi':
            await message.channel.send("bye")

client = MyClient()

client.run(str(os.environ.get('NTY2OTgwMTIwMzU5NzMxMjAw.XRjiSA.rXX1RqQxHt-TiORprNvNKrghTgI')))
