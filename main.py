import discord
import asyncio
import yaml
from craft import get_craft
from mcstatus import mc_servstatus

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel, 'Good to see you , There is a list of available commands:')
        await client.send_message(message.channel, '```!recipe <item> : search any corresponding crafting recipe for <item>\n!status: Show server status```')
    elif message.content.startswith('!recipe'):
        if message.content[len('!recipe'):].strip() == '':
            await client.send_message(message.channel, 'Greetings. Which item you want to craft Type !recipe item')
        else:
            craft = message.content[len('!recipe'):].strip()
            if get_craft(craft) is None:
                await client.send_message(message.channel, "There is something about this search that troubles me. I cannot find anything")
            else:
                await client.send_message(message.channel, "Good to see you! Here is my search result:")
                for result in get_craft(craft):
                    em = discord.Embed(title=result['title'], description='', url=result['url'], colour=0xDEADBF)
                    em.set_author(name='www.minecraftcraftingguide.net', icon_url=client.user.default_avatar_url)
                    em.set_image(url="https:%s" % result['src'])
                    await client.send_message(message.channel, embed=em)
    elif message.content.startswith('!status'):
        res = mc_servstatus(cfg['server']['address'])
        await client.send_message(message.channel, 'Good day. **{}:{}** is **{}**, **{}** players connected'.format(res[0], res[1], res[2], res[3]))

client.run(cfg['bot']['api_token'])
