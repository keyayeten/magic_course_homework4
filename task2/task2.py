# Вы работаете над романом и храните множество черновиков.
# Напишите программу, которая удаляет все файлы
# с расширением .draft в текущем каталоге.

# сначала можно запустить функцию для создания
import os
import random


def create_drafts(new_path: str):
    path = ""
    os.chdir('task2')
    os.makedirs(new_path, exist_ok = True)
    if "stories" not in os.getcwd():
        path = new_path + "//"
    for i in range(random.randint(15, 20)):
        with open(f"{path}file_{i}.draft", "w", encoding = 'utf-8') as f:
            f.write("Я ПЧЕЛА)))) ЖЖЖЖЖЖЖ")


def delete_drafts(draft_list: list[str]):
    os.chdir(new_path)
    count = 0
    for i in draft_list:
        if '.draft' in i:
            os.remove(i)
            count += 1
    return count


if __name__ == "__main__":
    new_path = 'stories'
    create_drafts(new_path)
    draft_list = os.listdir(new_path)
    count_del = delete_drafts(draft_list)
    print(f'Удалено {count_del} файлов')
