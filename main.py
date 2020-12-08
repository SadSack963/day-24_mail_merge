# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Read all lines from the letter into a list
with open("./Input/Letters/starting_letter.docx", mode="r") as file:
    raw_letter = file.readlines()

# Read names into a list
with open("./Input/Names/invited_names.txt", mode="r") as file:
    raw_names = file.readlines()

# Strip trailing newlines from names.
# Strings in Python are immutable, so strip returns a new string.
# If omitted or None, the chars argument defaults to removing whitespace.
# Hence no need to specify name.strip("\n")
# strip() only removes the specified characters from the leading and
# training ends of a string - not from the middle of a string.
names = []
for name in raw_names:
    names.append(name.strip())

# Compile the letter for each name, and write to named files
for name in names:
    letter = [raw_letter[0].replace("[name]", name)]
    for i in range(1, len(raw_letter)):
        letter.append(raw_letter[i])
    with open(f"./Output/ReadyToSend/{name}.docx", mode="x") as file:
        for line in letter:
            file.write(line)

