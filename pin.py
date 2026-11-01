class AccountPINChecker:
    def __init__(self, pin: str):
        self.__pin = "0000"
        self.set_pin(pin)

    def set_pin(self, new_pin: str):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
        else:
            print("Invalid PIN! Must be 4 digits.")

    def __str__(self) -> str:
        return f"Account [PIN: {'*' * len(self.__pin)}]"

if __name__ == "__main__":
    account = AccountPINChecker("1234")
    print(account)  

    account.set_pin("abcd") 
    
    try:
        print(account.__pin)
    except AttributeError:
        print("Access denied: Private attribute is protected outside the class.")
