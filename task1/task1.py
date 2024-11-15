# Представьте, что вы решили создать личную цифровую
# библиотеку. Напишите программу,
# которая создает директорию library,
# а внутри — папки для жанров: fiction, non-fiction,
# history, fantasy. Это будет ваш цифровой архив книг.

import os
def create_library():
    if not os.path.exists('library'):   # проверяем что каталога с таким названием нет
        os.mkdir('library')                     # создадим директорию
        for subdir in ('fiction', 'non-fiction', 'history', 'fantasy'):
            os.makedirs(os.path.join('library', subdir))

if __name__ == "__main__":
    create_library()
