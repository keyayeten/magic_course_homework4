# Напишите программу для управления списком задач (To-Do List). 
# Программа должна уметь:
# Добавлять новую задачу.
# Удалять задачу по номеру.
# Отмечать задачу как выполненную.
# Выводить список всех задач с указанием их статуса (выполнена/не выполнена).

def show_tasks(file_name) -> list[str]:
    with open(file_name, 'r', encoding = 'utf-8') as file:
        data = file.read().split('\n')
    return data

def add_task(file_name, task):
    with open(file_name, 'a', encoding='utf-8') as file:
        num = len(show_tasks(file_name))
        file.write(f'{num} | {task} | не выполнено\n')

def del_task(file_name, d_task):
    data = show_tasks(file_name)
    count = 1
    new_data = []
    for i in data:
        if i == '':
            continue
        num, task, status = i.split(' | ')
        if int(num) == d_task:
            continue
        new_data.append(f'{count} | {task} | {status}\n')
        count += 1
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for i in new_data:
            file.write(i)

def change_status_task(file_name, number: int, res_task: str):
    data = show_tasks(file_name)
    new_data = []
    for i in range(len(data)):
        if data[i] == '':
            continue
        num, task, status = data[i].split(' | ')
        if int(num) == number:
            new_data.append(f'{i + 1} | {task} | {res_task}\n')
        else:
            new_data.append(f'{i + 1} | {task} | {status}\n')
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for i in new_data:
            file.write(i)

if __name__ == "__main__":
    file_name = 'todo_list.txt'
    task = 'Приготовить пожрать'
    d_task = 3
    number, res_task = 2, 'выполнено'
    print(show_tasks(file_name))
    # add_task(file_name, task)
    # del_task(file_name, d_task)
    change_status_task(file_name, number, res_task)
