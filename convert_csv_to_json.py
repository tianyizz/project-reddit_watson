from typing import Any, Union

import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader

path = r"C:\Users\Brandon\Desktop\Reddit VR\Code"
file_in = path + r'\all_vive_data.csv'
file_out = path + r'\all_vive_data.json'

df = pd.read_csv(file_in)
df.to_json(file_out, orient=r'records')