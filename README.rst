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

#. Download files from this repo

#. Create a virtual environment: ``virtualenv env``

#. Activate your virtual environment: ``source env/bin/activate``

#. Install all requirements: ``pip install -r requirements.txt``

#. Put your API key into your shell environment. I suggest adding it to a
   file called *secrets.sh* and adding this ``export`` line:

   .. parsed-literal::

       export BOT_API_TOKEN="xoxb-245937039254-BP7YPA3y3fePTfOBv7qNO26z"

   Now, you can export your variable into the environment like this:

   .. code-block:: bash

        source secrets.sh

#. With your secrets sourced and your environment activated, run *queue_bot.py*

#. Send queue messages!


Available Commands
==================

[WIP]