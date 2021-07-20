import PySimpleGUI as sg
from common.constant import COMMANDS
from common.errors import *
from merger.add_file.add_file_in_english import AddFileInEnglish
from merger.add_file.add_file_in_russian import AddFileInRussian
from merger.translate.translate_file import TranslateFile
from merger.transfer.transfer_file import TransferFile
from merger.streamline.streamline_file import StreamlineFile
from merger.general.general_work_with_directory import GeneralWorkWithDirectory
from merger.search_untrans_string.search_untrans_string import SearchUntransString
from merger.search_update_string.search_update_string import SearchUpdateString

def __check_input(general_path, add_path):
    if not general_path or not add_path:
        raise NotEnterPath
    if general_path == add_path:
        raise PathMatch
    if '.yml' not in general_path and '.txt' not in general_path:
        raise PathNotLeadToFile
    if '.yml' not in add_path and '.txt' not in add_path:
        raise PathNotLeadToFile

list_commands = [COMMANDS.ADDITIONAL_ENGLISH, COMMANDS.ADDITIONAL_RUSSIAN, COMMANDS.TRANSFER_FILE,
                 COMMANDS.ALL_TRANSLATE_DIRECTRY, COMMANDS.TRANSLATE_FILE, COMMANDS.ALL_TRANSFER_DIRECTORY,
                 COMMANDS.STREAMLINE_FILE, COMMANDS.STREAMLINE_DIRECTORY, COMMANDS.SEARCH_UPDATE_STRING_FILE,
                 COMMANDS.SEARCH_UNTRANS_STRING_FILE]

layout = [
    [sg.Combo(values=list_commands, key='MODE', default_value=list_commands[0], size=(85, 1))],
    [sg.Text('Оригинальный файл', size=(20, 1)), sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
    [sg.Text('Файл пользователя', size=(20, 1)), sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
    [sg.Text('Доп. файл (если нужно)', size=(20, 1)), sg.InputText(key='OTHER_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
    [sg.Button(button_text='Выполнить')]
]
window = sg.Window('File Merger', layout)
while True:
    try:
        event, values = window.read()
        # print(event, values) #debug
        if event in (None, 'Exit', 'Cancel'):
            break
        elif event == 'Выполнить':
            mode = values['MODE']
            general_file_path = '/home/mitry/Документы/мёрджер/файлы_для_руссификации_тест/focus_BEX_l_english.yml' #values['GENERAL_PATH']
            additional_file_path = '/home/mitry/Документы/мёрджер/файлы_для_руссификации_тест/focus_BEX_l_russian.yml' #values['ADDITIONAL_FILE']
            other_path = '/home/mitry/Документы/мёрджер/BEX-The_Great_Northern_War/focus_BEX_l_english.yml' #values['OTHER_FILE']
            if mode == COMMANDS.ADDITIONAL_ENGLISH:
                __check_input(general_file_path, additional_file_path)
                merger = AddFileInEnglish()
                merger.execute_operation(general_file_path, additional_file_path)
            elif mode == COMMANDS.ADDITIONAL_RUSSIAN:
                __check_input(general_file_path, additional_file_path)
                merger = AddFileInRussian()
                merger.execute_operation(general_file_path, additional_file_path)
            elif mode == COMMANDS.TRANSLATE_FILE:
                __check_input(general_file_path, additional_file_path)
                merger = TranslateFile()
                merger.execute_operation(general_file_path, additional_file_path)
            elif mode == COMMANDS.ALL_TRANSLATE_DIRECTRY:
                merger = GeneralWorkWithDirectory(TranslateFile)
                merger.excution_operation_with_directory(general_file_path)
            elif mode == COMMANDS.TRANSFER_FILE:
                __check_input(general_file_path, additional_file_path)
                merger = TransferFile()
                merger.execute_operation(general_file_path, additional_file_path)
            elif mode == COMMANDS.ALL_TRANSFER_DIRECTORY:
                merger = GeneralWorkWithDirectory(TransferFile)
                merger.excution_operation_with_directory(general_file_path)
            elif mode == COMMANDS.STREAMLINE_FILE:
                __check_input(general_file_path, additional_file_path)
                merger = StreamlineFile()
                merger.execute_operation(general_file_path, additional_file_path)
            elif mode == COMMANDS.STREAMLINE_DIRECTORY:
                merger = GeneralWorkWithDirectory(StreamlineFile)
                merger.excution_operation_with_directory(general_file_path)
            elif mode == COMMANDS.SEARCH_UPDATE_STRING_FILE:
                merger = SearchUpdateString()
                merger.execute_operation(general_path_new_v=general_file_path,
                                         add_path=additional_file_path,
                                         general_path_old_v=other_path)
            elif mode == COMMANDS.SEARCH_UNTRANS_STRING_FILE:
                merger = SearchUntransString()
                merger.execute_operation(additional_file_path)

    except NotADirectoryError:
        print('Указанный путь не является папкой, укажите путь до папки')
    except FileNotFoundError:
        print('Указанные пути не ведут к файлам')
    except NotEnterPath:
        print('Один или несколько путей не введены, введите оба пути')
    except PathNotLeadToFile:
        print('Указанный путь не является файлом, укажите путь до файла')
    except PathMatch:
        print('Пути должны отличаться, укажите пути к разным файлам')
    except ConnectError:
        print('Отсутствует соединение с интернетом')
    except Exception as error:
        print('Неизвестная ошибка {} пожалуйста вышлите её автору проекта'.format(error))


#
#   /home/mitry/Документы/BEX/focus_BEX_l_english.yml
#   /home/mitry/Документы/файлы для руссификации/focus_BEX_l_russian.yml

#ТЕСТ ПЕРЕВОДА ДИРРЕКТОРИИ
# '/home/mitry/Документы/localization_test'
# '/home/mitry/Документы/файлы для руссификации/focus_BEX_l_russian.yml'

#/home/mitry/Документы/localization_test/focus_BEX_l_english.yml
#/home/mitry/Документы/localization_test/focus_BEX_l_russian.yml

#/home/mitry/Документы/BEX-Pax Andronikos/ideas_BEX_l_english.yml
#/home/mitry/Документы/файлы для руссификации/ideas_BEX_l_russian.yml