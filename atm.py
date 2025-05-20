class ATM:
  def __init__(self):
    self.balance = 5000
    self.pin = 1234

  def check_pin(self, input_pin) :
    return input_pin == self.pin

  def check_balance(self) :
    print(f"your current balance is RS. {self.balance}")

  def deposit(self,input_pin,amount) :
    if not self.check_pin(input_pin):
      print("Incorrect PIN.")
      return
      print("Deposit amount must be greater than 0.")
      return
    self.balance += amount
    print(f"RS. {amount} deposited. New balance: RS. {self.balance}")

  def withdraw(self, input_pin, amount):
    if not self.check_pin(input_pin) :
      print("Incorrect PIN.")
    
      return
    if amount <= 0:
      print("withdrawal amount must be greater than 0.")

      return
    if amount > self.balance:
      print("Insufficient Balance.")
      return

    self.balance -= amount
    print(f"Rs. {amount} withdrawal. New balance: Rs. {self.balance}")
    
  def exit(self):
      print("Thankyou for using the ATM. Goodbye!")
      quit()
      
atm = ATM()

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        pin = int(input("Enter your PIN: "))
        if atm.check_pin(pin):
            atm.check_balance()
        else:
            print("Incorrect PIN")
            
    elif choice == '2':
        pin = int(input("Enter your PIN: "))
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(pin, amount)
        
    elif choice == '3':
        pin = int(input("Enter your PIN: "))
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(pin, amount)
        
    elif choice == '4':
        atm.exit()
        
        
    else:
        print("Invalid choice.please try again.")
    
