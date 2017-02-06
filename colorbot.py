#!/usr/bin/python3
import discord
import json
import logging
import random
import asyncio
client = discord.Client()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
@client.event
async def on_ready():
    logger.info("Username: {}".format(client.user.name))
    logger.info("User Discriminator: {}".format(client.user.discriminator))
    logger.info("User ID: {}".format(client.user.id))
async def rand_color():
    await client.wait_until_ready()
    numb = random.randint(1,15)
    if numb == 1:
        color = 0x9400D3
    if numb == 2:
        color = 0x4B0082
    if numb == 3:
        color = 0x0000FF
    if numb == 4:
        color = 0x00FF00
    if numb == 5:
        color = 0xFFFF00
    if numb == 6:
        color = 0xFF7F00
    if numb == 7:
        color = 0xFF0000
    if numb == 8:
        color = 0xf442bc 
    if numb == 9:
        color = 0xf4eb42
    if numb == 10:
        color = 0x42d4f4
    if numb == 11:
        color = 0x6bf442
    if numb == 12:
        color = 0x4265f4
    if numb == 13:
        color = 0xf44253
    if numb == 14:
        color = 0x42f4e8
    if numb == 15:
        color = 0xf49542
    color = discord.Colour(color)
    for server in client.servers:
        for role in server.roles:
            if not role == server.default_role:
                try:
                    await client.edit_role(server, role, colour=color)
                    logger.info("{} has changed color in {}".format(role.name, server.name))
                    await asyncio.sleep(7)
                except:
                    logger.info("Error changing: {} in {}".format(role.name, server.name))
    await rand_color()
client.loop.create_task(rand_color())
with open('config.json', 'r') as f:
    config = json.load(f)
client.run(config['token'])
