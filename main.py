import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types

from models import session, Payment, User

API_TOKEN = os.environ.get('TELEGRAM_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['go'])
async def start_handler(message):
    await message.answer('Go Johny Go!')


@dp.message_handler()
async def handler(message: types.Message):
    #msg = bot.send_message(message.chat.id, 'Откуда парсить?')
    #m = bot.register_next_step_handler(msg, askForWhat)

    if message.text.isdigit():
        user = session.query(User).get(1)

        payment = Payment(amount=float(message.text), user_id=user.id, goal='soe' )
        session.add(payment)
        session.commit()

    await message.answer([i.amount for i in session.query(Payment).all()])



def askForWhat(message):
    return message.text


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
