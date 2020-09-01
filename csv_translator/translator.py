from googletrans import Translator

translator = Translator()


def list_translator(list):

    translated_list = []

    for sentences in list:
        translated_sentence = translator.translate(sentences, src='ru', dest='kk')
        translated_list.append(translated_sentence.text)

    return translated_list

# test_list = ["я человек", "я иду в школу" , "я помогаю всем"]
# print(list_translator(test_list))
