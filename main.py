from atm import Atm

whole = Atm()  # object of Atm class is created by name 'whole'
runner = True
while runner:
    whole.menu()  # method menu is called use 'whole' object
    n = input(f"\n Enter '0' for 'menu' and '1' for 'exit':-")
    if n == "0":
        print(f"Thank you for using our service")
    elif n == "1":
        runner = False

