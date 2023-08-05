import logging

from aiogram.utils.exceptions import (Unauthorized, MessageCantBeDeleted, MessageToDeleteNotFound, MessageNotModified,
                                      MessageTextIsEmpty, CantParseEntities, CantDemoteChatCreator, InvalidQueryID,
                                      RetryAfter, TelegramAPIError, BadRequest)

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):

    if isinstance(exception, Unauthorized):
        logging.info(f'Unauthorized: {exception}')
        return True     # Неавторизованный

    if isinstance(exception, MessageCantBeDeleted):
        logging.info('Message cant be deleted.')
        return True     # Сообщение не может быть удалено.

    if isinstance(exception, MessageToDeleteNotFound):
        logging.info('Message to delete not found.')
        return True     # Сообщение для удаления не найдено.

    if isinstance(exception, MessageNotModified):
        logging.info('Message is not modified.')
        return True     # Сообщение не изменено.

    if isinstance(exception, MessageTextIsEmpty):
        logging.debug('Message text is empty.')
        return True     # Текст сообщения пуст.

    if isinstance(exception, CantParseEntities):
        logging.debug(f'Can\'t parse entities. ExceptionArgs: {exception.args}')
        return True     # Не удается разобрать объекты

    if isinstance(exception, CantDemoteChatCreator):
        logging.debug('Can\'t demote chat creator.')
        return True     # Невозможно понизить создателя чата.

    if isinstance(exception, InvalidQueryID):
        logging.exception(f'InvalidQueryID: {exception} \nUpdate: {update}')
        return True     # Недопустимый идентификатор запроса

    if isinstance(exception, RetryAfter):
        logging.exception(f'RetryAfter: {exception} \nUpdate: {update}')
        return True     # Повторить после

    if isinstance(exception, BadRequest):
        logging.exception(f'BadRequest: {exception} \nUpdate: {update}')
        return True     # Неверный запрос

    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True     # Ошибка API Telegram

    # Другая ошибка
    logging.exception(f'Update: {update} \nException: {exception}')
