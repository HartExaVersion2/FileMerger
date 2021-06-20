from interfaces.work_with_directory_interface import GeneralWorkWithInterface
import os

class GeneralWorkWithDirectory(GeneralWorkWithInterface):

    def __init__(self, operations):
        self.operations = operations()

    def excution_operation_with_directory(self, general_directory):
        list_of_files = os.listdir(general_directory)
        for english_file_name in list_of_files:
            name_rus_file = english_file_name.replace('l_english', 'l_russian')
            self.operations.execute_operation(general_directory + '/{}'.format(english_file_name),
                                              general_directory + '/{}'.format(name_rus_file))