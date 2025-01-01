class SimpleEncryptor:
    def __init__(self, key):
        self.key = key

    def encrypt(self, password):
        encrypted = ''.join(chr(ord(char) + self.key) for char in password)
        return encrypted