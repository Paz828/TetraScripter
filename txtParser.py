with open('test.txt') as f:
    contents = f.read().upper()
    char_list = []

    for char in contents:
        char_list.append(char)

    

    print(char_list)