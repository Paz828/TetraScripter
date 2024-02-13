

position = ['full', 'top', 'bottom']
last_letter_obj = {
    'letter': '',
    'pos': '',
    'special': 'false',
}
tetra_dict = {
    'A': 'A',
    'a': 'a',
    'B': 'B',
    'b': 'b',
    'C': 'C',
    'c': 'c',
    'D': 'D',
    'd': 'd',
    'E': 'E',
    'e': 'e',
    'F': 'F',
    'f': 'f',
    'G': 'G',
    'g': 'g',
    'H': 'H',
    'h': 'h',
    'I': 'I',
    'i': 'i',
    'J': 'J',
    'j': 'j',
    'K': 'K',
    'k': 'k',
    'L': 'L',
    'l': 'l',
    'M': 'M',
    'm': 'm',
    'N': 'N',
    'n': 'n',
    'O': 'O',
    'o': 'o',
    'P': 'P',
    'p': 'p',
    'Q': 'Q',
    'q': 'q',
    'R': 'R',
    'r': 'r',
    'S': 'S',
    's': 's',
    'T': 'T',
    't': 't',
    'U': 'U',
    'u': 'u',
    'V': 'V',
    'v': 'v',
    'W': 'W',
    'w': 'w',
    'X': 'X',
    'x': 'x',
    'Y': 'Y',
    'y': 'y',
    'Z': 'Z',
    'z': 'z'
}



# Read the File
with open('test.txt') as f:
    contents = f.read().lower()
    char_list = []
    output = []
    index = 0

    def t_check(ltr):
        if ltr.lower() == 't' and last_letter_obj['pos'] == position[2]:
            last_letter_obj['pos'] = position[1]

    for char in contents:
        char_list.append(char)

# for now, this is where I check each letter's position in relation to the letters around it and choose the proper form based on that.
    for letter in char_list:
        current_letter_obj = {
        'letter': letter,
        'pos': position[0],
        'special': 'false',
        }
        index += 1

        if last_letter_obj['letter'] == '':
            pass

        if last_letter_obj['pos'] == position[0] and last_letter_obj['letter'] != ' ':

            if current_letter_obj['letter'] == ' ':
                last_letter_obj['pos'] = position[0]
                last_letter_obj['letter'] = last_letter_obj['letter'].upper()
            
            else:
                last_letter_obj['pos'] = position[1]
                current_letter_obj['pos'] = position[2]

        elif last_letter_obj['pos'] == position[2]:
            t_check(last_letter_obj['letter'])
            current_letter_obj['pos'] = position[0]

        if last_letter_obj['letter']:

            if last_letter_obj['letter'] == ' ':
                output.append(last_letter_obj['letter'])
            
            else:
                output.append(tetra_dict[last_letter_obj['letter']])

        if index == len(char_list):

            if current_letter_obj['pos'] == position[0]:
                current_letter_obj['letter'] = current_letter_obj['letter'].upper()

            output.append(tetra_dict[current_letter_obj['letter']])

        last_letter_obj = current_letter_obj
        
    print(''.join(output))