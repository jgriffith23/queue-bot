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

First, follow these instructions to be able to run the code:

#. Download files from this repo

#. Create a virtual environment: ``virtualenv env``

#. Activate your virtual environment: ``source env/bin/activate``

#. Install all requirements: ``pip install -r requirements.txt``

#. Put your API key into your shell environment. I suggest adding it to a
   file called *secrets.sh* and adding this ``export`` line:

   .. parsed-literal::

       export BOT_API_TOKEN="a-really-long-thing-that-is-your-bot-token"

   Now, you can export your variable into the environment like this:

   .. code-block:: bash

        source secrets.sh

   Just be sure to add *secrets.sh* to your *.gitignore* file to keep your
   secrets off the Internet!

#. With your secrets sourced and your environment activated, run *queue_bot.py*

To integrate a custom bot with your Slack team, do the following:

#. 

#. In the Slack team where you want to 


Available Commands
==================

[WIP]