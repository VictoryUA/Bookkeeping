def caesar_cipher_formula(message, key): # definition of the encryption function
    result = '' # create a result variable in which the encrypted message will be stored
    for char in message: # iteration over message symbols
        if char.isalpha(): # checking if a character is a letter
            is_upper = char.isupper()
            first = ord('A') if is_upper else ord('a') # determine whether a letter is uppercase or lowercase, and set the base values for uppercase and lowercase ASCII codes
            last = ord('Z') if is_upper else ord('z') 
            # calculation of the encrypted symbol according to the given formula
            encrypted_symbol = (ord(char) - first + key) % (last - first + 1) + first
            result += chr(encrypted_symbol) # appending the encrypted character to the result
        else:
            result += char # else if the symbol is not a letter, we add it without changes to the result

    return result # returning an encrypted message

# User input and function call
try:
    key = int(input('Enter a number as the key: ')) # key: 1
    message = input('Enter a message to encrypt: ') # enter message:'The quick brown fox jumps over the lazy dog'

    encrypted_message = caesar_cipher_formula(message, key)
    print('\nencrypted_message:', encrypted_message) # Result: Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.
    
except ValueError:
    print('Please enter a valid integer for the key.')