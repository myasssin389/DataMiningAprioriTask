import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_frequent_itemsets_support_bar_charts(frequent_itemsets_per_level_dict):
    all_frequent_itemsets_dict = get_all_frequent_itemsets_support_dict(frequent_itemsets_per_level_dict)
    cleaned_itemsets = get_cleaned_itemsets_list(all_frequent_itemsets_dict)

    df = pd.DataFrame(cleaned_itemsets, columns=['Itemset', 'Support Count'])

    sns.barplot(x='Itemset', y='Support Count', data=df)
    plt.title('Frequent Itemsets Support Count Bar Chart')
    plt.xlabel('Itemset')
    plt.ylabel('Support Count')
    plt.show()

def get_all_frequent_itemsets_support_dict(frequent_itemsets_per_level_dict):
    all_frequent_itemsets_dict = {}
    for Lk_frequent_itemsets_dict in frequent_itemsets_per_level_dict.values():
        for frequent_itemset in Lk_frequent_itemsets_dict.keys():
            all_frequent_itemsets_dict[frequent_itemset] = Lk_frequent_itemsets_dict[frequent_itemset]

    return all_frequent_itemsets_dict

def get_cleaned_itemsets_list(all_frequent_itemsets_support_dict):
    cleaned_itemsets = []
    for itemset, support in all_frequent_itemsets_support_dict.items():
        itemset_str = "{" + ", ".join(itemset) + "}"
        cleaned_itemsets.append((itemset_str, support))
    return cleaned_itemsets