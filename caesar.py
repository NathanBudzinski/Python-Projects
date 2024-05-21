# Caesar Cipher encryption, decryption, and brute force decryption

def encrypt(plaintext, shift):
    plaintext = plaintext.upper()
    ciphertext = ''
    for x in plaintext:
        ascii_num = ord(x)
        if ascii_num == ord(' '): continue
        shifted = ascii_num + shift
        if shifted > ord('Z'): shifted -= 26
        ciphertext += chr(shifted)
    return ciphertext

def decrypt(ciphertext, shift): 
    ciphertext = ciphertext.upper()
    plaintext = ''
    for x in ciphertext: 
        ascii_num = ord(x)
        shifted = ascii_num - shift
        if shifted < ord('A'): shifted += 26
        plaintext += chr(shifted)
    return plaintext

def brute_force(ciphertext):
    ciphertext = ciphertext.upper().strip()
    returntext = ""
    for i in range(25, 0, -1):
        plaintext = ''
        for x in ciphertext:
            ascii_num = ord(x)
            shifted = ascii_num + i
            if shifted > ord('Z'):
                shifted -= 26
            plaintext += chr(shifted)
        returntext += f'Shift {26-i}: {plaintext}\n'
    return returntext

def menu_select():

    user_input = int(input("Choose an option:\n1) Encrypt\n2) Decrypt\n3) Brute Force Decrypt\n4) Quit\n"))
    if user_input == 1:
        plaintext = input("Enter plaintext: ")
        shift = int(input("Enter shift amount: "))
        shift = shift % 26
        return encrypt(plaintext, shift)
    elif user_input == 2:
        ciphertext = input("Enter ciphertext: ")
        shift = int(input("Enter shift amount: "))
        shift = shift % 26
        return decrypt(ciphertext, shift)
    elif user_input == 3:
        ciphertext = input("Enter ciphertext: ")
        return brute_force(ciphertext)
    elif user_input == 4:
        print("Thanks for using my caesar cipher encoder/decoder!")
        quit()
    else:
        return "Error: Invalid input"


while True:
    print(menu_select(), "\n")
