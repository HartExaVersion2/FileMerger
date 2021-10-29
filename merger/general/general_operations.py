from program_interfaces.general_operations_interface import GeneralOperationsInterface
import shutil
import codecs
import os

class GeneralOperations(GeneralOperationsInterface):

    def file_in_list(self, path_on_file) -> list:
        file = self.file_for_read(path_on_file)
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
        file = self.file_for_read(path_on_file)
        dict_string = {}
        for line in file:
            if line and line != '\n':
                try:
                    dict_string[line.split(':', 1)[0]] = ':' + line.split(':', 1)[1]
                except:
                    pass
        file.close()
        return dict_string

    def encod_utf8_bom(self, path_on_file: str):
        with codecs.open(path_on_file, encoding="utf-8") as f_in, codecs.open(path_on_file + ".tmp", encoding="utf-8-sig", mode="w") as f_out:
            f_out.write(f_in.read())
            shutil.move(path_on_file + ".tmp", path_on_file)

    def change_file_extension(self, path_on_file, extension):
        path_on_file = path_on_file
        path_without_extension = os.path.splitext(path_on_file)[0]
        os.rename(path_on_file, path_without_extension + extension)

    def file_for_read(self, path_to_file: str):
        return codecs.open(path_to_file, 'r', 'utf_8_sig')

    def file_for_write(self, path_to_file: str):
        return codecs.open(path_to_file, 'w', 'utf_8_sig')