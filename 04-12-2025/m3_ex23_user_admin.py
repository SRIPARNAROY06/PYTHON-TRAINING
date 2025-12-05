
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.active = True

    def deactivate(self):
        self.active = False
        print(f"User '{self.username}' deactivated.")

    def delete_user(self, target_username, users_registry):
        print("Error: Only admins can delete users.")

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}, Active: {self.active}"


class Admin(User):
    def delete_user(self, target_username, users_registry):
        if target_username in users_registry:
            del users_registry[target_username]
            print(f"Admin '{self.username}' deleted user '{target_username}'.")
        else:
            print(f"User '{target_username}' not found.")


# ---- Example Usage ----
if __name__ == "__main__":
    users = {
        "asha": User("asha", "asha@example.com"),
        "ravi": User("ravi", "ravi@example.com"),
        "imran": User("imran", "imran@example.com"),
    }

    admin = Admin("admin1", "admin@example.com")

    print("Before deletion:")
    for name, user in users.items():
        print(user)

    admin.delete_user("ravi", users)

    print("\nAfter deletion:")
    for name, user in users.items():
        print(user)


