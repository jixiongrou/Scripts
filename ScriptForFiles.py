import os
from shutil import move

path = input('please input path: ') + '\\'

def mkdir(path):
	folder = os.path.exists(path)
	if not folder:                 
		os.makedirs(path)          

file_names = os.listdir(path)

def MergingFiles():
    """creat dirs with the same prefix"""
    for i in range(len(file_names)):
        file_name = file_names[i]
        
        file_name_renamed = file_names[i].replace('】', ' ')
        file_name_renamed = file_names[i].replace('《', ' ')
        file_name_renamed = file_names[i].replace('-', ' ')
        
        os.rename(path+file_name, path+file_name_renamed)
        
        if i == 0:
            dir_name = file_name_renamed.split(' ')[0]
            print(dir_name)
            mkdir(path+dir_name)
            move(path+file_name_renamed, path+dir_name)
        else:         
            temp = file_name_renamed.split(' ')[0]
            if temp != dir_name:
                dir_name = temp
                print(dir_name)
                mkdir(path+dir_name)
                move(path+file_name_renamed, path+dir_name)
            else:
                move(path+file_name_renamed, path+dir_name)

def ChangingFilesExtensions():
    os.chdir(path)
    will_replaced_part = input('Input the part of the file name, what you wanna replace it: ')
    replaced_part = input('and replaced as: ')
    for i in range(len(file_names)):
        file_name_renamed = file_names[i].replace(will_replaced_part, replaced_part)
        os.rename(file_names[i], file_name_renamed)

print("1. Dirct; 2. rename")
user_choice = input()
if user_choice == '1':
    MergingFiles()
elif user_choice == '2':
    ChangingFilesExtensions()
