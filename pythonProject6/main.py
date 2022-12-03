import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5765230906:AAFnoejgqqbKmkWc9KGJCnmt97jJOpwbBNw")
dp = Dispatcher(bot)


from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
greet_markup = ReplyKeyboardMarkup()
button_hi = KeyboardButton("/help")
greet_markup.add(button_hi)
button_1 = KeyboardButton("Кто ты?")
greet_markup.add(button_1)
button_2 = KeyboardButton("Ты бот?")
greet_markup.add(button_2)
button_3 = KeyboardButton("Умножить")
greet_markup.add(button_3)
button_4 = KeyboardButton("Отнять")
greet_markup.add(button_4)
button_5 = KeyboardButton("Прибавить")
greet_markup.add(button_5)
button_6 = KeyboardButton("Разделить")
greet_markup.add(button_6)
button_7 = KeyboardButton("анекдот.1")
greet_markup.add(button_7)
button_8 = KeyboardButton("анекдот.2")
greet_markup.add(button_8)
button_9 = KeyboardButton("анекдот.3")
greet_markup.add(button_9)
button_10 = KeyboardButton("анекдот.4")
greet_markup.add(button_10)
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Здарова ботик!Я умею выполнять команды Кто ты?,Ты бот?,умножить,Отнять,прибавить,Разделить?,а также анекдот.[цифра]",reply_markup=greet_markup)


@dp.message_handler(commands="getPos")
async def cmd_test(message: types.Message):
    await message.reply("Будущая команда пока в разработке")


i = 1


@dp.message_handler()
async def cmd_text(message: types.Message):
    if message.text == "Кто ты?":
        await bot.send_message(message.from_user.id, "Я ашот")
    elif message.text == "Ты бот?":
        await bot.send_message(message.from_user.id, "Нет")
    elif message.text == "Умножить":
        global i
        i = i * 2
        await bot.send_message(message.from_user.id, str(i))

    elif message.text == "Отнять":
        i = i - 2
        await bot.send_message(message.from_user.id, str(i))
    elif "Прибавить" in message.text:
        i = i + 2
        await bot.send_message(message.from_user.id, str(i))
    elif message.text == "Разделить":
        i = i / 2
        await bot.send_message(message.from_user.id, str(i))
    elif message.text == "Что ты умеешь?":
        await bot.send_message(message.from_user.id, "Я могу: Разделить, Умножить, Ты бот?, Ты кто? и д. р. ")
    elif message.text == "анекдот.1":
        await bot.send_message(message.from_user.id, "\nНепонятно почему штаны, в которых лучше всего лежать на диване, называются «спортивные»")
    elif message.text == "анекдот.2":
        await bot.send_message(message.from_user.id,  "Штирлиц напоил кошку бензином.Кошка прошла два метра и упала.Бензин закончился,подумал Штирлиц.")
    elif message.text == "анекдот.3":
        await bot.send_message(message.from_user.id,  "Сидят две девочки.Одна смеется,другая плачет.Приходит мужик и говорит:Девочка,Что ты плачешь?А ты девочка,что ты смеешься?Говорит та,что смеется:а там теть Люба белье на балконе вешала,и упала с балкона!Девочка,как ты можежь смеяться из-за этого?А я не с этого смеюсь!А что она не видела!И он спрашивает ту,что плачет:а ты что плачешь?А я не видела!!!!!")
    elif message.text == "анекдот.4":
        await bot.send_message(message.from_user.id, "Бабушка две недели играла с внуком в школу. К концу второй недели она узнала, что делает за него домашнее задание")
    else:
        await  bot.send_message(message.from_user.id, 'Мне нечего ответить')
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)