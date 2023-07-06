import os
import shutil
from rich_demo.console import Console

console = Console()

# Let's create a source directory and a few files inside it
os.makedirs('src_dir', exist_ok=True)
with open('src_dir/file1.txt', 'w') as f:
    f.write('This is file1')
with open('src_dir/file2.txt', 'w') as f:
    f.write('This is file2')

# Create a destination directory
os.makedirs('dst_dir', exist_ok=True)

# Print contents of the directories before copy operation
console.print("Before copy operation")
console.print("Contents of source directory:", os.listdir('src_dir'))
console.print("Contents of destination directory:", os.listdir('dst_dir'))

# Use shutil.copy2() to copy file1.txt to dst_dir, preserving file metadata
shutil.copy2('src_dir/file1.txt', 'dst_dir')

# Print contents of the directories after copy operation
console.print("After copy operation")
console.print("Contents of source directory:", os.listdir('src_dir'))
console.print("Contents of destination directory:", os.listdir('dst_dir'))

# Use shutil.copytree() to copy entire directory
shutil.copytree('src_dir', 'dst_dir_copy', dirs_exist_ok=True)

# Print out the contents of src_dir and dst_dir_copy
console.print("After copytree operation")
console.print("Contents of source directory:", os.listdir('src_dir'))
console.print("Contents of copied directory:", os.listdir('dst_dir_copy'))

# Use shutil.rmtree() to remove a directory and all its contents
shutil.rmtree('dst_dir_copy')

# Check if dst_dir_copy still exists
if not os.path.exists('dst_dir_copy'):
    console.print("The directory 'dst_dir_copy' was successfully removed", style="green")
