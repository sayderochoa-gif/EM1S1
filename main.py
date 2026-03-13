from itertools import product


def calculate_total(price, amount): return price * amount

def apply_discount(total, discount): return total - (total * (discount/100))

def show_result(product, amount, price, discount, total, final):
    print(f"Producto: {product} | Cantidad: {amount} | Precio: {price}")
    print(f"Total: {total} | Descuento: {discount}, | Total a pagar: {final}")
    

product = input("Producto: ")
amount = int(input("Cantidad: "))
price = float(input("Precio unitario: "))
discount = int(input("Descuento (%): "))

total = calculate_total(price, amount)
show_result(product, amount, price, discount, total, apply_discount(total, discount))
