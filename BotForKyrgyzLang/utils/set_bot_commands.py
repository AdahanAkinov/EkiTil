from aiogram import types

async def set_default_commands(dp): # Создаём функцию которая устанавливает команды бота
    await dp.bot.set_my_commands([ # Создаём команды бота
        # Пример - types.BotCommand('Команда', 'Описание команды')
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('menu', 'Посмотреть меню')
    ], scope=types.BotCommandScopeAllPrivateChats())