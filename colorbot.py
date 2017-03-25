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
    while True:
        color =
             (
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
        server = discord.utils.get(client.servers, id=config['server'])
        for role in server.roles:
            if not role == server.default_role:
                try:
                    await client.edit_role(server, role, colour=color)
                    logger.info("{} has changed color in {}".format(role.name, server.name))
                    await asyncio.sleep(5)
                except:
                    logger.info("Error changing: {} in {}".format(role.name, server.name))

client.run(sys.argv[1])
