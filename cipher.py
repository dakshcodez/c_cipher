def encrypt(plain_text,shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            base_shift = 65 if char.isupper() else 97
            cipher_text += chr(((ord(char) - base_shift + shift) % 26) + base_shift)
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text,shift):
    return encrypt(cipher_text,-shift)

def main():
    plain_text = "follow @dakshcodez"
    encrypted = encrypt(plain_text, shift = 5);
    print(encrypted)
    decrypted = decrypt(encrypted, shift = 5)
    print(decrypted)
    

if __name__ == "__main__":
    main()
