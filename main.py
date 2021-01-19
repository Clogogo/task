import pandas as pd
from datetime import datetime


def split_csv():
    file = 'Test_task_1.csv'
    columns = ['person_name', 'id', 'Total', 'Paid', 'Date', 'No']

    # read csv file, convert comma and Date
    df = pd.read_csv(file, sep=';', decimal=',', parse_dates=['Date'])
    # insert Header
    df.columns = columns

    # sort by id
    df = df.sort_values(by='id')

    # convert Date columns to datetime format 21-Aug-19
    df['Date'] = df['Date'].dt.strftime('%d-%b-%y')

    # validate and convert "No columns" to datetime format 2009-Aug-19 with condition
    for row in df['No']:
        if row.__contains__('/'):
            con_row = datetime.strptime(row, '%d/%m/%Y')  # convert to datetime format
            df['No'] = df['No'].replace([row], con_row.strftime('%Y-%m-%d'))  # replace with new datetime format

    # split by first duplicate
    split = df.duplicated(subset=['id'], keep='first')
    if split.any():
        df.loc[~split].to_csv("split.csv", index=False, header=True, sep=';')  # create and write to csv

    # split by second duplicate
    split = df.duplicated(subset=['id'], keep='last')
    if split.any():
        df.loc[~split].to_csv("split_1.csv", index=False, header=True, sep=';')  # create and write to csv


split_csv()
