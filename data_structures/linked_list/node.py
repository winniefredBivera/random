"""
linked list node
"""

class node:
    """individual elements of a linked list"""

    element = None
    next = None

    def __init__(self, element):
        """constructor"""
        self.element = element
        self.next = None
