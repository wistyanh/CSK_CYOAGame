import time
import sys
import random
from art import *

#global variables
global activity
activity = ""
global friendsNames
friendsNames = ""
global solo
solo = False

#Functions
def slowType(msg):
    for letter in msg:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)
    print('')

def superSlowType(msg):
    for letter in msg:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.5)
    print('')

def medType(msg):
    for letter in msg:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0045)
    print('')

def friendsResponse(answer, activity):
    act = activity
    if answer.lower() == "y":
        slowType("Awesome! Who would you like to invite?")
        #friendsNames = input()
        doActivity(act, input(), False)
    elif answer.lower() == "n":
        slowType("We stan an independent person who can relax by themself!")
        #solo = True
        doActivity(act, friendsNames, True)
    else:
        slowType("Sorry I didn't quite get that, could you type y/n?")
        friendsResponse(input())

def secChoice(answer):
    if answer.lower() == "shopping":
        activity = "shopping"
        slowType("Great! Would you like to invite your friends? (y/n)")
        friendsResponse(input(), activity)
    elif answer.lower() == "hiking":
        activity = "hiking"
        slowType("Great! Would you like to invite your friends? (y/n)")
        friendsResponse(input(), activity)
    else:
        slowType("Sorry I didn't quite get that, could you type 'shopping' or 'hiking'?")
        secChoice(input())

def doActivity(activity, friendsNames, solo):
    if activity == "beach":
        if solo == False:
            slowType("After a fun day at the beach with your friends, " + friendsNames + ", you all decide to get some food on the way home! What would you like to eat?")
            food = input()
            slowType("Oh yum good choice! As you were in line to get some delicious " + food + ", you stumbled across a, rather cute (｡◕‿‿◕｡),")
            superSlowType("...")
            slowType(" stranger who asked if you wanted to join them in a game of hangman. Do you accept their offer? (y/n)")
            hangman(input())
        else:
            slowType("After a fun day at the beach, you decide to get some food on the way home! What would you like to eat?")
            food = input()
            slowType("Oh yum good choice! As you were in line to get some delicious " + food + ", you stumbled across a, rather cute (｡◕‿‿◕｡),")
            superSlowType("...")
            slowType(" stranger who asked if you wanted to join them in a game of hangman. Do you accept their offer? (y/n)")
            hangman(input())
    elif activity == "shopping":
        if solo == False:
            slowType("After shopping with your friends, " + friendsNames + ", you all decide to get some food on the way home! What would you like to eat?")
            food = input()
            slowType("Oh yum good choice! As you were in line to get some delicious " + food + ", you stumbled across a, rather cute (｡◕‿‿◕｡),")
            superSlowType("...")
            slowType(" stranger who asked if you wanted to join them in a game of hangman. Do you accept their offer? (y/n)")
            hangman(input())
        else:
            slowType("After a fun day of shopping, you decide to get some food on the way home! What would you like to eat?")
            food = input()
            slowType("Oh yum good choice! As you were in line to get some delicious " + food + ", you stumbled across a, rather cute (｡◕‿‿◕｡),")
            superSlowType("...")
            slowType(" stranger who asked if you wanted to join them in a game of hangman. Do you accept their offer? (y/n)")
            hangman(input())
    elif activity == "hiking":
        if solo == False:
            slowType("After hiking with your friends, " + friendsNames + ", you all decide to get some food on the way home! What would you like to eat?")
            food = input()
            slowType("Oh yum good choice! As you were in line to get some delicious " + food + ", you stumbled across a, rather cute (｡◕‿‿◕｡),")
            superSlowType("...")
            slowType(" stranger who asked if you wanted to join them in a game of hangman. Do you accept their offer? (y/n)")
            hangman(input())
        else:
            slowType("After a fun day of hiking, you decide to get some food on the way home! What would you like to eat?")
            food = input()
            slowType("Oh yum good choice! As you were in line to get some delicious " + food + ", you stumbled across a, rather cute (｡◕‿‿◕｡),")
            superSlowType("...")
            slowType(" stranger who asked if you wanted to join them in a game of hangman. Do you accept their offer? (y/n)")
            hangman(input())

