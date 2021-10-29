from abc import ABC, abstractmethod

class GeneralWorkWithInterface(ABC):

    @abstractmethod
    def excution_operation_with_directory(self, general_directory):
        pass