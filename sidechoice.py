from time import *
from charclasses import *
from interface import *

# DEFINE SIDE CHOICE FUNCTION

def sidechoice(characters):

    player = characters[0]
    luke = characters[1]
    vincent = characters[2]
    elliot = characters[3]

    if player.clubpartner == luke:
        cafe_face = "img_cafe_luke.gif"

    elif player.clubpartner == elliot:
        cafe_face = "img_cafe_elliot.gif"

    if player.clubpartner != vincent: # as long as club partner is not vincent, run

        changeInterface(cafe_face, '''Today you both are feeling peckish after club,
and decide to drop by the nearby coffee shop
for a snack.''')

        changeInterface(cafe_face, '''"My treat today!
What can I get for you?"''')

        changeInterface("img_cafe.gif", '''"I'd like a..."

1. "Sausage, Egg and Cheese English Muffin, please!"

2. "Bacon, Egg and Cheese English Muffin, please!"''')

        sandwich = win.getKey() # get keyboard input

        # while not one of the 2 options, wait.
        while sandwich not in ['1', '2']:
                sandwich = win.getKey()

        # if one of 2 options, return string to game
        if sandwich == "1":
            sandwich = "1"
        elif sandwich == "2":
            sandwich = "2"
            
        #User picks SEC. 

        if sandwich == "1":

        #Add affection points for making the "right" choice according to Caitlin ;)

            player.clubpartner.addpoints(5)

            userInterface("img_cafe.gif", '''You get your sandwiches and take
a seat by the window.''')

            changeInterface("img_cafe.gif", '''You take a bite of your sandwich,
sigh and say, "Sausage, egg and cheese is
honestly the ultimate breakfast sandwich."''')

            changeInterface(cafe_face, '''"Right??? Truly. Like everything is
so essential. The sausage is the crux of the flavour,
and while the egg is almost tasteless, it provides
necessary moisture and texture. And cheese really
ties everything together."''')

            changeInterface(cafe_face, '''"Right! I got a egg and cheese by
accident once and I was so upset. I almost
wasted the sandwich. But without the sausage there
really is nothing worth eating."''')

            changeInterface(cafe_face, '''"I can understand why egg and cheese is thing
though, we do have to cater to vegetarians. One thing
I can’t wrap my head around, however, is people who
like BACON, egg and cheese."''')

            changeInterface(cafe_face, '''"Right?? I’ve got so many thoughts on that. Like
why? The sausage is perfect because it every bit
of sandwich and egg has some of it. With bacon, it’s
not uniform, there are holes. And it’s so easy to
accidentally pull out a whole slice of bacon when
you’re eating and be left with just egg and cheese."''')

            changeInterface(cafe_face, '''"It’s just… a faulty sandwich."''')

            changeInterface(cafe_face, '''"Agreed."''')

            changeInterface("img_cafe.gif", '''You and '''+ player.clubpartner.name + ''' sit
in comfortable silence eating your sandwiches.''')

            changeInterface("img_cafe.gif", '''It's nice.''')

        #User picks BEC.

        else:

            userInterface(cafe_face, '''"I think you’ll have to pay for your own
sandwich, it’s against my morals to pay for bacon,
egg and cheese," '''+ player.clubpartner.name + ''' says cheekily as they pay
for the order.''')

            changeInterface(cafe_face, '''"Why, do you have a thing against
bacon, egg and cheese?"''')

            changeInterface(cafe_face, '''"Yes, I do, in fact. But I like you enough...
so I guess I won’t end the friendship just yet." '''+ player.clubpartner.name + ''' grins,
but you can sense that they’re kinda serious.''')

            changeInterface(cafe_face, '''"You know what? I’ll treat you to bubble tea,
to make up for making you go against your morals."''')

            changeInterface(cafe_face, player.clubpartner.name + ''', while not upset in the first place,
immediately brightens up.''')

            changeInterface(cafe_face, '''"You’re the best!"''')
            
            changeInterface("img_cafe.gif", '''Food really is the way into someone’s heart.''')

        characters = [player, luke, vincent, elliot]
        return characters
    
    else:
        characters = [player, luke, vincent, elliot]
        return characters