def hangman(answer):
    if answer.lower() == "y":
        #hangman game that I coded summer 2019

        potential_words = ["rawr", "cutie", "cs kickstart", "berkeley"]        #can change to liking
        word = random.choice(potential_words)       #randomly chooses an element from the list
        word = word.lower()     #ensures word is always in lowercase
        print(word)

        easyword = []
        current_word = []
        maxfails = 6            #can change to liking
        fails = 0               #starting fails

        for letter in word:
            easyword.append(str(letter))        #makes an empty space for each letter in the word

        for letter in word:
            current_word.append("_")            #replaces empty space with "_"


        while fails < maxfails:
            print(current_word)
            guess=input('Guess a letter: ')
            guess = guess.lower()           #ensures guess is always in lowercase

            def numberOfTries(fails):
                if fails == 0:
                    print("You guessed the word correctly in 1 try!")
                    ending()
                elif (fails + 1) > 1:
                    print("You guessed the word correctly and have " + str(totalFails - 1) + " tries left!")
                    ending()

            if guess.isnumeric():              #ensures user's guess isn't a number
                print("Type a lower case letter please!")
            elif guess == word:
                print("Congratulations!")
                numberOfTries(fails)
                break
            elif guess in word:
                for i in range(len(word)):
                    if guess== word[i]:
                        current_word[i] = guess
                if current_word == easyword:
                    print("Congratulations!")
                    numberOfTries(fails)
                    break
            else:
                fails += 1
                totalFails = maxfails - fails
                print("Try again! You have " + str(totalFails) + " tries left.")

    elif answer.lower() == "n":
        slowType("That's too bad, sorry stranger!")
        ending()
    else:
        slowType("Sorry I didn't quite get that, could you type 'shopping' or 'hiking'?")
        hangman(input())

def ending():
    slowType("Well it's been a long day so you should take a shower and get some sleep! I hope you had a fun day! If you did make sure to follow me on Instagram @wistyanh ( ͡° ͜ʖ ͡ -)")
    time.sleep(5)

#beginning
header = text2art("Summer 2020")
medType(header)
slowType("(if covid didn't happen)")
superSlowType("...")
print(r"""                             \
                               ._ o o
                               \_`-)|_
                            ,""       \
                          ,"  ## |   ಠ ಠ.
                        ," ##   ,-\__    `.
                      ,"       /     `--._;)
                    ,"     ## /
                  ,"   ##    /

                     TA DA!

            """)
time.sleep(0.85)

slowType("Type your name to begin: ")
name = input()

print (r"""
            ⊂_ヽ
            　＼＼ Good
            　 ＼( ͡° ͜ʖ ͡°)
            　　　 >　⌒ヽ
            　　　/ 　 へ＼
            　　 /　　/　＼ Morning
            　　 ﾚ　ノ　　 ヽ_つ
            　　/　/
            　 /　/|
            　(　(ヽ           """ + name + """
            　|　|、 ＼
            　| 丿 ＼ ⌒)
            　| |　　) /
             ノ )　　Lﾉ
            (_/
        """)
time.sleep(0.85)
slowType("It's a beautiful summer day in Southern California where covid doesn't exist:) \
School starts in a couple of weeks so let's enjoy your last summer as a kid! \
A great perk of living in SoCal is that you have easy access to the beach! Would you like to have a beach trip? (y/n)")
beachResponse = input()

if beachResponse == "y":
    activity = "beach"
    slowType("Great! Would you like to invite your friends? (y/n)")
    friendsResponse(input(), activity)
elif beachResponse == "n":
    slowType("That's alright! Would you rather go shopping or hiking?")
    secChoice(input())
else:
    slowType("Sorry I didn't quite get that, could you type y/n?")
    beachResponse == input()
