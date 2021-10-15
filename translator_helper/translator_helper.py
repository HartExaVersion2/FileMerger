from translator_helper.translator_helper_operations import TranslatorHealperOperations

class TranslatorHealper(TranslatorHealperOperations):

    def further(self, title, desc):
        self.write_focus(title, desc)
        self.save()
        next_focus = self.get_focus()
        return next_focus


    def save(self):
        if self.translator_dictionary:
            self.save_in_file()
