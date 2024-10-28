import pandas as pd


def find_duplicates(file1, file2, key_columns):

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2, sep=';')

    df1.columns = df1.columns.str.strip()
    df2.columns = df2.columns.str.strip()


    merged_df = pd.merge(df1, df2, on=key_columns, how='inner')

    if not merged_df.empty:
        print("Find duplicates:")
        print(merged_df)
    else:
        print("duplicates not found.")


file1 = 'Lesson_13/csv_homework/random.csv'
file2 = 'Lesson_13/csv_homework/random-michaels.csv'

key_columns = ['ContactID', 'FirstName', 'LastName', 'Birthday', 'EmailAddress']

find_duplicates(file1, file2, key_columns)
