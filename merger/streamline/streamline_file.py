from merger.general.general_operations import GeneralOperations


class StreamlineFile(GeneralOperations):

    def execute_operation(self, general_path, add_path):
        '''упорядочивает файл'''
        additional_file_in_dict = self.file_in_dict(add_path)

        general_file = self.read_file(general_path)
        additional_file = self.write_in_file(add_path)
        additional_file.write('l_russian:\n')

        #ToDo добавить предупреждение о несовпадению кол-ва переменных
        for line in general_file:
            try:
                if 'l_english' in line:
                    continue
                elif ':' in line:
                    variables = line.split(':')[0]
                    text = additional_file_in_dict[variables]
                    strline = variables + text
                    additional_file.write(strline)
                else:
                    additional_file.write(line)
            except Exception as e:
                print(e)
                additional_file.write(line)
        general_file.close()
        additional_file.close()
        self.encod_utf8_bom(add_path)