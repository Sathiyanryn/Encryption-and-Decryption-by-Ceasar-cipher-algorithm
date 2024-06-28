def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if character is a letter
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Get input from the user
plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value (as an integer): "))

# Encrypt the plaintext
encrypted_text = caesar_encrypt(plaintext, shift)
print("Encrypted:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted:", decrypted_text)
