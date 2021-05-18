import easygui as eg
import os

assets = os.path.join(os.path.dirname(__file__), 'Assets')
preggo = os.path.join(assets, 'preggo.jpg')
pepe = os.path.join(assets, 'pepe.png')
da_baby_img = os.path.join(assets, 'dababy.png')
da_baby_convertible = os.path.join(assets, 'dababy_convertible.jpeg')
jermadying = os.path.join(assets, 'jermadying.jpg')


def red_blue_talk():
    temp = eg.buttonbox('''You: Where?
Blue: Admin, I saw Red coming from there, I am dead sure he killed him
Red: That's straight cap, I saw Blue kill IN FRONT OF ME but he reported the body as soon as he saw it
Blue: Bruh stop lying, I saw you running from the body and you started chasing me 
* Blue votes Red *
* Red Votes Blue *

Whom will you vote?''', choices=['Red', 'Blue', 'Skip'])
    return temp






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



