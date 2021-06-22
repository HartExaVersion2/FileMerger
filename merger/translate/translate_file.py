from translator.translator import Translator
from merger.general.general_operations import GeneralOperations

class TranslateFile(GeneralOperations):

    def __init__(self):
        self.translator = Translator()

    def execute_operation(self, path_general_file, path_additional_file):
        list_english_line = self.file_in_list(path_general_file)
        dict_english_line = self.file_in_dict(path_general_file)
        additional_file = open(path_additional_file, 'w')
        for line in list_english_line:
            if 'l_english' in line:
                additional_file.write('l_russian:\n')
            elif '#' in line:
                additional_file.write(line)
            elif '\n' in line:
                additional_file.write('\n')
            elif line == ' \n':
                additional_file.write(' \n')
            elif line == '  \n':
                additional_file.write('  \n')
            else:
                try:
                    ru_text = self.translator.transleate_text(text=dict_english_line[line].replace('"', ''))
                    ru_text = '"' + ru_text + '"'
                    additional_file.write(line + ru_text + '\n')
                    if 'desc' in line:
                        additional_file.write('\n')
                except:
                    additional_file.write(line)
        additional_file.close()
        print('Файл' + ' ' + path_additional_file.split('/')[-1] + ' Переведён')