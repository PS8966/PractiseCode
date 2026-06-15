
from pathlib import Path
test_file = Path('C:\\Temp\\test1.txt')
# Append
with test_file.open('a', encoding='utf-8') as file:
    file.write("\nAppend line")
# Read
with test_file.open('r', encoding='utf-8') as file:
    file_content = file.read()
print(file_content)
