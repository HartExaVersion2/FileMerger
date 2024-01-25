import PySimpleGUI as sg
import io
import os
from common.constant import COMMANDS
from PIL import Image

list_commands = [COMMANDS.ADDITIONAL_ENGLISH, COMMANDS.ADDITIONAL_RUSSIAN, COMMANDS.TRANSFER_FILE,
                 COMMANDS.ALL_TRANSLATE_DIRECTRY, COMMANDS.TRANSLATE_FILE, COMMANDS.ALL_TRANSFER_DIRECTORY,
                 COMMANDS.STREAMLINE_FILE, COMMANDS.STREAMLINE_DIRECTORY, COMMANDS.SEARCH_UPDATE_STRING_FILE,
                 COMMANDS.SEARCH_UNTRANS_STRING_FILE]


class Interfaces:


    def __init__(self, settings):
        self.settings = settings
        self.__bio_image_setting = self.__get_image('setting.png')
        self.__bio_image_help = self.__get_image('help.png')
        self.__bio_image_logo = self.__get_image('logo.png')
        self.__bio_image_main_setting = self.__get_image('main_setting.png', size=(200, 200))

    def __get_image(self, image_name, size=(45, 45)):
        path_to_image = self.__get_path_to_images() + '\\' + image_name
        image = Image.open(path_to_image)
        image.thumbnail(size)
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        return bio


    def __get_path_to_images(self):
        path_to_project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_images = path_to_project + '\common\images'
        return path_to_images

    def get_add_file_eng(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ADDITIONAL_ENGLISH, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить'), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_add_file_ru(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ADDITIONAL_RUSSIAN, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить'), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_search_untrans_str(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.SEARCH_UNTRANS_STRING_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Файл для поиска непереведённых слов:')],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор')],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить'), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_search_update_str(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.SEARCH_UPDATE_STRING_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Файл локализации (новый):')],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Файл локализации (старый):')],
        [sg.InputText(key='OTHER_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить'), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_streamline_file(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.STREAMLINE_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить'), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_trinsfer_file(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.TRANSFER_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить'), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_translate_file(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.TRANSLATE_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить'), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_transfer_directory(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ALL_TRANSFER_DIRECTORY, size=(85, 1), enable_events=True)],
        [sg.Text('Дирректория с файлами локализации:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить'), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_translate_directory(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ALL_TRANSLATE_DIRECTRY, size=(85, 1), enable_events=True)],
        [sg.Text('Дирректория с файлами локализации:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить'), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_streamline_directory(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.STREAMLINE_DIRECTORY, size=(85, 1), enable_events=True)],
        [sg.Text('Дирректория с файлами локализации:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить'), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_interface_translator_path(self):
        return [[sg.Checkbox(default=True, text='Помощник в переводе', key='HELPER')],
         [sg.Text('Оригинальный файл:', size=(20, 1))],
         [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
         [sg.Text('Ваш файл:', size=(20, 1))],
         [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
         [sg.Button(button_text='Назад'), sg.Button(button_text=COMMANDS.BEGIN_TRANSLATE), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_interface_translator_without_helper(self, param: list):
        return [[sg.Text(param[0], size=(60, 10)), sg.Multiline(size=(60, 10), key='title')],
                [sg.Text(param[1], size=(60, 40)), sg.Multiline(size=(60, 40), key='desc')],
                [sg.Button(button_text='Назад'), sg.Button(button_text='Сохранить'), sg.Button(button_text='Далее')],
                [sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_interface_translator_with_helper(self, param: list):
        return [[sg.Text(param[0], size=(60, 10)), sg.Text(param[2], size=(60, 10)), sg.Multiline(size=(60, 10), key='title')],
                [sg.Text(param[1], size=(60, 40)), sg.Text(param[3], size=(60, 40)), sg.Multiline(size=(60, 40), key='desc')],
                [sg.Button(button_text='Назад'), sg.Button(button_text='Сохранить'), sg.Button(button_text='Далее')],
                [sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]

    def get_settings(self):
        translators = ['GoogleTranslator', 'YandexTranslator', 'DeepLTranslator']
        game = ['HoI4']
        lang_to = []
        lang_from = []
        image = [[sg.Image(data=self.__bio_image_main_setting.getvalue())]]
        return [[sg.Column(image, vertical_alignment='center', justification='center', k='-C-')],
                [sg.Text('Тема:'), sg.Combo(values=sg.theme_list(), default_value=self.settings.theme, auto_size_text=True, key='NEW_THEME', enable_events=True)],
                [sg.Text('Переводчик:'), sg.Combo(values=translators, default_value=self.settings.translator, auto_size_text=True, key='NEW_TRANSLATOR', enable_events=True)],
                [sg.Text('Игра:'), sg.Combo(values=game, default_value=self.settings.game, auto_size_text=True, key='NEW_GAME', enable_events=True)],
                [sg.Text('Оригинальный язык:'), sg.Combo(values=lang_from, default_value=self.settings.game, auto_size_text=True, key='LANG_FROM', enable_events=True)],
                [sg.Text('Язык перевода:'), sg.Combo(values=lang_to, default_value=self.settings.game, auto_size_text=True, key='LANG_TO', enable_events=True)],
                [sg.Text('API ключ:'), sg.InputText(key='API_KEY'), sg.Button(button_text='Добавить')],
                [sg.Button(button_text='Назад')]]

    def get_default(self):
        return [[sg.Image(key="help", data=self.__bio_image_help.getvalue(), enable_events=True), sg.Push(), sg.Image(key="settings", data=self.__bio_image_setting.getvalue(), enable_events=True)],
        [sg.Text('Привет, выбери желаемый режим', auto_size_text=True)],
        [sg.Combo(values=list_commands, default_value=list_commands[2], key='MODE', auto_size_text=True, enable_events=True)],
        [sg.Button(button_text=COMMANDS.INTERFACE_TRANSLATOR_PATH, auto_size_button=True), sg.Push(), sg.Image(key="logo", data=self.__bio_image_logo.getvalue())]]