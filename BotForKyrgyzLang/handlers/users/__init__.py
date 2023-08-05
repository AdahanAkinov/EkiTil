from .Start import dp
from .AI_GPT import dp
from .other.Error import dp # Ловит все текстовые сообщения поэтому мы импортируем этот хендлер последним

__all__ = ['dp'] # Список параметров которые можно импортировать из папки users