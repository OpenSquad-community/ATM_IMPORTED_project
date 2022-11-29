# CONCEPT USED: OOPS - classes, object,constructor,file handling
# Created by :-Akash mishra(mak650650)
class Atm:
    # CONSTRUCTOR
    def __init__(self):
        # DATA
        # ---------- #
        self.pin = ""
        self.balance = 0
        # ---------- #

        # self.menu()

    # MENU METHOD
    def menu(self):
        user_input = input("""
                            Hello Welcome,
                                How would you like to proceed?           
                                1.Enter 1 to change pin
                                2.Enter 2 to deposit amount
                                3.Enter 3 to withdraw amount
                                4.Enter 4 to check current balance
                                5.Enter 5 to exit.
        :-""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print()

    # METHOD FOR CHANGING PIN

    def create_pin(self):
        with open("pin_and_balance.txt", "r") as f:
            data = f.readlines()
            self.pin = input("Enter your old pin :-")
            data[0] = data[0].strip("\n")
            if data[0] == self.pin:
                self.pin = input("Enter your new pin :-")
                data[0] = self.pin
                print("Pin set successfully")
                data[0] = data[0] + "\n"
                with open("pin_and_balance.txt", "w") as x:
                    x.writelines(data)
                    x.close()
                    f.close()
            else:
                print("Invalid pin")

    # METHOD FOR DEPOSITING A AMOUNT

    def deposit(self):
        with open("pin_and_balance.txt", "r") as f:
            data = f.readlines()
            data[0] = data[0].strip("\n")
            self.pin = data[0]
            data[0] = data[0] + "\n"
            temp = input("Enter your pin :-")
            if temp == self.pin:
                amount = int(input("Enter the deposit amount :-"))
                self.balance = int(data[1])
                self.balance += amount
                data[1] = str(self.balance)
                with open("pin_and_balance.txt", "w") as x:
                    x.writelines(data)
                    x.close()
                    f.close()
                    print("Deposit successful")
            else:
                print("Invalid pin")
            f.close()

    # METHOD FOR WITHDRAWING A AMOUNT

    def withdraw(self):
        with open("pin_and_balance.txt", "r") as f:
            data = f.readlines()
            data[0] = data[0].strip("\n")
            self.pin = data[0]
            data[0] = data[0] + "\n"
            temp = input("Enter your pin :-")
            if temp == self.pin:
                amount = int(input("Enter the withdraw amount :-"))
                self.balance = int(data[1])
                if amount <= self.balance:
                    self.balance -= amount
                    data[1] = str(self.balance)
                    with open("pin_and_balance.txt", "w") as x:
                        x.writelines(data)
                        x.close()
                        f.close()
                    print(f"Amount {amount} successfully withdrawn")
                else:
                    print("insufficient balance")
            else:
                print("Invalid pin")
            f.close()

    # METHOD FOR CHECKING BALANCE AMOUNT

    def check_balance(self):
        with open("pin_and_balance.txt", "r") as f:
            data = f.readlines()
            data[0] = data[0].strip("\n")
            self.pin = data[0]
            data[0] = data[0] + "\n"
            temp = input("Enter your pin :-")
            if temp == self.pin:
                self.balance = data[1]
                print(f"Balance amount:-{self.balance}")
            else:
                print("Invalid pin")
            f.close()
