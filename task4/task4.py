# У вас есть список любимых песен в файле
# favorite_playlist.txt. Напишите программу,
# которая проверяет, существует ли этот файл,
# чтобы убедиться, что ваша музыкальная коллекция
# не потеряна.
import os


def is_file_exist(filename: str):
    files_list = []
    for adress, dirs, files in os.walk("C:\\Users\\a.zhukov\\Desktop\\magic\\magic_course_homework4"):
        for file in files:
            if filename == file:
                files_list.append(file)
                break
    if filename in files_list:
        return print(f"{filename} найден")
    else:
        return print(f"{filename} не найден")






if __name__ == "__main__":
    filename = "favorite_playlist.txt"
    # print(filename, is_file_exist(filename))
    is_file_exist(filename)
