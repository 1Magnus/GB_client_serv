import json


def write_order_to_json(item, quantity, price, buyer, date):
    order_dict = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    with open('orders.json', encoding='utf-8') as f_n:
        OBJ = json.load(f_n)
    with open('orders.json', 'w', encoding='utf-8') as f_n:
        OBJ['orders'].append(order_dict)
        json.dump(OBJ, f_n, indent=4)


if __name__ == '__main__':
    write_order_to_json(1, 2, 3, 4, 5)
    write_order_to_json(1, 2, 3, 4, 5)
    write_order_to_json(1, 2, 3, 4, 5)
    write_order_to_json(1, 2, 3, 4, 5)
