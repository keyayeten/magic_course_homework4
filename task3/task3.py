# Прочитай текст из файла text.txt и автоматически
# найди самые часто встречающиеся слова (например, топ 10)
# и выведи их в порядке убывания частоты.
# Это полезно для анализа книг или длинных текстов.


def find_most_frequent(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read().replace('\n', ' ').split(' ')
    a = {}
    for word in data:
        if word in a:
            a[word] += 1
        else:
            a[word] = 1
    sorted_a = sorted(a.items(), key=lambda item: item[1], reverse=True)
    max_10 = []
    for i in range(10):
        max_10.append(sorted_a[i][0])

    return max_10


if __name__ == "__main__":
    print(find_most_frequent("text.txt"))
