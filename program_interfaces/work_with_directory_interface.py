from abc import ABC, abstractmethod

class GeneralWorkWithDirectoryInterface(ABC):

    @abstractmethod
    def excution_operation_with_directory(self, general_directory):
        pass