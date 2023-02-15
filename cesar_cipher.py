
def welcome():
    
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher")

def enter_message():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        if mode == "e" or mode == "d":
            break
        else:
            print("Invalid Mode")
    message = ""
    if (mode == "e"):
        message = input("What message would you like to encrypt: ").upper()
    else:
        message = input("what message would you like to decrypt: ").upper()
    while True:
        shift = input("What is the shift number from 1 to 26: ")
        if shift.isdigit():
            shift = int(shift)
            if shift<=26:
                break
            else:
                print("You can only shift the number from 1 to 26. So, enter again")
        else:
            print("Invalid shift")
    return mode, message, shift

def encrypt(message, shift_number):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift_number
            if shifted >ord('Z'):
                shifted = shifted - 26
            final_char = chr(shifted)
            encrypted_message += final_char
        else:
            encrypted_message += char
    return encrypted_message


def decrypt_caesar(code, shift):
    decrypted_text = ""
    for char in code:
        if char.isalpha():
            shift_c = chr((ord(char) - shift - 65) % 26 + 65)
            decrypted_text += shift_c
        else:
            decrypted_text += char
    
    return decrypted_text


def main():
    welcome()
    while True:
        mode, message, shift = enter_message()
        if(mode == "e"):
            encrypt_message = encrypt(message, shift)
            print(encrypt_message)
        else:
            decrypt_message = decrypt_caesar(message, shift)
            print(decrypt_message)
        again = input("Would you like to encrypt or decrypt another message? (y/n): ")
        if(again != "y"):
            print("Thanks for using the program, goodbye!")
            break 
        
if __name__=="__main__":
    main()
