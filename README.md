Rebooster - A bot for boosting specific tags in Fediverse Apps
==============================================================

Rebooster is an easy-to-use bot written in Python3 by [Lambda@mescl.in](https://mescl.in/Lambda) that you can use to boost Mastodon, Pleroma, and other Fediverse content tagged with specific tags. 


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


![Rebooster running in Windows](https://github.com/Lambdanaut/Rebooster/blob/master/screenshots/jonathanpiresbot.png)
