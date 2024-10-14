import CellPhoneClass as cp

def main():

    
    arg1 = str(input('Enter your cell phone brand: '))
    arg2 = str(input('Enter your cell phone model: '))
    arg3 = float(input('Enter your cell phone price: '))
    
    my_phone = cp.CellPhone(arg1, arg2, arg3)
    
    brand = my_phone.set_manufact()
    model = my_phone.set_model()
    price = my_phone.set_retail_price()

    phone_model_price = print(f'''
    You are using a(n) {brand} {model}, which is
    a ${price} phone!''')

main()
