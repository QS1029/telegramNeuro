from aiogram import executor, Dispatcher, Bot, types
from config import TELEGRAM_TOKEN
from neuroBot.neuro_gen import generate_image
from neuroBot.neuro_assistent import get_response

API_KEY = TELEGRAM_TOKEN
bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

@dp.message_handler(commands = 'start')
async def func_start(message: types.Message):
    await message.answer("Приветик. Я твой шедеврум за 20 копеек.")

# @dp.message_handler()
# async def analize_message(message:types.Message):
#     response_text = await get_response((message.text))
#     await message.answer(response_text)

@dp.message_handler()
async def handle_message(message: types.Message):
    response_text = await get_response((message.text))
    user_text = response_text
    await message.reply('Генерирую, жди.')
    try:
        image_data = generate_image(user_text)
        await message.reply_photo(photo=image_data)
    except Exception as e:
        await message.reply(f"Произошла ошибка, wallahi... {e}")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)