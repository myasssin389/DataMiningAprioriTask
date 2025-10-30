from data_reading import read_data_from_excel_file
from apriori import apriori
from rule_generation import generate_rules
from confidence_computing import compute_confidence
from lift_computing import compute_lift
from strong_rules_filter import filter_strong_rules


transaction_list = read_data_from_excel_file("data/Horizontal_Format.xlsx")
frequent_itemsets_per_level_dict = apriori(transaction_list, 3)
for level in frequent_itemsets_per_level_dict.keys():
    print("Level: ", level)
    print(frequent_itemsets_per_level_dict[level])

strong_rules_list_with_computed_lift = []
for level in frequent_itemsets_per_level_dict.keys():
    all_possible_rules_list = generate_rules(frequent_itemsets_per_level_dict[level])
    rules_list_with_computed_confidence = compute_confidence(all_possible_rules_list)
    strong_rules_list = filter_strong_rules(rules_list_with_computed_confidence)
    strong_rules_list_with_computed_lift = compute_lift(strong_rules_list)
