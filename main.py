import cipher
import time
import sys

def main():
    file1 = open('caesar_cipher.txt','r')
    content = file1.read()
    print(content)

    cipher_text = cipher.encrypt(content, shift= 9)
    print(cipher_text)

if __name__ == "__main__":
    main()