from merger.general.general_operations import GeneralOperations
import re

class SearchUntransString(GeneralOperations):

    def execute_operation(self, add_path):
        work_file_dict = self.file_in_dict(add_path)
        english_keys = []
        for key in work_file_dict:
            string = work_file_dict[key]
            russian_letter = re.findall(r'[а-яА-ЯёЁ]', string)
            if not russian_letter:
                english_keys.append(key)

        if english_keys:
            add_file = open(add_path, 'w')
            for key in english_keys:
                add_file.write(work_file_dict[key])
                del work_file_dict[key]

            for key in work_file_dict:
                add_file.write(work_file_dict[key])

            add_file.close()



