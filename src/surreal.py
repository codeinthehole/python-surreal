import re

class Surreal(object):
    """
    Surreal number
    """
    def __init__(self, raw):
        string = str(raw)
        self.number = None
        self.left = None
        self.right = None

        # Check if is integer
        if string.isdigit():
            self.number = int(string)
        # Check string for the {L|R} syntax
        m = re.match(r'^{(.*)\|(.*)}$', string)
        if m and len(m.groups()) == 2:
            self.left = m.group(1)
            self.right = m.group(2)

    def __eq__(self, other):
        return int(self) == int(other)

    def __int__(self):
        if self.number != None:
            return int(self.number)
        if self.left == '' and self.right == '':
            return 0
        if self.left == '1':
            return 1

    def __repr__(self):
        if self.left != None and self.right != None:
            return '{%s|%s}' % (self.left, self.right)

class Zero(Surreal):
    def __init__(self):
        super(Zero, self).__init__('', '')

