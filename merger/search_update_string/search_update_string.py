from merger.general.general_operations import GeneralOperations


class SearchUpdateString(GeneralOperations):

    def execute_operation(self, general_path_old_v, general_path_new_v, add_path):
        old_v_dict = self.file_in_dict(general_path_old_v)
        new_v_dict = self.file_in_dict(general_path_new_v)
        add_dict = self.file_in_dict(add_path)

        incumbent_string = []

        for old_v_key in old_v_dict:
            if 'l_english' in old_v_key or 'l_russian' in old_v_key:
                continue
            if old_v_dict[old_v_key] != new_v_dict[old_v_key]:
                incumbent_string.append(old_v_key)

        if incumbent_string:
            add_file = self.write_in_file(add_path)
            add_file.write('l_russian:\n')
            for key in add_dict:
                if 'l_english' in key or 'l_russian' in key:
                    continue
                if key not in incumbent_string:
                    add_file.write(key + add_dict[key])
                    if 'desc' in key:
                        add_file.write('\n')
                else:
                    add_file.write(key + add_dict[key].replace('\n', '') + ' # ИЗМЕНЕНО В НОВОЙ ВЕРСИИ!\n') #ToDo разукрасить
                    if 'desc' in key:
                        add_file.write('\n')
            add_file.close()
            self.encod_utf8_bom(add_path)
