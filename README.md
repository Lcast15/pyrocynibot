## Project Details

* **Name:**			PyrocyniBot
* **Type:**			Bot/Twitter
* **URL:**			https://apps.lcast15.com/PyrocyniBot
* **Links:**		https://twitter.com/PyrocyniBot
* **Language:**		Python 3.7

## Project Description

PyrocyniBot is a simple Twitter bot that replies to tweets by Pyrocynical (internet sensation) with a random meme inspired or taken from him (or her).

## How To Use

### 1. **Install Libraries Required**
 > pip install python-twitter
### 2. Create a Twitter App, If You Haven't Already
 Follow steps 1 & 2 of [this tutorial from Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app). Disregard the other steps, we don't use them in this bot.
### 3. **Config the Bot**
 Open *pyrocynibot.py* in a text editor and change these variables to your own apps settings:
```
ConsumerKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ConsumerSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
AccessToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
AccessTokenSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```
 Now, go to [tweeterid.com](https://tweeterid.com/) and type the target account’s Twitter handle. We require that you do not abuse this to target and harass people.
 > Please note we have left Pyrocynical's Twitter ID blank for a reason. Do not use this bot on anyone who has not approved of it.
 Then, use that ID the website gave you and paste it in here:
```
PyroAccount = 'xxxxxxxxxxxxxxxxxx'
```
### 4. **Start the Bot**
 By this point, the bot should run just fine. If you have an issue that isn't a config issue, please either contact me or use the issues feature on GitHub.

## Required Libraries

* [python-twitter](https://github.com/bear/python-twitter)
