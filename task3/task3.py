# Прочитай текст из файла text.txt и автоматически
# найди самые часто встречающиеся слова (например, топ 10)
# и выведи их в порядке убывания частоты.
# Это полезно для анализа книг или длинных текстов.


from collections import Counter

def find_most_frequent(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().lower()
    words = content.split()
    frequent_words = Counter(words)
    most_common_words = frequent_words.most_common(10)
    return most_common_words

if __name__ == "__main__":
    print(find_most_frequent("text.txt"))
    