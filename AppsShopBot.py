from functools import cache
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.types import callback_query, message, reply_keyboard
from aiogram.utils import executor

import os

TOKEN = "2144505945:AAGoKEiWJSITVB0fLbgDbUGlA5wCOi4AU8k"

QIWI_TOKEN = "3b3d95a360041576ec639fbdb64b2c53"
PHONE_NUMBER = "+79869244397"

photoPrimer = open('Files/gf.png','rb')

bot = Bot(TOKEN)
dp = Dispatcher(bot)

englishSelected = False
russianSelected = False

@dp.message_handler()
async def command_func(message : types.Message):
    if message.text == "/start":
       buttons = [
           types.InlineKeyboardButton(text="КУПИТЬ 🛒",callback_data="BUY"),
           types.InlineKeyboardButton(text="ПОДДЕРЖКА 👤",callback_data="SUP"),
           types.InlineKeyboardButton(text="ПРИМЕРЫ ПРИЛ 🌅",callback_data="PRIMER"),
           types.InlineKeyboardButton(text="ЧТО ВХОДИТ В ТОВАР? 📦",callback_data="ABOUT"),
           types.InlineKeyboardButton(text="ЗАКАЗАТЬ 🛎",callback_data="SAP")
       ]

       keyboard = types.InlineKeyboardMarkup(row_width=2)
       keyboard.add(*buttons)

       await message.answer('Привествую вас в ШОПЕ ПРИЛ NERA SHOP 🎮 \n— Прилы на любой вкус от белых до черных \n— Белые вы можете купить сразу \n— Серые и Черные вы можете заказать у меня в личном чате',reply_markup=keyboard)

@dp.callback_query_handler(text_contains = "ABOUT")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
        types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK")
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=3)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('ЧТО ВХОДИТ В ТОВАР? \n — Архив с .abb прилы для загрузки \n — Папка со скриншотами, баннером и иконкой \n — GP-README.txt, Текстовый файл с благодарностью и данными для заполнения страницы приложения \n\n НИЖЕ ПРЕДСТАВЛЕН ВИД АРХИВА',reply_markup = keyboard2)
    await bot.send_photo(chat_id=call.from_user.id,photo = photoPrimer)


@dp.callback_query_handler(text_contains = "PRIMER")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
           types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK"),
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=3)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('Список всех прил сделанные за пол года \n(Некоторые прилы отсутствуют по причине бана) \n\n1. https://play.google.com/store/apps/details?id=com.BulletsGames.ArrowEndlessFlying&hl=ru&gl=US \n\n2. https://play.google.com/store/apps/details?id=com.NastyGames.TaptoBalloons&hl=ru&gl=US \n\n3. https://play.google.com/store/apps/details?id=com.DmitriGames.CannonShoting3D&hl=ru&gl=US \n\n4. https://play.google.com/store/apps/details?id=com.oleksiGames.CarsRacing2D&hl=ru&gl=US \n\n5. https://play.google.com/store/apps/details?id=com.DarydDealGames.CutTheCubs&hl=ru&gl=US \n\n6. https://play.google.com/store/apps/details?id=com.MaximGames.ArrowShooting&hl=ru&gl=US \n\n7. https://play.google.com/store/apps/details?id=com.PonkyGames.BombVSEnemys&hl=ru&gl=US \n\n8. https://play.google.com/store/apps/details?id=com.TopPokyGames.ShurikenthrowingSimulator&hl=ru&gl=US \n\n9. https://play.google.com/store/apps/details?id=com.oleksiGames.HockeySimulator&hl=ru&gl=US \n\n10. https://play.google.com/store/apps/details?id=com.bottels.ShootatBottle&hl=ru&gl=US \n\n11. https://play.google.com/store/apps/details?id=com.pikanosikal.Shootatbottles3D&hl=ru&gl=US \n\n12. https://play.google.com/store/apps/details?id=com.Serhio.ZombieShooter&hl=ru&gl=US \n\n13. https://play.google.com/store/apps/details?id=com.bunkerBundiGames.BikeRacing2D&hl=ru&gl=US \n\n14. https://play.google.com/store/apps/details?id=com.ComPanySeries.ArrowSpeedestFlying \n\n15. https://play.google.com/store/apps/details?id=com.ComPanySeries.PaperPlaneEndlessFlying \n\n16. https://play.google.com/store/apps/details?id=com.GAMESCOMICS.MouseCutTheCHEESE',reply_markup = keyboard2)

@dp.callback_query_handler(text_contains = "BUY")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
        types.InlineKeyboardButton(text="1 шт (6000 руб + 150 руб)",callback_data="app1"),
        types.InlineKeyboardButton(text="2 шт (12000 руб + 150 руб)",callback_data="app2"),
        types.InlineKeyboardButton(text="3 шт (18000 руб + 200 руб)",callback_data="app3"),
        types.InlineKeyboardButton(text="4 шт (24000 руб + 200 руб)",callback_data="app4"),
        types.InlineKeyboardButton(text="5 шт (30000 руб + 250 руб)",callback_data="app5"),
        types.InlineKeyboardButton(text="6 шт (36000 руб + 300 руб)",callback_data="app6"),
        types.InlineKeyboardButton(text="7 шт (42000 руб + 350 руб)",callback_data="app7"),
        types.InlineKeyboardButton(text="8 шт (48000 руб + 400 руб)",callback_data="app8"),
        types.InlineKeyboardButton(text="9 шт (54000 руб + 550 руб)",callback_data="app9"),
        types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK"),
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=1)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('Выберите количество прил, которое вам требуется :',reply_markup = keyboard2)


