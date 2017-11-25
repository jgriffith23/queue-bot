"""Implementation of a node.

Useful for trees, linked lists, graphs, etc.
"""


class Node(object):
    """A node for a linked list.

    Make a node:

        >>> apple = Node("apple")
        >>> apple.data
        'apple'
        >>> print(apple.next)
        None
        >>> print(apple.prev)
        None

    And another:

        >>> berry = Node("berry")
        >>> apple.next = berry
        >>> berry.prev = apple

        >>> print(apple.next)
        <Node berry>
        >>> print(berry.prev)
        <Node apple>
        >>> print(berry.next)
        None
    """

    def __init__(self, data):
        """Initialize the node's attributes."""

        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """A human-readable representation of a node."""

        return "<Node {data}>".format(data=self.data)
