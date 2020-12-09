import os
import shutil


def create_file(name, text=None):
    ''' function to create file
    :param name: file name
    :param text: some text
    :return: new file
    '''
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    ''' function to create folder
    :param name: folder name
    :return: new folder
    '''
    try:
        os.mkdir(name)
    except FileExistsError:
        print('This folder has been yet')


def get_list(folders_only=False):
    ''' to show all file and folder in the current dirrectory if need to
    :return: all file and folder
    '''
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    ''' delete file or dirrectory
    :param name: file or dirrectory name
    :return: delete file or dirrectory
    '''
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    ''' copy file or dirrectory
    :param name: file or dirrectory name
    :param new_name: file or dirrectory new name
    :return: new file or dirrectory
    '''
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('This folder has been yet')
    else:
        shutil.copy(name, new_name)


if __name__ == '__main__':
    create_file('test.dat')
    create_file('test.dat', 'some text')
    create_folder('new_f')
    create_folder('new_f_1')
    get_list()
    get_list(True)
    delete_file('new_f_1')
    delete_file('test.dat')
    copy_file('new_f', 'new_f1')
    create_file('test.dat')
    copy_file('test.dat', 'new_test.dat')
