#WAP to print the contents of a directory using the os module. Search Online for function which does that and use the comments to lable the program.

import os 

#Specify the directory you want to list
directory_path = '/'

#List all files and directories in the specified path
contents = os.listdir(directory_path)

#Print each file and directory name
for item in contents: 
        print(item)
