def get_description(name,price_zl,price_gr):return f'Price of {name} is {price_zl}.{price_gr}'
def print_description(name,price_zl,price_gr): print(get_description(name,price_zl,price_gr))
print_description("banana", 1, 42)


