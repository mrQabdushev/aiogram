import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

TOKEN = "5104047796:AAGfvvthefht18MLS3PngdBvdKFFx99FgXc"
id = 152071291

#loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode="HTML") #<i>Italic</i>, <b>Bold</b>
dp = Dispatcher(bot)

async def send_to_admin(dp):
    await bot.send_message(chat_id=id, text="Salem, Demalaiyqsh")

@dp.message_handler()
async def echo(message: Message):
    text = f"Salem, ty tochno immel v vidu: {message.text}"
    await bot.send_message(chat_id=message.from_user.id, text=text)

executor.start_polling(dp)
# if __name__ == "__main__":
#     executor.start_polling(dp)