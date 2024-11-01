# Вы решили создать резервную копию вашего проекта
# с кулинарными рецептами. Напишите программу,
# которая копирует файл recipes.txt в файл
# recipes_backup.txt.


import pathlib
import shutil
def copy_recipes(filename, new_filename):
    path = pathlib.Path(filename)
    if not path.exists():
        print(f"Файл {filename} не найден")
        return
    else:
        return shutil.copy(filename, new_filename)


if __name__ == "__main__":
    filename = "recipes.txt"
    new_filename = "recipes_backup.txt"
    copy_recipes(filename, new_filename)
    