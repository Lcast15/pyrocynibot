#!/usr/bin/env python
import tweepy, threading, time, os
#from our keys module (keys.py), import the keys dictionary
from keys import keys

#Created by:
# _     _____   ___   _____ _____ __   _____ 	   ___  ____________  _____ 
#| |   /  __ \ / _ \ /  ___|_   _/  | |  ___|	  / _ \ | ___ \ ___ \/  ___|
#| |   | /  \// /_\ \\ `--.  | | `| | |___ \ 	 / /_\ \| |_/ / |_/ /\ `--. 
#| |   | |    |  _  | `--. \ | |  | |     \ \	 |  _  ||  __/|  __/  `--. \
#| |___| \__/\| | | |/\__/ / | | _| |_/\__/ /	 | | | || |   | |    /\__/ /
#\_____/\____/\_| |_/\____/  \_/ \___/\____/ 	 \_| |_/\_|   \_|    \____/                                                          
#
#Project Name:			PyrocyniBot
#Project Type:			Bot/Twitter
#Project URL:			https://apps.lcast15.com/pyrocynibot
#Project Resources:		https://twitter.com/PyrocyniBot
#
#Project Description:
#	PyrocyniBot is a simple Twitter bot that replies to tweets by certain people that Pyrocynical (YouTuber) is associated with.
#	Its main purpose is to reply with 'blunt' to those tweets, although is planned to be extended in future.
#
#Project Variable Names:
#	i# 		-	Instance Number.
#	IN 		-	Instance Number in number form.
#	twts 	-	Tweets list.
#	sn		-	The user it is replying too.
#	m		-	The text it is replying with.
#	iF		-	Instance Final, it is the last instance that restarts the script so it can loop.
#	iT		-	Instance Test, it is fairly self explanatory.
#	iS		-	Self reply
#	LTN		-	Last tweet number, the file name of the last replied tweet ID, so it doesnt spam someone with replys on older tweets.
#	LT		-	Actually 
#
#Instance Users:
#1 - Dolan Dark
#2 - Bamanboi
#3 - ImAlexx
#4 - NFKRZ
#5 - WarranHarper28
#6 - Zaptie
#7 - Brad Does Banter
#8 - Colossal is Crazy

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#start a loop, like Nightofv5, it will not be launched every 30 seconds, it will just stay launched looping
def i1():
	try:
		IN = '1'
		#open the file containing the last tweet ID in read only mode
		LT = open("last_tweet_" + IN, 'r')
		#turn the contents of that file into a interger so it can be compared later on
		FID = int(float(LT.read()))
		
		print("Instance ",IN," started! /n")

		twts = api.search(q="from:DolanDark")
	
		#list of specific strings we want to check for in Tweets
		#t = ['']

		for s in twts:
		#these lines check the specific string filter, which we dont want right now
		#	for i in t:
		#		if i == s.text:
			if s.id > FID and s.id != FID:
				sn = s.user.screen_name
				m = "@%s blunt" % (sn)
				s = api.update_status(m, s.id)
				#close the last tweet file we opened ages ago
				LT.close()
				#reopen that file we closed just now, but in write mode. !!!you cant use r+ before because that adds to the file, we want to overwrite the file!!!
				NLT = open("last_tweet_" + IN, 'w')
				NLT.write(str(s.id))
				NLT.close()
				print("Replied too ",sn," regarding their tweet '",s.id,"' \n")
			else:
				#close the file
				LT.close()
			
	except tweepy.error.TweepError as e:
		print("There's been an error in instance ",IN,"!")
		i2()
	i2()

def i2():
	try:
		IN = '2'
		LT = open("last_tweet_" + IN, 'r')
		FID = int(float(LT.read()))
		print("Instance ",IN," started!")
		twts = api.search(q="from:Bamanboi")
		#t = ['']
		for s in twts:
		#	for i in t:
		#		if i == s.text:
			if s.id > FID and s.id != FID:
				sn = s.user.screen_name
				m = "@%s blunt" % (sn)
				s = api.update_status(m, s.id)
				LT.close()
				NLT = open("last_tweet_" + IN, 'w')
				NLT.write(str(s.id))
				NLT.close()
				print("Replied too ",sn," regarding their tweet '",s.id,"' \n")
			else:
				LT.close()
	except tweepy.error.TweepError as e:
		print("There's been an error in instance ",IN,"!")
		i3()
	i3()
	
def i3():
	try:
		IN = '3'
		LT = open("last_tweet_" + IN, 'r')
		FID = int(float(LT.read()))
		print("Instance ",IN," started!")
		twts = api.search(q="from:ImAllexx")
		#t = ['']
		for s in twts:
		#	for i in t:
		#		if i == s.text:
			if s.id > FID and s.id != FID:
				sn = s.user.screen_name
				m = "@%s blunt" % (sn)
				s = api.update_status(m, s.id)
				LT.close()
				NLT = open("last_tweet_" + IN, 'w')
				NLT.write(str(s.id))
				NLT.close()
				print("Replied too ",sn," regarding their tweet '",s.id,"' \n")
			else:
				LT.close()
	except tweepy.error.TweepError as e:
		print("There's been an error in instance ",IN,"!")
		i4()
	i4()
	
