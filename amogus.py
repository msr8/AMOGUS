# from playsound import playsound
import threading as thr
import requests as rq
import platform as pf
import getpass as gp
import easygui as eg
import os

def red_blue_talk():
    temp = eg.buttonbox('''You: Where?
Blue: Admin, I saw Red coming from there, I am dead sure he killed him
Red: That's straight cap, I saw Blue kill IN FRONT OF ME but he reported the body as soon as he saw me
Blue: Bruh stop lying, I saw you running from the body and you started chasing me 
* Blue votes Red *
* Red Votes Blue *

Whom will you vote?''', choices=['Red', 'Blue', 'Skip'])
    return temp

def download_image(url, path):
    with open(path, 'wb') as f:
        f.write( rq.get(url, allow_redirects=False).content )

def get_user():
    try:
        ret = gp.getuser()
    except:
        try:
            if pf.system() == 'Darwin':
                temp_list = os.getcwd().split('/')
            elif pf.system() == 'Windows':
                temp_list = os.getcwd().split('\\')
            ret = temp_list [temp_list.index('Users') + 1]
        except:
            try:
                if pf.system() == 'Darwin':
                    temp_list = __file__.split('/')
                elif pf.system() == 'Windows':
                    temp_list = __file__.split('\\')
                ret = temp_list [temp_list.index('Users') + 1]
            except:
                ret = 'Unable to determine'
    return ret





def voted_out():
    again = False
    eg.buttonbox('You report the body and the following conversation ensues:', choices=['Continue'])
    eg.buttonbox('''You: I saw Red kill in admin
Red: Na fam, it wasn't me
You: I swear to god it was him, I was going to electrical while I heard a kill sound and when I went there, Red was standing beside the body
* You vote Red *
* Red votes you *
Blue: I mean, Red, I last saw you in admin with Cyan and you were also faking the card swipe even though we have wires as our common task
Red: Ughhhh fine, I admit its me, BUT Blue do you remember that nude I sent you?
Blue: *blushing* Yes I do senpai
Red: I am gonna show you everything in person right now if you vote Yellow
Blue: Okay! Sounds like a good enough deal to me UwU
*Blue votes you*''', choices=['Continue'])
    eg.buttonbox('You realise you lost, its over. The dread spreads across your face as you gets ejected from the crewship. You take one last look at the crewship and you see Red and Blue making out, and you close your eyes for one last time as a tear falls out of your eye while you dissolve into nothingness', choices=['Continue'])
    chc_again = eg.buttonbox('''
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄

You got ending #1 - Getting voted out
Do you want to play again or exit?''', choices=['Play again', 'Exit'])
    if chc_again == 'Play again':
        again = True
    return again



def stabbed():
    again = False
    eg.buttonbox('Seeing the imposter with the dead body, you panic and start running. But as you are running...........', choices=['Continue'])
    eg.buttonbox('You feel a sudden pain in your back, like somebody stabbed you. You feel the blood oozing from your back as you slowly fall down and lose your consciousness', choices=['Continue'])
    chc_again = eg.buttonbox('''
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄

You got ending #2 - Getting stabbed
Do you want to play again or exit?''', choices=['Play again', 'Exit'])
    if chc_again == 'Play again':
        again = True
    return again



def pregnant():
    again = False
    eg.buttonbox('You vote Blue and so does Red, and Blue gets ejected out. Its now only Red and you left. Due to your makeout session before, Red doesnt kill you', choices=['Continue'])
    eg.buttonbox('You marry Red and he impregnates you and live happily ever after with the love of your life', choices=['continue'], image = preggo)
    chc_again = eg.buttonbox('''
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄

You got ending #3 - Marrying red (aka the best ending)
Do you want to play again or exit?''', choices=['Play again', 'Exit'])
    if chc_again == 'Play again':
        again = True
    return again    



