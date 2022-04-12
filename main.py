from rich import print as printf
import easygui as eg

from script import ENDING_1, ENDING_2, ENDING_3, ENDING_4, ENDING_5, ENDING_6, ENDING_7, ENDING_8, ENDING_9, HELP_TEXT





logchc = lambda node, chc:    printf(f'[grey50][b][{node}][/] {chc}[/]')





def home():
    chc = eg.buttonbox('What do ya wanna do', choices=['Play', 'Info', 'Exit'], title='Home')
    logchc('HOME', chc)
    if chc == 'Play':      node1()
    elif chc == 'Info':    info()

def info():
    chc = eg.buttonbox(HELP_TEXT, choices=['Home'], title='Info')
    logchc('INFO', chc)
    if chc == 'Home':    home()

def node1():
    chc = eg.buttonbox('You have a task in medbay, and electrical, where do you go first?', choices=['Electrical', 'Medbay'], title='Node 1')
    logchc('NODE 1', chc)
    if chc == 'Electrical':    node2()
    elif chc == 'Medbay':      node10()

def node2():
    chc = eg.buttonbox('You suddenly hear a noise in admin, do you investigate or ignore it and go to electrical?', choices=['Investigate', 'Ignore'], title='Node 2')
    logchc('NODE 2', chc)
    if chc == 'Investigate':    node3()
    elif chc == 'Ignore':       node9()

def node3():
    chc = eg.buttonbox('You walk into admin and what you see next shocks you........' , choices=['Continue'], title='Node 3')
    if not chc:              exit()
    chc = eg.buttonbox('You see the imposter standing next to the body! Do you report the body, run away, or try to convince the imposter not to kill you?', choices=['Report', 'Run', 'Convince'], title='Node 3')
    logchc('NODE 3', chc)
    if chc == 'Report':      node4()
    if chc == 'Run':         node5()
    if chc == 'Convince':    node6()

def node4():
    for i in ENDING_1[:-1]:
        chc = eg.buttonbox(i, choices=['Continue'], title='Node 4')
        if not chc:    exit()
    chc = eg.buttonbox(ENDING_1[-1], choices=['Home', 'Play Again', 'Exit'], title='Node 4')
    logchc('NODE 4', chc)
    if chc == 'Home':            home()
    elif chc == 'Play Again':    node1()

def node5():
    for i in ENDING_2[:-1]:
        chc = eg.buttonbox(i, choices=['Continue'], title='Node 5')
        if not chc:    exit()
    chc = eg.buttonbox(ENDING_2[-1], choices=['Home', 'Play Again', 'Exit'], title='Node 5')
    logchc('NODE 5', chc)
    if chc == 'Home':            home()
    elif chc == 'Play Again':    node1()

def node6():
    chc = eg.buttonbox('In order to try and convince the chad imposter, you start gently carressing him and kissing his soft lips, but suddenly..........', choices=['Continue'], title='Node 6')
    if not chc:              exit()
    chc = eg.buttonbox('Blue reports Cyan\'s body! Now you are on the voting screen, who will you vote? Will you vote blue, or betray your one true love and vote Red?', choices=['Vote Blue', 'Vote Red'], title='Node6')
    logchc('NODE 6', chc)
    if chc == 'Vote Blue':      node7()
    elif chc == 'Vote Red':     node8()

def node7():
    for i in ENDING_3[:-1]:
        chc = eg.buttonbox(i, choices=['Continue'], title='Node 7')
        if not chc:    exit()
    chc = eg.buttonbox(ENDING_3[-1], choices=['Home', 'Play Again', 'Exit'], title='Node 7')
    logchc('NODE 7', chc)
    if chc == 'Home':            home()
    elif chc == 'Play Again':    node1()

def node8():
    for i in ENDING_4[:-1]:
        chc = eg.buttonbox(i, choices=['Continue'], title='Node 8')
        if not chc:    exit()
    chc = eg.buttonbox(ENDING_4[-1], choices=['Home', 'Play Again', 'Exit'], title='Node 8')
    logchc('NODE 8', chc)
    if chc == 'Home':            home()
    elif chc == 'Play Again':    node1()

def node9():
    for i in ENDING_5[:-1]:
        chc = eg.buttonbox(i, choices=['Continue'], title='Node 9')
        if not chc:    exit()
    chc = eg.buttonbox(ENDING_5[-1], choices=['Home', 'Play Again', 'Exit'], title='Node 9')
    logchc('NODE 9', chc)
    if chc == 'Home':            home()
    elif chc == 'Play Again':    node1()

