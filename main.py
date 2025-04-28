# Maybe Work. IDK
import discord
import colorama
import asyncio
from discord.ext import commands, tasks
from colorama import Fore

colorama.init()

intents = discord.Intents.all()

statuses = [
    discord.Game(name="𝕊𝕟𝕚𝕡𝕖𝕣. | Killing the Discord User"),
    discord.Game(name="𝕊𝕟𝕚𝕡𝕖𝕣. | Fucking Discord"),
    discord.Game(name="𝕊𝕟𝕚𝕡𝕖𝕣. | Rapeing Discord"),
    discord.Game(name="𝕊𝕟𝕚𝕡𝕖𝕣. | 闇に落ちている目。"),
    discord.Game(name="𝕊𝕟𝕚𝕡𝕖𝕣. | Die"),
]

with open("token.txt", "r", encoding="utf-8") as file:
    tokens = [line.strip() for line in file.readlines()]

class DMCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def X(self, ctx, id_user: int, times: int, *, message: str):
        try:
            user = await self.bot.fetch_user(id_user)
            for i in range(times):
                await user.send(f"{message}")
            print(f"{Fore.GREEN}[+] {Fore.RESET} {user}")
        except Exception as e:
            await ctx.send(f"[🔴] ERROR: {e}")

async def create_bot(token):
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"{Fore.GREEN}[+] {Fore.RESET} {bot.user}")

        rotate_status.start(bot)

    @tasks.loop(seconds=30) 
    async def rotate_status(bot):
        current_status = statuses.pop(0)  
        await bot.change_presence(activity=current_status)  
        statuses.append(current_status)  

    await bot.add_cog(DMCommands(bot))

    await bot.start(token)

async def main():
    await asyncio.gather(*(create_bot(token) for token in tokens))

asyncio.run(main())
