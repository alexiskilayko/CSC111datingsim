from graphics import *

win = GraphWin("Forever in this Moment", 1000, 500)

def userInterface(bg, text):

    # draw background
    bg = Image(Point(500, 250), bg)
    bg.draw(win)

    # draw text window
    textwin = Image(Point(500, 400), "img_textwin.gif")
    textwin.draw(win)

    # draw text
    dialogue = Text(Point(500, 400), text)
    dialogue.setFace("courier")
    dialogue.setSize(11)
    dialogue.draw(win)

def changeInterface(bg, text):

    while True:
        userSpace = win.getKey()
        if userSpace == "space":
            userInterface(bg, text)
            break
