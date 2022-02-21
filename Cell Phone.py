import CellPhoneClass as cell                     


# The main function.
def main():
    manufact = "Verizon"
    model = "iPhone 13 Pro Max"
    retail_price = 1299.99

    my_phone = cell.CellPhone(manufact, model, retail_price)  

    # Display the side of the coin that is facing up.
    print('The manufacturer of this cell phone is', my_phone.get_manufact())
    print('The phone model is', my_phone.get_model())
    print('The retail price of the phone is', my_phone.get_retail_price())

    print()

    my_phone.set_manufact("Android")
    my_phone.set_model("Samsung Galaxy 14")
    my_phone.set_retail_price(1999.99)    

    print('The manufacturer of this cell phone is', my_phone.get_manufact())
    print('The phone model is', my_phone.get_model())
    print('The retail price of the phone is', my_phone.get_retail_price())

main()