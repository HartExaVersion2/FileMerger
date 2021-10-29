from program_interfaces.work_with_directory_interface import GeneralWorkWithInterface
import os

class GeneralWorkWithDirectory(GeneralWorkWithInterface):

    def __init__(self, operations):
        self.operations = operations()

    def excution_operation_with_directory(self, general_directory):
        list_of_files = os.listdir(general_directory)

        '''ВЫБОР РАЗДЕЛИТЕЛЯ (WINDOWS ИЛИ LINUX)'''
        if '/' in general_directory:
            delimeter = '/'
        else:
            delimeter = '\\'

        for english_file_name in list_of_files:
            name_rus_file = english_file_name.replace('l_english', 'l_russian')
            self.operations.execute_operation(general_directory + delimeter + english_file_name,
                                              general_directory + delimeter + name_rus_file)