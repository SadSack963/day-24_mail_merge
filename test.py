with open("./Input/Letters/starting_letter.docx", mode="r") as file:
    # Read all lines into a list
    contents = file.readlines()
    print(contents)
    # RESULT: ['Dear [name],\n', '\n', 'You are invited to my birthday this Saturday.\n', '\n', 'Hope you can make it!\n', '\n', 'Angela\n']

with open("./Input/Letters/starting_letter.docx", mode="r") as file:
    # Read lines into a list. Do not read new lines once the "hint" number of bytes is exceeded.
    contents = file.readlines(20)
    print(contents)
    # RESULT: ['Dear [name],\n', '\n', 'You are invited to my birthday this Saturday.\n']

with open("./Input/Letters/starting_letter.docx", mode="r") as file:
    # Read one line
    contents = file.readline()
    print(contents)
    # RESULT: Dear [name],

with open("./Input/Letters/starting_letter.docx", mode="r") as file:
    # Read one line, up to the "hint" number of bytes
    contents = file.readline(8)
    print(contents)
    # # RESULT: Dear [na
