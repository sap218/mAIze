#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:14:24 2019

@author: samantha
"""

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

opening_statement = "Hello, I am maize. And you are amazing / aMAIZEing."
print("\n%s%s%s" % (colours[2], opening_statement, colours[7]))

print("%sI am an AI chatbot designed to help you with your feelings.%s\n" % (colours[6], colours[7]))

##################################################

#text = "I am feeling sad"
text = input("%sTell me how you are feeling right now:%s \t" % (colours[6], colours[7]))
spare = text+".".lower()
text = text.lower()

if text.endswith("."):
    pass
else:
    text = text+"."

##################################################

text = TextBlob(text)
text = text.correct()
#print(text.correct())

if str(text) == spare:
    pass
else:
    print("I detected a minor spelling mistake - I am trying to fix that now!")
#print(spare)
#print(text)

##################################################

emotion_statement = "My readings are telling me that you are"
sad = ("%ssad%s" % (colours[3],colours[7]))
happy = ("%shappy%s" % (colours[1],colours[7]))
unsure = ("%sunsure%s" % (colours[4],colours[7]))

# https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
#subjectivitiy = text.sentiment.subjectivity
emotion = text.sentiment.polarity

if emotion < -0.2:
    print("\n%s: %s" % (emotion_statement, sad))
elif emotion > 0.2:
    print("\n%s: %s" % (emotion_statement, happy))
else:
    print("\n%s: %s \t...perhaps I am not reading you fully." % (emotion_statement, unsure))
  
print("\n")


