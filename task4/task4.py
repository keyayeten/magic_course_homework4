# У вас есть список любимых песен в файле
# favorite_playlist.txt. Напишите программу,
# которая проверяет, существует ли этот файл,
# чтобы убедиться, что ваша музыкальная коллекция
# не потеряна.
import os

def is_file_exist(filename: str):
    if filename not in os.listdir():
        return False
    with open(f"{filename}", "r", encoding="utf-8") as f:
        # для простоты считаем что в плейлисте не может быть пустых строк
        if f.readline() in [None, '', '\n', '\r\n']:
            return False
    return True


if __name__ == "__main__":
    filename = "favorite_playlist.txt"

    print(filename, is_file_exist(filename))
