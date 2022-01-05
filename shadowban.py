from discord.ext import commands
bot = commands.Bot(command_prefix="!")

shadowbanned_users = [] #TODO add user ids to ban here
@bot.listen()
async def on_message(message):
    msg_cnt = message.content.lower()
    print('message', message)
    if message.author.id in shadowbanned_users:
        await message.delete()

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None and member.id in shadowbanned_users:
       await member.move_to(None)

bot.run('') #TODO add the bot here
