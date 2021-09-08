import PySimpleGUI as sg
from common.constant import COMMANDS

list_commands = [COMMANDS.ADDITIONAL_ENGLISH, COMMANDS.ADDITIONAL_RUSSIAN, COMMANDS.TRANSFER_FILE,
                 COMMANDS.ALL_TRANSLATE_DIRECTRY, COMMANDS.TRANSLATE_FILE, COMMANDS.ALL_TRANSFER_DIRECTORY,
                 COMMANDS.STREAMLINE_FILE, COMMANDS.STREAMLINE_DIRECTORY, COMMANDS.SEARCH_UPDATE_STRING_FILE,
                 COMMANDS.SEARCH_UNTRANS_STRING_FILE]

class Interfaces:
    def get_add_file_eng(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ADDITIONAL_ENGLISH, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_add_file_ru(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ADDITIONAL_RUSSIAN, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_search_untrans_str(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.SEARCH_UNTRANS_STRING_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Файл для поиска непереведённых слов:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_search_update_str(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.SEARCH_UPDATE_STRING_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Файл локализации (новый):')],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Файл локализации (старый):')],
        [sg.InputText(key='OTHER_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_streamline_file(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.STREAMLINE_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_trinsfer_file(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.TRANSFER_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_translate_file(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.TRANSLATE_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_transfer_directory(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ALL_TRANSFER_DIRECTORY, size=(85, 1), enable_events=True)],
        [sg.Text('Дирректория с файлами локализации:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_translate_directory(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ALL_TRANSLATE_DIRECTRY, size=(85, 1), enable_events=True)],
        [sg.Text('Дирректория с файлами локализации:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_streamline_directory(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.STREAMLINE_DIRECTORY, size=(85, 1), enable_events=True)],
        [sg.Text('Дирректория с файлами локализации:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_default(self):
        return [[sg.Text('Привет, выбери желаемый режим')],
        [sg.Button(button_text='Включить интерфейс переводчика')],
        [sg.Combo(values=list_commands, key='MODE', size=(85, 1), enable_events=True)]]
