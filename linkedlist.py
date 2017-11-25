"""Implementation of a linked list."""

from node import Node


class LinkedList(object):
    """A doubly linked list, consisting of Nodes that track next and prev.

    Let's make a list. I'm hungry, so it's gonna be fruits.

        >>> fruits = LinkedList()

    Add a node to be the head:

        >>> fruits.append("apple")
        >>> fruits.head
        <Node apple>
        >>> fruits.tail
        <Node apple>

    Now let's add some more:

        >>> fruits.append("berry")
        >>> fruits.tail
        <Node berry>
        >>> fruits.head.next
        <Node berry>
        >>> fruits.tail.prev
        <Node apple>

        >>> fruits.append("cherry")
        >>> fruits.append("dragonfruit")
        >>> fruits.append("eggplant")
        >>> fruits.append("fig")

    I think I want to eat the apple first.

       >>> fruits.remove("apple")

    What's left?

        >>> fruits.display()
        berry
        cherry
        dragonfruit
        eggplant
        fig

    Now a fig.

        >>> fruits.remove("fig")

    What's left?

        >>> fruits.display()
        berry
        cherry
        dragonfruit
        eggplant

    Okay, cherries are awesome.

        >>> fruits.remove("cherry")

    What's left?

        >>> fruits.display()
        berry
        dragonfruit
        eggplant

    Let's save those for later.
    """

    def __init__(self):
        """Initialize an empty LL."""

        self.head = None
        self.tail = None

    def __repr__(self):
        """A human-readable representation of the linked list."""

        return "<LinkedList Head: {head_data} Tail: {tail_data}>".format(
            head_data=self.head.data, tail_data=self.tail.data)

    def append(self, data):
        """Add a new node to the end of the list."""

        new_node = Node(data)

        # Do we have a head yet?

        if self.head is None:
            self.head = new_node

        # Do we have a tail yet? If so, we have to make the new node its
        # next and make the new node's previous the current tail, before
        # updating tail to the new node.

        if self.tail is not None:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node

    def remove(self, data):
        """Remove the node with the given data from the linked list.

        Only remove first occurrence seen.
        """

        # Start at the head.
        current = self.head

        # Iterate over the linked list. If we've hit the end, we can just
        # adjust the tail. Otherwise, we have to move pointers for both
        # nodes around the node to remove.

        while current is not None:

            if current.data == data:
                # A typical case -- removing from the middle.

                if current.prev is not None and current.next is not None:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                # Removing the head.

                elif current.prev is None:
                    if current.next is None:
                        self.head = None
                        self.tail = None

                    else:
                        self.head = self.head.next
                        self.head.prev = None

                # Removing the tail, when it is not the head.

                else:
                    current.prev.next = None
                    self.tail = current.prev

            current = current.next

    def display(self):
        """Blat the contents of the list to stdout."""

        current = self.head

        while current is not None:
            print(current.data)

            current = current.next
