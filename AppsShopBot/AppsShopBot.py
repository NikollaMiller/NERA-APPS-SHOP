from functools import cache
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.types import callback_query, message, reply_keyboard
from aiogram.utils import executor

import os

TOKEN = "2144505945:AAGoKEiWJSITVB0fLbgDbUGlA5wCOi4AU8k"

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
           types.InlineKeyboardButton(text="ЗАКАЗАТЬ 🛎",callback_data="SAP")
       ]

       keyboard = types.InlineKeyboardMarkup(row_width=2)
       keyboard.add(*buttons)

       await message.answer('Привествую вас в ШОПЕ ПРИЛ NERA SHOP 🎮 \n— Прилы на любой вкус от белых до черных \n— Белые вы можете купить сразу \n— Серые и Черные вы можете заказать у меня в личном чате',reply_markup=keyboard)

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

@dp.callback_query_handler(text_contains = "BACK")
async def command_func(call : callback_query.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.answer(cache_time = 60)
    buttons3 = [
           types.InlineKeyboardButton(text="КУПИТЬ 🛒",callback_data="BUY"),
           types.InlineKeyboardButton(text="ПОДДЕРЖКА 👤",callback_data="SUP"),
           types.InlineKeyboardButton(text="ПРИМЕРЫ ПРИЛ 🌅",callback_data="PRIMER"),
           types.InlineKeyboardButton(text="ЗАКАЗАТЬ 🛎",callback_data="SAP")
       ]
    keyboard3 = types.InlineKeyboardMarkup(row_width=2)
    keyboard3.add(*buttons3)
    await call.message.answer('Привествую вас в ШОПЕ ПРИЛ NERA SHOP 🎮 \n— Прилы на любой вкус от белых до черных \n— Белые вы можете купить сразу \n— Серые и Черные вы можете заказать у меня в личном чате',reply_markup=keyboard3)

executor.start_polling(dp,skip_updates = True)


