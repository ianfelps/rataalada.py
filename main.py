# rataalada.com

import os
import time
import random
import webbrowser

def rataaladaW():

    #riddles
    class riddle:
        def __init__(self, question, answer):
            self.question = question
            self.answer = answer
        def __repr__(self):
            return '{'+ self.question +', '+ self.answer +'}'

    qriddle = [
        riddle(">>  UNDERNEATH THE BRIDGE THE TARP HAS SPRUNG A LEAK. IT'S OKAY TO EAT THE FISH BECAUSE THEY DON'T HAVE ANY... WHAT?", "FEELINGS"),
        riddle(">>  THOSE WHO MAKE ME ARE LIKELY TO BREAK ME.", "LAWS"),
        riddle(">>  THE MORE I'M REVEALED, THE LESS I EXIST.", "SECRET"),
        riddle(">>  I'M GREEK. I'M LATIN. I'M 500 YEARS OLD. I SPEAK IN RIDDLES. WHAT AM I?", "ENIGMA"),
        riddle(">>  IT SINKS ANS SWIMS. IT CAN BE ROTTEN, EVEN WHEN IT'S ALL DRESSED UP.", "ICEBERG"),
        riddle(">>  WITHOUT A DOUBT GOTHAM'S ELITE LIVE HERE, BETWEEN LIGHT AND DARKNESS.", "SHADOWS"),
        riddle(">>  FEAR HE WHO HIDES BEHIND ME.", "MASK"),
        riddle(">>  WHAT'S BLACK AND BLUE AND DEAD ALL OVER?", "BATMAN"),
        riddle(">>  IT'S NOT A JOKE, BUT SOMETIMES YOU NEED TO SHOUT IT TWICE TO REALLY MEAN IT.", "HA"),
        riddle(">>  TO WIT: A WILD CAR IN THE TRUEST SENSE.", "JOKER")
    ] 

    hitList = [">>  YOU'RE SMATER THAN I THOUGHT YOU WOULD BE. TRY THIS NEXT RIDDLE.", ">>  A CORRECT ANSWER LEADS YOU CLOSER TO FULFILLMENT. NOW, HERE'S ONE MORE RIDDLE.", ">>  YOU'RE ONE OF THE SMARTE ONES. NEXT."]
    errorList = [">>  IF YOU WANT REAL POWER, YOU NEED TO KNOW THE TRUTH. TRY AGAIN.", ">>  YOU SEARCH FOR THE RIGHT ANSWERS, BUT YOU NEED TO LOOK DEEPER.", ">>  POWER HAS CORRUPTED YOU, AND YOUR ANSWER. THINK A LITTLE HARDER."]

    errors = 0
    hits = 0

    #login
    os.system('cls')
    time.sleep(1)
    print(">>  TRACEROUTE RATAALADA.COM")
    time.sleep(1)
    print("    POS-0-3-0-0-CR01. ARKHAM.GOTHAMDATA.NET	     [27.05.19.39]")
    time.sleep(0.5)
    print("    TBR2.N54GHTM.IP.GOTHAMISP2.NET	             [01.03.19.40]")
    time.sleep(0.5)
    print("    CR2.N54GTHM.IP. GOTHAMISP2.NET	             [58.12.19.41]")
    time.sleep(0.5)
    print("    CR2.GTHMX.IP.GOTHAMISP2.NET	                     [140.10.19.48]")
    time.sleep(0.5)
    print("    CR1.GTHMX.IP.GOTHAMISP2.NET	                     [405.03.19.87]")
    time.sleep(0.5)
    print("    CR3.GTHMX.IP.GOTHAMISP3.NET	                     [16.04.19.43]")
    time.sleep(0.5)
    print("    CORRECTIONS. ARKHAM.GOV	                     [258.10.19.74]")
    time.sleep(0.5)
    print("    03.04.20.22	                                     [03.04.20.22]")
    time.sleep(1)
    print(">>  REROUTING...")
    time.sleep(1)
    print(">>  SSH UPSTANDING-CITIZEN@RATAALADA.COM")

    time.sleep(3)
    os.system('cls')

    #riddles

    time.sleep(1)
    print(">>  I'VE BEEN EXPECTING YOU. WANT TO PLAY A GAME?")
    time.sleep(1)
    print(">>  PROCEED? [Y/N]")
    start = input()

    if start in ("Y", "y"):
        time.sleep(1)
        print(">>  IT'S MORE THAN JUST A GAME. ANSWER RIGHT, AND JUSTICE WILL BE YOUR REWARD.")
        time.sleep(1)
    else:
        time.sleep(1)
        print(">>  FAREWELL. WE'LL TRY TO PLAY ANOTHER TIME.")
        time.sleep(1)
        print(">>  BYE-BYE <?>")
        time.sleep(3)
        exit()

    for riddle in qriddle:
        time.sleep(2)
        print(f"{(riddle.question)}")
        userInput = input()
        time.sleep(1)

        if (userInput.lower() == riddle.answer.lower()):
            hits = hits + 1
            print(f"{random.choice(hitList)}")
        else:
            print(f"{random.choice(errorList)}")
            errors = errors + 1
            if errors == 3:
                time.sleep(1)
                print(">>  HOW WILL GOTHAM BE SAVED WITH ANSWER LIKE THAT?")
                time.sleep(1)
                print(">>  BYE-BYE <?>")
                time.sleep(3)
                exit()

    if hits == 10:
        time.sleep(1)
        os.system('cls')
        time.sleep(1)
        print(">>  YOU HAVE SOLVED ALL MY RIDDLES. AND NOW THE TRUTH IS REVEALED.")
        time.sleep(1)
        print(">>  WHILE YOU UNMASK EVERYTHING THAT HAS YET TO BE REVEALED, I'M SAFE HERE. WITH MY NEW FRIEND. WE WILL SEE YOU SOON.")
        time.sleep(1)
        print(">>  BYE-BYE <?>")
        time.sleep(1)
        webbrowser.open('https://drive.google.com/file/d/1Xgfa4jBMUZIXvLUhRG85wZw21pTdapST/view?usp=share_link')
        time.sleep(5)
        exit()
    else:
        time.sleep(1)
        os.system('cls')
        time.sleep(1)
        print(">>  STOP GUESSING AND START THINKING. TRY ANOTHER TIME.")
        time.sleep(1)
        print(">>  BYE-BYE <?>")
        time.sleep(3)
        exit()

rataaladaW()

# comando executavel
# pyinstaller --onefile /document