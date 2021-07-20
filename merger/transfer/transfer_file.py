from merger.general.general_operations import GeneralOperations


class TransferFile(GeneralOperations):

    def execute_operation(self, general_path, add_path):
        general_file = self.read_file(general_path)
        add_file = self.write_in_file(add_path)
        add_file.write('l_russian:\n')
        for line in general_file:
            if 'l_english' in line:
                continue
            else:
                add_file.write(line)
        print('Перенос файла {} завершён'.format(general_path))
        add_file.close()
        self.encod_utf8_bom(add_path)