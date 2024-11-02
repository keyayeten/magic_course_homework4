# Представьте, что вы решили создать личную цифровую
# библиотеку. Напишите программу,
# которая создает директорию library,
# а внутри — папки для жанров: fiction, non-fiction,
# history, fantasy. Это будет ваш цифровой архив книг.
import os

def create_library():
    """
    Функция создает директорию library, а внутри — папки для жанров: fiction, non-fiction, history, fantasy.
    """
    os.makedirs("library/fiction")
    os.makedirs("library/non-fiction")
    os.makedirs("library/history")
    os.makedirs("library/fantasy")
