# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    return cipher


def decrypt(message):
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter

        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    return decipher


def encryptor():
    message = input("Put your message here to encrypt it.\n")
    result = encrypt(message.upper())
    print(result)


def decryptor():
    message = input("Put your morse code here to decrypt it.\n")
    result = decrypt(message)
    print(result)


def main():
    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
  __  __                        _____          _        _______                  _       _             
 |  \/  |                      / ____|        | |      |__   __|                | |     | |            
 | \  / | ___  _ __ ___  ___  | |     ___   __| | ___     | |_ __ __ _ _ __  ___| | __ _| |_ ___  _ __ 
 | |\/| |/ _ \| '__/ __|/ _ \ | |    / _ \ / _` |/ _ \    | | '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|
 | |  | | (_) | |  \__ \  __/ | |___| (_) | (_| |  __/    | | | | (_| | | | \__ \ | (_| | || (_) | |   
 |_|  |_|\___/|_|  |___/\___|  \_____\___/ \__,_|\___|    |_|_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|   
                                                                                                       
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                                                                      
                                    M@d3 With ♥ -- VirusZzWarning          
                         Read my blogs on : https://viruszzwarning.medium.com/                              
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    print("Choose from below:")

    opt = input(
        "• Press 1 to translate Text to Morse code. \n• Press 2 to translate Morse code to Text.\nType here: ")
    opt = int(opt)

    if (opt == 1):
        encryptor()
    elif (opt == 2):
        decryptor()
    else:
        print("Please choose a valid input.")


if __name__ == '__main__':
    main()
