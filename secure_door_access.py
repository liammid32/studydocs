#the goal is to build a security system with low/med/high and only with certain levels get access

class Employee:
    def __init__(self, name, badge_number, access_level):
        self.name = name
        self.badge_number = badge_number
        self.access_level = access_level.lower()

        # Validate the badge number (make sure it's 5 digits and prime)
        if len(badge_number) == 5 and badge_number.isdigit():
            if self.is_prime(int(badge_number)):
                print("✅ Badge is valid")
            else:
                print("❌ Badge number is not prime")
        else:
            print("❌ Badge number is not in a valid format")

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):  
            if num % i == 0:
                return False
        return True

    def can_access(self, zone):
        zone = zone.lower()  # fixed assignment bug
        match zone:
            case "low":
                return True
            case "mid":
                return self.access_level in ["mid", "high"]
            case "high":
                return self.access_level == "high"
            case _:
                print("Invalid zone.")
                return False

    def __str__(self):
        return f"{self.name} | Badge #{self.badge_number} | Access level: {self.access_level}"


#driver code goes here
name = input("Name: ")
badge = input("5-digit badge number: ")
level = input("Access level (low/mid/high): ")

employee = Employee(name, badge, level)

zone = input("Enter zone to access (low/mid/high): ")

if employee.can_access(zone):
    print("✅ Access granted")
else:
    print("❌ Access denied")
