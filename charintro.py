from time import *
from charclasses import *
from interface import *

# DEFINE CHARACTER INTRODUCTIONS ---------------------------------
    
def charIntro():

    # opening screen ---------------------------------

    bg = Image(Point(500, 250), "openscreen.gif")
    bg.draw(win)

    # INTRO dialogue ---------------------------------

    changeInterface("img_black.gif", '''"Be good, OK? I know it’s tough starting
at a new school senior year, but try to enjoy it."''')

    changeInterface("img_black.gif", '"Don’t worry, Mom… I’ll be fine."')

    changeInterface("img_black.gif", '''It’s the first day of senior year and
also your first day at your new school,
Timberline High School.''')

    changeInterface("img_black.gif", '''NEW SCHOOL, NEW ME, MAYBE I'LL FIND "THE ONE"!''')

    # MEETING LUKE dialogue ---------------------------------

    changeInterface("img_street.gif", '''You get on the bus, and just as the bus is
about to leave…''')

    changeInterface("img_street.gif", '''You see a boy dashing madly toward the bus.
Wow, he’s fast.''')

    changeInterface("img_street.gif", '''"WAIT. I think that guy wants to board."''')

    changeInterface("img_street_luke.gif", '''He makes it. He's tall, with short brown
hair and dark eyes. He looks like he could be
intimidating, but he's actually kinda cute, even
with the sweat dripping down his forehead.''')

    changeInterface("img_street_luke.gif", '''"Omigod, thank you so much. I couldn’t be
late on my first day back. I’ve got to keep my
record clean if I want Coach to let me participate
in next month’s meet."''')

    changeInterface("img_street_luke.gif", '''"Meet? What meet?"''')

    changeInterface("img_street_luke.gif", '''"This month the track team is organising a
run-a-thon for the School Pocket Money fund, to
provide lunch for lower income students in the city.''')
    changeInterface("img_street_luke.gif", '''I really love all the kids, so I’m really excited
to have the track team do this. Do you run? Oh yeah,
I’ve never seen you around before, which is weird
considering we get on at the same stop, are you new?
I’m Luke! How about you?"
(Answer in Python console)''')

    # Ask player for name.
    name = input("What's your name? ENTER NAME: ").title().strip()
    print()
    print('To continue, return to game window and press spacebar.')
    print()
    player = Player(name) # Define Player object.

    userInterface("img_street_luke.gif", '''"I'm ''' + player.name +''', and..."''')

    # Ask player response.
    changeInterface("img_street.gif", '''Do you like running?
 
1. YES
2. NO

(select a number)''')

    ########## I want to make getting keyboard input into a function
    ########## but i haven't figured it out...

    choice1 = win.getKey() # get keyboard input

    # while not one of the 2 options, wait (get another key)
    while choice1 not in ['1', '2']:
        choice1 = win.getKey()

    # if one of 2 options, return string to game
    if choice1 == "1":
        choice1 = "1"
    elif choice1 == "2":
        choice1 = "2"

    # Player says yes.
    if choice1 == "1":

        luke.addpoints(2) # Luke likes you more by 2

        userInterface("img_street_luke.gif", '''"Yes, I love running!"''')

        changeInterface("img_street_luke.gif", '''"You should join us! There are lots of people
coming and the track team is really awesome! It’ll
be a great way to make friends! And since we live
close to each other we could go running together to
train some time!"''')

    # Player says no.
    else:

        luke.addpoints(1) # Luke likes you more by 1

        userInterface("img_street_luke.gif", '''"No, but I’d love to help out with the run-a-thon,
may I?"''')

        changeInterface("img_street_luke.gif", '''"Well you could sponsor me, haha. And if you’re up
for it, you could still run with us! Everyone on the
track team is real cool and would love for another member.
We take runners of all levels. And since we live so close
to each other, we could go running together some time.
It’ll be fun!"''')

    # Resume dialogue.
    changeInterface("img_street_luke.gif", '''"I’d love to, it’ll be fun!!"''')

    changeInterface("img_street.gif", '''The bus pulls into the parking lot.
You’ve reached school.''')

    changeInterface("img_street_luke.gif", '''"Great! It’s a date then! I’ll see you
around, I’ve got to get to training."''')

    changeInterface("img_street.gif", '''And he was gone as fast as he appeared.''')

    # MEETING VINCENT dialogue ---------------------------------
    
    changeInterface("img_hall.gif", '''OK, you’ve got things to do, like finding
your locker and then homeroom, so let’s
get to it!!!''')

    changeInterface("img_hall.gif", '''You finally find your locker... on
the third floor. Just as you’re trying to
stuff your books into your locker, the
bell rings.''')

    changeInterface("img_hall.gif", '''You’re shocked, and you drop your bag.
You were SURE you had at least half an hour
before class started.''')

    changeInterface("img_hall.gif", '''"Don’t worry about it, that bell means you’ve
got half an hour till homeroom."''')

    changeInterface("img_hall_vincent.gif", '''Someone’s helping you gather your papers.
He's about your height, with dark black,
almost blue, hair and black eyes. He's got
earphones in so you wonder if he can hear you
thank him.''')

    changeInterface("img_hall_vincent.gif", '''He take his earphones out. "Here you go."
It’s your papers.''')

    changeInterface("img_hall_vincent.gif", '''"Thank you so much! I’m '''+ player.name + ''' by the way,
what’s your name?"''')

    changeInterface("img_hall_vincent.gif", '''"Oh. I’m Vincent. Nice to meet you."''')

    changeInterface("img_hall_vincent.gif", '''Silence. This is kinda awkward. Quick.
Say something.''')

    # Ask player response.

    changeInterface("img_hall_vincent.gif", '''What should you say?

1. "I’m new here. It’s kinda overwhelming,
so thank you for helping me."

2. "Ooh, I noticed your headphones, what
are you listening to right now?"''')

    choice2 = win.getKey() # get keyboard input

    # while not one of the 2 options, wait.
    while choice2 not in ['1', '2']:
        choice2 = win.getKey()

    # if one of 2 options, return string to game
    if choice2 == "1":
        choice2 = "1"
    elif choice2 == "2":
        choice2 = "2"

    # Player chooses 1st response.
    if choice2 == "1":

        vincent.addpoints(1) # Vincent's affection for you grows by 1
        
        userInterface("img_hall_vincent.gif", '''"I’m new here. It’s kinda overwhelming,
so thank you for helping me."''')

        changeInterface("img_hall_vincent.gif", '''"No problem. Let me know if you need
any help settling in. I was new last year,
so I know how it feels. See you around."''')

    # Player chooses 2nd response.
    else:

        vincent.addpoints(2) # Vincent's affection for you grows by 2
        
        userInterface("img_hall_vincent.gif", '''"Ooh, I noticed your headphones, what
are you listening to right now?"''')

        changeInterface("img_hall_vincent.gif", '''Vincent’s eyes light up.''')

        changeInterface("img_hall_vincent.gif", '''"It’s MAYDAY. They’re a Taiwanese band
I’ve been into recently. They’re really good!
Have you heard of them?"''')

        # Ask player response.
        changeInterface("img_hall_vincent.gif", '''Have you heard of MAYDAY?

1. YES
2. NO''')

        choice3 = win.getKey() # get keyboard input

        # while not one of the 2 options, wait.
        while choice3 not in ['1', '2']:
            choice3 = win.getKey()

        # if one of 2 options, return string to game
        if choice3 == "1":
            choice3 = "1"
        elif choice3 == "2":
            choice3 = "2"

        # Player says yes. 
        if choice3 == "1":

            vincent.addpoints(3) # Vincent's affection for you grows by 3
            
            userInterface("img_hall_vincent.gif", '''"I love them! I can really feel the emotion in their
voices and melody even when I can’t understand
the lyrics!"''')

            changeInterface("img_hall_vincent.gif", '''"RIGHT!! EXACTLY!! That’s exactly why I think they’re
so great! They can go from mellow to emotional
just like that and…"''')

            changeInterface("img_hall_vincent.gif", '''He trails off and blushes.''')

            changeInterface("img_hall_vincent.gif", '''"Sorry, I’m getting overly excited. But you’re the
first person I’ve met who knows and enjoys them.
Thank you."''')

            changeInterface("img_hall_vincent.gif", '''"No no, don’t apologize, hearing you so passionate
made me happy too. We should hang out some time
and listen to their music!"''')

            changeInterface("img_hall_vincent.gif", '''Vincent smiles. "Yeah, that’d be nice... I’ve got
to go. See you around."''')

        # Player says no.
        else:
            userInterface("img_hall_vincent.gif", '''"No, I haven't, but seeing your eyes light up when you
talk about them, I’ve got to look them up!"''')

            changeInterface("img_hall_vincent.gif", '''He blushes.''')

            changeInterface("img_hall_vincent.gif", '''"I’ll have to show you some time. But I’ve got to go,
I’ll see you around."''')


    # Resume dialogue.
    changeInterface("img_hall.gif", '''He’s quiet. But you get good vibes off him.
You kind of want to get to know him better.''')

    # MEETING ELLIOT dialogue ---------------------------------

    changeInterface("img_hall.gif", '''You check your watch. Homeroom starts in 10
minutes! And you don’t know where it is!!!''')

    changeInterface("img_class.gif", '''Somehow, you make it. 5 minutes into
homeroom. Your teacher points you to the
only seat left in class.''')

    changeInterface("img_class.gif", '''As you walk to your seat, you notice Luke
and Vincent both in your class. Vincent
gives you a small smile and a nod, and
Luke does an excited wave. It’s nice to
have some friendly faces in class.''')

    changeInterface("img_class.gif", '''The girl next to you doesn’t even flinch
when you pull up beside her. She’s frantically
typing something on her laptop. She’s stressed.
It’s the first day of school, you wonder what
she’s so stressed about.''')

    changeInterface("img_class.gif", '''"Okay class, I know some of you know each
other already, but many of you don’t, so please
turn to your neighbour and introduce yourselves.
This will be where you’ll be sitting for the rest
of the year."''')

    changeInterface("img_class.gif", '''Your neighbour turns to your with a bright
smile, as if she was never stressed in the first
place. She’s got a lovely smile.''')

    changeInterface("img_class_elliot.gif", '''"Hi! I’m Elliot! Nice to meet you! I’ve never
seen you around before, are you new here?"''')

    changeInterface("img_class_elliot.gif", '''Wow, she’s bubbly. But she’s nice. Cute, too.''')

    changeInterface("img_class_elliot.gif", '''"I’m '''+ player.name +'''! Yeah, I just moved here! It’s kinda
scary starting anew senior year, but you
seem nice. I can’t wait to get to know you!"''')

    changeInterface("img_class_elliot.gif", '''"Awww shucks. I’m excited to be friends now! We’re
going to be best buds!"''')

    changeInterface("img_class_elliot.gif", '''Elliot notices the book on your desk.''')

    changeInterface("img_class_elliot.gif", '''"Is that The Vegetarian? I just finished reading
that! How are you finding it?"''')

    # Ask player response.
    changeInterface("img_class.gif", '''How are you liking The Vegetarian?

1. "I really like it."

2. "I don't know how to feel about it to be honest -
it's a lot."''')

    choice4 = win.getKey() # get keyboard input

    # while not one of the 2 options, wait.
    while choice4 not in ['1', '2']:
        choice4 = win.getKey()

    # if one of 2 options, return string to game
    if choice4 == "1":
        choice4 = "1"
    elif choice4 == "2":
        choice4 = "2"

    # Player chooses 1.
    if choice4 == "1":

        elliot.addpoints(1) # Elliot likes you 1 point more

        userInterface("img_class_elliot.gif", '''"I really like it."''')

        changeInterface("img_class_elliot.gif", '''"ME TOO. It really makes you think. I am in awe of
how such simple language can be so powerful."''')

    # Player chooses 2.
    else:

        elliot.addpoints(2) # Elliot likes you 2 points more

        userInterface("img_class_elliot.gif", '''"I don’t know how I feel about it – it’s a lot."''')

        changeInterface("img_class_elliot.gif", '''"Right?! It just… makes you think. I had to take SO
many breaks in between because there’s just
SO MUCH to think about."''')

    # Dialogue resumes.
    changeInterface("img_class_elliot.gif", '''You and Elliot get into a really fascinating
discussion about The Vegetarian, Han Kang,
translated works, and everything in between.
You find out the thing Elliot was typing was
the ‘letter from the Editor’ for the newspaper’s
first issue. You’re really glad you had The
Vegetarian on hand, Elliot’s really amazing.''')

    changeInterface("img_class.gif", '''"Okay class, sorry to interrupt your fascinating
conversations, but it’s time you picked your
electives for the year. This year we’re choosing
between Robotics and Art."''')

    characters = [player, luke, vincent, elliot]
    
    return characters
