# from .errors import dp
# from .groups import dp
from .users import dp # Из папки users мы импортируем dp (хендлеры для личной переписки с пользователем)

__all__ = ['dp'] # Список параметров которые можно импортировать из папки handlers