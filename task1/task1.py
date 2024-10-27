# Представьте, что вы решили создать личную цифровую
# библиотеку. Напишите программу,
# которая создает директорию library,
# а внутри — папки для жанров: fiction, non-fiction,
# history, fantasy. Это будет ваш цифровой архив книг.
import os

def create_library():
    base_parh='library'
    for item in ["fiction", "non-fiction","history", "fantasy"]:
        os.makedirs(f"{base_parh}/{item}",exist_ok=True)

create_library()