def betray():
    again = False
    eg.buttonbox('You vote Red and get him ejected. The look on his face when he realised you used him, crushed you from inside but you knew what you did was for the best', choices=['Continue'])
    eg.buttonbox('Although you win the game, as time passes, you start feeling worse and worse. The lonliness comes creeping back and the guilt that you killed one of only people who cared for you. This continues until the pain becomes too much for you to handle and you hang yourself in an attempt to reunite and see your one true love once again', choices=['Continue'], image = pepe)
    chc_again = eg.buttonbox('''
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄

You got ending #4 - Killing yourself to reunite with Red
Do you want to play again or exit?''', choices=['Play again', 'Exit'])
    if chc_again == 'Play again':
        again = True
    return again 



def voted_out_ignore():
    again = False
    eg.buttonbox('As you are running to electrical, you see Blue pass by you in storage coming from electrical and 10 seconds later.......', choices=['Continue'])
    eg.buttonbox('Blue reports Cyan dead body, and the following conversation ensues:', choices=['Continue'])
    eg.buttonbox('''You: Where?
Blue: Admin, I saw Yellow coming from there
Yellow: But I came from cafetaria and I didn't even go into Admin ;-;
Red: Thats heavy cap, I left Yellow with Cyan in Admin and Yellow was also faking the admin swipe even though we have wires as our common task
Blue: That's right, I think we all know who the imposter is here
*Blue votes you*
*Red votes you*
You: B-Bu ''', choices=['Continue'])
    eg.buttonbox('Before you know it, the voting time is over and you are being ejected out of the crewship', choices=['Continue'])
    eg.buttonbox('You are numb, all you can feel is disbelief, on how easy it was to get you ejected out. You take one last look at the ship and you see blue panicking and red smiling menacingly. This is the last thing you see before finally closing your eyes and embracing your fate', choices=['Continue'])
    chc_again = eg.buttonbox('''
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄

You got ending #5 - Getting voted out
Do you want to play again or exit?''', choices=['Play again', 'Exit'])
    if chc_again == 'Play again':
        again = True
    return again 



def vote_red():
    again = False
    eg.buttonbox('You vote Red and you watch him as he gets ejected from the ship. It feels like someone has slowed down time, and Red was......',choices=['Continue'])
    eg.buttonbox('the Imposter! You win and are appreciated by your friends for making the right decision :)', choices=['Continue'])
    chc_again = eg.buttonbox('''
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄

    You got ending #6 - Getting Red voted out
    Do you want to play again or exit?''', choices=['Play again', 'Exit'])
    if chc_again == 'Play again':
        again = True
    return again 



def vote_blue():
    again = False
    eg.buttonbox('You vote Blue and you watch him as he gets ejected from the ship. It feels like someone has slowed down time, and Blue was......',choices=['Continue'])
    eg.buttonbox('not the imposter! You suddenly feel an immense sense of dread and you know its over, you lost, you fucked up', choices=['Continue'])
    eg.buttonbox('You look red in the eye as he takes out his 6 inch knife and he stabs you in the abdomen', choices=['Continue'])
    eg.buttonbox('You feel the blood leaking out of you as you slowly lose conciousness and your soul dissolves into nothingness', choices=['Continue'])
    chc_again = eg.buttonbox('''
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄

    You got ending #7 - Getting stabbed cause you voted wrong
    Do you want to play again or exit?''', choices=['Play again', 'Exit'])
    if chc_again == 'Play again':
        again = True
    return again 



def sus_kill():
    again = False
    eg.buttonbox('You close your eyes, and relax yourself as your soul dissolves into nothingness', choices=['Continue'])
    chc_again = eg.buttonbox('''
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄

    You got ending #8 - Getting your soul eaten
    Do you want to play again or exit?''', choices=['Play again', 'Exit'])
    if chc_again == 'Play again':
        again = True
    return again 



