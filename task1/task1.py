# Представьте, что вы решили создать личную цифровую
# библиотеку. Напишите программу,
# которая создает директорию library,
# а внутри — папки для жанров: fiction, non-fiction,
# history, fantasy. Это будет ваш цифровой архив книг.

import os

LIBRARY_PATH = "library"
GENRES_PATH = ["fiction", "non-fiction", "history", "fantasy"]
def create_library():
    os.makedirs(LIBRARY_PATH, exist_ok=True)

    for genre in GENRES_PATH:
        genre_path = os.path.join(LIBRARY_PATH, genre)
        os.makedirs(genre_path, exist_ok=True)

if __name__ == "__main__":
    create_library()
