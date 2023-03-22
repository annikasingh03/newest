def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    option = int(input("Please enter an option: "))


def encode_password(password):
    encoded_password = ''
    for digit in password:
        if digit == '1':
            encoded_password += '4'
        elif digit == '2':
            encoded_password += '5'
        elif digit == '3':
            encoded_password += '6'
        elif digit == '4':
            encoded_password += '7'
        elif digit == '5':
            encoded_password += '8'
        elif digit == '6':
            encoded_password += '9'
        elif digit == '0':
            encoded_password += '3'
        else:
            encoded_password += digit
    return encoded_password

def decode_password(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        if digit == '4':
            decoded_password += '1'
        elif digit == '5':
            decoded_password += '2'
        elif digit == '6':
            decoded_password += '3'
        elif digit == '7':
            decoded_password += '4'
        elif digit == '8':
            decoded_password += '5'
        elif digit == '9':
            decoded_password += '6'
        elif digit == '3':
            decoded_password += '0'
        else:
            decoded_password += digit
    return decoded_password


if __name__ == "__main__":
     while True:
         print("Menu")
         print("-------------")
         print("1. Encode")
         print("2. Decode")
         print("3. Quit")
         print()
         print()
         option = int(input("Please enter an option: "))
         if option == 1:
                password = int(input("Please enter your password to encode: "))
                print(encode_password)
         elif option == 2:
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
         elif option == 3:
                break
