# Прочитай текст из файла text.txt и автоматически
# найди самые часто встречающиеся слова (например, топ 10)
# и выведи их в порядке убывания частоты.
# Это полезно для анализа книг или длинных текстов.
import os

def find_most_frequent(filename : str) -> dict [str : int]:
    """
    Функция, которая принимает на вход путь к файлу и находит самые часто встречающиеся слова
    и выводит их в порядке убывания частоты. 
    """

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read() 

    words = text.split() 

    word_dict = {}

    for word in words:
        word = word.lower()
        if word in word_dict: 
            word_dict[word] += 1
        else:
            word_dict[word] = 1


    sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    return sorted_word_dict

if __name__ == "__main__":
    print(find_most_frequent("text.txt"))
