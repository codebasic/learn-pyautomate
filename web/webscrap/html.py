# coding: utf-8
import pandas as pd

def 표추출(table_elements):
    table_frames = pd.read_html(str(table_elements))
    return table_frames
