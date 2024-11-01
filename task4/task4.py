# У вас есть список любимых песен в файле
# favorite_playlist.txt. Напишите программу,
# которая проверяет, существует ли этот файл,
# чтобы убедиться, что ваша музыкальная коллекция
# не потеряна.

import pathlib
def is_file_exist(filename: str):
    path = pathlib.Path("Playlist") / filename
    return path.exists()


if __name__ == "__main__":
    filename = "favorite_playlist.txt"
    print(filename, is_file_exist(filename))
