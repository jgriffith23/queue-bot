from slackclient import SlackClient
import os, time, re, random
from slackqueue import SlackQueue


# Todo: use an actual queue data structure, built on a linked list
# SERIOUSLY DO THIS. Don't use a dictionary forever; that's gross. The
# list is also inefficient.

_QUEUE = SlackQueue()

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


def run_bot_update_queue(sc, channel_name):
    """Check latest messages constantly and update queue."""

    # Set the channel to send messages to, based on name passed
    channel_info = sc.server.channels.find(channel_name)
    channel_id = channel_info.id

    # TODO: Add whitelist of users who are allowed to interact with queue bot
    # to make sure staff are the only ones who can manage the queue.

    # Read messages forever!
    while True:

        latest = sc.rtm_read()

        # Are there any new messages, and are they not the stock bot connection
        # message?
        if (latest != [] and
            latest != [{'text': u'hello'}]):

            latest = latest[0]

            # Make sure we're in the desired channel and the latest update
            # was actually a message, not a typing notification.
            if (latest.get("channel") == channel_id and
                latest.get("type") == "message"):

                text = latest["text"]
                print "Latest:", latest

                if "queue.open()" in text.lower():
                    _QUEUE.open = True

                elif "queue.close()" in text.lower():
                    while not _QUEUE.is_empty():
                        _QUEUE.dequeue()

                    _QUEUE.open = False

                if _QUEUE.open:
                    respond_to_message(sc, text, channel_id)

                time.sleep(.5)


def respond_to_message(sc, text, channel_id):
    """Given a Slack client and text, decide how to respond to the message."""

    # If someone indicated the queue should be empty, then empty it.
    # FIXME: refactor to use .lower(). This means updating the list of empty
    # messages, too.
    if text in QUEUE_EMPTY_MESSAGES:
        while not _QUEUE.is_empty():
            _QUEUE.dequeue()

    # Add a new student to the queue. Staff should still have to do
    # this manually.
    elif "queue.enqueue" in text.lower():

        # Use regex to find all user handles in the message, using Slack's
        # standard format for referring to users: <@the-user's-id> (the id
        # is *not* the user's handle).

        users_to_enqueue = re.findall(r"<@\w+>", text)
        _QUEUE["users"].extend(users_to_enqueue)

    # A staff member should still say "on my way" before
    # dequeuing, but they can dequeue instead of manually re-typing
    # the whole queue.

    elif "queue.dequeue" in text.lower():
        _QUEUE["users"].pop(0)

    # A user could be allowed to remove themselves.
    elif "queue.remove" in text.lower():
        user_to_remove = re.search(r"<@\w+>", text).group()
        _QUEUE["users"].remove(user_to_remove)

    # FIXME: Need to stop bot from posting every time a message is sent.
    # Perhaps map commands to function identfiers in a dictionary, check if
    # command in dict, call appropriate function if so, and then send message
    # inside if block?

    sc.rtm_send_message(
        channel_id,
        _QUEUE.generate_display()
    )


if __name__ == "__main__":

    # Get API token and instantiate a client for all our Slack
    # interactions.
    slack_token = os.environ.get("BOT_API_TOKEN")
    sc = SlackClient(slack_token)

    # Try to connect to the real time messaging service
    if sc.rtm_connect():
        run_bot_update_queue(sc, "help")
    else:
        print "Connection Failed"
