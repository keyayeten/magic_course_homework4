# Вы решили создать резервную копию вашего проекта
# с кулинарными рецептами. Напишите программу,
# которая копирует файл recipes.txt в файл
# recipes_backup.txt.
import os
import shutil


def copy_recipes(filename, new_filename):
    directoria = os.getcwd()
    for i in os.listdir(directoria):
        if i in filename:
            shutil.copy(filename, new_filename)
        return new_filename


if __name__ == "__main__":
    filename = "recipes.txt"
    backup_filename = "recipes_backup.txt"
    copy_recipes(filename, backup_filename)
