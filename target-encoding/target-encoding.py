from collections import defaultdict
def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.

    """
    
    mapping = defaultdict(list)#{category:[sum,frequency]}

    for category, target in zip(categories,targets):
        if category in mapping:
            mapping[category] = [mapping[category][0] + target, mapping[category][1] + 1]
        else:
            mapping[category] = [target,1]
    target_encoding = []

    for mp in categories:
        encoding = mapping[mp][0]/mapping[mp][1]
        target_encoding.append(encoding)
    
    return target_encoding
    
