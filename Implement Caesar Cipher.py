def caesar_cipher_encrypt(text, shift):
    """
    Encrypts the given text using the Caesar Cipher algorithm.
    
    Parameters:
    text (str): The input text to be encrypted.
    shift (int): The shift value for the Caesar Cipher.
    
    Returns:
    str: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Handle shift wrapping within the alphabet range
            shift_amount = shift % 26
            if char.islower():
                # Encrypt lowercase letters
                shifted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                # Encrypt uppercase letters
                shifted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """
    Decrypts the given text using the Caesar Cipher algorithm.
    
    Parameters:
    text (str): The input text to be decrypted.
    shift (int): The shift value for the Caesar Cipher.
    
    Returns:
    str: The decrypted text.
    """
    # Decryption is simply encryption with a negative shift
    return caesar_cipher_encrypt(text, -shift)

def main():
    """
    The main function that provides a menu for the user to choose between
    encryption, decryption, or exiting the program.
    """
    while True:
        print("Caesar Cipher Algorithm")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
