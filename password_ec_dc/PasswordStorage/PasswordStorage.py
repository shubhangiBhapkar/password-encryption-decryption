
class PasswordStorage:
    def __init__(self, filename):
        self.filename = filename


    def save_password(self, service, encrypted_password):
        with open(self.filename, "a") as file:
            file.write(f"{service}: {encrypted_password}\n")


    def retrieve_passwords(self):
        try:
            with open(self.filename, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return []


    def retrieve_password_by_service(self, service):
        passwords = self.retrieve_passwords()
        for entry in passwords:
            stored_service, encrypted_password = entry.strip().split(": ")
            if stored_service == service:
                return encrypted_password
        return None  