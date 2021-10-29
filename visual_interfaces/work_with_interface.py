import PySimpleGUI as sg
from common.constant import COMMANDS
from visual_interfaces.interfaces import Interfaces


class WorkWIthInterface():

    def __init__(self):
        self.current_mode = None
        self.interfaces = Interfaces()

    def change_interfase(self, mode, extra_options=None):
        if mode == COMMANDS.ADDITIONAL_ENGLISH:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_add_file_eng())
        elif mode == COMMANDS.ADDITIONAL_RUSSIAN:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_add_file_ru())
        elif mode == COMMANDS.TRANSFER_FILE:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_trinsfer_file()).Finalize()
        elif mode == COMMANDS.TRANSLATE_FILE:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_translate_file()).Finalize()
        elif mode == COMMANDS.STREAMLINE_FILE:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_streamline_file()).Finalize()
        elif mode == COMMANDS.SEARCH_UPDATE_STRING_FILE:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_search_update_str()).Finalize()
        elif mode == COMMANDS.SEARCH_UNTRANS_STRING_FILE:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_search_untrans_str()).Finalize()
        elif mode == COMMANDS.ALL_TRANSLATE_DIRECTRY:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_translate_directory()).Finalize()
        elif mode == COMMANDS.STREAMLINE_DIRECTORY:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_streamline_directory()).Finalize()
        elif mode == COMMANDS.ALL_TRANSFER_DIRECTORY:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_transfer_directory()).Finalize()
        elif mode == COMMANDS.INTERFACE_TRANSLATOR_PATH:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_interface_translator_path()).Finalize()
        elif mode == COMMANDS.WHITH_HELPER:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_interface_translator_with_helper(extra_options)).Finalize()
        elif mode == COMMANDS.WHITHOUT_HELPER:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_interface_translator_without_helper(extra_options)).Finalize()
        else:
            window = sg.Window('LTA (localization translator assistant)', self.interfaces.get_default()).Finalize()
        return window

    def get_default_interface(self):
        return sg.Window('LTA (localization translator assistant)', self.interfaces.get_default(), size=(700, 100))

    def get_theme(self):
        # sg.theme('Dark')
        sg.theme('DarkAmber')
        #sg.theme('Dark Brown')
        #sg.theme('Dark Blue 8')