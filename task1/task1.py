# Представьте, что вы решили создать личную цифровую
# библиотеку. Напишите программу,
# которая создает директорию library,
# а внутри — папки для жанров: fiction, non-fiction,
# history, fantasy. Это будет ваш цифровой архив книг.
import os

def create_library():
    os.mkdir('library')
    os.mkdir('library/fiction')
    os.mkdir('library/non-fiction')
    os.mkdir('library/history')
    os.mkdir('library/fantasy')

create_library()
