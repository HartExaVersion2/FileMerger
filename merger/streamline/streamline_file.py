from merger.general.general_operations import GeneralOperations

class StreamlineFile(GeneralOperations):

    def execute_operation(self, general_path, add_path):
        additional_file_in_dict = self.file_in_dict(add_path)

        general_file = open(general_path, 'r')
        additional_file = open(add_path, 'w')

        #ToDo добавить ошибку на несовпадение кол-ва переменных
        for line in general_file:
            try:
                if 'l_english:' in line:
                    additional_file.write('l_russian:\n')
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