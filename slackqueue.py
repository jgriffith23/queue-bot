from queue_ll import Queue
import random


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

    def __init__(self):
        super(SlackQueue, self).__init__()

        self.open = False

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
