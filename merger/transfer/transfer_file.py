from merger.general.general_operations import GeneralOperations
from common.decorator_for_output_errors import decorator_for_output_errors

class TransferFile(GeneralOperations):

    @decorator_for_output_errors()
    def __update_progressbar(self, progressbar, start_progressbar, step_progressbar):
        if progressbar is not None:
            progressbar.UpdateBar(start_progressbar + step_progressbar)
            start_progressbar += step_progressbar
            return start_progressbar
        return 0

    @decorator_for_output_errors()
    def execute_operation(self, general_path, add_path, progressbar=None):
        general_file = self.file_for_read(general_path)
        add_file = self.file_for_write(add_path)
        add_file.write('l_russian:\n')

        start_progressbar = 0
        step_progressbar = 100 / len(self.file_in_list(general_path))

        for line in general_file:
            if 'l_english' in line:
                continue
            else:
                add_file.write(line)
                start_progressbar = self.__update_progressbar(progressbar, start_progressbar, step_progressbar)
        print('Перенос файла {} завершён'.format(general_path))
        add_file.close()
        self.encod_utf8_bom(add_path)