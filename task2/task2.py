# Вы работаете над романом и храните множество черновиков.
# Напишите программу, которая удаляет все файлы
# с расширением .draft в текущем каталоге.

# сначала можно запустить функцию для создания
import os
import random


def create_drafts():
    path = ""
    if "task2" not in os.getcwd():
        path = "task2//"
    for i in range(random.randint(10, 20)):
        with open(f"{path}file_{i}.draft", "w") as f:
            f.write("Я ПЧЕЛА)))) ЖЖЖЖЖЖЖ")


def delete_drafts():
    path = os.getcwd()
    for files in os.listdir(path):
        # if files == p.glob("*.draft"):  #glob - находит все файлы с указанным расширением удаление в модуде pathlib (* обязательна)
        if files.endswith(".draft"):  #endswith - метод питона находит все файлы с указанным расширением
            files_path = os.path.join(path, files)
            os.remove(files_path)


if __name__ == "__main__":
    # create_drafts()
    delete_drafts()
