
from pathlib import Path
test_file = Path('C:\\Temp\\test1.txt')
# Append
with test_file.open('a', encoding='utf-8') as file:
    file.write("\nAppend line")
# Read
with test_file.open('r', encoding='utf-8') as file:
    file_content = file.read()
print(file_content)

try:   
#lines to write
  lines_to_write = [
      "user,password,id",
      "john,223@,100",
      "adam,243@,101"
      ]

  with test_file.open('w', encoding='utf-8') as f:
      f.writelines(f"{line}\n" for line in lines_to_write )
except Exception as e:
    print(f" error - {e}")

# Read and write
with test_file.open('r+', encoding='utf-8') as file:
    file.write("Added content\n")
    file_content = file.read()
print(file_content)
