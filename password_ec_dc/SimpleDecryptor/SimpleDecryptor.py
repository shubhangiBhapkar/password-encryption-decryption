class SimpleDecryptor:
    def __init__(self, key):
        self.key = key

    def decrypt(self, encrypted_password):
        decrypted = ''.join(chr(ord(char) - self.key) for char in encrypted_password)
        return decrypted