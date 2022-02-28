import yaml

data = {
    'items': ['a', 'b', 'c'],
    'quantity': 4,
    'items_price': {
        'a': '100€',
        'b': '200€',
        'c': '300€'
    }
}

with open('file.yaml', 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml') as f_n:
    print(f_n.read())
