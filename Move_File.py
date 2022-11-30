import os
import shutil
source = 'C:/Users/lizsi/OneDrive/Documents'
destination = 'C:/Users/lizsi'

list_of_files = os.listdir (from_dir)
for file_name in list_of_files: 
    name, extension = os.path.splitext (file_name)