#!/usr/bin/env python3
'''Reading API JSON data and converting to CSV & Excel'''

import requests
import pandas as pd
import pyexcel
from pandas.io.json import json_normalize


def main():

    # URL for API as a variable
    dnd = "https://www.dnd5eapi.co/api/monsters/"

    # fetch data from API
    resp = requests.get(dnd).json()

    # j = resp.json()

    # JSON to Dataframe
    df = pd.json_normalize(resp)

    # convert DataFrame to CSV, out put to CSV file
    df.to_csv('/Users/jeffrlek/PythonClass/DnData/monsters.csv')
    # convert DAtaframe to Excel, out put to Excel file
    df.to_excel('/Users/jeffrlek/PythonClass/DnData/monsters.xlsx',
                sheet_name='monman')


if __name__ == "__main__":
    main()
