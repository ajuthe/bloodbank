class BloodBank:
    def __init__(self):
        self.blood_inventory = {
            "A+": 10,
            "B+": 15,
            "AB+": 5,
            "O+": 20,
            "A-": 8,
            "B-": 12,
            "AB-": 3,
            "O-": 10,
        }

    def check_blood_availability(self, blood_type):
        return self.blood_inventory.get(blood_type, 0)

    def donate_blood(self, blood_type, amount):
        if blood_type in self.blood_inventory:
            self.blood_inventory[blood_type] += amount
        else:
            self.blood_inventory[blood_type] = amount

    def distribute_blood(self, blood_type, amount):
        if blood_type in self.blood_inventory:
            if self.blood_inventory[blood_type] >= amount:
                self.blood_inventory[blood_type] -= amount
                return True
            else:
                return False
        else:
            return False

def main():
    blood_bank = BloodBank()

    while True:
        print("Blood Bank Application")
        print("1. Check Blood Availability")
        print("2. Donate Blood")
        print("3. Distribute Blood")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            blood_type = input("Enter blood type: ")
            availability = blood_bank.check_blood_availability(blood_type)
            print(f"Available units of {blood_type}: {availability}")
        
        elif choice == "2":
            blood_type = input("Enter blood type: ")
            amount = int(input("Enter amount to donate: "))
            blood_bank.donate_blood(blood_type, amount)
            print("Thank you for donating!")
        
        elif choice == "3":
            blood_type = input("Enter blood type: ")
            amount = int(input("Enter amount to distribute: "))
            if blood_bank.distribute_blood(blood_type, amount):
                print("Blood distributed successfully.")
            else:
                print("Insufficient blood units.")
        
        elif choice == "4":
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
