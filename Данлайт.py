import discord
import random
from discord.ext import tasks, commands
import asyncio
import nekos
import os
import time
from discord.utils import get
Bot = commands.Bot(command_prefix= "+")
Bot.remove_command('help')

@Bot.command()
async def help(ctx):
	embed = discord.Embed(title= "разделы:", description="", color=0xeee657)
	embed.add_field(name="helpstuff", value="help команда для модераторов", inline=False)
	embed.add_field(name="helpcustom", value="кастомные команды, то есть,для приколюх", inline=False)
	await ctx.send(embed=embed)

@Bot.command()
async def helpstuff(ctx):
    embed = discord.Embed(title="commands", description="", color=0xeee657)
    embed.set_footer(text='help command 1/2.')
    embed.add_field(name="mute", value="мутить нарушителей", inline=False)
    embed.add_field(name="unmute", value="размутить нарушителя", inline=False)
    embed.add_field(name="tempmute", value="замутить участника сервера на время", inline=False)
    embed.add_field(name="ban", value="забанить нарушителя", inline=False)
    embed.add_field(name="kick", value="кикнуть нарушителя", inline=False)
    await ctx.send(embed=embed)


@Bot.command()
async def helpcustom(ctx):
    embed = discord.Embed(title="commands", description="", color=0xeee657)
    embed.set_footer(text='help command 2/2.')
    embed.add_field(name="kiss", value="поцеловать участника сервера", inline=False)
    embed.add_field(name="hug", value="обнять участника сервер", inline=False)
    embed.add_field(name="slap", value="шлёпнуть участника сервера", inline=False)
    embed.add_field(name="шар", value="гадание", inline=False)
    embed.add_field(name="avatar", value="показывает аватар участника", inline=False)
    embed.add_field(name="teleportation", value="телепортировать участника с 1 голосовго канала на вторую", inline=False)
    embed.add_field(name="pat", value="погладить участника", inline=False)
    await ctx.send(embed=embed)


@Bot.command()
@commands.has_permissions(administrator= True)
async def unmute(ctx, member : discord.Member = None ):
                    await ctx.message.delete()
                    if not member:
                        ctx.send("Укажите пользователя!")
                    else:
                        membern = member.nick
                        if member.nick == None:
                            membern = member.name
                        unmute_cnt = f"Пользователь {membern} был размучен админом {ctx.author}!"
                        unmute = discord.Embed(title= "UnMute", description= unmute_cnt, colour= 0x000000)
                        role = discord.utils.get(ctx.message.guild.roles, name="Muted")
                        await member.remove_roles(role)
                        await ctx.send(embed= unmute)           

@Bot.command(pass_context= True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason = None):
            await ctx.guild.ban(user)
            emb = discord.Embed(title = "*** Пользователь {} был забанен***".format(user), colour= 0x42f4f4)
            await ctx.send(embed= emb)        
            await member.ban( reason = reason)

@Bot.command(pass_context= True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
                        await ctx.guild.kick(user)
                        emb = discord.Embed(title = "*** Пользователь {} был кикнут***".format(user), colour= 0x42f4f4)
                        await ctx.send(embed= emb)

@Bot.command()                 
async def avatar(ctx, member : discord.Member = None):
                            user = ctx.message.author if (member == None) else member
                            await ctx.messkage.delete()
                            embed = discord.Embed(title=f'Аватар пользователя {user}', description= f'[Ссылка на изображение]({user.avatar_url})', color=user.color)
                            embed.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
                            embed.set_image(url=user.avatar_url)
                            await ctx.send(embed=embed)

@Bot.command()
async def ping(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    emb = discord.Embed(
        title= 'Текущий пинг',
        description= f'{Bot.ws.latency * 1000:.0f} ms'
    )
    await ctx.send(embed=emb) 
      
@Bot.command()
@commands.has_permissions(administrator = True)
async def say(ctx, channel: discord.TextChannel, *, text):
    attachments = ctx.message.attachments
    emb = discord.Embed(
        description = text,
        colour = 0x00ff80
    )
    for a in attachments:
        if a.url != None:
            emb.set_image(url= f"{a.url}")    
    await channel.send(embed=emb)
    await ctx.message.delete() 

@Bot.command()
async def cat(ctx):
            await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")                               

@Bot.command()
async def dog(ctx):
            await ctx.send("https://media.tenor.com/images/a0e28d22bb8f37bc83e1d4d1f1337e2b/tenor.gif")                                             

                      
     
@Bot.event
async def on_ready():
        await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="PornHub | +help"))
