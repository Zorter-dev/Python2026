def calculate_delivery_cost(order, customer, address):
    if not order or not address or order.get('weight', 0) <= 0:
        return {'error': 'Ошибка. Неверные входные данные'}

    weight = order.get('weight')
    total_price = order.get('total_price', 0)
    delivery_type = address.get('delivery_type', 'courier')
    region_type = address.get('region_type', 'standard')
    vip = customer.get('vip', False)
    new = customer.get('new', False)

    if weight > 50 or total_price < 1000:
        return {'error': 'Ошибка. Заказ не соответствует требованиям'}
    if delivery_type == 'pickup':
        return {'cost': 0}
    if vip and total_price > 5000:
        return {'cost': 0}
    if total_price >= 10000 and region_type != 'remote':
        return {'cost': 0}
    if delivery_type == 'courier':
        if weight <= 5:
            cost = 300
        if weight <= 10:
            cost = 500
        else:
            cost = 500 + (weight - 10) * 30
    elif delivery_type == 'region':
        cost = 1000 + weight * 100
    else:
        return {'error': 'Ошибка. Неизвестный тип дсотавки'}
    if new:
        cost *= 0.85
    if region_type == 'remote':
        cost *= 1.20
    return {'cost': round(cost, 2)} # Создаем словарь и округляем до двух знаков после запятой

order = {'weight': 3, 'total_price': 6000}
address = {'delivery_type': 'courier', 'region_type': 'remote'}
customer = {'is_vip': False, 'is_new': True}
print(calculate_delivery_cost(order, customer, address))