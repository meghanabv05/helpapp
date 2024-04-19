


def buy_item(cost_item):
    return cost_item +  add_tax(cost_item)

def add_tax(cost_item):
    tax_rate = 0.03
    return cost_item * tax_rate


final_cost = buy_item(50)

print(final_cost)




def dict_name(FN,MN,LN):
    dict_items = {"FN":FN,"MN":MN,"LN":LN}
    return dict_items


print(dict_name("Meghana","B","v"))