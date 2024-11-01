# Представьте, что вы решили создать личную цифровую
# библиотеку. Напишите программу,
# которая создает директорию library,
# а внутри — папки для жанров: fiction, non-fiction,
# history, fantasy. Это будет ваш цифровой архив книг.


import pathlib
def create_library():
    my_library = set()
    path = pathlib.Path("Library")
    path.mkdir(exist_ok=True)
    genres = ['fiction', 'non-fiction', 'history', 'fantasy']
    for genre in genres:
        genre_path = path / genre
        genre_path.mkdir (exist_ok=True)
        my_library.add(genre_path)
    for i in my_library:
        print(i)

create_library()

