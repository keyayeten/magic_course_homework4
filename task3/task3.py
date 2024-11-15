# Прочитай текст из файла text.txt и автоматически
# найди самые часто встречающиеся слова (например, топ 10)
# и выведи их в порядке убывания частоты.
# Это полезно для анализа книг или длинных текстов.

def sort_key_fn(a):
    return a[1]
def find_most_frequent(filename):
    data = None
    with open("text.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
    stroka = " ".join(data).lower()

    words = stroka.split()
    wdict = {}
    for w in words:
        wdict[w] = wdict.get(w, 0) + 1
    wlist = []
    for w in wdict:
        c = wdict[w]
        wlist.append([w, c])
    wlist = sorted(wlist, key=sort_key_fn, reverse=True)
    return wlist[:10]

if __name__ == "__main__":
    print(find_most_frequent("text.txt"))
