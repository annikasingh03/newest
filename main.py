def encoder(user_input):
    encodestr= ""
    for char in user_input:
        add = str( int(char) + 3 )
        encodestr += add
    return encodestr

def decoder(encodestr):
    return user_input



if __name__ == "__main__":

    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        option = int(input('Please enter an option: '))
        if option == 1:
            user_input = input('Please enter your password to encode: ')
            encoded = encoder(user_input)
            print('Your password has been encoded and stored!')
        elif option == 2:
            print('The encoded password is ' + encoded + ', and the original password is ' + user_input +'.')

        elif option == 3:
            break
