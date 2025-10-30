import pandas as pd

def read_data_from_excel_file(file_path):
    df = pd.read_excel(file_path)
    transaction_list = []
    for items_string in df['items']:
        items = [item.strip() for item in str(items_string).split(',') if item.strip()]
        transaction_list.append(frozenset(items))
    return transaction_list