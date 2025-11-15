from data_reading import read_data_from_excel_file
from apriori import apriori
from frozenset_formatter import get_formatted_frozenset
from strong_rule_generation import generate_strong_rules
from support_visualization import generate_frequent_itemsets_support_bar_charts

transaction_list = read_data_from_excel_file("data/Horizontal_Format.xlsx")

frequent_itemsets_dict = apriori(transaction_list, 3)
print("Frequent itemsets:")
for itemset in frequent_itemsets_dict.keys():
    formatted_itemset = get_formatted_frozenset(itemset)
    print(formatted_itemset, ": ", frequent_itemsets_dict[itemset])

print("")

print("Strong rules:")
strong_rules = generate_strong_rules(frequent_itemsets_dict, min_confidence=0.8)
for rule in strong_rules:
    rule.print_rule()
    print("")

generate_frequent_itemsets_support_bar_charts(frequent_itemsets_dict)