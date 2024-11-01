# Вы работаете над романом и храните множество черновиков.
# Напишите программу, которая удаляет все файлы
# с расширением .draft в текущем каталоге.

# сначала можно запустить функцию для создания
import os
import random


def create_drafts():
    path = ""
    if "dz4" not in os.getcwd():
        path = "dz4//"
    for i in range(random.randint(10, 20)):
        with open(f"{path}file_{i}.draft", "w") as f:
            f.write("Я ПЧЕЛА)))) ЖЖЖЖЖЖЖ")


if __name__ == "__main__":
    create_drafts()


import pathlib
def delete_drafts():  
    path = pathlib.Path("")
    for file in path.iterdir():
        if file.suffix == ".draft":
            file.unlink()

delete_drafts()
