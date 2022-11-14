import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime

#def get_soup(url: str) -> BeautifulSoup:
   # response = requests.get(url)
   # return BeautifulSoup(response.content, 'html.parser')

#def get_csv_from_url(url:str) -> pd.DataFrame:
 #   s=requests.get(url).content
  #  return pd.read_csv(io.StringIO(s.decode('utf-8')))

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

df = pd.read_csv("DataFrame/Viki.csv")
print_tabulate(df)