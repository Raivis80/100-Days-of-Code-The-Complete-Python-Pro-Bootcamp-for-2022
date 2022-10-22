
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt', 'r') as names_file:
    names = names_file.readlines()

with open('./Input/Letters/starting_letter.txt', 'r') as letter_file:
    start_letter = letter_file.read()

for name in names:
    compiled_letter = start_letter.replace(PLACEHOLDER, name.strip())
    with open(f'./Output/ReadyToSend/letter_for_{name.strip()}.txt', 'w') as new_letter:
        new_letter.write(compiled_letter)


