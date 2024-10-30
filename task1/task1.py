import pathlib

# Представьте, что вы решили создать личную цифровую
# библиотеку. Напишите программу,
# которая создает директорию library,
# а внутри — папки для жанров: fiction, non-fiction,
# history, fantasy. Это будет ваш цифровой архив книг.

folders = ["fiction", "non-fiction", "history", "fantasy"]
dir = "library"


def create_library(dir, folders):
    path = pathlib.Path(dir)
    path.mkdir(exist_ok=True)

    for i in folders:
        folders_path = path / i
        folders_path.mkdir(exist_ok=True)


create_library(dir, folders)
