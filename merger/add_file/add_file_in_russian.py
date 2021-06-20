from mtranslate import translate
from merger.general.general_operations import GeneralOperations

class AddFileInRussian(GeneralOperations):


    def execute_operation(self, path_general_file, path_additional_file):

        general_list_string = self.file_in_list(path_general_file)
        additional_list_string = self.file_in_list(path_additional_file)

        general_dict_string = self.file_in_dict(path_general_file)
        additional_dict_string = self.file_in_dict(path_additional_file)

        common_line = list(set(general_list_string) & set(additional_list_string))
        additional_file = open(path_additional_file, 'w')

        for line in general_list_string:
            if 'l_english' in line:
                additional_file.write('l_russian\n')
            elif '\n' in line:
                pass
            elif line == ' \n':
                pass
            elif line == '  \n':
                pass
            elif line not in common_line:
                eng = general_dict_string[line]
                ru = translate(eng, 'ru', 'auto')
                additional_file.write(line + ru+'\n')
                if 'desc' in line:
                    additional_file.write('\n')

        for line in additional_list_string:
            if line == '\n':
                additional_file.write('\n')
            elif line == '  \n':
                additional_file.write('\n')
            else:
                additional_file.write(line + additional_dict_string[line])
        additional_file.close()
        print('Операция завершена')