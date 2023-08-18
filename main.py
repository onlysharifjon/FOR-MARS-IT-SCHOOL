import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboards.default import til

# Set up logging
logging.basicConfig(level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
API_TOKEN = '6597297326:AAENgyOMwxllHeuLmG_SVMgoHZz5KuakF1k'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await message.answer('''
Assalomu aleykum! Botimizga xush kelibsiz! 
Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik.
    ''', reply_markup=til)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
