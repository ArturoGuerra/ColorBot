import discord
client = discord.Client()

async def on_no():
    await client.wait_until_ready()
    server =  discord.utils.get(client.servers, id='203164299458379776')
    for role in server.roles:
        await client.edit_role(server, role, colour=discord.Colour(0x99AAB5))
client.loop.create_task(on_no())
client.run("Mjc1MDQ5NDkzMDUxNzM2MDY0.C7iByw.dP-RqDGQyZdtFQ3flk3WLM3WgLE")
