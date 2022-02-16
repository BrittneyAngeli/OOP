import InsectClass as ins                   


# The main function.
def main():
    # Create an object from the Coin class.
    mosquito = ins.Insect(2,4)
    housefly = ins.Insect(3,6)

    mosquito.flight_length()
    housefly.flight_length()

    # Randomize the mileage (between 1 and 10 miles)
    mosquito.flight_length()
    housefly.flight_length()

    # Display the number of miles the insect flys
    print('This mosquito flew', mosquito.get_flight(), 'miles')   
    print('This housefly flew', housefly.get_flight(), 'miles')   


# Call the main function.

main()
