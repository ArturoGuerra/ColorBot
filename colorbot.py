#!/usr/bin/env python3
import sys
import json
import random
import discord
import logging
import asyncio
client = discord.Client()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
@client.event
async def on_ready():
    logger.info("Username: {}".format(client.user.name))
    logger.info("User Discriminator: {}".format(client.user.discriminator))
    logger.info("User ID: {}".format(client.user.id))


async def on_color():
    await client.wait_until_ready()
    server = discord.utils.get(client.servers, id=sys.argv[2])
    role = discord.utils.get(server.roles, id=sys.argv[3])
    logger.info(role.name)
    while True:
        colors = (
             0x9400D3,
             0x4B0082,
             0x0000FF,
             0x00FF00,
             0xFFFF00,
             0xFF7F00,
             0xFF0000,
             0xf442bc,
             0xf4eb42,
             0x42d4f4,
             0x6bf442,
             0x4265f4,
             0xf44253,
             0x42f4e8,
             0xf49542,
             )
        numb = random.randint(0, len(colors) -1)
        color = discord.Colour(colors[numb])
        try:
             await client.edit_role(server, role, colour=color)
             logger.info("{} has changed color in {}".format(role.name, server.name))
             await asyncio.sleep(1)
        except:
             logger.info("Error changing: {} in {}".format(role.name, server.name))
client.loop.create_task(on_color())
client.run(sys.argv[1])
