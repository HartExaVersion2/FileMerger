class Settings:

    def __init__(self):
        self._theme = None
        self._lang_to = None
        self._lang_from = None
        self._screen_resolution = None
        self._game = None
        self._translator = None
        self._api_key = None
        self._deepl_api_key = None
        self.__get_settings()

    def __get_dict_settings(self):
        return {'theme': self._theme,
                'lang_to': self._lang_to,
                'lang_from': self._lang_from,
                'screen_resolution': self._screen_resolution,
                'game': self._game,
                'translator': self._translator,
                'api_key': self._api_key}

    def __get_settings(self):
        file = open('common/setting.txt', 'r')
        for line in file:
            key = line.split('=')[0]
            if key == 'theme':
                self._theme = line.split('=')[1].replace('\n', '')
            elif key == 'lang_to':
                self._lang_to = line.split('=')[1].replace('\n', '')
            elif key == 'lang_from':
                self._lang_from = line.split('=')[1].replace('\n', '')
            elif key == 'screen_resolution':
                self._screen_resolution = line.split('=')[1].replace('\n', '')
            elif key == 'game':
                self._game = line.split('=')[1].replace('\n', '')
            elif key == 'translator':
                self._translator = line.split('=')[1].replace('\n', '')
            elif key == 'api_key':
                self._api_key = line.split('=')[1].replace('\n', '')
            else:
                pass

    def __set_settings(self):
        file = open('common/setting.txt', 'w')
        dict_settings = self.__get_dict_settings()
        for setting in dict_settings:
            file.write(str(setting) + '=' + str(dict_settings[setting]) + '\n')


    @property
    def theme(self):
        return self._theme

    @property
    def lang_to(self):
        return self._lang_to

    @property
    def lang_from(self):
        return self._lang_from

    @property
    def screen_resolution(self):
        return self._screen_resolution

    @property
    def game(self):
        return self._game

    @property
    def translator(self):
        return self._translator

    @property
    def api_key(self):
        return self._api_key

    @theme.setter
    def theme(self, new_theme):
        self._theme = new_theme
        self.__set_settings()

    @lang_to.setter
    def lang_to(self, new_lang_to):
        self._lang_to = new_lang_to
        self.__set_settings()

    @lang_from.setter
    def lang_from(self, new_lang_from):
        self._lang_from = new_lang_from
        self.__set_settings()

    @screen_resolution.setter
    def screen_resolution(self, new_screen_resolution):
        self._screen_resolution = new_screen_resolution
        self.__set_settings()

    @game.setter
    def game(self, new_game):
        self._game = new_game
        self.__set_settings()

    @translator.setter
    def translator(self, new_translator):
        self._translator = new_translator
        self.__set_settings()

    @api_key.setter
    def api_key(self, new_key):
        self._api_key = new_key
        self.__set_settings()