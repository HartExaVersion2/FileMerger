from merger.general.general_operations import GeneralOperations
from common.decorator_for_output_errors import decorator_for_output_errors

class TransferFile(GeneralOperations):

    @decorator_for_output_errors()
    def execute_operation(self, general_path, add_path):
        general_file = self.file_for_read(general_path)
        add_file = self.file_for_write(add_path)
        add_file.write('l_russian:\n')
        for line in general_file:
            if 'l_english' in line:
                continue
            else:
                add_file.write(line)
        print('Перенос файла {} завершён'.format(general_path))
        add_file.close()
        self.encod_utf8_bom(add_path)