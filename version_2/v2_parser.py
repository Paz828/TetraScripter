from line_linked_list import Char_List, Char

with open('../translation.txt') as f:
    position = ['full', 'top', 'bottom']
    txt = f.read()
    txt_list = []

    for char in txt:
        char_obj = {
        'letter': char,
        'pos': position[0],
        'special': False,
        'post_o': False,
        'pre_o': False,
        }
        txt_list.append(char_obj)

    clist = Char_List(txt_list)

    print(clist.head.next.prev)