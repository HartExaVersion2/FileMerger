from abc import ABC, abstractmethod

class GeneralOperationsInterface(ABC):

    @abstractmethod
    def file_in_list(self, path_on_file) -> list:
        pass

    @abstractmethod
    def file_in_dict(self, path_on_file) -> dict:
        pass