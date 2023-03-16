from pyrogram import Client, filters

bot = Client(
    "My first Project",
    api_id = "10738943",
    api_hash = "da61e3a08b5ac78ce28b4a4cd854aeec",
    bot_token = "5974422696:AAEGU0ZYnhgrNeNlpf_Nw8dPbbt00Wmctpc"
)

@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, "Heya, I am  a simple testing Bot")

bot.run()

