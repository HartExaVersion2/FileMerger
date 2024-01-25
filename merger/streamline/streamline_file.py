from merger.general.general_operations import GeneralOperations
from common.decorator_for_output_errors import decorator_for_output_errors

class StreamlineFile(GeneralOperations):

    @decorator_for_output_errors()
    def __update_progressbar(self, progressbar, start_progressbar, step_progressbar):
        if progressbar is not None:
            progressbar.UpdateBar(start_progressbar + step_progressbar)
            start_progressbar += step_progressbar
            return start_progressbar
        return 0

    @decorator_for_output_errors()
    def execute_operation(self, general_path, add_path, progressbar=None):
        '''упорядочивает файл'''
        additional_file_in_dict = self.file_in_dict(add_path)

        general_file = self.file_for_read(general_path)
        additional_file = self.file_for_write(add_path)
        additional_file.write('l_russian:\n')

        start_progressbar = 0
        step_progressbar = 100 / len(additional_file_in_dict.keys())

        for line in general_file:
            try:
                if 'l_english' in line:
                    continue
                elif ':' in line:
                    variables = line.split(':')[0]
                    text = additional_file_in_dict[variables]
                    strline = variables + text
                    additional_file.write(strline)
                    start_progressbar = self.__update_progressbar(progressbar, start_progressbar, step_progressbar)
                else:
                    additional_file.write(line)
            except Exception as e:
                additional_file.write(line)
        general_file.close()
        additional_file.close()
        self.encod_utf8_bom(add_path)