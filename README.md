Rebooster - A bot for boosting specific tags in Mastodon
==========================================================

Rebooster is an easy-to-use bot written in Python3 by [Lambdanaut@mastodon.gamedev.place](https://mastodon.gamedev.place/@Lambdanaut) that you can use to boost Mastodon content tagged with specific tags. 


How to install and run it
-------------------------

* [Download](https://github.com/Lambdanaut/Rebooster/archive/master.zip) the latest version of Rebooster
* Extract the zipped file
* Ensure that [Python3](https://www.python.org/) and pip3 are both installed. 
* In a terminal, navigate to the project root and install the dependencies by running `pip3 install -r requirements.txt`
* Rename the `config_example.py` file to `config.py` 
* Edit `config.py` to have your bot's Mastodon credentials, and fill out the tags you would like to boost
* Run the bot with `python3 rebooster.py`
* Check out your bot's feed. It should be boosting any new toots with your specified hashtags.
