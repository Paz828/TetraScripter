from line_linked_list import Char_List, Char
from grammar_rules import Grammar

with open('../translation.txt') as f:
    position = ['full', 'top', 'bottom']
    txt = f.read()
    txt_list = []
    index = 0

    for char in txt:
        char_obj = {
        'index': index,
        'letter': char,
        'pos': position[0],
        'special': False,
        'post_o': False,
        'pre_o': False,
        }

        txt_list.append(char_obj)
        index += 1

    clist = Char_List(txt_list)

    print(clist.head.prev)