# Прочитай текст из файла text.txt и автоматически
# найди самые часто встречающиеся слова (например, топ 10)
# и выведи их в порядке убывания частоты.
# Это полезно для анализа книг или длинных текстов.

from collections import Counter

def find_most_frequent(filename:str):
    with open(filename, 'r', encoding= 'utf-8') as file:
        text = file.read().replace("/n", " ")

    word_counts = Counter(text.lower().split())

    top_words = word_counts.most_common()

    return top_words

if __name__ == "__main__":
    print(find_most_frequent("text.txt"))
