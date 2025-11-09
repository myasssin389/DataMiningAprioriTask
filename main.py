from data_reading import read_data_from_excel_file
from apriori import apriori
from support_visualization import generate_frequent_itemsets_support_bar_charts


transaction_list = read_data_from_excel_file("data/Horizontal_Format.xlsx")
frequent_itemsets_per_level_dict = apriori(transaction_list, 3)
for level in frequent_itemsets_per_level_dict.keys():
    print("Level: ", level)
    print(frequent_itemsets_per_level_dict[level])

# Visualization using Bar Charts
generate_frequent_itemsets_support_bar_charts(frequent_itemsets_per_level_dict)