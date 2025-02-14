from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '7289568184:AAFhXh6UVR0-deFXB6aD-cDkHr4ZGPbp9jo'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands = ["start"]))
async def process_start_command(message:Message):
    await message.answer('Привет!\nМеня зовут эхо-бот!\nНапиши мне что-нибудь!')

@dp.message(Command(commands = ["help"]))
async def process_start_command(message:Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')

@dp.message()
async def process_start_command(message:Message):
    await message.send_message(text = message.text)

if __name__ == '__main__':
    dp.run_polling(bot)