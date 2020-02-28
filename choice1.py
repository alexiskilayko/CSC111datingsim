from time import *
from charclasses import *
from interface import *

# DEFINE CHOICE 1 FUNCTION ---------------------------------

def choice1(characters):

    player = characters[0]
    luke = characters[1]
    vincent = characters[2]
    elliot = characters[3]

    # Ask user what elective they want.

    changeInterface("img_class.gif", '''She hands out the slips to sign up.
Which elective will you choose?

1. Robotics
2. Art''')

    elective = win.getKey() # get keyboard input

    # while not one of the 2 options, wait.
    while elective not in ['1', '2']:
            elective = win.getKey()

    # if one of 2 options, return string to game
    if elective == "1":
        elective = "1"
    elif elective == "2":
        elective = "2"

    # User chooses elective 1, Robotics.

    if elective == "1":

        player.elective = 'Robotics' # Append to player's self.elective trait.

        luke.addpoints(1)
        elliot.addpoints(1)

        # Dialogue

        userInterface("img_class.gif", '''You write down Robotics. You
wonder if anyone you'll know will be there.''')
        
        changeInterface("img_class.gif", '''Turns out both Luke and Elliot
are in Robotics with you. That's exciting!''')

        changeInterface("img_class.gif", '''The teacher wants everyone to
pair up for the final projects. Luke wants
to prototype a dancing bot, that he wants
to use to impress the kids he works with at
the Pocket Money fund. Elliot wants to create
a grammar checker that also checks tone.''')

        # Ask user who they want as partner.

        changeInterface("img_class.gif", '''They both offer to partner up with
you. Who would you like to work with?

1. Luke
2. Elliot''')

        partner = win.getKey() # get keyboard input

        # while not one of the 2 options, wait.
        while partner not in ['1', '2']:
                partner = win.getKey()

        # if one of 2 options, return string to game
        if partner == "1":
            partner = "1"
        elif partner == "2":
            partner = "2"
    
        # User chooses Luke.

        if partner == "1":

            player.electivepartner = luke # luke is made your partner

            luke.addpoints(1)

            # Dialogue

            userInterface("img_class.gif", '''"Hey Luke, can I join you? I really want
to help you out with the Pocket Money fund.
You're so passionate about it."''')

            changeInterface("img_class_luke.gif", '''"That would be great! I would love to team up.
This will be so great!! The kids will really love
you too!! And we can go for runs between the
project when we meet up!!"''')

            changeInterface("img_class_luke.gif", '''He blushes, "Sorry, I got really excited.
I guess I'm really excited to have the chance to
spend more time with you."''')

            changeInterface("img_class_luke.gif", '''Now that made me blush. "No no, I'm glad
you are so excited to spend time with me. The
feeling's mutual."''')

            changeInterface("img_class_luke.gif", '''His face lights up. "Great! Are you free
tomorrow morning? Let's get to school early, and
we can go for a run before homeroom."''')

            changeInterface("img_class_luke.gif", '''You don't know about waking up early just
for a run, but his excitement is contagious, and
you're really looking forward to this project
now.''')
            
        # User chooses Elliot.

        else:

            player.electivepartner = elliot # replacing list

            elliot.addpoints(1)

            # Dialogue

            userInterface("img_class.gif", '''"Elliot! Can I join you? I would love to help
you with your project. I really feel for not
knowing how to email teachers ever, whether my tone
is right or whatnot. I absolutely know that this
project is going to be awesome."''')

            changeInterface("img_class_elliot.gif", '''"That would be great! I think we'd make a
great team! Yeah honestly, I feel. It's always
so tough with the newspapers too, each section of
the newspaper has like a different writing style like
you do a front page news thing, you know?"''')

            changeInterface("img_class.gif", '''You guys nerd it out with words and impact,
it's really really nice actually.''')


        # Dialogue continues.

        changeInterface("img_class.gif", '''Working on the project was nice. It's very easy
being in ''' + player.electivepartner.name + ''''s presence. Conversation is
easy, but also not necessary. It's comfortable and
just... nice spending time with ''' + player.electivepartner.name +'''.''')
        
    # User chooses elective 2, Art.

    else:

        player.elective = "Art" # Change to player's self.elective trait.

        player.electivepartner = vincent

        vincent.addpoints(2)
        

        # Dialogue.

        userInterface("img_class_vincent.gif", '''Vincent gives you a smile when he sees you at
the back of the art room. You can’t stop the
butterflies in your stomach when he sits next to
you.''')

        changeInterface("img_class_vincent.gif", '''Today, the teacher had you guys work on still
life, a crushed can. It’s nice, working next to
each other in silence. You can really tell when
Vincent’s focusing - his brows furrow, his lips
purse, but most of all, there’s a sense of purpose
in his eyes, his whole demeanor shifts, and
frankly, it’s pretty amazing.''')
        
    # Dialogue continues.

    changeInterface("img_class.gif", '''Class is over too quick, and you're not
really looking forward to Pre-Calc.''')

    changeInterface("img_black.gif", '''Electives quickly become one of your
favourite parts of the day. It’s nice to spend
time with ''' + player.electivepartner.name + '''.''')

    characters = [player, luke, vincent, elliot]

    return characters

