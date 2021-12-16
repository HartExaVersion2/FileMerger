from mtranslate import translate
from common.decorator_for_output_errors import decorator_for_output_errors

class Translator:

    @decorator_for_output_errors()
    def transleate_text(self, text, lang_to='ru', lang_from='auto'):
        return translate(text, lang_to, lang_from)