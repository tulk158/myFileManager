import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game_reverse import game_reverse
from game import game


save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо ввести команду. help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            delete_file(name)
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            change_dir(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутствует название файла и название копии')
        else:
            copy_file(name, new_name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('game - небольшая игра')
        print('game_reverse - небольшая игра наоборот')
    elif command == 'game_reverse':
        game_reverse()
    elif command == 'game':
        game()

    save_info('Конец')
