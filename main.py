# from playsound import playsound
import threading as thr
from endings import *
import easygui as eg
import os

assets = os.path.join(os.path.dirname(__file__), 'Assets')
chad_impo_path = os.path.join(assets, 'chadimpo.jpg')
jerma_sus_path = os.path.join(assets, 'jermasus.jpeg')
jerma2 = os.path.join(assets, 'jerma2.jpg')
jerma3 = os.path.join(assets, 'jerma3.jpg')
jerma4 = os.path.join(assets, 'jerma4.jpg')
preggo = os.path.join(assets, 'preggo.jpg')


on_menu = True
while on_menu:
    chc_menu = eg.buttonbox('What do ya wanna do', choices=['Play', 'Info', 'Exit'],)
    if chc_menu == 'Exit':
        raise 'User exited at menu'
    elif chc_menu == 'Info':
        eg.buttonbox('You are a crewmate and your color is Yellow. Your objective is to make it out alive. You are playing on Skeld with Blue, Red, and Cyan. There are a total of 9 endings. Will you make it out alive or will you die? Play to find out', choices=['Menu'])
    else:
        on_menu = False

is_playing = True
while is_playing:
    chc_main = eg.buttonbox('You have a task in medbay, and electrical, where do you go first?', choices=['Electrical', 'Medbay'])
    # Electrical
    if chc_main == 'Electrical':
        chc_noise = eg.buttonbox('You suddenly hear a noise in admin, do you investigate or ignore it and go to electrical?', choices=['Investigate', 'Ignore'])
        # Investigate
        if chc_noise == 'Investigate':
            eg.buttonbox('You walk into admin and what you see next shocks you........' , choices=['Continue'])
            chc_chadred = eg.buttonbox('You see the imposter standing next to the body! Do you report the body, run away, or try to convince the imposter not to kill you?', choices=['Report', 'Run', 'Convince'], image = chad_impo_path)
            # Report
            if chc_chadred == 'Report':
                # Get voted out ending #1
                if not voted_out():
                    is_playing = False
            # Run
            elif chc_chadred == 'Run':
                # Getting stabbed ending #2
                if not stabbed():
                    is_playing = False
            # Fuck
            elif chc_chadred == 'Convince':
                eg.buttonbox('In order to try and convince the chad imposter, you start gently carressing him and kissing his soft lips, but suddenly..........', choices=['Continue'])
                chc_betray = eg.buttonbox('Blue reports Cyan\'s body! Now you are on the voting screen, who will you vote? Will you vote blue, or betray your one true love and vote Red?', choices=['Vote Blue', 'Vote Red'])
                # Vote Blue
                if chc_betray == 'Vote Blue':
                    # Get pregnant ending #3
                    if not pregnant():
                        is_playing = False
                # Betray Red
                elif chc_betray == 'Vote Red':
                    # Kill missing red ending #4
                    if not betray():
                        is_playing = False
        elif chc_noise == 'Ignore':
            # Get voted out cz ignored ending #5
            if not voted_out_ignore():
                is_playing = False
    # Medbay
    elif chc_main == 'Medbay':
        eg.buttonbox('You start doing the medbay scan but in the middle of your scan, Blue reports Cyan\'s body. The following conversation ensues:', choices=['Continue'])
        chc_vote = red_blue_talk()
        # Vote Red
        if chc_vote == 'Red':
            # Vote Red when not fucking ending
            if not vote_red():
                is_playing = False 
        # Vote Blue    
        elif chc_vote == 'Blue':
            # Vote blue ending
            if not vote_blue():
                is_playing = False 
        # Skip
        else:
            # Skip
            eg.buttonbox('You choose to skip, and now its only you, Red, and Blue in Cafeteria. Red takes out his 6 inch knife as you let out a gasp. Now you all 3 are staring at each other, you know you are dead, you know you fucked up. But before he could harm either of you, something appears in the ship which shocks all 3 of you........', choices=['Continue'])
            eg.buttonbox('Its JERMA SUS!!', choices=['Continue'], image = jerma_sus_path)
            eg.buttonbox('He slowly sucks the life out of Red and Blue while you just watch, frozen by fear, unable to move', choices=['Continue'], image = jerma2)
            eg.buttonbox('He faces you and starts sucking the life out of you. You realise this is the end, this is how you die. You striggle to fight him but keep failing', choices=['Continue'], image = jerma3)
            chc_pill = eg.buttonbox('You can barely move anymore. Suddenly, a red pill appears behind SUS. Do you try and grab the red pill, or do you give up to your fate?', choices=['Give up', 'Try to grab the pill'], image = jerma4)
            # Give up
            if chc_pill == 'Give up':
                # Sus kill ending
                if not sus_kill():
                    is_playing = False
            # Take the pill
            else:
                # Da baby ending
                if not da_baby():
                    is_playing = False 