print("Я запущен !")
                        
@Bot.command()
async def on_command_error(ctx, error):
         if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send(f'error 404 {ctx.message.author.mention}') 
      
@Bot.command()
@commands.has_permissions(administrator= True)
async def clear(ctx, amount: int):
            await ctx.channel.purge(limit=amount)
            await ctx.send("ваши сообщении удалились")

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        EMerror = discord.Embed(
    title = 'Error!',
    description = 'The command prefix is"+".',
    colour = discord.Colour.red()
    )
    EMerror.set_footer(text='by Lyamch.')
    EMerror.set_image(url='')
    EMerror.set_thumbnail(url='')
    EMerror.set_author(name='', icon_url='')
    EMerror.add_field(name='Error', value='clear [amount].', inline=True)
    await ctx.send(embed=EMerror)

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        EMerror = discord.Embed(
    title = 'Error!',
    description = 'The command prefix is"+".',
    colour = discord.Colour.red()
    )
    EMerror.set_footer(text='by Lyamch.')
    EMerror.set_image(url='')
    EMerror.set_thumbnail(url='')
    EMerror.set_author(name='', icon_url='')
    EMerror.add_field(name='Error', value='say [argument].', inline=True)
    await ctx.send(embed=EMerror)



@Bot.command(pass_context=True, aliases=["whois", "info" ])
 
async def userinfo(ctx, member: discord.Member):

    roles = [role for role in member.roles]



    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f'User Info -{member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)


    embed.add_field(name='ID:', value=member.id)
    embed.add_field(name='Guild name:', value=member.display_name)

    embed.add_field(name='Created at:', value=member.created_at.strftime('%a, %#d %B %Y %I:%M %p EST'))
    embed.add_field(name='Joined at:', value=member.joined_at.strftime('%a, %#d %B %Y %I:%M %p EST'))

    embed.add_field(name=f'Roles ({len(roles)})', value=' '.join([role.mention for role in roles]))

    embed.add_field(name='Top role:', value=member.top_role.mention)
    
    embed.add_field(name='Bot?', value=member.bot) 

    await ctx.send(embed=embed)
    
@Bot.command()
async def kiss(ctx, member : discord.Member):
    await ctx.message.delete()
    emb = discord.Embed(description= f'{member.mention}, Вас поцеловал(а) {ctx.message.author.mention}.')
    await ctx.send(embed=emb)

@Bot.command()
async def hug(ctx, member : discord.Member):
    await ctx.message.delete()
    emb = discord.Embed(description= f'{member.mention}, Вас обнял(а) {ctx.message.author.mention}.')
    await ctx.send(embed=emb)

@Bot.command()
async def slap(ctx, member : discord.Member):
    await ctx.message.delete()
    emb = discord.Embed(description= f'{member.mention}, Вас ударил(а) {ctx.message.author.mention}.')
    await ctx.send(embed=emb)

@Bot.command()
async def pat(ctx, member : discord.Member):
    await ctx.message.delete()
    emb = discord.Embed(description= f'{member.mention}, Вас погладил(а) {ctx.message.author.mention}.')
    await ctx.send(embed=emb)

@slap.error
async def slap_error(ctx, error):
	 if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("+slap [ping]")
          
@hug.error
async def hug_error(ctx, error):
	 if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("+hug [ping]")

@kiss.error
async def kiss_error(ctx, error):
	 if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("+kiss [ping]")

@pat.error
async def pat_error(ctx, error):
	 if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("+pat [ping]")

@Bot.command(pass_context=True)
@commands.has_permissions(manage_roles = True)
async def addrole(ctx, member : discord.Member, *, role : discord.Role):
    await member.add_roles(role)
    await ctx.send(f"added the role '{role}' to {member}!") 
  
