# У вас есть список любимых песен в файле
# favorite_playlist.txt. Напишите программу,
# которая проверяет, существует ли этот файл,
# чтобы убедиться, что ваша музыкальная коллекция
# не потеряна.
import os

def is_file_exist(filename: str):
    if "task4" not in os.getcwd():
        path = "task4//"
    else:
        path = os.getcwd()
    for i in os.listdir(path):
        if i == filename:
            return "существует"

    return "не существует"


if __name__ == "__main__":
    filename = "favorite_playlist.txt"
    print(filename, is_file_exist(filename))
