import os
import time
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import keyboard
TOKEN = "TOKEN"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Alt+Tab")
    button_2 = types.KeyboardButton(text="Alt+F4")
    button_3 = types.KeyboardButton(text="Enter")
    button_4 = types.KeyboardButton(text="Shut down")
    button_5 = types.KeyboardButton(text="mute")
    button_6 = types.KeyboardButton(text="next video")
    button_7 = types.KeyboardButton(text="Full screan")
    button_8 = types.KeyboardButton(text="pause")
    button_9 = types.KeyboardButton(text="back")
    button_10 = types.KeyboardButton(text="next")
    button_11 = types.KeyboardButton(text="pause")
    button_12 = types.KeyboardButton(text="back")
    button_13 = types.KeyboardButton(text="Pycharm")
    keyboard.add(button_1)
    keyboard.add(button_2)
    keyboard.add(button_3)
    keyboard.add(button_4)
    keyboard.add(button_5)
    keyboard.add(button_6)
    keyboard.add(button_7)
    keyboard.add(button_8)
    keyboard.add(button_9)
    keyboard.add(button_10)
    keyboard.add(button_11)
    keyboard.add(button_12)
    keyboard.add(button_13)

    await message.answer("Это все я умею", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "next video")
async def next_video(message: types.Message):
    keyboard.send("shift+n")
    await message.reply("next video")


@dp.message_handler(lambda message: message.text == "Full screan")
async def full_screan(message: types.Message):
    keyboard.send("f")
    await message.reply("Right click")

@dp.message_handler(lambda message: message.text == "pause")
async def pause(message: types.Message):
    keyboard.send("k")
    await message.reply("pause")

@dp.message_handler(lambda message: message.text == "next")
async def next(message: types.Message):
    keyboard.send("right")
    await message.reply("right")


@dp.message_handler(lambda message: message.text == "back")
async def back(message: types.Message):
    keyboard.send("left")
    await message.reply("back")

@dp.message_handler(lambda message: message.text == "Pycharm")
async def pycharm(message: types.Message):
    os.system(r'C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\bin\pycharm64.exe')
    await message.reply("Pycharm")






@dp.message_handler(lambda message: message.text == "Alt+Tab")
async def alt_tab(message: types.Message):
    keyboard.send("alt+tab")
    await message.reply("Alt+Tab")

@dp.message_handler(lambda message: message.text == "Alt+F4")
async def alt_f4(message: types.Message):
    keyboard.send("Alt+F4")
    await message.reply("Alt+F4")

@dp.message_handler(lambda message: message.text == "Enter")
async def enter(message: types.Message):
    keyboard.send("Enter")
    await message.reply("Enter")

@dp.message_handler(lambda message: message.text == "Shut down")
async def shut_down(message: types.Message):
    os.system('systemctl poweroff')
    await message.reply("Alt+Tab")

@dp.message_handler(lambda message: message.text == "mute")
async def mute(message: types.Message):
    keyboard.send("m")
    await message.reply("mute")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    text = msg.text.split()
    if text[0] == "/write":
        del text[0]
        text = " ".join(text)
        keyboard.write(text)
    elif text[0] == "/send":
        del text[0]
        text = " ".join(text)
        keyboard.send(text)
    elif text[0] == "/do_command":
        del text[0]
        text = " ".join(text)
        keyboard.send("win+r")
        time.sleep(0.5)
        keyboard.write("cmd")
        time.sleep(0.01)
        keyboard.send("enter")
        time.sleep(1)
        keyboard.write(text)
        time.sleep(0.01)
        keyboard.send("enter")
    elif text[0] == "/do_hack":
        keyboard.send("win+r")
        time.sleep(0.5)
        keyboard.write("cmd")
        time.sleep(0.01)
        keyboard.send("enter")
        time.sleep(1)
        keyboard.send("F11")
        time.sleep(0.1)
        keyboard.write("color a")
        time.sleep(0.01)
        keyboard.send("enter")
        keyboard.write("for /l %q in (0) do tree")
        time.sleep(0.01)
        keyboard.send("enter")
    elif text[0] == "/finish":
        exit()
    elif text[0] == "/close":
        keyboard.send("Alt+F4")

while True:      # Старт бота
   executor.start_polling(dp)
