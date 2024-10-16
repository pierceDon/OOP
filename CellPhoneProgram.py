import CellPhoneClass as cp

def main():

    
    phone1 = cp.CellPhone('Apple','iPhone 16', 1650)
    phone2 = cp.CellPhone('Samsung', 'Galaxy 10', 1450)
    

    phone1.set_retail_price(1250)
    phone2.set_retail_price(1050)

    print(phone1)
    print(phone2)

main()
