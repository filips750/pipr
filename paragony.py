def get_description(name,price_zl,price_gr):return f'Price of {name} is {price_zl}.{price_gr}'
def print_description(name,price_zl,price_gr): 
    description = get_description(name,price_zl,price_gr)
    print (description)



print_description("banana", 1, 42)

