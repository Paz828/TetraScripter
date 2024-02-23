from line_linked_list import Char_List
from grammar_rules import Grammar

with open('../translation.txt') as f:
    position = ['full', 'top', 'bottom']
    txt = f.read()
    txt_list = []
    index = 0
# Creates the Char linked List
    for char in txt:
        char_obj = {
        'index': index,
        'letter': char.lower(),
        'pos': position[0],
        'doubled': False,
        'oo': False,
        'special': False,
        'post_o': False,
        'after_l': False,
        'pre_o': False,
        }

        txt_list.append(char_obj)
        index += 1

    clist = Char_List(txt_list)

# Formats each node in the linke list
    for char in clist:
        data = char.data
        
        if char.next:
            next = char.next.data

        if char.prev:
            prev = char.prev.data

            if prev['special']:

                if prev['oo']:
                    prev['oo'] = False
                    clist.remove_index(char.next.data['index'])
                    
                clist.remove_index(data['index'])
                prev['special'] = False

            elif data['letter'] == 'o':
                clist.remove_index(data['index'])

            else:
                Grammar(char).check()
                

        else:
            Grammar(char).check()
        
    translated_list = []

    for char in clist:
        translated_list.append(char.data['letter'])

    print(clist)
    print(''.join(translated_list))