from deep_translator import GoogleTranslator
from common.decorator_for_output_errors import decorator_for_output_errors

class TextTranslator:

    def __init__(self):
        self.trans = GoogleTranslator(source='auto', target='ru')

    @decorator_for_output_errors()
    def transleate_text(self, text, lang_to='ru', lang_from='auto'):
        return self.trans.translate(text)