position = ['full', 'top', 'bottom']
breaks = [' ', '\n', '.']

class Grammar():

    def __init__(self, current):
        self.data = current.data
        self.letter = self.data['letter'].lower()
        self.next = current.next
        self.prev = current.prev
    
    def format(self):

    # sets the position of each character based on it's neighbors
        if not self.prev:

            if not self.next:
                self.data['pos'] = position[0]
                return
            
            if self.next.data['letter'] in breaks:
                self.data['pos'] = position[0]

            else:
                self.data['pos'] = position[1]

        elif not self.next:
            prev = self.prev.data
            prev_pos = prev['pos']

            if prev_pos == position[0] or prev_pos == position[2]:
                self.data['pos'] = position[0]

            else:
                self.data['pos'] = position[2]

        else:
            next = self.next.data
            next_ltr = next['letter']

            if next_ltr in breaks and (prev_pos == position[0] or prev_pos == position[2]):
                self.data['pos'] = position[0]

            if prev_pos == position[0] or prev_pos == position[2]:
                self.data['pos'] = position[1]

            else:
                self.data['pos'] = position[2]

    # fixes the position for any characters with specific rules
        self.special()
        self.double()
        self.t()
        self.o()
        self.l()

    def double(self):
        pass

    def special(self):
        pass

    def t(self):

        if self.letter == 't' and pos == position[2]:
            pos = self.data['pos']

            if self.final_char:
                pos = position[0]

            else:
                next = self.next.data

                if next['letter'] in breaks:
                    pos = position[0]

                else:
                    pos = position[1]

    def o(self):
        pass

    def l(self):
        pass

    def convert(self):
        pass

    def check(self):
        self.format()
        self.convert()