@dp.callback_query_handler(text_contains = "BACK")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.answer(cache_time = 60)
    buttons3 = [
           types.InlineKeyboardButton(text="КУПИТЬ 🛒",callback_data="BUY"),
           types.InlineKeyboardButton(text="ПОДДЕРЖКА 👤",callback_data="SUP"),
           types.InlineKeyboardButton(text="ПРИМЕРЫ ПРИЛ 🌅",callback_data="PRIMER"),
           types.InlineKeyboardButton(text="ЧТО ВХОДИТ В ТОВАР? 📦",callback_data="ABOUT"),
           types.InlineKeyboardButton(text="ЗАКАЗАТЬ 🛎",callback_data="SAP")
       ]
    keyboard3 = types.InlineKeyboardMarkup(row_width=2)
    keyboard3.add(*buttons3)
    await call.message.answer('Привествую вас в ШОПЕ ПРИЛ NERA SHOP 🎮 \n— Прилы на любой вкус от белых до черных \n— Белые вы можете купить сразу \n— Серые и Черные вы можете заказать у меня в личном чате',reply_markup=keyboard3)

#--------------------------------------------ТОВАРЫ------------------------------------------------#

@dp.callback_query_handler(text_contains = "app1")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
        types.InlineKeyboardButton(text="QIWI",callback_data="qiwi"),
        types.InlineKeyboardButton(text="BTC (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="ETH (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="DOGE (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="MONERO (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK"),
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=3)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('Выберите способ оплаты :',reply_markup = keyboard2)

@dp.callback_query_handler(text_contains = "app2")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
        types.InlineKeyboardButton(text="QIWI",callback_data="qiwi"),
        types.InlineKeyboardButton(text="BTC (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="ETH (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="DOGE (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="MONERO (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK"),
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=3)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('Выберите способ оплаты :',reply_markup = keyboard2)


@dp.callback_query_handler(text_contains = "app3")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
        types.InlineKeyboardButton(text="QIWI",callback_data="qiwi"),
        types.InlineKeyboardButton(text="BTC (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="ETH (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="DOGE (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="MONERO (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK"),
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=3)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('Выберите способ оплаты :',reply_markup = keyboard2)

@dp.callback_query_handler(text_contains = "app4")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
        types.InlineKeyboardButton(text="QIWI",callback_data="qiwi"),
        types.InlineKeyboardButton(text="BTC (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="ETH (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="DOGE (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="MONERO (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK"),
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=3)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('Выберите способ оплаты :',reply_markup = keyboard2)


@dp.callback_query_handler(text_contains = "app5")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
        types.InlineKeyboardButton(text="QIWI",callback_data="qiwi"),
        types.InlineKeyboardButton(text="BTC (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="ETH (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="DOGE (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="MONERO (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK"),
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=3)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('Выберите способ оплаты :',reply_markup = keyboard2)


@dp.callback_query_handler(text_contains = "app6")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
        types.InlineKeyboardButton(text="QIWI",callback_data="qiwi"),
        types.InlineKeyboardButton(text="BTC (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="ETH (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="DOGE (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="MONERO (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK"),
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=3)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('Выберите способ оплаты :',reply_markup = keyboard2)

@dp.callback_query_handler(text_contains = "app7")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
        types.InlineKeyboardButton(text="QIWI",callback_data="qiwi"),
        types.InlineKeyboardButton(text="BTC (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="ETH (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="DOGE (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="MONERO (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK"),
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=3)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('Выберите способ оплаты :',reply_markup = keyboard2)

@dp.callback_query_handler(text_contains = "app8")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
        types.InlineKeyboardButton(text="QIWI",callback_data="qiwi"),
        types.InlineKeyboardButton(text="BTC (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="ETH (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="DOGE (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="MONERO (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK"),
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=3)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('Выберите способ оплаты :',reply_markup = keyboard2)


@dp.callback_query_handler(text_contains = "app9")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    buttons2 = [
        types.InlineKeyboardButton(text="QIWI",callback_data="qiwi"),
        types.InlineKeyboardButton(text="BTC (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="ETH (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="DOGE (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="MONERO (СКОРО)",callback_data="№"),
        types.InlineKeyboardButton(text="НАЗАД 🔙",callback_data="BACK"),
    ]
    keyboard2 = types.InlineKeyboardMarkup(row_width=3)
    keyboard2.add(*buttons2)
    await call.answer(cache_time = 60)
    await call.message.answer('Выберите способ оплаты :',reply_markup = keyboard2)



executor.start_polling(dp,skip_updates = True)


