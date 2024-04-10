import asyncio
import json

from aiogram import types
from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = Bot(token="7015553058:AAFOnBCvk4v0oNZSLMIY7mq3fxRghOSrnj4")
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    
    item1 = KeyboardButton(text=" 🛍 Internet magazin", web_app=WebAppInfo(url="https://bahrom88ak.github.io/"))
    item2 = KeyboardButton(text="✍️ Uyda utirib ishlash uchun ariza yuborish", web_app=WebAppInfo(url="https://faberlic.com/"))
    item3 = KeyboardButton(text="🚀 Ishga kirganla uchun maxsus ilova", web_app=WebAppInfo(url="https://apps.rustore.ru/app/com.faberlic"))
    keyboard = ReplyKeyboardMarkup (keyboard=[[item1],[item2],[item3]], resize_keyboard=True)
    await bot.send_message(message.from_user.id, "Assalomu aleykum! * Faberli3 🛍 * shaxsiy gruxga obuna bulishni unutmang https://t.me/FABERLI3  Men shaxsiy bot xizmatidan foydalanganim sabab ishim juda kup ulgurmayapman, online ishga kirish va sotib olish saxifa mavjud! tugmalardan foydalanib xarid qilish yoki ishga kirishingiz mumkin🙂 Botni qayta ishga tushirish tugmasi /start ", reply_markup=keyboard, parse_mode="Markdown")
    

@dp.message()
async def web_app(callback_query):
    json_data = callback_query.web_app_data.data
    parsed_data = json.loads(json_data)
    message = ""
    for i, item in enumerate(parsed_data['items'], start=1):
        position = int(item['id'].replace('item', ''))
        message += f"Позиция {position}\n"
        message += f"Стоимост: {item['price']}\n\n"

    message += f"Общая стоимост товара:{parsed_data['totalPrice']}"

    await bot.send_message(callback_query.from_user.id, f""")
{message}
""")
    await bot.send_message('6005830556', f"""
Новый Заказ
{message}
""")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
