from merger.general.general_operations import GeneralOperations
import re
from common.decorator_for_output_errors import decorator_for_output_errors

class SearchUntransString(GeneralOperations):

    @decorator_for_output_errors()
    def __update_progressbar(self, progressbar, start_progressbar, step_progressbar):
        if progressbar is not None:
            progressbar.UpdateBar(start_progressbar + step_progressbar)
            start_progressbar += step_progressbar
            return start_progressbar
        return 0

    @decorator_for_output_errors()
    def execute_operation(self, add_path, progressbar=None):
        work_file_dict = self.file_in_dict(add_path)
        english_keys = []

        start_progressbar = 0
        step_progressbar = 100 / len(work_file_dict.keys())

        for key in work_file_dict:
            string = work_file_dict[key]
            russian_letter = re.findall(r'[а-яА-ЯёЁ]', string)
            if not russian_letter:
                english_keys.append(key)

        if english_keys:
            add_file = self.file_for_write(add_path)
            add_file.write('l_russian:\n')
            for key in english_keys:
                if 'l_english' in key or 'l_russian' in key:
                    continue
                add_file.write(key + work_file_dict[key])
                if 'desc' in key:
                    add_file.write('\n')
                    start_progressbar = self.__update_progressbar(progressbar, start_progressbar, step_progressbar)
                del work_file_dict[key]

            for key in work_file_dict:
                if 'l_english' in key or 'l_russian' in key:
                    continue
                add_file.write(key + work_file_dict[key])
                if 'desc' in key:
                    add_file.write('\n')
                    start_progressbar = self.__update_progressbar(progressbar, start_progressbar, step_progressbar)

            add_file.close()
            self.encod_utf8_bom(add_path)
