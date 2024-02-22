

position = ['full', 'top', 'bottom']
last_letter_obj = {
    'letter': '',
    'pos': '',
    'special': False,
    'post_o': False,
    'pre_o': False,
}
tetra_dict = {
    'A': 'A',
    'a': 'a',
    'B': 'B',
    'b': 'b',
    'C': 'C',
    'c': 'c',
    'CH': 'CH',
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
    'PH': 'PH',
    'Q': 'Q',
    'q': 'q',
    'R': 'R',
    'r': 'r',
    'S': 'S',
    's': 's',
    'SH': 'SH',
    'T': 'T',
    't': 't',
    'TH': 'TH',
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
    'z': 'z',
    '\n': '\n',
    '`': '`',
}



# Read the File
with open('translation.txt') as f:
    contents = f.read().lower()
    char_list = []
    output = []
    index = 0

    def t_check(ltr):

        if ltr.lower() == 't' and last_letter_obj['pos'] == position[2]:
            last_letter_obj['pos'] = position[1]

    def o_check(current):

        if current['letter'] == 'o' or last_letter_obj['pre_o']:
            
            if last_letter_obj['pre_o'] or last_letter_obj['post_o']:
                current['pre_o'] = True
            
            else:
                last_letter_obj['post_o'] = True
                current['post_o'] = True

    def double_check(current):

        if last_letter_obj['letter'].lower() == current['letter'].lower():

            if last_letter_obj['special']:
                current['special'] = True

            current['letter'] = '`'
            current['pos'] = last_letter_obj['pos']

    def generate_special(ltr):
        current = current_letter_obj['letter'].lower()   

        match ltr.lower():

            case '`': # special case for doubler mark

                if last_letter_obj['special']:
                    current_letter_obj['special'] = True

            case 'l': # L
                    
                if last_letter_obj['pos'] == position[1]:
                    last_letter_obj['letter'] = last_letter_obj['letter'].upper()
                    last_letter_obj['pos'] = position[0]

                    current_letter_obj['pos'] = position[1]
                    current_letter_obj['special'] = True

            case 't': #TH

                if current == 'h':
                    last_letter_obj['letter'] = 'TH'
                    last_letter_obj['pos'] = position[0]
                    last_letter_obj['special'] = True

            case 'c': # CH

                if current == 'h':
                    last_letter_obj['letter'] = 'CH'
                    last_letter_obj['pos'] = position[0]
                    last_letter_obj['special'] = True

            case 's': # SH

                if current == 'h':
                    last_letter_obj['letter'] = 'SH'
                    last_letter_obj['pos'] = position[0]
                    last_letter_obj['special'] = True

            case 'p': # PH

                if current == 'h':
                    last_letter_obj['letter'] = 'PH'
                    last_letter_obj['pos'] = position[0]
                    last_letter_obj['special'] = True       

    def handle_special(current):
        special_obj = {
            'th': True,
            'ch': True,
            'sh': True,
            'ph': True,
        }

        if last_letter_obj['special']:
            
            if not last_letter_obj['letter'].lower() in special_obj or last_letter_obj['letter'] == '`':
                current['pos'] = position[1]
            
            else:
                #skip current letter
                return 'skip'


    for char in contents:
        char_list.append(char)

    # for now, this is where I check each letter's position in relation to the letters around it and choose the proper form based on that.
    for letter in char_list:
        current_letter_obj = {
        'letter': letter,
        'pos': position[0],
        'special': False,
        'post_o': False,
        'pre_o': False,
        }
        index += 1

        t_check(last_letter_obj['letter'])
        double_check(current_letter_obj)
        o_check(current_letter_obj)

        # Positons the last letter to the top position and current letter to the bottom positon. Also checks for if a space is next in which case it puts the letter in the full position if need be
        if (last_letter_obj['pos'] == position[0] or last_letter_obj['pos'] == position[1]) and last_letter_obj['letter'] != ' ':

            if last_letter_obj['letter'] != '\n':

                if current_letter_obj['letter'] == ' ' or current_letter_obj['letter'] == '\n':
                    last_letter_obj['pos'] = position[0]
                    last_letter_obj['letter'] = last_letter_obj['letter'].upper()
                
                else:
                    last_letter_obj['pos'] = position[1]
                    current_letter_obj['pos'] = position[2]

        # Positions the next letter to the default(full) position. Also checks to see if last letter is a 't' in which case it positions it accordingly
        elif last_letter_obj['pos'] == position[2]:
            current_letter_obj['pos'] = position[0]

        generate_special(last_letter_obj['letter'])
        skip = handle_special(current_letter_obj)

        if skip == 'skip':
            current_letter_obj = {
                'letter': '',
                'pos': position[2],
                'special': False,
                'pre_o': current_letter_obj['pre_o'],
                'post_o': current_letter_obj['post_o'],
            }


        # Get rid of the o's        
        if current_letter_obj['letter'].lower() == 'o':
            current_letter_obj['letter'] = ''
            current_letter_obj['pos'] = last_letter_obj['pos']

        # Appends the letter to the output either as a space, or translating it through the dict
        if last_letter_obj['letter']:

            if last_letter_obj['letter'] == ' ' or last_letter_obj['letter'] == '\n':
                output.append(last_letter_obj['letter'])
            
            elif last_letter_obj['post_o']:
                output.append(tetra_dict[last_letter_obj['letter']] + '*')

            elif last_letter_obj['pre_o']:
                output.append('*' + tetra_dict[last_letter_obj['letter']])  
                current_letter_obj['pre_o'] = False              
            
            else:
                output.append(tetra_dict[last_letter_obj['letter']])

        # A check to make sure the last letter of the text file is still appended and in its proper position
        if index == len(char_list):

            if current_letter_obj['pos'] == position[0]:
                current_letter_obj['letter'] = current_letter_obj['letter'].upper()

            output.append(tetra_dict[current_letter_obj['letter']])

        print(last_letter_obj)
        # print(current_letter_obj)
        last_letter_obj = current_letter_obj
        
    print(''.join(output))