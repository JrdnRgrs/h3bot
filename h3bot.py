#!/usr/bin/python

# This example requires the 'members' privileged intents
import os
from email.message import Message
import discord
from discord.ext import commands
from discord.utils import get
from discord import Color
import random
from dotenv import load_dotenv

load_dotenv()
description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

booster_channel_env = os.getenv('booster_channel')
mod_channel_env = os.getenv('mod_channel')
booster_name_env = os.getenv('booster_name')
mod_name_env = os.getenv('mod_name')
notify_channel_env = os.getenv('notify_channel')


#booster_channel_env = os.environ.get('booster_channel')
#mod_channel_env = os.environ.get('mod_channel')
#booster_name_env = os.environ.get('booster_name')
#mod_name_env = os.environ.get('mod_name')
#notify_channel_env = os.environ.get('notify_channel')

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name="boostrole", aliases=['boostr'])
async def boostrole(ctx, member: discord.Member):
    roleName = member.name + "#"+member.discriminator
    guild = ctx.guild
    user = member
    author = ctx.author
    cid = ctx.message.channel.id

    boosterChannelId = booster_channel_env
    modbotChannelId = mod_channel_env


    modRoleName = mod_name_env

    #by name
    modRole = discord.utils.get(guild.roles, name=modRoleName)
    if modRole in author.roles:
        isMod = True
    else:
        isMod = False

    role = discord.utils.get(guild.roles, name=roleName)

    isInBoost = str(cid) == boosterChannelId
    isInMod = str(cid) == modbotChannelId

    if isInBoost or isInMod:
        if isMod:
            if role is None:
                # Doesn't exist, create the role here
                await ctx.send("Creating role: **"+roleName+"**")
                await guild.create_role(name=roleName)
                role = discord.utils.get(ctx.guild.roles, name=roleName)
                await ctx.send(ctx.author.mention+", please move the user's role above the Server Booster role.")
            else:
                await ctx.send("Role: **"+roleName+"** exists")

            if role not in member.roles:
                await user.add_roles(role)
                await ctx.send("Added: "+ member.mention +" to **"+roleName+"**")
            else:
                await ctx.send("User is already in **"+roleName+"**")
        else:
            await ctx.send("You must be a @Moderator to run this command.")


@bot.command(name="boostrolecolor", aliases=['boostrc'])
async def boostrolecolor(ctx, member: discord.Member, ucolor):
    roleName = member.name + "#"+member.discriminator

    boosterChannelId = booster_channel_env
    modbotChannelId = mod_channel_env
    notifyChannel = notify_channel_env
    cid = ctx.message.channel.id
    author = ctx.author
    colorCode = int(ucolor, 16)
    guild = ctx.guild
    user = member


    #modRoleName = "Moderator"
    modRoleName = mod_name_env
    #boostRoleName = "Server Booster"
    boostRoleName = booster_name_env

    #by name
    modRole = discord.utils.get(guild.roles, name=modRoleName)
    if modRole in author.roles:
        isMod = True
    else:
        isMod = False

    #by name
    boosterRole = discord.utils.get(guild.roles, name=boostRoleName)
    if boosterRole in author.roles:
        isBoost = True
    else:
        isBoost = False


    role = discord.utils.get(guild.roles, name=roleName)

    isInBoost = str(cid) == boosterChannelId
    isInMod = str(cid) == modbotChannelId
    channel = bot.get_channel(int(notifyChannel))

    if isInBoost or isInMod:
        if isMod:
            if role is None:
                # Doesn't exist, create the role here
                await ctx.send("Creating role: "+roleName+" of Color: "+ucolor)
                await guild.create_role(name=roleName, colour=discord.Colour(colorCode))
                role = discord.utils.get(ctx.guild.roles, name=roleName)
                await ctx.send(ctx.author.mention+", please move the user's role above the Server Booster role.")
            else:

                await ctx.send("Setting Role: **"+roleName+"** color to "+ucolor)
                await role.edit(colour=discord.Colour(colorCode))

            if role not in member.roles:
                await user.add_roles(role)
                await ctx.send("Added: "+ member.mention +" to **"+roleName+"**")
            else:

                await ctx.send("User is already in **"+roleName+"**")
        else:
            if isBoost:
                if role is None:
                    await ctx.send("Role does not exist. Please contact a @Moderator")
                else:
                    await ctx.send("Setting Role: **"+roleName+"** color to "+ucolor)
                    await role.edit(colour=discord.Colour(colorCode))
            else:
                await ctx.send("Only Boosters can run this command! Get out of this channel!")
                uroles = ctx.message.author.roles
                urole_names = []
                for rol in uroles:
                    urole_names.append(rol.name)
                urole_names.pop(0)
                await channel.send("User "+member.mention+" not detected as Booster. Roles: ")
                await channel.send(urole_names)
                print('User {0.name}#{0.discriminator} not detected as Booster.'.format(member))
                print("Roles: ")
                for ro in ctx.message.author.roles:
                        print("\t", ro.name)



token = os.environ.get('bot_token')
bot.run(token)