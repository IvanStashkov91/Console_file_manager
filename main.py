import sys
from core import (create_file,
                  create_folder,
                  get_list,
                  delete_file,
                  copy_file,
                  save_info,
                  )

save_info('Start')
command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('File has no name')
    else:
        create_file(name)
elif command == 'create_folder':
    name = sys.argv[2]
    create_folder(name)
elif command == 'delete':
    name = sys.argv[2]
    delete_file(name)
elif command == 'copy':
    name = sys.argv[2]
    new_name = sys.argv[3]
    copy_file(name, new_name)
elif command == 'help':
    print('list - list of files and dirrectory')
    print('create_file - create file')
    print('create_folder - create dirrectory')
    print('delete - delete file or dirrectory')
    print('copy - copy file or dirrectory')

save_info('Finish')
