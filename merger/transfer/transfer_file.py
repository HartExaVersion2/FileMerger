from merger.general.general_operations import GeneralOperations


class TransferFile(GeneralOperations):

    def execute_operation(self, general_path, add_path):
        general_file = open(general_path, 'r')
        add_file = open(add_path, 'w')
        for line in general_file:
            if 'l_english' in line:
                add_file.write('l_russian:\n')
            else:
                add_file.write(line)
        print('Перенос файла {} завершён'.format(general_path))
        add_file.close()
        self.encod_utf8_bom(add_path)