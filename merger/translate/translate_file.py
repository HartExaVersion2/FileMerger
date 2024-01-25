from translator.translator import TextTranslator
from merger.general.general_operations import GeneralOperations
from urllib.request import urlopen
from common.errors import ConnectError
from common.decorator_for_output_errors import decorator_for_output_errors
import time

class TranslateFile(GeneralOperations):

    def __init__(self):
        self.translator = TextTranslator()

    def __update_progressbar(self, progressbar, start_progressbar, step_progressbar):
        if progressbar is not None:
            progressbar.UpdateBar(start_progressbar + step_progressbar)
            start_progressbar += step_progressbar
            return start_progressbar
        return 0

    def __check_count_symbol(self, list_offers, new_offer):
        count_symbol = 0
        for offer in list_offers:
            count_symbol_in_offer = len(offer)
            count_symbol += count_symbol_in_offer
        count_symbol_in_new_offer = len(new_offer)
        if count_symbol + count_symbol_in_new_offer > 4500:
            return True
        else:
            return False

    @decorator_for_output_errors()
    def execute_operation(self, path_general_file, add_path, progressbar=None):
        list_focuses_for_translate = []
        list_headers = []
        count = 0

        list_english_line = self.file_in_list(path_general_file)
        dict_english_line = self.file_in_dict(path_general_file)
        additional_file = self.file_for_write(add_path)

        count_focuses = len(list_english_line)

        start_progressbar = 0
        step_progressbar = 100 / len(list_english_line)

        for line in list_english_line:
            if 'l_english' in line:
                additional_file.write('l_russian:\n')
            elif '#' in line:
                additional_file.write(line)
            elif '\n' in line:
                additional_file.write('\n')
            elif line == ' \n':
                additional_file.write(' \n')
            elif line == '  \n':
                additional_file.write('  \n')
            elif 'Focus Tree' in dict_english_line[line]:
                additional_file.write(line+dict_english_line[line])
            else:
                try:
                    # self.__check_connection() #ToDo пофиксить
                    text = dict_english_line[line].replace(':0 "', '').replace(':0"', '').replace('"', '')+' ' + '%'
                    if self.__check_count_symbol(list_focuses_for_translate, text) or count == count_focuses-1:
                        focuses_in_russian = self.translator.transleate_text(text=''.join(list_focuses_for_translate))
                        list_focuses_in_russian = focuses_in_russian.split('%')
                        for number_focus in range(len(list_headers)):
                            header = list_headers[number_focus]
                            text_focus = list_focuses_in_russian[number_focus].rstrip().rstrip('\n').lstrip()
                            additional_file.write(header + ':0 "' + text_focus + '"' + '\n')
                            start_progressbar = self.__update_progressbar(progressbar, start_progressbar, step_progressbar)
                            if 'desc' in list_headers[number_focus]:
                                additional_file.write('\n')
                    else:
                        list_focuses_for_translate.append(text)
                        list_headers.append(line)
                        count += 1
                except:
                    additional_file.write(line)
        additional_file.close()
        print('Файл' + ' ' + add_path.split('/')[-1] + ' Переведён')
        self.encod_utf8_bom(add_path)

    @decorator_for_output_errors()
    def __check_connection(self):
        for timeout in [1, 5, 10, 15]:
            try:
                response = urlopen('http://google.com', timeout=timeout)
            except:
                raise ConnectError