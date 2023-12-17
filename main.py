import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from id import *

intents = nextcord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print("Bot is ready")
    print("----------------------------")


@client.event
async def on_member_join(member):
    channel = client.get_channel(channel_wilkommen)
    await channel.send(f"Hallo <@{member.id}>, wilkommen im ButterflyHub. Um dir selbst Game-Roles zu geben schau gerne in 'Channels & Roles' (ganz oben in der Seitenleiste) vorbei. Wenn du Fragen oder Probleme hast zieh gerne ein Ticket in <#1079887914869194762>. Ansonsten viel Spaß auf dem Server :Butterfly_butterfly:.")


@client.slash_command(name = "test", description = "Testcommand um Zeugs zu testen", guild_ids=[server_id])
async def test(interaction: Interaction):
    await interaction.response.send_message("Nur ein Test :)")


client.run(bot_token)
