from SimpleDecryptor.SimpleDecryptor import SimpleDecryptor
from SimpleEncryptor.SimpleEncryptor import SimpleEncryptor
from PasswordStorage.PasswordStorage import PasswordStorage
from UserInputHandler.UserInputHandler import UserInputHandler

key = 3  
encryptor = SimpleEncryptor(key)
decryptor = SimpleDecryptor(key)
storage = PasswordStorage("passwords.txt")
user_input_handler =UserInputHandler(encryptor, decryptor, storage)

while True:
    print("\nPassword Manager")
    print("1. Add a new password")
    print("2. Retrieve all passwords")
    print("3. Retrieve password by service name")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        user_input_handler.add_password()
    elif choice == "2":
        user_input_handler.retrieve_all_passwords()
    elif choice == "3":
        user_input_handler.retrieve_password_by_service()
    elif choice == "4":
        print("Exiting Password Manager.")
        break
    else:
        print("Invalid choice. Please try again.")