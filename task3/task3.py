# Прочитай текст из файла text.txt и автоматически
# найди самые часто встречающиеся слова (например, топ 10)
# и выведи их в порядке убывания частоты.
# Это полезно для анализа книг или длинных текстов.


def find_most_frequent(filename):

    with open("text.txt", "r", encoding="utf-8") as file:
        data = file.read().lower().split()
        # print(data)

    top_words = {}

    for words in data:
        if words in top_words:
            top_words[words] += 1
        else:
            top_words[words] = 1

    top_10_words = sorted(top_words.items(), key=lambda item: item[1], reverse=True)
    top_10_words = top_10_words[:10]

    return top_10_words


if __name__ == "__main__":
    print(find_most_frequent("text.txt"))
