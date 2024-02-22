class Char_List(object):
    
# Constructor
    def __init__(self, chars=None):
        self.head = None

        if chars is not None:
            char = Char(data=chars.pop(0))
            prev = None
            self.head = char

            for elem in chars:
                char.next = Char(data=elem)
                char.prev = prev
                prev = char
                char = char.next 

# Representer
    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('End')

        return "\n".join(map(str, nodes))
    
# Iteration
    def __iter__(self):
        char = self.head

        while char is not None:
            yield char
            char = char.next

# Delete
    # def 
    
class Char(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)
    
        # self.char = ltr
        # self.pos = None
        # self.special = None
        # self.post_o = False
        # self.pre_o = False
        # self.doubled = False