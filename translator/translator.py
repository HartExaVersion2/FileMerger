from mtranslate import translate

class Translator:

    def transleate_text(self, text, lang_to='ru', lang_from='auto'):
        return translate(text, lang_to, lang_from)