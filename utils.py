import os
import shutil

# type extension file
def extension_type(event): #:)
    # tranto a porcaria do error --> "ValueError: substring not found"
    try:
        return event.src_path[event.src_path.rindex('.') + 1:]

    except:
        print('Not Found Extension')
        pass


# is file txt?
def is_file_txt(event): #:)
    if extension_type(event) == 'txt':
        return True
    return False


# make folder -> if not exist folder
def to_make_folder(foldername): #:)
    os.chdir("Insira\\Seu\\Diretorio\\de\\Downloads")
    if os.path.exists(foldername) == True:
        print('already exist folder')
        return os.getcwd() + os.sep + str(foldername)
    else:
        print('make folder')
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


# move file corresponding folder
def move_file_corresponding_folder(event, foldername):
    try:
        # mover arquivo
        print('move file')
        shutil.move(event.src_path, foldername)
    except:
        print('file exist in folder')
        pass
