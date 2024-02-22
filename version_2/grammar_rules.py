postition = ['full', 'top', 'bottom']

class Grammar():

    def __init__(self, current):
        self.data = current.data
        self.letter = self.data['letter'].lower()
        self.next = current.next.data
        self.prev = current.prev.data

    def t(self):
        pos = self.data['pos']

        if self.letter == 't' and pos == postition[2]:
            pos = postition