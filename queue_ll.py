from linkedlist import LinkedList


class Queue(object):
    """A queue. FIFO.

    Operations: enqueue(item), dequeue(), peek(), is_empty()

    Make a queue:

        >>> karaoke_playlist = Queue()

    Anything in the queue?

        >>> karaoke_playlist.is_empty()
        True

    If there's nothing in the karaoke queue, how can we sing like crazy
    people? Let's add songs.

        >>> karaoke_playlist.enqueue("Try Everything -- Shakira")
        >>> karaoke_playlist.enqueue("Sing -- Pentatonix")
        >>> karaoke_playlist.enqueue("Best Day of My Life -- American Authors")

    Anything in the queue now?

       >>> karaoke_playlist.is_empty()
       False

    Sweeeet. Now we can belt some tunes. Which song is first?

       >>> karaoke_playlist.peek()
       'Try Everything -- Shakira'

    Let's sing it!

       >>> song = karaoke_playlist.dequeue()

    Are we singing the right song?

       >>> print(f"Now singing: {song}")
       Now singing: Try Everything -- Shakira

    Looks about right. What's next?

       >>> karaoke_playlist.peek()
       'Sing -- Pentatonix'

    We can take a break now...

    But let's see how our repr comes out, anyway.

       >>> print(karaoke_playlist)
       <Queue Front: Sing -- Pentatonix>
    """

    def __init__(self):
        """Initialize queue."""

        self.items = LinkedList()

    def __repr__(self):
        """A human-readable representation of the queue instance."""

        return "<Queue Front: {front}>".format(front=self.peek())

    def is_empty(self):
        """Return True if no items in queue. Return False otherwise."""

        return self.items.head is None

    def enqueue(self, item):
        """Place an item at the back of the queue."""

        self.items.append(item)

    def dequeue(self):
        """Remove the item at the front of the queue and return it."""

        front_item = self.items.head

        self.items.remove(self.items.head.data)

        return front_item.data

    def peek(self):
        """Check the item at the front of the queue and return it."""

        if self.items.head:
            return self.items.head.data

        else:
            return None
