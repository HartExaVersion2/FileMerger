import PySimpleGUI as sg
from common.constant import COMMANDS

list_commands = [COMMANDS.ADDITIONAL_ENGLISH, COMMANDS.ADDITIONAL_RUSSIAN, COMMANDS.TRANSFER_FILE,
                 COMMANDS.ALL_TRANSLATE_DIRECTRY, COMMANDS.TRANSLATE_FILE, COMMANDS.ALL_TRANSFER_DIRECTORY,
                 COMMANDS.STREAMLINE_FILE, COMMANDS.STREAMLINE_DIRECTORY, COMMANDS.SEARCH_UPDATE_STRING_FILE,
                 COMMANDS.SEARCH_UNTRANS_STRING_FILE]

class INTERFACE:
    ADD_FILE_ENG = [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ADDITIONAL_ENGLISH, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Выполнить')]]

    ADD_FILE_RU = [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ADDITIONAL_RUSSIAN, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Выполнить')]]

    SEARCH_UNTRANS_STR = [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.SEARCH_UNTRANS_STRING_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Файл для поиска непереведённых слов:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор')],
        [sg.Button(button_text='Выполнить')]]

    SEARCH_UPDATE_STR = [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.SEARCH_UPDATE_STRING_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Файл локализации (новый):')],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Файл локализации (старый):')],
        [sg.InputText(key='OTHER_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Выполнить')]]

    STREAMLINE = [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.STREAMLINE_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Выполнить')]]

    TRANSFER = [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.TRANSFER_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Выполнить')]]

    TRANSLATE = [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.TRANSLATE_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Выполнить')]]

    TRANSFER_DIRECTORY = [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ALL_TRANSFER_DIRECTORY, size=(85, 1), enable_events=True)],
        [sg.Text('Дирректория с файлами локализации:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Выполнить')]]

    TRANSLATE_DIRECTORY = [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ALL_TRANSLATE_DIRECTRY, size=(85, 1), enable_events=True)],
        [sg.Text('Дирректория с файлами локализации:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Выполнить')]]

    STREAMLINE_DIRECTORY = [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.STREAMLINE_DIRECTORY, size=(85, 1), enable_events=True)],
                            [sg.Text('Дирректория с файлами локализации:')],
                            [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
                            [sg.Button(button_text='Выполнить')]]

    DEFAULT = [[sg.Text('Привет, выбери желаемый режим')],
               [sg.Combo(values=list_commands, key='MODE', size=(85, 1), enable_events=True)]]

# class WINDOW:
#
#     ADD_FILE_ENG = sg.Window('LTA (localization translator assistant)', INTERFACE.ADD_FILE_ENG).Finalize()
#
#     ADD_FILE_RU = sg.Window('LTA (localization translator assistant)', INTERFACE.ADD_FILE_RU).Finalize()
#
#     SEARCH_UNTRANS_STR = sg.Window('LTA (localization translator assistant)', INTERFACE.SEARCH_UNTRANS_STR).Finalize()
#
#     SEARCH_UPDATE_STR = sg.Window('LTA (localization translator assistant)', INTERFACE.SEARCH_UPDATE_STR).Finalize()
#
#     STREAMLINE = sg.Window('LTA (localization translator assistant)', INTERFACE.STREAMLINE).Finalize()
#
#     TRANSFER = sg.Window('LTA (localization translator assistant)', INTERFACE.TRANSFER).Finalize()
#
#     TRANSLATE = sg.Window('LTA (localization translator assistant)', INTERFACE.TRANSLATE).Finalize()
#
#     TRANSFER_DIRECTORY = sg.Window('LTA (localization translator assistant)', INTERFACE.TRANSFER_DIRECTORY).Finalize()
#
#     TRANSLATE_DIRECTORY = sg.Window('LTA (localization translator assistant)', INTERFACE.TRANSLATE_DIRECTORY).Finalize()
#
#     STREAMLINE_DIRECTORY = sg.Window('LTA (localization translator assistant)', INTERFACE.STREAMLINE_DIRECTORY).Finalize()
#
#     DEFAULT = sg.Window('LTA (localization translator assistant)', INTERFACE.DEFAULT).Finalize()