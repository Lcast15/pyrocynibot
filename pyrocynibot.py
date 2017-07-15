#!/usr/bin/env python
import twitter, os, json
from random import randint

ConsumerKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ConsumerSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
AccessToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
AccessTokenSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
PyroAccount = 'xxxxxxxxxxxxxxxxxx'

API = twitter.Api(consumer_key=ConsumerKey, consumer_secret=ConsumerSecret, access_token_key=AccessToken, access_token_secret=AccessTokenSecret)

def RandMeme():
	MemeList = [(False, 'blunt lol'), (False, 'lol'), (False, 'blunt'), (False, 'nama jeff'), (False, 'new upload on pyrozella in 5 minutes'), (False, 'memes'), (False, 'try not to laugh cringe'), (False, 'hey hows it going bros my nama pewdieepie'), (False, 'stay away from me'), (False, 'dolan dark but he doesnt make memes'), (False, 'my name jeff'), (False, 'my name is jeff'), (False, 'leafy is here'), (False, 'fidget spinner'), (False, 'i am lesbian lol'), (False, 'youtube is dead'), (False, 'my channel is dead'), (False, 'at least im not leafy'), (False, 'weed'), (True, 'trump.jpg'), (True, 'bye.png'), (True, 'robmyrotten.jpg'), (True, 'fat.jpg'), (True, 'trumpo.gif'), (True, 'killme.gif'), (True, 'howdareyou.gif'), (True, 'hair.gif'), (True, 'memes.gif'), (True, 'timbs.gif'), (True, 'clap.gif'), (True, 'flashback.gif'), (True, 'case.gif'), (True, 'style.gif'), (True, 'stomedy.gif'), (True, 'scarce.jpg'), (True, 'house.gif'), (True, 'no.gif'), (True, 'content.gif')]
	return MemeList[randint(0, len(MemeList) - 1)]

if __name__ == '__main__':
	print('Initialized!')
	for i in API.GetStreamFilter(follow=[PyroAccount]):
		Data = json.loads(json.dumps(i))
		try:
			if Data['user']['id_str'] != PyroAccount:
				pass
			else:
				RandomMeme = RandMeme()
				if RandomMeme[0]:
					API.PostMedia('@' + Data['user']['screen_name'] + ' ', os.getcwd() + '\memes\\' + RandomMeme[1], in_reply_to_status_id=int(Data['id']))
					print('TRIGGERED! image ID=' + str(int(Data['id'])))
				else:
					Content= '@' + Data['user']['screen_name'] + ' ' + RandomMeme[1]
					API.PostUpdate(Content, in_reply_to_status_id=int(Data['id']))
					print('TRIGGERED! non image ID=' + str(int(Data['id'])))
		except Exception as e:
			print('Something went wrong.')
			print(Data)
			print(str(e))
		