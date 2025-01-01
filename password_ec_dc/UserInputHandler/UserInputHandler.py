
class UserInputHandler:
    def __init__(self, encryptor, decryptor, storage):
        self.encryptor = encryptor
        self.decryptor = decryptor
        self.storage = storage

    def add_password(self):
        service = input("Enter the service name: ")
        password = input("Enter the password: ")
        encrypted_password = self.encryptor.encrypt(password)
        self.storage.save_password(service, encrypted_password)
        print("Password saved successfully!")

    def retrieve_all_passwords(self):
        passwords = self.storage.retrieve_passwords()
        if passwords:
            print("\nStored Passwords:")
            for entry in passwords:
                service, encrypted_password = entry.strip().split(": ")
                decrypted_password = self.decryptor.decrypt(encrypted_password)
                print(f"{service}: {decrypted_password}")
        else:
            print("No passwords found.")

    def retrieve_password_by_service(self):
        service = input("Enter the service name to retrieve the password: ")
        encrypted_password = self.storage.retrieve_password_by_service(service)
        if encrypted_password:
            decrypted_password = self.decryptor.decrypt(encrypted_password)
            print(f"Password for {service}: {decrypted_password}")
        else:
            print(f"No password found for service: {service}")