def i4():
	try:
		IN = '4'
		LT = open("last_tweet_" + IN, 'r')
		FID = int(float(LT.read()))
		print("Instance ",IN," started!")
		twts = api.search(q="from:NFKRZAlt")
		#t = ['']
		for s in twts:
		#	for i in t:
		#		if i == s.text:
			if s.id > FID and s.id != FID:
				sn = s.user.screen_name
				m = "@%s blunt" % (sn)
				s = api.update_status(m, s.id)
				LT.close()
				NLT = open("last_tweet_" + IN, 'w')
				NLT.write(str(s.id))
				NLT.close()
				print("Replied too ",sn," regarding their tweet '",s.id,"' \n")
			else:
				LT.close()
	except tweepy.error.TweepError as e:
		print("There's been an error in instance ",IN,"!")
		i5()
	i5()
	
def i5():
	try:
		IN = '5'
		LT = open("last_tweet_" + IN, 'r')
		FID = int(float(LT.read()))
		print("Instance ",IN," started!")
		twts = api.search(q="from:warrenharper28")
		#t = ['']
		for s in twts:
		#	for i in t:
		#		if i == s.text:
			if s.id > FID and s.id != FID:
				sn = s.user.screen_name
				m = "@%s blunt" % (sn)
				s = api.update_status(m, s.id)
				LT.close()
				NLT = open("last_tweet_" + IN, 'w')
				NLT.write(str(s.id))
				NLT.close()
				print("Replied too ",sn," regarding their tweet '",s.id,"' \n")
			else:
				LT.close()
	except tweepy.error.TweepError as e:
		print("There's been an error in instance ",IN,"!")
		i6()
	i6()

def i6():
	try:
		IN = '6'
		LT = open("last_tweet_" + IN, 'r')
		FID = int(float(LT.read()))
		print("Instance ",IN," started!")
		twts = api.search(q="from:Zaptie")
		#t = ['']
		for s in twts:
		#	for i in t:
		#		if i == s.text:
			if s.id > FID and s.id != FID:
				sn = s.user.screen_name
				m = "@%s blunt" % (sn)
				s = api.update_status(m, s.id)
				LT.close()
				NLT = open("last_tweet_" + IN, 'w')
				NLT.write(str(s.id))
				NLT.close()
				print("Replied too ",sn," regarding their tweet '",s.id,"' \n")
			else:
				LT.close()
	except tweepy.error.TweepError as e:
		print("There's been an error in instance ",IN,"!")
		i7()
	i7()

def i7():
	try:
		IN = '7'
		LT = open("last_tweet_" + IN, 'r')
		FID = int(float(LT.read()))
		print("Instance ",IN," started!")
		twts = api.search(q="from:BradDontBanter")
		#t = ['']
		for s in twts:
		#	for i in t:
		#		if i == s.text:
			if s.id > FID and s.id != FID:
				sn = s.user.screen_name
				m = "@%s blunt" % (sn)
				s = api.update_status(m, s.id)
				LT.close()
				NLT = open("last_tweet_" + IN, 'w')
				NLT.write(str(s.id))
				NLT.close()
				print("Replied too ",sn," regarding their tweet '",s.id,"' \n")
			else:
				LT.close()
	except tweepy.error.TweepError as e:
		print("There's been an error in instance ",IN,"!")
		i8()
	i8()
	
def i8():
	try:
		IN = '8'
		LT = open("last_tweet_" + IN, 'r')
		FID = int(float(LT.read()))
		print("Instance ",IN," started!")
		twts = api.search(q="from:ColossalisCrazy")
		#t = ['']
		for s in twts:
		#	for i in t:
		#		if i == s.text:
			if s.id > FID and s.id != FID:
				sn = s.user.screen_name
				m = "@%s blunt" % (sn)
				s = api.update_status(m, s.id)
				LT.close()
				NLT = open("last_tweet_" + IN, 'w')
				NLT.write(str(s.id))
				NLT.close()
				print("Replied too ",sn," regarding their tweet '",s.id,"' \n")
			else:
				LT.close()
	except tweepy.error.TweepError as e:
		print("There's been an error in instance ",IN,"!")
		iS()
	iS()
	
def iF():
	IN = 'Final'
	print("Instance ",IN," started! This means the script has completed! Restarting soon!")
	#so we dont stress our server or suspend our own twitter account
	time.sleep(300)
	i1()

def iS():
	try:
		IN = 'S'
		LT = open("last_tweet_" + IN, 'r')
		FID = int(float(LT.read()))
		print("Instance ",IN," started!")
		twts = api.search(q="to:pyrocynibot")
		#t = ['']
		for s in twts:
		#	for i in t:
		#		if i == s.text:
			if s.id > FID and s.id != FID:
				sn = s.user.screen_name
				m = "@%s blunt" % (sn)
				s = api.update_status(m, s.id)
				LT.close()
				NLT = open("last_tweet_" + IN, 'w')
				NLT.write(str(s.id))
				NLT.close()
				print("Replied too ",sn," regarding their tweet '",s.id,"' \n")
			else:
				LT.close()
	except tweepy.error.TweepError as e:
		print("There's been an error in instance ",IN,"!")
		iF()
	iF()

def iT():
	IN = 'Test'
	SID = int(float(819087548802662400))
	LT = open("last_tweet_" + IN, 'r')
	FID = int(float(LT.read()))
	print (FID)
	if SID > FID:
		print("This would be replied too")
		File.close()
		NFile = open(LTN, 'w')
		NFile.write(str(sid))
		NFile.close()
	else:
		print("This wouldn't be replied too")


# goto loop start
iF()	