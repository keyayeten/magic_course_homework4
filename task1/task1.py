# Представьте, что вы решили создать личную цифровую
# библиотеку. Напишите программу,
# которая создает директорию library,
# а внутри — папки для жанров: fiction, non-fiction,
# history, fantasy. Это будет ваш цифровой архив книг.


import os
from pathlib import Path

def create_library(directory_name: str, stack: str):
    os.mkdir(directory_name)
    os.chdir(directory_name)
    for i in stack:
        os.mkdir(i)

directory_name = 'library'
stack = ["fiction", "non-fiction", "history", "fantasy"]
create_library(directory_name, stack)
print(f'Директория {directory_name} с поддиректориями {stack} успешно созданы')
