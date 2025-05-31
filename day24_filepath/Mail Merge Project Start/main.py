#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    names = [name.strip() for name in names]
    print(names)

# open name and create list + strip 


with open("input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    # print(letter_contents)
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        # print(new_letter)
        # print("-------------")
        with open(f"output/readytosend/letter_for_{name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)





# open template and create new file + replace name + save at destination