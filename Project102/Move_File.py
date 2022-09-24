from distutils import extension
import os
import shutil

from_dir =  "C:\\Users\\Raghav\\Downloads"
to_dir = "C:\\Users\\Raghav\\Desktop\\Document_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files :
  name,extension =  os.path.splitext(file)
  print(name)
  print(extension)

  if extension=='':
    continue
  
  if extension in [‘.txt’, ‘.doc’, ‘.docx’, ‘.pdf’]:
    path 1 = from_dir + '/' + file_name
    path 2 = to_dir + '/' + "Text_files"
    path 3 = to_dir + '/' + "Text_files" + '/' +  file_name
 
 