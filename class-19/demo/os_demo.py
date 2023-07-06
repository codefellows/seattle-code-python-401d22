import os
# https://docs.python.org/3/library/os.html

# Creates a folder if not existing.
# If exist, skip
if os.path.exists('test_dir'):
    print('The directory already exists')
else:
    os.mkdir('test_dir')
    print('Directory Created')

# List files and folders that are in a directory
print('List of files / directories')
print(os.listdir('.'))

# Create a new file in the created directory
# test_dir/test_file.md
file_path = os.path.join('test_dir', 'test_file.md')
print(f'Constructed File Path: {file_path}')

with open(file_path, 'w') as file:
    file.write('Hello World!')

# Split the file path into root and extension
root, ext = os.path.splitext(file_path)
print(f'Root of the file path: {root}')
print(f'Extension of the file path: {ext}')
