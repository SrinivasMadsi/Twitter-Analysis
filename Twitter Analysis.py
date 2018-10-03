# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 01:36:53 2018

@author: Srinivas
"""

from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt


def percentage(part,whole):
    return (100*float(part)/float(whole))

consumerKey = "g7mwEGkVbVC25WjjBK9tV0LI4"
consumerSecret = "501KHUUGe95SUw41izCIRjcYFVxLJmMsW1tk07zJaaFwnWzS8i"
accessToken = "1159965804-E3KJKCc9LF1PqL7MXSLtjperkIilaeK2Ll3q21y"
accessTokenSecret = "eopl9rMZ7jM6waYYuht8IGng14nQBTqrLcjSOJXkTca8h"

#For establishing connection
auth = tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

#Taking inputs from user

searchTerm = input("Enter keyword/Hashtag to search:")
noOfSearchTerms = int(input("Enter how many tweets you wanna analyse:"))
tweets = tweepy.Cursor(api.search,q=searchTerm).items(noOfSearchTerms)

positive =0
negative = 0
neutral =0
polarity = 0


for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    
    if(analysis.sentiment.polarity == 0 ):
        neutral += 1
    elif(analysis.sentiment.polarity > 0.00):
        positive += 1
    elif(analysis.sentiment.polarity < 0.00):
         negative += 1
         
     
positive = percentage(positive,noOfSearchTerms)
negative = percentage(negative,noOfSearchTerms)
neutral = percentage(neutral,noOfSearchTerms)
polarity = percentage(polarity,noOfSearchTerms)



positive = format(positive, '.2f')
neutral = format(neutral,'.2f')
negative = format(negative,'.2f')


print("How  people are reacting on "+searchTerm+ "by analyzing" + str(noOfSearchTerms)+"Tweets.") 


if(polarity ==0):
    print("Neutral")
elif(polarity < 0 ):
    print("Negative")
elif(polarity > 0):
    print("Positive")    

#Pictorial representation of the analysis using  Piechart
    
labels = ['Positive['+str(positive)+'%]','Neutral['+str(neutral)+'%]','Negative['+str(negative)+'%]']
sizes = [positive,neutral,negative]
colors = ['yellowgreen','gold','red']
patches,texts = plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc='best')
plt.title("How people are reacting on "+searchTerm+"by analyzing"+ str(noOfSearchTerms)+"Tweets")
plt.axis('equal')
plt.tight_layout()
plt.show() 
  
    
    