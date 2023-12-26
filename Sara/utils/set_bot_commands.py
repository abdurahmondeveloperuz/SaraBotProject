from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "🔄 Botni ishga tushurish"),
            types.BotCommand("help", "🆘 Bot qo'llanmasi bo'yicha yordam olish"),
        ]
    )
