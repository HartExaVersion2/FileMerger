from merger.general.general_operations import GeneralOperations
from translator.translator import Translator
from common.constant import FOCUS

class TranslatorHealperOperations(GeneralOperations):

    def __init__(self, path_general_file, add_path):
        self.translator = Translator()

        self.add_path = add_path
        self.general_dict = self.file_in_dict(path_general_file)
        self.headers = list(self.general_dict.keys())
        self.focuses = list(self.general_dict.values())
        self.current_text_focus = ''
        self.current_title_focus = ''
        self.variable_current_desc_focus = ''
        self.variable_current_title_focus = ''
        self.translator_dictionary = {}

    def __search_focus(self):#ToDo нет условия остановки. Оно будет работать бесконечно с Последними найденными значениями
        for header in self.headers:
            if 'desc' in header:
                self.current_text_focus = self.general_dict[header][4:-3]
                self.variable_current_desc_focus = header
                index = self.headers.index(header)
                self.current_title_focus = self.general_dict[self.headers[index-1]][4:-3]
                self.variable_current_title_focus = self.headers[index-1]
                self.headers[index-1] = self.headers[index] = '0'
                break

    def get_focus(self):
        self.__search_focus()
        if self.current_title_focus is not None and self.current_text_focus is not None:
            trans_title = self.translator.transleate_text(self.current_title_focus)
            trans_desc = self.translator.transleate_text(self.current_text_focus)
            all_focus = {FOCUS.TITLE: self.current_title_focus, FOCUS.DESC: self.current_text_focus, FOCUS.TRANSLATE_TITLE:
                         trans_title, FOCUS.TRANSLATE_DESC: trans_desc}
            return all_focus
        else:
            return None

    def write_focus(self, title, desc):
        if title != '\n' and desc != '\n':
            self.translator_dictionary[self.variable_current_title_focus] = ':0 "' + title + '"'
            self.translator_dictionary[self.variable_current_desc_focus] = ':0 "' + desc + '"'

    def save_in_file(self):
        variables = list(self.translator_dictionary.keys())
        file = self.file_for_write(self.add_path)
        file.write('l_russian:')
        for variable in variables:
            file.write(variable + self.translator_dictionary[variable])
            if 'desc' in variable:
                file.write('\n')
        file.close()