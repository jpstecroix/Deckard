import discord
import asyncio
from craft import get_craft

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!recipe'):
        await client.send_message(message.channel, 'What you want to craft Type !recipe item')

        def check(msg):
            return msg.content[len('!recipe'):].strip()

        message = await client.wait_for_message(author=message.author, check=check)
        craft = message.content[len('!recipe'):].strip()
        print(craft)
        get_craft(craft)
        #print(message.content)


        em = discord.Embed(title='Crafting Recipe', description='', url='https://www.minecraftcraftingguide.net/search/?s=wood+slab', colour=0xDEADBF)
        em.set_author(name='www.minecraftcraftingguide.net', icon_url=client.user.default_avatar_url)
        em.set_image(url="https://www.minecraftcraftingguide.net/img/crafting/wood-slabs-crafting.gif")
        await client.send_message(message.channel, embed=em)


        #await client.send_message(message.channel, '{}'.format(get_craft(craft)))
        #await client.


client.run('')
