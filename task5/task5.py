# Вы решили создать резервную копию вашего проекта
# с кулинарными рецептами. Напишите программу,
# которая копирует файл recipes.txt в файл
# recipes_backup.txt.
from shutil import copy

def copy_recipes(filename, new_filename):
    copy(filename, new_filename)



if __name__ == "__main__":
    filename = "recipes.txt"
    backup_filename = "recipes_backup.txt"
    copy_recipes(filename, backup_filename)
