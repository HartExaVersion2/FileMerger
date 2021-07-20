from interfaces.general_operations_interface import GeneralOperationsInterface
import shutil

class GeneralOperations(GeneralOperationsInterface):

    def file_in_list(self, path_on_file) -> list:
        file = open(path_on_file, 'r')
        list_string = []
        for line in file:
            if line and (':' in line):
                try:
                    list_string.append(line.split(':', 1)[0])
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
                    dict_string[line.split(':', 1)[0]] = ':' + line.split(':', 1)[1]
                except:
                    pass
        file.close()
        return dict_string

    def encod_utf8_bom(self, path_on_file: str):
        with open(path_on_file, encoding="utf-8") as f_in, open(path_on_file + ".tmp", encoding="utf-8-sig", mode="w") as f_out:
            f_out.write(f_in.read())
            shutil.move(path_on_file + ".tmp", path_on_file)