# У вас есть список любимых песен в файле
# favorite_playlist.txt. Напишите программу,
# которая проверяет, существует ли этот файл,
# чтобы убедиться, что ваша музыкальная коллекция
# не потеряна.

import os

def is_file_exist(file_name: str):
    os.chdir('task4')
    if file_name in os.listdir():
        result = 'не стырили. всё на месте :)'
    else:
        result = 'всё пропало!!! AAAAAAAAAAAAA'
    return result


if __name__ == "__main__":
    file_name = "favorite_playlist.txt"
    print(is_file_exist(file_name))
