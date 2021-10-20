
def get_description(name,price):return f'Price of {name} is {price//100:}.{price%100:02}'
def print_description(name,price): 
    description = get_description(name,price)
    print (description)



# print_description("banana", 434)
print_description("banana", 201)
