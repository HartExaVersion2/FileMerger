from merger.general.general_operations import GeneralOperations
from common.decorator_for_output_errors import decorator_for_output_errors
class Preprocessor(GeneralOperations):

    def __init__(self, general_path, add_path):
        self.general_path = general_path
        self.general_dict = self.file_in_dict(general_path)
        self.add_dict = self.file_in_dict(add_path)

    @decorator_for_output_errors()
    def __build_dict_untranslated_focuses(self):
        general_keys = set(list(self.general_dict.keys()))
        add_keys = set(list(self.add_dict.keys()))
        total_keys = list(general_keys - add_keys)
        total_dict = {}
        for key in total_keys:
            total_dict[key] = self.general_dict[key]
        return total_dict

    @decorator_for_output_errors()
    def get_general_dict(self):
        dictionary_untranslated_focuses = self.__build_dict_untranslated_focuses()
        general_keys = list(self.general_dict.keys())
        untranslated_keys = list(dictionary_untranslated_focuses.keys())
        '''УПОРЯДОЧИВАНИЕ СЛОВАРЯ'''
        total_dict = dict()
        for line in general_keys:
            if line in untranslated_keys:
                total_dict[line] = dictionary_untranslated_focuses[line]
        return total_dict