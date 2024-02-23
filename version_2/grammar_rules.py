position = ['full', 'top', 'bottom']
breaks = [' ', '\n', '.', '']

class Grammar():

    def __init__(self, current):
        self.data = current.data
        self.letter = self.data['letter']
        self.next = current.next
        self.prev = current.prev
    
    def format(self):
    
    # sets the general position of each character based on it's neighbors
        if not self.prev:

            if not self.next:
                self.data['pos'] = position[0]
                return
            
            if self.next.data['letter'] in breaks:
                self.data['pos'] = position[0]

            else:
                self.data['pos'] = position[1]

        elif not self.next:
            prev_pos = self.prev.data['pos']

            if prev_pos == position[0] or prev_pos == position[2]:
                self.data['pos'] = position[0]

            else:
                self.data['pos'] = position[2]

        else:
            next_ltr = self.next.data['letter']
            prev_pos = self.prev.data['pos']

            if self.letter in breaks:
                self.data['pos'] = position[0]
                return

            if next_ltr in breaks and prev_pos == position[2]:
                self.data['pos'] = position[0]

            elif prev_pos == position[0] or prev_pos == position[2] or self.prev.data['after_l']:
                self.data['pos'] = position[1]

            else:
                self.data['pos'] = position[2]

    # fixes the position for any characters with specific rules
        self.special()
        self.double()
        self.t()
        self.o()
        self.l()

    def special(self):
        
        if self.next:
            next_ltr = self.next.data['letter']

            match self.letter:
                
                case 'c' | 'p' | 's' | 't':
                    
                    if next_ltr == 'h':
                        self.data['letter'] = self.letter + 'h'
                        self.data['pos'] = position[0]
                        self.data['special'] = True

    def double(self):
        
        if self.next:
            next_ltr = self.next.data['letter']

            if self.letter == next_ltr:
                self.data['doubled'] = True
                self.data['special'] = True

    def t(self):

        if self.letter == 't' and self.data['pos'] == position[2]:

            if not self.next:
                self.data['pos'] = position[0]

            else:

                if self.next.data['letter'] in breaks:
                    self.data['pos'] = position[0]

                else:
                    self.data['pos'] = position[1]

    def o(self):
            
        if self.next:

            if self.data['doubled'] and self.next.next.data['letter'] == 'o':
                self.data['post_o'] = True
                
            if self.next.data['letter'] == 'o':
                self.data['post_o'] = True

                if self.next.next:

                    if self.next.next.data['letter'] == 'o':
                        self.data['oo'] = True

                        if self.next.next.next:
                            self.next.next.next.data['pre_o'] = True

                self.data['special'] = True

    def l(self):

        if self.data['after_l']:
            self.data['pos'] = position[1]

        if self.letter == 'l':

            if self.data['pos'] == position[1]:
                self.data['pos'] = position[0]

                next = self.next
                next_ltr = next.data['letter']
                    
                while next_ltr == 'o' or next_ltr == 'l':
                    next_ltr = next.data['letter']
                    next = next.next

                next.data['after_l'] = True

    def convert(self):
        
        if self.data:
            data = self.data

            if data['pos'] == position[0]:
                self.data['letter'] = self.data['letter'].upper()

            if data['doubled']:

                if self.next.next.data['letter'] in breaks and data['pos'] == position[1]:
                    self.data['letter'] = self.data['letter'].upper()

                self.data['letter'] = self.data['letter'] + '`'

            if data['post_o']:
                self.data['letter'] = self.data['letter'] + '*'

            if data['pre_o']:
                self.data['letter'] = '*' + self.data['letter']

    def check(self):
        self.format()
        self.convert()