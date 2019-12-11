#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:14:24 2019

@author: samantha
"""

import os
import time
from textblob import TextBlob


def main():
    
    colours = ["\033[1;31;48m", # red
               "\033[1;32;48m", # green
               "\033[0;33;48m", # yellow
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
    
    time.sleep(3)
    
    print("%sI am a chatbot designed to help you with your feelings.%s\n" % (colours[6], colours[7]))
    
    time.sleep(3)
    
    ##################################################
    ################################################## NAME
    ##################################################
    
    path = os.path.dirname(__file__)+"/input/name.txt"
    path_file_name = open(path, "r")
    name = ""
    for n in path_file_name:
        name = n
    path_file_name.close()
    
    
    if len(name) == 0:
        print("This is our first time meeting.")
        
        name = input("What is your name?\t")
        name = name.lower()
        name = name.capitalize()
        
        with open(path, "w") as f:
            f.write("%s" % str(name)) 
        f.close()
        
        print("")
        print("Nice to meet you, %s%s%s." % (colours[4], name, colours[7]))
    else: 
        name = name.lower()
        print("Hello again, %s%s%s." % (colours[4], name.capitalize(), colours[7]))
    
    time.sleep(2)
    
    ##################################################
    ################################################## EMOTION ANALYSIS
    ##################################################
    
    print("\n###########################\n")
    
    sad = ("%ssad%s" % (colours[3],colours[7]))
    happy = ("%shappy%s" % (colours[1],colours[7]))
    unsure = ("%sunsure%s" % (colours[4],colours[7]))
    
    print("Setting up...")
    
    path = os.path.dirname(__file__)+"/input/emotion.txt"
    path_file_emotion = open(path, "r")
    emotion = ""
    for e in path_file_emotion:
        emotion = e.lower().strip()
    path_file_emotion.close()
    
    time.sleep(3)
    
    if len(emotion) == 0:
        print("I look forward to our adventure!")
    else: 
        print("Welcome back!")
    
    time.sleep(2)
    
    old_emotion = emotion
    
    ################################################## FIRST MEET
    
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
        
        time.sleep(3)
        
        if sentiment < -0.2:
            emotion = "sad"
            print("My readings are telling me that you are %s" % sad)
            if "because" in text:
                pass
            else:
                print("I don't think you explained your feelings in full detail.")
                why = input("Why are you feeling %s: \t" % sad)
        elif sentiment > 0.2:
            emotion = "happy"
            print("My readings are telling me that you are %s" % happy)
            if "because" in text:
                pass
            else:
                print("I don't think you explained your feelings in full detail.")
                why = input("Why are you feeling %s: \t" % happy)
        else:
            emotion = "unsure"
            print("My readings are telling me that you are %s...or perhaps I could not fully read your emotions." % unsure) 
    
        time.sleep(3)
    
        print("\n")        
        if emotion == "sad":
            print("I am sorry to hear that you are %s" % sad)
            print("Maybe we can meet again soon to talk more!")
        elif emotion == "happy":
            print("I am glad to hear that you are %s" % happy)
            print("Maybe we can meet again soon to talk more!")
        elif emotion == "unsure":
            print("I apologise for not fully understanding your emotions. Maybe we can try again somtime in the future?")
        print("\n")
        
        time.sleep(2)
        
        print("That was a great first meeting! I am glad to have met you!")
        print("Come back tomorrow and we can have a nice chat!")
    
        with open(path, "w") as f:
            f.write("%s" % str(emotion)) 
        f.close()
        
        print("")
        time.sleep(10)
        print("")
        
        exit()
    
    ################################################## RETURNING
    
    elif emotion == "sad":
        print("I remember that the last time we spoke, you were feeling %s" % sad)
        r = input("Is this still the case? (yes/no)\t")
        if r == "yes":
            print("\nSorry to hear that.\n")
        elif r == "no":
            print("\nAh I would like to hear more!\n")
            emotion = "unsure"
            
    elif emotion == "happy":
        print("I remember that the last time we spoke, you were feeling %s" % happy)
        r = input("Is this still the case? (yes/no)\t")
        #while r != "yes" or r != "no":
        #    r = input("Sorry please repeat that: (yes/no)\t")
        if r == "yes":
            print("\nYay!\n")
        elif r == "no":
            print("\nSorry to hear that.\n")
            emotion = "unsure"
            
    elif emotion == "unsure":
        print("I remember that the last time we spoke, it wasn't clear how you were feeling, so lets talk!")
    
    
    time.sleep(5)
    
    ##################################################
    ################################################## TODAY IS A NEW DAY
    ##################################################
    
    today_emotion = emotion
    
    print("\n###########################\n")
    
    print("%sToday is a new day!%s" % (colours[6], colours[7]))
    
    
    text = input("%sTell me how you are feeling at the moment:%s \t" % (colours[6], colours[7]))
    text = text.lower()
    spare = text
    
    text = TextBlob(text)
    text = text.correct()
    #print(text.correct())
    
    org = str(text)
    if org == spare:
        pass
    else:
        print("I detected a minor spelling mistake - I am trying to fix that now!")
    
    ################################################## RESULTS
    
    emotion_statement = "My readings are telling me that you are"
    sad = ("%ssad%s" % (colours[3],colours[7]))
    happy = ("%shappy%s" % (colours[1],colours[7]))
    unsure = ("%sunsure%s" % (colours[4],colours[7]))
    
    emotion = text.sentiment.polarity
    
    if emotion < -0.2:
        emotion = "sad"
        print("\n%s: %s\n" % (emotion_statement, sad))
        if "because" in text:
            pass
        else:
            print("I don't think I computed that you explained why.")
            response = input("Why don't tell me why you are %s? \t" % sad)
    elif emotion > 0.2:
        emotion = "happy"
        print("\n%s: %s" % (emotion_statement, happy))
        if "because" in text:
            pass
        else:
            print("I don't think I computed that you explained why.")
            response = input("Why don't tell me why you are %s? \t" % happy)
    else:
        emotion = "unsure"
        print("\n%s: %s \t...perhaps I am not reading you fully." % (emotion_statement, unsure))
        response = input("Are you able to explain in more detail? \t")
      
    print("\n")
    time.sleep(3)
    now_emotion = emotion
      
    ################################################## ENDING
         
    if emotion == "sad":
        print("I am sorry to hear that you are %s" % sad)
        if old_emotion == "sad":
            print("Especially since you felt %s last time." % sad)
        elif old_emotion == "happy":
            print("Especially since you felt %s last time." % happy)
        print("Maybe we can meet again soon to talk more!")
    elif emotion == "happy":
        print("I am glad to hear that you are %s" % happy)
        if old_emotion == "sad":
            print("Especially since you felt %s last time." % sad)
        elif old_emotion == "happy":
            print("I am really happy for you!." % happy)
        print("Maybe we can meet again soon to talk more!")
    elif emotion == "unsure":
        print("I apologise for not fully understanding your emotions. Maybe we can try again somtime in the future?")
        if old_emotion == "sad":
            print("Perhaps being %s is better than being %s?" % (unsure, sad))
        elif old_emotion == "happy":
            print("Last time I felt like you were %s but now you are %s - sorry about that." % (happy, unsure))
    print("\n")
    
    time.sleep(2)
    
    print("Thank you for coming back for a chat!")
    print("Come back tomorrow!")
    
    with open(path, "w") as f:
        f.write("%s" % str(emotion)) 
    f.close()
    
    print("")
    time.sleep(10)
    print("")
    
    exit()



if __name__ == "__main__":
    main()   