@Bot.command(pass_context=True)
@commands.has_permissions(manage_roles = True)
async def removerole(ctx, member : discord.Member, *, role : discord.Role):
    await member.remove_roles(role)
    await ctx.send(f"removed the role '{role}' to {member}!") 
                  
@Bot.command()
@commands.has_permissions(administrator = True) 
async def tempmute(ctx, member : discord.Member, time: int, *, reason=None):
																
	role = discord.utils.get(member.guild.roles,name="Muted")()
	await member.add_roles(role, reason=reason)
	await asyncio.sleep(time)
	await member.remove_roles(role)
   
@Bot.command(pass_context=True, aliases=["telep", "tp" ])
async def teleportation(ctx, arg=None, member: discord.Member = None):
        channels = ctx.author.voice.channel.id
        await ctx.message.delete()
        if not channels:
            await ctx.send('Нужно находиться в войсе', delete_after=10)
            return
        if not arg:
            await ctx.send('Нужно указать, куда переместить юзеров', delete_after=10)
            return
        voice = ctx.guild.voice_channels
        print(voice)
        try:
            vchannel = voice[int(arg) - 1]
        except:
            await ctx.send('Неправильный аргумент', delete_after=10)
            return
        if member == None:
            x = ctx.author.voice.channel.members
            for mem in x:
                    await mem.edit(voice_channel=vchannel)
        else:
            await member.edit(voice_channel=vchannel)
 
@Bot.event
async def on_member_join(member):
       role = get (member.guild.roles, name=Member)
       await Bot.add_roles(role)
       print(f"{member} далась роль {role}")
    
@Bot.event
async def on_ready():
     print('Logged in as')
     print('Moderation 2')
  
@Bot.event
async def on_member_join(member):
  print (f' {member} has joined a server.')

@Bot.event
async def on_member_remove(member):
  print (f' {member} has left a server.')

@Bot.command(aliases =['8ball'])
async def шар(ctx, *, question):
	await ctx.send(random.choice(["конечно",
	           "да",
	           "предврешено!",
	            "нет",
	             "конечно, нет",
	             "соглашусь",
	             "Хорошие перспективы :ok_hand:",
	             "мой ответ, нет :no_entry_sign"]))

@Bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '669423907874406444':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)
 
@Bot.command(pass_context = True)
async def softban(self, ctx, member: discord.Member):
        server = ctx.message.server
        if ctx.message.author.server_permissions.kick_Members:
            try:
                await self.bot.ban(member)
                await self.bot.unban(server, member)
                await self.bot.say('{} was softbanned'.format(member))
            except discord.Forbidden:
                await self.bot.say('I need **Ban Members** for this') 
 
@Bot.command()
@commands.has_permissions(ban_members=True)
async def warn(self, ctx, user: discord.Member, warnpoints: int, *, reason: str = "No reason specified"):
        addWarnPoints(user.id, warnpoints)
        if int(getWarnPoints(user.id)) >= 1000:
            await self.bot.ban(user)
        else:
            pass
        
        server = ctx.message.server
        if (server.id in admin["servers"]):
            log_channel = server.get_channel(admin["servers"][server.id])
        
        userID = (user.id)
        embed = discord.Embed(title="Member Warned", color = 0xB657D1)
        embed.add_field(name="Member", value="{} ".format(user) + "(<@{}>)".format(userID), inline=False)
        embed.add_field(name="Mod", value="{}".format(ctx.message.author), inline=True)
        embed.add_field(name="Increase", value = warnpoints, inline=True)
        embed.add_field(name="Reason", value="{}".format(reason), inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        embed.timestamp = datetime.utcnow()

@Bot.event
async def on_member_join(member):
	channel = discord.utils.get(member.guild.channels, name='👋║новички')
	emb = discord.Embed(description=f'добро пожаловать на сервер! {member.mention}')
	role = discord.utils.get(member.guild.roles, name='👉🏻Новичок👈🏻| 1 лвл |')
	await member.add_roles(role)
	await ctx.send(embed=emb)
    
Bot.run('NjA5NDAzNjc1NTg4NDI3Nzc4.XisUsw.3xTP2LNnBp2fvuLEKNSjW6wqYq8');