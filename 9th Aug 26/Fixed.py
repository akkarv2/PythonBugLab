def add_item(item, items=None):
    if items is None:
        items=[]
    items.append(item)
    return items

print(add_item("python"))
print(add_item("debugging"))
print(add_item("interview"))