import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboards.default import till

DataBase = {
    'User_id': [],
}

# Set up logging
logging.basicConfig(level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
API_TOKEN = '6597297326:AAENgyOMwxllHeuLmG_SVMgoHZz5KuakF1k'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
from Keyboards.default import vacansy1


class VacansyStates(StatesGroup):
    naming = State()
    age = State()
    tex = State()
    tel = State()
    hud = State()
    price = State()
    kasb = State()
    maqsad = State()
    Carier = State()


@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await message.answer(message.from_user.id)
    await message.answer(f'''
<b>Assalom alaykum {message.from_user.first_name}</b>
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!
''', reply_markup=vacansy1)


@dp.message_handler(text='Ish joyi kerak')
async def ish_joyI(message: types.Message, state=FSMContext):
    await message.answer('''
<b>Ish joyi topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
''')
    await message.answer('<b>Ism Familyangizni kiriting !</b>')
    await VacansyStates.naming.set()


@dp.message_handler(state=VacansyStates.naming, content_types=types.ContentType.TEXT)
async def naming_writer(message: types.Message, state=FSMContext):
    ismi = message.text
    DataBase[str(message.from_user.id)] = [ismi]
    await message.answer('Yoshingizni kirting!')
    await state.finish()
    await VacansyStates.age.set()


@dp.message_handler(state=VacansyStates.age, content_types=types.ContentType.TEXT)
async def age_write(message: types.Message, state=FSMContext):
    age_user = message.text
    qalesan = DataBase.get(str(message.from_user.id))
    qalesan.append(age_user)
    await message.answer('''
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
''')
    await state.finish()
    await VacansyStates.tex.set()


@dp.message_handler(state=VacansyStates.tex, content_types=types.ContentType.TEXT)
async def texnalogiya(message: types.Message, state=FSMContext):
    tex_user = message.text
    qalesan1 = DataBase.get(str(message.from_user.id))
    qalesan1.append(tex_user)

    await message.answer('''
📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
    ''')
    await state.finish()
    await VacansyStates.tel.set()


@dp.message_handler(state=VacansyStates.tel, content_types=types.ContentType.TEXT)
async def telefon(message: types.Message, state=FSMContext):
    tel_user = message.text
    qalesan2 = DataBase.get(str(message.from_user.id))
    qalesan2.append(tel_user)
    await message.answer('''
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
    ''')
    await state.finish()
    await VacansyStates.hud.set()


@dp.message_handler(state=VacansyStates.hud, content_types=types.ContentType.TEXT)
async def hudud(message: types.Message, state=FSMContext):
    hud_user = message.text
    qalesan3 = DataBase.get(str(message.from_user.id))
    qalesan3.append(hud_user)
    await message.answer('''
💰 Narxi:

ㅤ·•• печатает ㅤ, [8/23/2023 3:54 PM]
Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
        ''')
    await state.finish()
    await VacansyStates.price.set()


@dp.message_handler(state=VacansyStates.price, content_types=types.ContentType.TEXT)
async def price_writer(message: types.Message, state=FSMContext):
    price_user = message.text
    qalesan4 = DataBase.get(str(message.from_user.id))
    qalesan4.append(price_user)
    await message.answer('''
👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
        ''')
    await state.finish()
    await VacansyStates.kasb.set()


@dp.message_handler(state=VacansyStates.kasb, content_types=types.ContentType.TEXT)
async def kasb_writer(message: types.Message, state=FSMContext):
    kasb_writer = message.text
    qalesan4 = DataBase.get(str(message.from_user.id))
    qalesan4.append(kasb_writer)
    await message.answer('''
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
    ''')
    await state.finish()
    await VacansyStates.maqsad.set()


@dp.message_handler(state=VacansyStates.maqsad, content_types=types.ContentType.TEXT)
async def maqsad_writer(message: types.Message, state=FSMContext):
    maqsad_writer = message.text
    qalesan5 = DataBase.get(str(message.from_user.id))
    qalesan5.append(maqsad_writer)
    await message.answer('''
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
    ''')
    await state.finish()
    await VacansyStates.Carier.set()


@dp.message_handler(state=VacansyStates.Carier, content_types=types.ContentType.TEXT)
async def carier_writer(message: types.Message, state=FSMContext):
    print(DataBase)
    malumotcha = DataBase.get(str(message.from_user.id))
    print(type(malumotcha))
    print(malumotcha)
    await message.answer(f'''
👨Ish joyi kerak:

👨‍💼 Xodim: {malumotcha[0]}
🕑 Yosh: {malumotcha[1]}
📚 Texnologiya: {malumotcha[2]}
🇺🇿 Telegram: {message.from_user.username}
📞 Aloqa: {malumotcha[3]}
🌐 Hudud: {malumotcha[4]}
💰 Narxi:  {malumotcha[5]}
👨🏻‍💻 Kasbi: {malumotcha[6]}
🕰 Murojaat qilish vaqti: {malumotcha[7]}
    ''')
    await bot.send_message(1393750405, f'Yangi Xabar keldi {message.from_user.username} dan')
    await bot.send_message(1393750405, f'''
👨Ish joyi kerak:

👨‍💼 Xodim: {malumotcha[0]}
🕑 Yosh: {malumotcha[1]}
📚 Texnologiya: {malumotcha[2]}
🇺🇿 Telegram: {message.from_user.username}
📞 Aloqa: {malumotcha[3]}
🌐 Hudud: {malumotcha[4]}
💰 Narxi:  {malumotcha[5]}
👨🏻‍💻 Kasbi: {malumotcha[6]}
🕰 Murojaat qilish vaqti: {malumotcha[7]}
    ''')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
