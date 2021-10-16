from merger.general.general_operations import GeneralOperations

class Preprocessor(GeneralOperations):

    def __init__(self, general_path, add_path):
        self.general_dict = self.file_in_dict(general_path)
        self.add_dict = self.file_in_dict(add_path)

    def get_general_dict(self):
        general_keys = set(list(self.general_dict.keys()))
        add_keys = set(list(self.add_dict.keys()))
        total_keys = list(general_keys - add_keys)
        total_dict = {}
        for key in total_keys:
            total_dict[key] = self.general_dict[key]
        return total_dict