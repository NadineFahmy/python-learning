import os
from pathlib import Path

# Desktop Path
desktop_path = Path.home() / "Desktop"
python_folder = desktop_path / "Python"

# Create Folder
python_folder.mkdir(exist_ok=True)

# Create Files
for i in range(1, 51):
    if i == 25:
        file_path = python_folder / "special-text.txt"
        file_path.touch()
    else:
        file_path = python_folder / f"txt{i}.txt"
        with open(file_path, "w") as f:
            f.write(f"Elzero Web School => {i}")


# Current Working Directory
print(os.getcwd())
n
# Path of current file
current_file_path = Path(__file__).resolve()
print(current_file_path.parent)

# File name
print(current_file_path.name)

# Count files inside Python folder
files_count = len(list(python_folder.iterdir()))
print(files_count)

# -------- Assignment 02 --------

txt1_path = python_folder / "txt1.txt"

with open(txt1_path, "a") as file:
    for _ in range(50):
        file.write("\nAppended => Elzero Web School")
