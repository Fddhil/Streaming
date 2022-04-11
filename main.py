import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = " Fzzly ┊ FAST RESPON! ┊ LIVE ON!!┊ 24/7 Online ┊ PLAYING GTA SAMP ┊ https://discord.gg/ryHbUPTb ", url = "https://www.twitch.tv/fzzly_"))


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
