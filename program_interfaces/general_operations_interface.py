from abc import ABC, abstractmethod

class GeneralOperationsInterface(ABC):

    @abstractmethod
    def file_in_list(self, path_on_file: str) -> list:
        pass

    @abstractmethod
    def file_in_dict(self, path_on_file: str) -> dict:
        pass

    @abstractmethod
    def encod_utf8_bom(self, path_on_file: str):
        pass

    @abstractmethod
    def file_for_read(self, path_to_file: str):
        pass

    @abstractmethod
    def file_for_write(self, path_to_file: str):
        pass