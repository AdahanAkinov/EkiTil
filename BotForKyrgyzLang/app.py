async def on_startup(dp): # Создаём асинхронную функцию которая будет запускаться по запуску бота


    import filters
    filters.setup(dp)
    import middlewares
    middlewares.setup(dp)       

    from utils.notify_admins import on_startup_notify # Импортируем функцию которая отправляет сообщение о запуску бота всем администраторам
    await on_startup_notify(dp) # Запускаем функцию ⬆

    from utils.set_bot_commands import set_default_commands # Импортируем функцию которая устанавливает команды бота
    await set_default_commands(dp) # Запускаем функцию ⬆

    print('Бот запущен') # Выводим в консоль 'Бот запущен'
    
if __name__ == '__main__':
    from aiogram import executor # Импортируем executor для запуска полинга
    from handlers import dp # Из хендлеров импортируем dp
    
    executor.start_polling(dp, on_startup=on_startup) # Запускаем полинг бота, и функцию on_startup