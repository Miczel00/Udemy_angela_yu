#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('UDEMY/Mail Merge Project Start/Input/Names/invited_names.txt','r') as names_file:
    names = names_file.read().splitlines()
    
with open('UDEMY/Mail Merge Project Start/Input/Letters/starting_letter.txt') as starting_letter:
    letter = starting_letter.read()

def replacing(name, letter):
    for name_to_replace in name: 
        new_letter = letter.replace('[name]', name_to_replace)
        with open(f'UDEMY/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name_to_replace}.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)


replacing(names,letter)


