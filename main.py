


#--- BOT ---
import discord, aiohttp, io, random, string, requests, os
import colorama
from colorama import Fore, Style
from keep_alive import keep_alive
keep_alive()
from datetime import datetime
from time import sleep
from discord.ext import commands
now = datetime.now()
ftime = now.strftime("%H:%M:%S")
from colorama import Fore, Back, Style

TOKEN = os.environ['tokenn']

token = (TOKEN)

ping = False

os.system("title Satanic Self Bot v3.01 Made by Londres#0001")

print(f'''{Fore.RESET}
{Fore.RED}███████╗ █████╗ ████████╗ █████╗ ███╗   ██╗██╗ ██████╗
{Fore.RED}██╔════╝██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔════╝
{Fore.RED}███████╗███████║   ██║   ███████║██╔██╗ ██║██║██║     
{Fore.RED}╚════██║██╔══██║   ██║   ██╔══██║██║╚██╗██║██║██║     
{Fore.RED}███████║██║  ██║   ██║   ██║  ██║██║ ╚████║██║╚██████╗
{Fore.RED}╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝''' + Fore.RESET)
prefix = "$" 
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")
print(f'''{Fore.RESET}
{Fore.RED}[{Fore.GREEN}Credits{Fore.RED}] {Fore.MAGENTA}https://discord.gg/mota
{Fore.RED}[{Fore.GREEN}Prefix{Fore.RED}] {Fore.MAGENTA}$
{Fore.RED}[{Fore.GREEN}Commands{Fore.RED}] {Fore.MAGENTA}$help

                                ''' + Fore.RESET)


@bot.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
	       format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))
@bot.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send("**Help Self Bot Satanic 👻**\n**Prefix** **$**\n```purge - delete you meesage history\nowner - invite link owner server\nnitro - nitro generator code\nnuke - destroy server\navatar<user> - show avatar user\ncopy - copy server template\nstream - activity streaming\nread - read message all\ndmall - dm all user server\ndmusers<user> <message> - dm user mention\nfox - fox show image\ndog - dog show image```")

@bot.command(aliases=['server', 'code'])
async def owner(ctx):
    await ctx.message.delete()
    await ctx.send("https://discord.gg/mota")

@bot.command()
async def clean(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

@bot.command()
async def dmall(ctx, *, args=None): # b'\xfc'
    if args != None:
        members = ctx.guild.members
        for members in members:
            try:
                await members.send(args)
                print("'" + args + " ' sent to: " + members.name)
            except:
                print("Couldnt send '" + args + "' to" + members.name)
    else:
        await ctx.channel.send("You didnt provide arguments.")

@bot.command()
async def dmusers(ctx, *, message):  # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(1)
            await user.send(message)
            print("'" + args + " ' sent to: " + members.name)
        except:
            pass

@bot.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])  

@bot.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message'])) 

@bot.command()
async def copy(ctx): # b'\xfc'
    await ctx.message.delete()
    await bot.create_guild(f'{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in bot.guilds:
        if f'{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@bot.command()
async def nuke(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=pwned-by-abusando(),
            description="!                    abusando#1337",
            reason="!                    abusando#1337",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name=pwned-by-abusando())
    for _i in range(250):
        await ctx.guild.create_role(name=pwned-by-abusando(), color=RandomColor())

@bot.command()
async def nitro(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(Nitro())

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

@bot.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await bot.change_presence(activity=stream)   

@bot.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx): # b'\xfc'
    await ctx.message.delete()
    clear()

@bot.command(aliases=['markasread', 'ack'])
async def read(ctx): # b'\xfc'
    await ctx.message.delete()
    for guild in bot.guilds:
        await guild.ack()
 
@bot.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@bot.command(alises=['clear','pg'])
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass


bot.run(token, bot=False)
