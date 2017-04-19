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

def get_color():
    rand_int = lambda: random.randint(0, 15)
    rand_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    nums = ''
    for i in range(6):
        nums = nums + rand_list[rand_int()]
    return int("0x" + nums, 16)


async def on_color():
    await client.wait_until_ready()
    server = discord.utils.get(client.servers, id=sys.argv[2])
    role = discord.utils.get(server.roles, id=sys.argv[3])
    logger.info(role.name)
    while True:
        raw_color = get_color()
        logger.info(raw_color)
        color = discord.Colour(raw_color)
        logger.info(color)
        try:
            await client.edit_role(server, role, colour=color)
            logger.info("{} has changed color in {}".format(role.name, server.name))
            await asyncio.sleep(1)
        except Exception as e:
            logger.error(e)
            logger.info("Error changing: {} in {}".format(role.name, server.name))
client.loop.create_task(on_color())
client.run(sys.argv[1])
