from merger.general.general_operations import GeneralOperations

class AddFileInEnglish(GeneralOperations):

    def execute_operation(self, path_general_file, path_additional_file):
        '''Дополнить файл на английском'''

        general_dict_string = self.file_in_dict(path_general_file)
        additional_dict_string = self.file_in_dict(path_additional_file)

        general_list_string = list(general_dict_string.keys())
        additional_list_string = list(additional_dict_string.keys())

        common_string = set(general_list_string) & set(additional_list_string)
        additional_file = open(path_additional_file, 'w')
        additional_file.write('l_russian:\n')

        for line in general_list_string:
            if 'l_english' in line or 'l_russian' in line:
                continue
            elif '\n' in line:
                continue
            elif line == ' \n':
                continue
            elif line == '  \n':
                continue
            elif line not in common_string:
                additional_file.write(line + general_dict_string[line])
                if 'desc' in line:
                    additional_file.write('\n')
                del general_dict_string[line]

        other_string = list(general_dict_string.keys())
        for line in other_string:
            if 'l_english' in line or 'l_russian' in line:
                continue
            elif line == '\n':
                additional_file.write('\n')
            elif line == '  \n':
                additional_file.write('\n')
            elif ':' in additional_dict_string[line]:
                additional_file.write(line + additional_dict_string[line])
                if 'desc' in line:
                    additional_file.write('\n')
            else:
                additional_file.write(line)
        additional_file.close()

        self.encod_utf8_bom(path_additional_file)
