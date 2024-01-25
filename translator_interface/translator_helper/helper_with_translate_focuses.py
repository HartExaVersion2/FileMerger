from translator_interface.translator_helper.translator_helper_operations import TranslatorHealperOperations
from common.decorator_for_output_errors import decorator_for_output_errors

class TranslatorHealper(TranslatorHealperOperations):

    @decorator_for_output_errors()
    def further(self, title, desc):
        if title != '\n' and desc != '\n':
            self.write_focus(title, desc)
            self.save()
        next_focus = self.get_focus() #ToDO сюда может прилететь None. Сделать отработку как исключение
        return next_focus

    @decorator_for_output_errors()
    def save(self):
        if self.translator_dictionary:
            self.save_in_file()
