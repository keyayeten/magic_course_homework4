# Вы решили создать резервную копию вашего проекта
# с кулинарными рецептами. Напишите программу,
# которая копирует файл recipes.txt в файл
# recipes_backup.txt.


def copy_recipes(filename:str, new_filename:str):
    with open(filename, 'r', encoding='utf-8') as src:
        data = src.read()

    with open(new_filename, 'r', encoding='utf-8') as dest:
        dest.write(data)

if __name__ == "__main__":
    filename = "recipes.txt"
    backup_filename = "recipes_backup.txt"
    copy_recipes(filename, backup_filename)
