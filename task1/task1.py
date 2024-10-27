# Представьте, что вы решили создать личную цифровую
# библиотеку. Напишите программу,
# которая создает директорию library,
# а внутри — папки для жанров: fiction, non-fiction,
# history, fantasy. Это будет ваш цифровой архив книг.
import os

def create_library():
    lst = ['fiction', 'non-fiction', 'history', 'fantasy']
    a = 'library'
    os.makedirs(a)
    for i in lst:
        d = os.path.join(a, i)
        os.mkdir(d)
    return

create_library()
