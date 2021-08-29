import PySimpleGUI as sg
from common.constant import COMMANDS
from visual_interfaces.interfaces import INTERFACE


class WorkWIthInterface():

    def __init__(self):
        self.current_mode = None

    def change_interfase(self, mode):
        # if self.current_mode == mode:
        #     return None
        # else:
        #     self.current_mode = mode
        if mode == COMMANDS.ADDITIONAL_ENGLISH:
            window = sg.Window('LTA (localization translator assistant)', INTERFACE.ADD_FILE_ENG)
        elif mode == COMMANDS.ADDITIONAL_RUSSIAN:
            window = sg.Window('LTA (localization translator assistant)', INTERFACE.ADD_FILE_RU)
        elif mode == COMMANDS.TRANSFER_FILE:
            window = sg.Window('LTA (localization translator assistant)', INTERFACE.TRANSFER).Finalize()
        elif mode == COMMANDS.TRANSLATE_FILE:
            window = sg.Window('LTA (localization translator assistant)', INTERFACE.TRANSLATE).Finalize()
        elif mode == COMMANDS.STREAMLINE_FILE:
            window = sg.Window('LTA (localization translator assistant)', INTERFACE.STREAMLINE).Finalize()
        elif mode == COMMANDS.SEARCH_UPDATE_STRING_FILE:
            window = sg.Window('LTA (localization translator assistant)', INTERFACE.SEARCH_UPDATE_STR).Finalize()
        elif mode == COMMANDS.SEARCH_UNTRANS_STRING_FILE:
            window = sg.Window('LTA (localization translator assistant)', INTERFACE.SEARCH_UNTRANS_STR).Finalize()
        elif mode == COMMANDS.ALL_TRANSLATE_DIRECTRY:
            window = sg.Window('LTA (localization translator assistant)', INTERFACE.TRANSLATE_DIRECTORY).Finalize()
        elif mode == COMMANDS.STREAMLINE_DIRECTORY:
            window = sg.Window('LTA (localization translator assistant)', INTERFACE.STREAMLINE_DIRECTORY).Finalize()
        elif mode == COMMANDS.ALL_TRANSFER_DIRECTORY:
            window = sg.Window('LTA (localization translator assistant)', INTERFACE.TRANSFER_DIRECTORY).Finalize()
        else:
            window = sg.Window('LTA (localization translator assistant)', INTERFACE.DEFAULT).Finalize()
        return window

    def get_default_interface(self):
        return sg.Window('LTA (localization translator assistant)', INTERFACE.DEFAULT, size=(700, 100))