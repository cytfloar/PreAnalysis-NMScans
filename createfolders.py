import os, csv
import pandas as pd
folder_list= pd.read_csv("code_conversion.csv", header=None)
def create(x, axis=None):
  os.mkdir(f"horga/{x}")
  os.mkdir(f"horga/{x}/NM_NEX5")
  os.mkdir(f"horga/{x}/T1w")
folder_list.iloc[:, 0].apply(create, axis=1)
