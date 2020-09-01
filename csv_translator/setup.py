from csv_translator import csv_convert, translator
import pandas as pd

def translate_data_frame_and_make_new_csv(new_csv_name, base_csv_name):
    data_frame = pd.read_csv(base_csv_name, sep=';')
    data_frame["number"] = data_frame["Num"]
    data_frame["review"] = data_frame["Review"]
    data_frame["review_type"] = data_frame["review_type"]

    df = data_frame[["number", "review", "review_type"]]

    list = csv_convert.make_list_from_data_frame(df)
    print('--- list: ' + str(list))

    review_list = csv_convert.get_review_list_from_data_list(list)
    print('--- review list: ' + str(review_list))

    translated_review_list = translator.list_translator(review_list)
    print('--- translated review list: ' + str(translated_review_list))

    translated_list = csv_convert.create_new_data_list_from_translated_list(translated_review_list, list)

    csv_convert.make_csv_from_list(translated_list, 'new_kaz_dataset.csv')
    print("--- translated to kazakh!")