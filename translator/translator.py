from deep_translator import GoogleTranslator, YandexTranslator, DeeplTranslator
from common.decorator_for_output_errors import decorator_for_output_errors
from common.constant import TRANSLATOR_NAME

class TextTranslator:

    def __init__(self, translator_name=TRANSLATOR_NAME.GOOGLE, lang_from='auto', lang_to='ru', api_key=None):
        if translator_name == TRANSLATOR_NAME.GOOGLE:
            self.trans = GoogleTranslator(source=lang_from, target=lang_to)
        elif translator_name == TRANSLATOR_NAME.YANDEX:
            self.trans = YandexTranslator(source=lang_from, target=lang_to, api_key=api_key)
        elif translator_name == TRANSLATOR_NAME.DEEPL:
            self.trans = DeeplTranslator(source=lang_from, target=lang_to, api_key=api_key)

    @decorator_for_output_errors()
    def transleate_text(self, text):
        return self.trans.translate(text)

    # def langs(self):
    #     print(self.trans.get_supported_languages()) #as_dict=True
