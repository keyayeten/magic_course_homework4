# Вы работаете над романом и храните множество черновиков.
# Напишите программу, которая удаляет все файлы
# с расширением .draft в текущем каталоге.

# сначала можно запустить функцию для создания
import os
import random

DRAFT_EXT = ".draft"

def create_drafts():
    path = ""
    if "task2" not in os.getcwd():
        path = "task2//"
    for i in range(random.randint(10, 20)):
        with open(f"{path}file_{i}.draft", "w") as f:
            f.write("Я ПЧЕЛА)))) ЖЖЖЖЖЖЖ")


def delete_drafts():
    for file_name in os.listdir():
        if os.path.isfile(file_name) and file_name.endswith(DRAFT_EXT):
            os.remove(file_name)


if __name__ == "__main__":
    delete_drafts()
