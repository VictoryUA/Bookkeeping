def caesar_decipher_formula(ciphertext, key):
    result = ''

    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            first = ord('A') if is_upper else ord('a')
            last = ord('Z') if is_upper else ord('z')
            decrypted_symbol = (ord(char) - first - key) % (last - first + 1) + first
            result += chr(decrypted_symbol)
        else:
            result += char

    return result

try:
    key = int(input('Enter a number as the key: '))
    ciphertext = input('Enter a message to encrypt: ')

    decrypted_message = caesar_decipher_formula(ciphertext, key)

    print("\nResult:", decrypted_message) # Result: The quick brown fox jumps over the lazy dog

except ValueError:
    print('Please enter a valid integer for the key.')