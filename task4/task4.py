# У вас есть список любимых песен в файле
# favorite_playlist.txt. Напишите программу,
# которая проверяет, существует ли этот файл,
# чтобы убедиться, что ваша музыкальная коллекция
# не потеряна.

from pathlib import Path

def is_file_exist(filename: str):

    with Path("favorite_playlist.txt") as file:
        if file.is_file():
            return True
    return False

if __name__ == "__main__":
    filename = "favorite_playlist.txt"
    print(filename, is_file_exist(filename))
