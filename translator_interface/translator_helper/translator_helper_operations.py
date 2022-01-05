from merger.general.general_operations import GeneralOperations
from translator_interface.translator_helper.preprocessor import Preprocessor
from translator.translator import TextTranslator
from common.constant import FOCUS
from common.decorator_for_output_errors import decorator_for_output_errors

class TranslatorHealperOperations(GeneralOperations):

    def __init__(self, path_general_file, add_path, translate=True):
        self.translate = translate
        if translate:
            self.translator = TextTranslator()
        self.preprocessor = Preprocessor(path_general_file, add_path)

        self.add_path = add_path
        self.general_dict = self.preprocessor.get_general_dict()
        self.earlier_translation = self.file_in_dict(add_path)
        if 'l_russian' in self.earlier_translation.keys():
            del self.earlier_translation['l_russian']
        self.headers = list(self.general_dict.keys())
        self.focuses = list(self.general_dict.values())
        self.current_text_focus = ''
        self.current_title_focus = ''
        self.variable_current_desc_focus = ''
        self.variable_current_title_focus = ''
        self.translator_dictionary = self.earlier_translation
        if '' in list(self.translator_dictionary.keys()):
            del self.translator_dictionary['']

    @decorator_for_output_errors()
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

    @decorator_for_output_errors()
    def get_focus(self):
        self.__search_focus()
        if self.current_title_focus is not None and self.current_text_focus is not None:
            if self.translate:
                trans_title = self.translator.transleate_text(self.current_title_focus)
                trans_desc = self.translator.transleate_text(self.current_text_focus)
                all_focus = {FOCUS.TITLE: self.current_title_focus, FOCUS.DESC: self.current_text_focus, FOCUS.TRANSLATE_TITLE:
                             trans_title, FOCUS.TRANSLATE_DESC: trans_desc}
                return all_focus
            else:
                all_focus = {FOCUS.TITLE: self.current_title_focus, FOCUS.DESC: self.current_text_focus, FOCUS.TRANSLATE_TITLE:
                             None, FOCUS.TRANSLATE_DESC: None}
                return all_focus
        else:
            return None

    @decorator_for_output_errors()
    def write_focus(self, title, desc):
        if title != '\n' and desc != '\n':
            self.translator_dictionary[self.variable_current_title_focus] = ':0 "' + title.replace('\n', '') + '"' + '\n'
            self.translator_dictionary[self.variable_current_desc_focus] = ':0 "' + desc.replace('\n', '') + '"' + '\n'

    @decorator_for_output_errors()
    def save_in_file(self):
        variables = list(self.translator_dictionary.keys())
        file = self.file_for_write(self.add_path)
        file.write('l_russian:\n')
        for variable in variables:
            file.write(variable + self.translator_dictionary[variable])
            if 'desc' in variable:
                file.write('\n')
        file.close()