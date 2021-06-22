from interfaces.general_operations_interface import GeneralOperationsInterface

class GeneralOperations(GeneralOperationsInterface):

    def file_in_list(self, path_on_file) -> list:
        file = open(path_on_file, 'r')
        list_string = []
        for line in file:
            if line and (':' in line):
                try:
                    list_string.append(line.split(':')[0]) #ToDo узнать как делать сплит только по первому значению
                except:
                    pass
        file.close()
        return list_string

    def file_in_dict(self, path_on_file) -> dict:
        file = open(path_on_file, 'r')
        dict_string = {}
        for line in file:
            if line and line!='\n':
                try:
                    dict_string[line.split(':')[0]] = ':' + line.split(':')[1]
                except:
                    pass
        file.close()
        return dict_string