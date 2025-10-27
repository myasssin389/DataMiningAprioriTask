import pandas as pd

def read_data_from_excel_file(file_path):
    df = pd.read_excel(file_path)
    transaction_list = df['items'].tolist()
    return transaction_list