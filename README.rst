.. TODO: Write details on setting up your slack bot or link to tutorial
.. TODO: Add details on setting up bot in a particular team
.. TODO: Add resource links to Slack bot users, RTM, etc.

=========
Queue Bot
=========

Queue Bot was designed to manage Slack-based help queues. Built with Python 2.7
and Slack's Real Time Messaging API.


Setup
=====

You can get Queue Bot running in two stages: Slack setup and environment setup.


Creating a Custom Slack Bot Integration
---------------------------------------

First, integrate a bot with Slack so that you can get an API token for it. To 
integrate a custom bot with your Slack team, do the following:

#. Log into the Slack team where you want to integrate a Queue Bot, and go to
   "Manage Apps" from the left-hand menu. This should bring you to the browser
   admin interface for your channel.

   .. image:: https://github.com/jgriffith23/queue-bot/blob/master/images/manage_apps.png?raw=true

#. Click the "Browse" button.

   .. image:: https://github.com/jgriffith23/queue-bot/blob/master/images/browse_apps.png?raw=true

#. Use the search bar to find the Bots app. Select it.

   .. image:: https://github.com/jgriffith23/queue-bot/blob/master/images/find_bots_app.png?raw=true

#. Click the "Add Configuration" button and follow the setup only prompt:
   pick a username for your bot.
   
   .. image:: https://github.com/jgriffith23/queue-bot/blob/master/images/on_bots_page.png?raw=true

#. You should be sent to a page where you can customize your bot settings and
   view your API token. Yours should be something other than a blurry blob.
   
   .. image:: https://github.com/jgriffith23/queue-bot/blob/master/images/bots_config_page.png?raw=true

#. Make any customizations you want to make, save your integration, and head 
   back to Slack. Keep the bot integration page open.

#. Go to the channel where you want your bot to be able to post. In my code,
   the channel is called "help," but you can call it whatever you want.

#. Invite your bot to that channel with the username you gave it in the admin
   interface. 

Finally, copy your API token from the bot integration page of your Slack admin
interface, and open your terminal.


Running the Code
----------------

I assume you already have your preferred version of Python installed. As I said
before, this project was built with Python 2.7, but the setup for Python 3
should be similar.

#. Download the files from this repo to a new directory (Clone it if you like. 
   Heck, fork it and modify it.) and navigate into that directory.

#. Put your API key into your shell environment. I suggest adding it to a
   file called *secrets.sh* and adding this bit of bash code:

   .. code-block:: bash

       export BOT_API_TOKEN="a-really-long-thing-that-is-your-bot-token"

   Now, you can export your variable into the environment like this:

   .. code-block:: bash

        source secrets.sh

   Just be sure to add *secrets.sh* to your *.gitignore* file to keep your
   secrets off the Internet!

   *Fun fact: If you do accidentally push your Slack API token to GitHub, you'll
   receive a lovely email from Slack alerting you that your token was posted on
   the Internet and that they've disabled it. The email includes where the token
   was found and a link to how to issue a new one. Way to go, Slack!*

#. Create a virtual environment: 

   .. parsed-literal::

       virtualenv env

#. Activate your virtual environment:

   .. parsed-literal::

       source env/bin/activate

#. Install all requirements: 

   .. parsed-literal:: 

       pip install -r requirements.txt

#. With your secrets sourced and your environment activated, run *queue_bot.py*

The terminal should appear to hang. But if you start typing messages in the
channel you invited your bot to, you should see a dictionary print to stdout
for each message you send.


Available Commands
==================

If you're seeing message data appear in your terminal, you're ready to start
up a user queue. I've currently implemented four commands.

The following list shows the text you'd type in your Slack channel for each
command, followed by a brief description.

- ``queue.open()``: Tell folks that your user queue is ready to be used. Set it
  to empty to start.

- ``queue = []`` (or several other variations; see *queue_bot.py*): Empty the
  queue and show an emoji in their place to celebrate.

- ``queue.enqueue(@username)``: Add the given user to the queue and display
  the queue's current contents.

- ``queue.dequeue()``: Remove the next user from the queue and display the
  queue's current contents.

- ``queue.remove(@username)``: Remove the given user from the queue, wherever
  they are positioned, and display the queue's current contents.

That's it! Hope you enjoy your new Slack-based user queue assistant. 
