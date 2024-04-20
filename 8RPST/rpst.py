#Min Radix Priority Search Tree
class Node(object):
    def __init__(self, xval, yval):
        self.xval = xval
        self.yval = yval
        self.rtChild = None
        self.ltChild = None
        self.range = None
        
class RPSTree(object):
    def __init__(self):
        self.root = None
        
        
        