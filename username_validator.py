class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"Username: {self.username}"
    
    def is_valid_username(self):
        if len(self.username) < 5:
            return False
        if not self.username[0].isalpha():
            return False
        if not self.username.isalnum():
            return False
        return True

    def check_password_strength(self):
        score = 0
        special_chars = "!@#$%^&*()"

        if len(self.password) >= 8:
            score += 1
        if any(char.isupper() for char in self.password):
            score += 1
        if any(char.islower() for char in self.password):
            score += 1
        if any(char.isdigit() for char in self.password):
            score += 1
        if any(char in special_chars for char in self.password):
            score += 1

        if score <= 2:
            return "Weak"
        elif score == 3 or score == 4:
            return "Medium"
        else:
            return "Strong"


#driver code
user_list = []

num = int(input("How many users do you want to create? "))

for i in range(num):
    print(f"\n--- User {i+1} ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = User(username, password)

    if user.is_valid_username():
        print("Username is valid.")
        print("Password strength:", user.check_password_strength())
        user_list.append(user)
    else:
        print("Invalid username. Skipping user.")

# 🧾 Summary
print("\n--- Summary of Valid Users ---")
for u in user_list:
    print(u)