def node10():
    chc =  eg.buttonbox('You start doing the medbay scan but in the middle of your scan, Blue reports Cyan\'s body. The following conversation ensues:', choices=['Continue'], title='Node 10')
    if not chc:              exit()
    chc = eg.buttonbox('''You: Where?
Blue: Admin, I saw Red coming from there, I am dead sure he killed him
Red: That's straight cap, I saw Blue kill IN FRONT OF ME but he reported the body as soon as he saw me
Blue: Bruh stop lying, I saw you running from the body and you started chasing me 
* Blue votes Red *
* Red Votes Blue *
Whom will you vote?''', choices=['Red', 'Blue', 'Skip'], title='Node 10')
    logchc('NODE 10', chc)
    if chc == 'Red':      node11()
    elif chc == 'Blue':   node12()
    elif chc == 'Skip':   node13()

def node11():
    for i in ENDING_6[:-1]:
        chc = eg.buttonbox(i, choices=['Continue'], title='Node 11')
        if not chc:    exit()
    chc = eg.buttonbox(ENDING_6[-1], choices=['Home', 'Play Again', 'Exit'], title='Node 11')
    logchc('NODE 11', chc)
    if chc == 'Home':            home()
    elif chc == 'Play Again':    node1()

def node12():
    for i in ENDING_7[:-1]:
        chc = eg.buttonbox(i, choices=['Continue'], title='Node 12')
        if not chc:    exit()
    chc = eg.buttonbox(ENDING_7[-1], choices=['Home', 'Play Again', 'Exit'], title='Node 12')
    logchc('NODE 12', chc)
    if chc == 'Home':            home()
    elif chc == 'Play Again':    node1()

def node13():
    chc = eg.buttonbox('You choose to skip, and now its only you, Red, and Blue in Cafeteria. Red takes out his 6 inch knife as you let out a gasp. Now you all 3 \
are staring at each other, you know you are dead, you know you fucked up. But before he could harm either of you, something appears in the ship which shocks all \
3 of you........', choices=['Continue'], title='Node 13')
    if not chc:              exit()
    chc = eg.buttonbox('Its JERMA SUS!!', choices=['Continue'], title='Node 13')
    if not chc:              exit()
    chc = eg.buttonbox('He slowly sucks the life out of Red and Blue while you just watch, frozen by fear, unable to move', choices=['Continue'], title='Node 13')
    if not chc:              exit()
    chc = eg.buttonbox('He faces you and starts sucking the life out of you. You realise this is the end, this is how you die. You struggle to fight him but keep \
failing', choices=['Continue'], title='Node 13')
    chc = eg.buttonbox('You can barely move anymore. Suddenly, a red pill appears behind SUS. Do you try and grab the red pill, or do you give up to your fate?',
choices=['Give up', 'Try to grab the pill'], title='Node 13')
    logchc('NODE 13', chc)
    if chc == 'Give up':      node14()
    elif chc == 'Try to grab the pill':     node15()

def node14():
    for i in ENDING_8[:-1]:
        chc = eg.buttonbox(i, choices=['Continue'], title='Node 14')
        if not chc:    exit()
    chc = eg.buttonbox(ENDING_8[-1], choices=['Home', 'Play Again', 'Exit'], title='Node 14')
    logchc('NODE 14', chc)
    if chc == 'Home':            home()
    elif chc == 'Play Again':    node1()

def node15():
    for i in ENDING_9[:-1]:
        chc = eg.buttonbox(i, choices=['Continue'], title='Node 15')
        if not chc:    exit()
    chc = eg.buttonbox(ENDING_9[-1], choices=['Home', 'Play Again', 'Exit'], title='Node 15')
    logchc('NODE 15', chc)
    if chc == 'Home':            home()
    elif chc == 'Play Again':    node1()
    










home()



'''
-> Images
-> Sounds
-> Tkinter
-> Ending func
'''

'''
Script:

Electrical or medbay?               (n1)
  |_ Electrical                     (n2)
  |   |_ Investigate                (n3)
  |   |   |_ Report end(1)          (n4)
  |   |   |_ Run end(2)             (n5)
  |   |   |_ Convince               (n6)
  |   |       |_ Voteblue end(3)    (n7)
  |   |       |_ Votered end(4)     (n8)
  |   |_ Ignore end(5)              (n9)
  |_ Medbay                         (n10)
      |_ Red end(6)                 (n11)
      |_ Blue end(7)                (n12)
      |_ Skip                       (n13)
        |_ Giveup end(8)            (n14)
        |_ Grabpill end(9)          (n15)


'''

