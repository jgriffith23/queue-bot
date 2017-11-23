from slackclient import SlackClient
import os, time, re, random

# Todo: use an actual queue data structure, built on a linked list
_QUEUE = []

QUEUE_EMPTY_MESSAGES = {
    "QUEUE = []",
    "QUEUE =  [ ]",
    "QUEUE=[]",
    "QUEUE=[ ]",
    "QUEUE = [ ]",
    "queue = []",
    "queue= []",
    "queue =[]",
    "queue =  []",
    "queue=[ ]",
    "queue = [ ]",
    "queue =[ ]",
    "queue= [ ]",
    "QUEUE.open()",
    "QUEUE.open( )",
    "queue.open()",
    "queue.open( )",
}

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


def run_bot_update_queue(sc):
    """Check latest messages constantly and update queue."""

    help_channel = sc.server.channels.find("help")
    help_channel_id = help_channel.id

    # Read messages forever!

    # TODO: Add whitelist of users who are allowed to interact with queue bot
    # to make sure staff are the only ones who can manage the queue.

    while True:
        latest = sc.rtm_read()

        # Are there any new messages, and are they not the stock bot connection
        # message?
        if (latest != [] and
            latest != [{'text': u'hello'}]):

            latest = latest[0]

            # Make sure we're in the help channel.
            if (latest.get("channel") == help_channel_id and
                latest.get("type") == "message"):

                # Was the latest update posted by a user, and was it in fact
                # a message?
                if latest.get("user"):
                    text = latest["text"]
                    print "Latest:", latest

                    respond_to_message(sc, text, help_channel_id)

                time.sleep(.5)


def respond_to_message(sc, text, channel_id):
    """Given a Slack client and text, decide how to respond to the message."""

    # Did someone indicate the queue should be empty?
    if text in QUEUE_EMPTY_MESSAGES:
        message = "QUEUE = [{}]".format(random.choice(EMOJIS))
        print message
        sc.rtm_send_message(channel_id, message)

    # Add a new student to the queue. Staff should still have to do
    # this manually.
    elif "queue.enqueue" in text.lower():
        users_to_enqueue = re.findall(r"<@\w+>", text)
        print users_to_enqueue

        _QUEUE.extend(users_to_enqueue)

        sc.rtm_send_message(
            channel_id,
            "QUEUE = [{}]".format(" ".join(_QUEUE))
        )

    # A staff member should still say "on my way" before
    # dequeuing, but they can dequeue instead of manually re-typing
    # the whole queue.

    elif "queue.dequeue" in text.lower():
        _QUEUE.pop(0)

        # Check whether we should display students or silliness in QUEUE
        if _QUEUE != []:
            current_queue = " ".join(_QUEUE)

        else:
            current_queue = random.choice(EMOJIS)

        sc.rtm_send_message(
            channel_id,
            "QUEUE = [{}]".format(current_queue)
        )

    # A user could be allowed to remove themselves.
    elif "queue.remove" in text.lower():
        user_to_remove = re.search(r"<@\w+>", text).group()
        _QUEUE.remove(user_to_remove)

        sc.rtm_send_message(
            channel_id,
            "QUEUE = [{}]".format(" ".join(_QUEUE))
        )


if __name__ == "__main__":

    # Get API token and instantiate a client for all our Slack
    # interactions.
    slack_token = os.environ.get("BOT_API_TOKEN")
    sc = SlackClient(slack_token)

    # Try to connect to the real time messaging service
    if sc.rtm_connect():
        run_bot_update_queue(sc)
    else:
        print "Connection Failed"