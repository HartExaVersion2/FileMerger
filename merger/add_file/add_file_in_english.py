from merger.general.general_operations import GeneralOperations
from common.decorator_for_output_errors import decorator_for_output_errors

class AddFileInEnglish(GeneralOperations):

    @decorator_for_output_errors()
    def __update_progressbar(self, progressbar, start_progressbar, step_progressbar):
        if progressbar is not None:
            progressbar.UpdateBar(start_progressbar + step_progressbar)
            start_progressbar += step_progressbar
            return start_progressbar
        return 0

    @decorator_for_output_errors()
    def execute_operation(self, path_general_file, add_path, progressbar=None):
        '''Дополнить файл на английском'''

        general_dict_string = self.file_in_dict(path_general_file)
        additional_dict_string = self.file_in_dict(add_path)

        general_list_string = list(general_dict_string.keys())
        additional_list_string = list(additional_dict_string.keys())

        common_string = set(general_list_string) & set(additional_list_string)
        additional_file = self.file_for_write(add_path)
        additional_file.write('l_russian:\n')

        start_progressbar = 0
        step_progressbar = 100 / len(general_list_string)

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
                start_progressbar = self.__update_progressbar(progressbar, start_progressbar, step_progressbar)
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
                start_progressbar = self.__update_progressbar(progressbar, start_progressbar, step_progressbar)
                if 'desc' in line:
                    additional_file.write('\n')
            else:
                additional_file.write(line)
        additional_file.close()

        self.encod_utf8_bom(add_path)
