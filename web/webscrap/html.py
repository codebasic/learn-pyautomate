# coding: utf-8
import pandas as pd

def extract_tables(table_elements):
    table_frames = pd.read_html(str(table_elements))
    return table_frames
