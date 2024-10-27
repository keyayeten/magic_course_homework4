# Прочитай текст из файла text.txt и автоматически
# найди самые часто встречающиеся слова (например, топ 10)
# и выведи их в порядке убывания частоты.
# Это полезно для анализа книг или длинных текстов.

def add_to_dict(res, _str, punctuation_marks):
    i_start, r = 0, ''
    for i in range(len(_str)):
        if _str[i] in punctuation_marks:
            r = r + _str[i_start:i]
            i_start = i + 1
    r = r + _str[i_start:]

    for item in r.lower().split(' '):
        if item != '':
            res[item] = res.setdefault(item, 0) + 1


def find_most_frequent(filename):
    punctuation_marks = ".,;:()—|«»\r\n"
    result_count = 10
    res = {}

    with open(f"{filename}", "r", encoding="utf-8") as f:
        str_list = f.readlines()
        for _str in str_list:
            add_to_dict(res, _str, punctuation_marks)

    return sorted(res, key=lambda x: res.get(x), reverse=True)[:result_count]


if __name__ == "__main__":
    print(find_most_frequent("text.txt"))
