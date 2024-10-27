# Прочитай текст из файла text.txt и автоматически
# найди самые часто встречающиеся слова (например, топ 10)
# и выведи их в порядке убывания частоты.
# Это полезно для анализа книг или длинных текстов.


def find_most_frequent(filename):
    with open('text.txt', 'r', encoding='utf-8') as file:
        a = file.read()
        d = {}
        for i in a.split():
            d[i] = a.count(i)
        sorts = dict(list(sorted(d.items(), key=lambda x: x[1], reverse=True))[:10])
        return sorts


find_most_frequent('text.txt')


if __name__ == "__main__":
    print(find_most_frequent("text.txt"))
