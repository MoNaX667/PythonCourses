import string


class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.cipher_alphabet = self.generate_cipher_alphabet()

    def generate_cipher_alphabet(self):
        unique_letters = []
        for char in self.keyword:
            if char not in unique_letters and char in string.ascii_uppercase:
                unique_letters.append(char)

        remaining_letters = [char for char in string.ascii_uppercase if char not in unique_letters]

        return ''.join(unique_letters + remaining_letters)

    def encode(self, data):
        encoded_data = ''
        for char in data:
            if char.isalpha():
                if char.islower():
                    encoded_data += self.cipher_alphabet[string.ascii_lowercase.index(char)].lower()
                else:
                    encoded_data += self.cipher_alphabet[string.ascii_uppercase.index(char)].upper()
            else:
                encoded_data += char
        return encoded_data

    def decode(self, data):
        decoded_data = ''
        for char in data:
            if char.isalpha():
                if char.islower():
                    decoded_data += string.ascii_lowercase[self.cipher_alphabet.index(char)].lower()
                else:
                    decoded_data += string.ascii_uppercase[self.cipher_alphabet.index(char)].upper()
            else:
                decoded_data += char
        return decoded_data