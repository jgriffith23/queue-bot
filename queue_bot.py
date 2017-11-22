from slackclient import SlackClient
import os, time, re

QUEUE_EMPTY_MESSAGES = [
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
]


def run_bot_update_queue(sc):
    """Check latest messages constantly and update queue."""

    # TODO: Use a better queue data structure.
    _queue = []

    # Read messages forever!

    # TODO: Add whitelist of users who are allowed to interact with queue bot
    # to make sure staff are the only ones who can manage the queue.

    while True:
        latest = sc.rtm_read()

        # Are there any new messages, and are they not the stock bot connection
        # message?
        if latest != [] and latest != [{'text': u'hello'}]:
            latest = latest[0]

            # Was the latest update posted by a user, and was it in fact
            # a message?
            if latest.get("user") and latest.get("type") == "message":
                text = latest["text"]
                print "Latest:", latest

                # Did someone indicate the queue should be empty?
                if text in QUEUE_EMPTY_MESSAGES:
                    sc.rtm_send_message("general", "QUEUE = [:heart:]")

                # Add a new student to the queue. Staff should still have to do
                # this manually.
                elif "queue.enqueue" in text.lower():
                    users_to_enqueue = re.findall(r"<@\w+>", text)
                    print users_to_enqueue

                    _queue.extend(users_to_enqueue)

                    sc.rtm_send_message(
                        "general",
                        "QUEUE = [{}]".format(" ".join(_queue))
                    )

                # A staff member should still say "on my way" before
                # dequeuing, but they can dequeue instead of manually re-typing
                # the whole queue.

                elif "queue.dequeue" in text.lower():
                    _queue.pop(0)
                    sc.rtm_send_message(
                        "general",
                        "QUEUE = [{}]".format(" ".join(_queue))
                    )

                # A user would be allowed to remove themselves.
                elif "queue.remove" in text.lower():
                    user_to_remove = re.search(r"<@\w+>", text).group()
                    _queue.remove(user_to_remove)

                    sc.rtm_send_message(
                        "general",
                        "QUEUE = [{}]".format(" ".join(_queue))
                    )

            time.sleep(.5)


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