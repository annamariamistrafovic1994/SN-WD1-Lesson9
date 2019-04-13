print("Hello! This is a program that converts kilometers into miles. Follow the steps bellow for converting.")

while True:
    print("Please enter the value of kilometers you want to convert into miles. Note: enter only numbers.")

    km = input("Kilometers: ")

    km = float(km.replace(",", "."))  # replace comma with dot if user enters comma

    miles = km * 0.621371

    print("{0} kilometers is {1} miles.".format(km, miles))

    choice = input("Would you like to do another conversion (y/n): ")

    if choice != "y" and choice != "yes":
        break

