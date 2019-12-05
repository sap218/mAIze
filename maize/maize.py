#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:14:24 2019

@author: samantha
"""

import os
from textblob import TextBlob

colours = ["\033[1;31;48m", # red
           "\033[1;32;48m", # green
           "\033[1;33;48m", # yellow
           "\033[1;34;48m", # blue
           "\033[1;35;48m", # pink
           #"\033[1;36;40m", # cyan - can;t use this! CYANNOTATOR DOES!
           "\033[1;37;40m", # white on black
           "\033[1;30;48m", # black on white
           "\033[0;30;48m" # plain
           ] # bold (1/0) / colour / background (40 black background)

##################################################
################################################## INTRODUCTION
##################################################

opening_statement = "Hello, I am maize. I hope to be an aMAIZEing support system for you."
print("\n%s%s%s" % (colours[2], opening_statement, colours[7]))

print("%sI am an AI chatbot designed to help you with your feelings.%s\n" % (colours[6], colours[7]))

##################################################
################################################## NAME
##################################################

path = os.path.dirname(__file__)+"/input/name.txt"
path_file = open(path, "r")
name = ""
for n in path_file:
    name = n
path_file.close()


if len(name) == 0:
    print("This is our first time meeting.")
    print("I look forward to our adventure!")
    
    name = input("What is your name?\t")
    name = name.lower()
    name = name.capitalize()
    
    with open(path, "w") as f:
        f.write("%s" % str(name)) 
    f.close()
    
    print("")
    print("Nice to meet you, %s%s%s." % (colours[4], name, colours[7]))
    print("")
else: 
    name = name.lower()
    print("Hello again, %s%s%s." % (colours[4], name.capitalize(), colours[7]))


print("")


##################################################
################################################## EMOTION ANALYSIS
##################################################

sad = ("%ssad%s" % (colours[3],colours[7]))
happy = ("%shappy%s" % (colours[1],colours[7]))
unsure = ("%sunsure%s" % (colours[4],colours[7]))

print("\nSetting up...\n")

path = os.path.dirname(__file__)+"/input/emotion.txt"
path_file = open(path, "r")
emotion = ""
for e in path_file:
    emotion = e.lower().strip()
path_file.close()








if len(emotion) == 0:
    text = input("%sTell me how you are feeling at the moment:%s \t" % (colours[6], colours[7]))
    text = text.lower()
    spare = text
    
    text = TextBlob(text)
    text = text.correct()
    org = str(text)
    if org == spare:
        pass
    else:
        print("I detected a minor spelling mistake - I am trying to fix that now!")
        
    sentiment = text.sentiment.polarity
    if sentiment < -0.2:
        emotion = "sad"
    elif sentiment > 0.2:
        emotion = "happy"
    else:
        emotion = "unsure"
    




elif emotion == "sad":
    print("I remember that the last time we spoke, you were feeling %s" % sad)
    r = input("Is this still the case? (yes/no)\t")
    if r == "yes":
        pass
    elif r == "no":
        emotion = "unsure"
        
elif emotion == "happy":
    print("I remember that the last time we spoke, you were feeling %s" % happy)
    r = input("Is this still the case? (yes/no)\t")
    #while r != "yes" or r != "no":
    #    r = input("Sorry please repeat that: (yes/no)\t")
    if r == "yes":
        pass
    elif r == "no":
        emotion = "unsure"
        
elif emotion == "unsure":
    print("I remember that the last time we spoke, it wasn't clear how you were feeling, so lets talk!")

















'''

text = ("I am feeelING sad")
#text = input("%sTell me how you are feeling at the moment:%s \t" % (colours[6], colours[7]))
spare = (text.lower())+"."
text = text.lower()

if text.endswith("."):
    pass
else:
    text = text+"."

##################################################

text = TextBlob(text)
text = text.correct()
#print(text.correct())

org = str(text)
if org == spare:
    pass
else:
    #pass
    print("I detected a minor spelling mistake - I am trying to fix that now!")
#print(spare)
#print(text)
'''
##################################################
'''
emotion_statement = "My readings are telling me that you are"
sad = ("%ssad%s" % (colours[3],colours[7]))
happy = ("%shappy%s" % (colours[1],colours[7]))
unsure = ("%sunsure%s" % (colours[4],colours[7]))

# https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
#subjectivitiy = text.sentiment.subjectivity
emotion = text.sentiment.polarity

if emotion < -0.2:
    print("\n%s: %s\n" % (emotion_statement, sad))
    if "because" in text:
        pass
    else:
        print("I don't think I computed that you explained why")
        response = input("Why don't tell me why you are %s? \t" % sad)
elif emotion > 0.2:
    print("\n%s: %s" % (emotion_statement, happy))
    if "because" in text:
        pass
    else:
        print("I don't think I computed that you explained why")
        response = input("Why don't tell me why you are %s? \t" % happy)
else:
    print("\n%s: %s \t...perhaps I am not reading you fully." % (emotion_statement, unsure))
    response = input("Are you able to explain in more detail? \t")
  
print("\n")
'''





