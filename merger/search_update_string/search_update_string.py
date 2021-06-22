from merger.general.general_operations import GeneralOperations

class SearchUpdateString(GeneralOperations):

    def execute_operation(self, general_path_old_v, general_path_new_version, add_path):
        old_v_dict = self.file_in_dict(general_path_old_v)
        new_v_dict = self.file_in_dict(general_path_new_version)
        add_dict = self.file_in_dict(add_path)

        incumbent_string = []

        for old_v_key in old_v_dict:
            if old_v_dict[old_v_key] != new_v_dict[old_v_key]:
                incumbent_string.append(old_v_key)

        if incumbent_string:
            add_file = open(add_path, 'w')
            for key in add_dict:
                if key not in incumbent_string:
                    add_file.write(key + add_dict[key])
                else:
                    add_file.write(key + add_dict[key] + ' # ИЗМЕНЕНО В НОВОЙ ВЕРСИИ!') #ToDo разукрасить
            add_file.close()
