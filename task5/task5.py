# Вы решили создать резервную копию вашего проекта
# с кулинарными рецептами. Напишите программу,
# которая копирует файл recipes.txt в файл
# recipes_backup.txt.

import os
import shutil

def copy_recipes(file_name, new_file_name):
    os.chdir('task5')
    return shutil.copy(file_name, new_file_name)



if __name__ == "__main__":
    file_name = "recipes.txt"
    backup_file_name = "recipes_backup.txt"
    copy_recipes(file_name, backup_file_name)
