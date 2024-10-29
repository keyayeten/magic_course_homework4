# Прочитай текст из файла text.txt и автоматически
# найди самые часто встречающиеся слова (например, топ 10)
# и выведи их в порядке убывания частоты.
# Это полезно для анализа книг или длинных текстов.

import os

def find_most_frequent(file_name: str):
    os.chdir('task3')
    with open(file_name, 'r', encoding='utf-8') as file:
        text_lst = file.read().lower()
        freqs = {}
        for i in text_lst.split():
            freqs[i] = freqs.get(i, 0) + 1
        freqs_lst = sorted(list(freqs.items()), key = lambda x: x[1], reverse=True)
        last_lst = []
        for i in range(10):
            last_lst.append(freqs_lst[i])
        return last_lst


if __name__ == "__main__":
    file_name = 'text.txt'
    print(find_most_frequent(file_name))
