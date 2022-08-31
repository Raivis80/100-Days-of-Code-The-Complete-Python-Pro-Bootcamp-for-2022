from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Ceasar Cipher function for encrypting and decrypting text using a key
# Input: text, key (int) and choice (encrypt or decrypt)
# Keep in mind that the key is the number of letters to shift the alphabet by
# Example: Ceasar_Ciper('hello', 2, 'encrypt') will return 'jgnnq'
# Example: Ceasar_Ciper('hello world', 2, 'decrypt') will return 'jgnnq yqtnf'
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # If the cipher direction is decode, then we need to shift the alphabet backwards
    if cipher_direction == "decode":
        shift_amount *= -1
    # Loop through each character in the text
    for char in start_text:
        # If the character is a letter, then we need to shift it
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        # If the character is not a letter, then we just add it to the end text
        else:
            end_text += char
    # Return the end text
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Print the logo
print(logo)

should_end = False
# Loop until the user wants to quit
while not should_end:
    # Ask the user what to encrypt or decrypt
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Ask for the text and the shift key
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    # Call the Ceasar Cipher function with the user's input
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    # Ask the user if they want to quit and store the answer in a variable
    restart = input( "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
