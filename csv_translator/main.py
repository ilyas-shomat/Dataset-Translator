from csv_translator import setup as csv_setup
import pandas as pd


data_frame = pd.read_csv('rusText.csv', sep=';')
csv_setup.translate_data_frame_and_make_new_csv("kaz_data_set", "rusText.csv")
