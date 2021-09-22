import os


def py_files(path: str) -> list:
    for directory, _, files in os.walk(path):
        for text in files:
            if text.endswith("py"):
                file_path = os.path.join(directory, "main.py")
                yield file_path


this_path = os.path.abspath(os.path.join("..", ".."))
result = (i for i in py_files(this_path))
count_lines = 0

for path_file in result:
    with open(path_file, "r", encoding="utf-8") as file:
        for line in file.readlines():
            if len(line) - 1 > 0 and not line.startswith("#"):
                count_lines += 1

print("Обшая количество строк:", count_lines)

# зачет!
