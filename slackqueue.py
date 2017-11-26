from queue_ll import Queue
import random
import re


EMOJIS = [
    ":unicorn_face:",
    ":robot_face:",
    ":stuck_out_tongue_closed_eyes:",
    ":whale:",
    ":octopus:",
    ":earth_americas:",
    ":open_book:",
    ":deciduous_tree:",
    ":sign_of_the_horns:",
    ":blowfish:",
    ":frog:",
    ":hatched_chick:",
    ":floppy_disk:",
    ":truck:",
    ":balloon:",
    ":birthday:",
    ":dancers:",
    ":bento:",
    ":guitar:",
    ":airplane_departure:",
    ":grey_question:",
    ":world_map:",
    ":lion_face:",
    ":dog:",
    ":sunflower:",
    ":elephant:",
    ":poodle:",
    ":spider_web:",
    ":white_circle:",
    ":paw_prints:",
    ":fire:",
    ":two_women_holding_hands:",
    ":lion_face:",
]


class SlackQueue(Queue):
    """A queue class designed for use in Slack-based user queues."""

    _empty_messages = {
            "queue = []",
            "queue= []",
            "queue =[]",
            "queue =  []",
            "queue=[ ]",
            "queue = [ ]",
            "queue =[ ]",
            "queue= [ ]",
    }

    def __init__(self):
        super(SlackQueue, self).__init__()

        self.is_open = False
        self.has_changed = False

    def generate_display(self):
        """Decide what to show for the queue."""

        queue_template = "QUEUE = [{}]"

        # Check whether we should display students or silliness in QUEUE
        if not self.is_empty():
            queue_as_list = []
            current = self.items.head

            while current:
                queue_as_list.append(current.data)
                current = current.next

            queue_display = queue_template.format(" ".join(queue_as_list))

        else:
            queue_display = queue_template.format(random.choice(EMOJIS))

        return queue_display

    def update(self, text):
        """Update queue according to most recent command text, if valid."""

        # Empty the queue.
        if text.lower() in SlackQueue._empty_messages:
            while not self.is_empty():
                self.dequeue()

            self.has_changed = True

        # Add a new student to the queue. Staff should still have to do
        # this manually.
        elif "queue.enqueue" in text.lower():

            # Use regex to find all user handles in the message, using Slack's
            # standard format for referring to users: <@the-user's-id> (the id
            # is *not* the user's handle).

            users_to_enqueue = re.findall(r"<@\w+>", text)
            while users_to_enqueue:
                self.enqueue(users_to_enqueue.pop())

            self.has_changed = True

        # A staff member should still say "on my way" before
        # dequeuing, but they can dequeue instead of manually re-typing
        # the whole queue.

        elif "queue.dequeue" in text.lower():
            self.dequeue()
            self.has_changed = True

        # A user could be allowed to remove themselves.
        elif "queue.remove" in text.lower():
            user_to_remove = re.search(r"<@\w+>", text).group()
            self.items.remove(user_to_remove)

            self.has_changed = True

        # If we didn't get a valid command, then we haven't changed anything.
        else:
            self.has_changed = False
