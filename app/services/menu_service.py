# Exemple dans menu_service.py
def calculate_total_price(order_items: list):
    total = 0
    for item in order_items:
        total += item['price'] * item['quantity']
    return total
