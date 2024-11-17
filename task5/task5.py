# Вы решили создать резервную копию вашего проекта
# с кулинарными рецептами. Напишите программу,
# которая копирует файл recipes.txt в файл
# recipes_backup.txt.


def copy_recipes(filename, new_filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
    with open(new_filename, "w", encoding="utf-8") as f:
        f.write(data)


if __name__ == "__main__":
    filename = "recipes.txt"
    backup_filename = "recipes_backup.txt"
    copy_recipes(filename, backup_filename)