def da_baby():
    again = False
    eg.buttonbox('You grab the pill, but it doesn\'t do anything, and you just slip into nothingness. But.......', choices=['Continue'])
    eg.buttonbox('you feel, not bad. Is this what death feels like? Even the pain is vanishing now. It hits you, that you aren\'t dead. You open your eyes and what you see shocks you. Its........', choices=['Continue'])
    eg.buttonbox('DA BABY!!', choices=['Continue'], image = da_baby_img)
    eg.buttonbox('Somehow, the pill summoned Da Baby to help you', choices=['Continue'])
    eg.buttonbox('Suddenly, Da Baby turns into a convertible!', choices=['Continue'], image = da_baby_convertible)
    eg.buttonbox('Da baby convertible attacks Sus and defeats him!', choices=['Continue'], image = jermadying)
    eg.buttonbox('He says his signature "Less go" before finally vanishing away to save another crewmate from the Jerma Sus monster', choices=['Continue'])
    chc_again = eg.buttonbox('''
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄

    You got ending #9 - Getting saved by Da Baby
    Do you want to play again or exit?''', choices=['Play again', 'Exit'])
    if chc_again == 'Play again':
        again = True
    return again 








usr = get_user()
if pf.system() == 'Windows':
    assets = f'C:\\Users\\{usr}\\AppData\\Local\\AMOGUS\\Assets'
else:
    assets = f'/Users/{usr}/Library/Application Support/AMOGUS/Assets'

if not os.path.exists(assets):
    os.makedirs(assets)

chad_impo_link = 'https://i.imgur.com/jzlk041.png'
jerma_sus_link = 'https://i.imgur.com/OGniaSq.png'
jerma2_link = 'https://i.imgur.com/7mfPAu8.png'
jerma3_link = 'https://i.imgur.com/bYyLotP.png'
jerma4_link = 'https://i.imgur.com/2C8H4Zy.png'
preggo_link = 'https://i.imgur.com/41WADDP.png'
pepe_link = 'https://i.imgur.com/i6HaYau.png'
da_baby_img_link = 'https://i.imgur.com/4kbUyQG.png' 
da_baby_convertible_link = 'https://i.imgur.com/bCzjvNH.png'
jermadying_link = 'https://i.imgur.com/2CM9bUj.png'

chad_impo = os.path.join(assets, 'chadimpo.png')
jerma_sus = os.path.join(assets, 'jermasus.png')
jerma2 = os.path.join(assets, 'jerma2.png')
jerma3 = os.path.join(assets, 'jerma3.png')
jerma4 = os.path.join(assets, 'jerma4.png')
preggo = os.path.join(assets, 'preggo.png')
pepe = os.path.join(assets, 'pepe.png')
da_baby_img = os.path.join(assets, 'dababy.png')                            # Did da_baby_img cz da_baby is a func
da_baby_convertible = os.path.join(assets, 'dababy_convertible.png')
jermadying = os.path.join(assets, 'jermadying.png')

assets_list = [ [chad_impo_link,chad_impo] , [jerma_sus_link,jerma_sus] , [jerma2_link,jerma2] , [jerma3_link,jerma3] , [jerma4_link,jerma4] , [preggo_link,preggo] , [pepe_link,pepe] , [da_baby_img_link,da_baby_img] , [da_baby_convertible_link,da_baby_convertible] , [jermadying_link,jermadying] ]
for url, path in assets_list:
    download_image(url, path)

on_menu = True
while on_menu:
    chc_menu = eg.buttonbox('What do ya wanna do', choices=['Play', 'Info', 'Exit'],)
    if chc_menu == 'Exit':
        raise 'User exited at menu'
    elif chc_menu == 'Info':
        eg.buttonbox('You are a crewmate and your color is Yellow. Your objective is to make it out alive. You are playing on Skeld with Blue, Red, and Cyan. However there is an imposter among you who is trying to kill all of you. There are a total of 9 endings, in which 6 are bad, while 3 are good. Will you survive? or will you be a victim to the imposter? Play to find out!', choices=['Menu'])
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
            chc_chadred = eg.buttonbox('You see the imposter standing next to the body! Do you report the body, run away, or try to convince the imposter not to kill you?', choices=['Report', 'Run', 'Convince'], image = chad_impo)
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
            eg.buttonbox('Its JERMA SUS!!', choices=['Continue'], image = jerma_sus)
            eg.buttonbox('He slowly sucks the life out of Red and Blue while you just watch, frozen by fear, unable to move', choices=['Continue'], image = jerma2)
            eg.buttonbox('He faces you and starts sucking the life out of you. You realise this is the end, this is how you die. You struggle to fight him but keep failing', choices=['Continue'], image = jerma3)
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


