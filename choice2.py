from time import *
from charclasses import *
from interface import *

# DEFINE CHOICE 2 FUNCTION ---------------------------------

def choice2(characters):

    player = characters[0]
    luke = characters[1]
    vincent = characters[2]
    elliot = characters[3]

    # User selects which club they want to join.
    
    changeInterface("img_class.gif", '''You’re starting to get into the groove of
school, so it’s probably time to join a club.
It’s also the deadline for joining an organisation,
so you’ve got to get on to it.''')

    changeInterface("img_class.gif", '''You go to your homeroom teacher, and she
points you to the only three clubs that are still
actively looking for members, track and field,
orchestra, and newspaper. Which will you join?

1. Track and Field
2. Orchestra
3. Newspaper''')

    club = win.getKey() # get keyboard input

    # while not one of the 2 options, wait.
    while club not in ['1', '2','3']:
            club = win.getKey()

    # if one of 2 options, return string to game
    if club == "1":
        club = "1"
    elif club == "2":
        club = "2"
    elif club == '3':
        club = '3'
        
    # If user chooses club 1, Track and Field.

    if club == "1":

        player.club = "Track and Field" # Append to player's self.club trait.

        player.clubpartner = luke # Luke is made your club partner.

        luke.addpoints(1) # Luke gains affection

        # Dialogue

        userInterface("img_track.gif", '"Fancy meeting you here, stranger."')

        changeInterface("img_track_luke.gif", '''It’s Luke. Not that you’re surprised. He might have
been the reason for you choosing track in the first
place, not that anyone needs to know that though.''')

        changeInterface("img_track_luke.gif", '''"Yeah! I was thinking about it, and I really want to
be more active this year. And you did say that it
was a cool team, or were you just lying…"''')

        changeInterface("img_track_luke.gif", '''He laughs, it’s a nice laugh. It bubbles and
spreads warmth through your body. You want to hear
it more often.''')

        changeInterface("img_track_luke.gif", "But then he gets to business.")

        changeInterface("img_track_luke.gif", '''"Okay team, let’s warm up, and then we’ll split up as
usual. Oh, we’ve got a new member! This is ''' + player.name + ''',
they’re new, and they’ll be joining…"''')

        changeInterface("img_track.gif", '''He turns to you, what would be the safest bet?
Sprints? But then it’s obvious who the weakest
link is.''')


        changeInterface("img_track.gif", '''Long-distance? You heard that that affects the
knees in the long run… long run, haha you’re funny.''')

        changeInterface("img_track.gif", '''Maybe mid-distance…? You told Luke that you would
run with him some time, jogging always sounds
like mid-distance, maybe that’s a good bet.''')

        changeInterface("img_track.gif", '''Hurdles? No, that sounds like a lot of embarrassing
yourself. Gah, you wished you knew what Luke
specialised in…''')

        changeInterface("img_track.gif", '''"I like...!"

1. Sprinting
2. Mid-Distance
3. Long-Distance
4. Hurdles''')


        # User selects speciality

        speciality = win.getKey() # get keyboard input

        # while not one of the 3 options, wait.
        while speciality not in ['1', '2', '3', '4']:
            speciality = win.getKey()

        # if one of 3 options, return string to game
        if speciality == "1":
            speciality = "1"
        elif speciality == "2":
            speciality = "2"
        elif speciality == "3":
            speciality = "3"
        elif speciality == "4":
            speciality = "4"

        userInterface("img_track_luke.gif", '''"Hey that’s my speciality!" He says excitedly, his
eyes bright. His team chuckles, and he blushes.''')

        changeInterface("img_track_luke.gif", '''And then it’s back to business, and you get
to training.''')


        # Time passing
        changeInterface("img_track.gif", "...")

        changeInterface("img_track.gif", '''It wasn’t too bad… You just… feel like death.
But hey, you’re getting fit, and you get to spend
more time with Luke. It’s a lose-win-win.''')

    # If user chooses club 2, Orchestra.

    elif club == "2":

        player.club = "Orchestra" # Append to player's self.elective trait

        player.clubpartner = vincent # Vincent is made your club partner

        vincent.addpoints(1) # Vincent gains affection

        # Dialogue
        
        userInterface("img_orchestra.gif", '''You grab your violin and go up to the conductor.
After you introduce yourself, he hands your scores
and points you to your seat, next to where the
violin soloist would sit.''')

        changeInterface("img_orchestra.gif", '''Ooh, this year you guys are playing the theme
from Amadeus, the musical. You love the violin part
for this piece. You’re glad you picked orchestra.''')

        changeInterface("img_orchestra.gif", '''Students start filing in, collecting their scores
and finding their seats.''')

        changeInterface("img_orchestra_vincent.gif", '''And you see Vincent, carrying a violin case.
That’s exciting. You do a little wave at him, and he
gives you a small smile. You hope he’s assigned
somewhere near you.''')

        changeInterface("img_orchestra_vincent.gif", '''Turns out, Vincent is the soloist this year. He
seems a little embarrassed sitting next to you. You
hope it’s not because you looked too in awe of him
when he sat in the soloist spot.''')

        changeInterface("img_orchestra_vincent.gif", '"Hi ' + player.name + '''. I didn’t expect to see you here."''')

        changeInterface("img_orchestra_vincent.gif", '''"Haha, I hope that’s not a bad thing… I didn’t
expect to see you here either."''')

        changeInterface("img_orchestra_vincent.gif", "His eyes widen.")

        changeInterface("img_orchestra_vincent.gif", '''"Oh no no, it’s not that I don’t want you here,
I just… didn’t expect it."''')

        changeInterface("img_orchestra_vincent.gif", '''"Yeah, I feel, it’s a nice surprise though! And what
were the chances that we were assigned to seats next
to each other! Wow, soloist huh?"''')

        changeInterface("img_orchestra_vincent.gif", "You grin.")

        changeInterface("img_orchestra_vincent.gif", '''He blushes. As he was about to respond, the conductor
shushes and gives you both a dirty look.''')

        changeInterface("img_orchestra_vincent.gif", "You both smile embarrassed.")

        # Time passing
        changeInterface("img_orchestra.gif", "...")

        changeInterface("img_orchestra.gif", '''Orchestra was fun, you loved the pieces, and getting
to watch Vincent play was amazing. You’re looking
forward to the rest of the year.''')

    #  If user chooses club 3, Newspaper.

    elif club == "3":

        player.club = "Newspaper" # Append to player's self.elective trait.

        player.clubpartner = elliot # Vincent is made your club partner

        elliot.addpoints(1) # Elliot gains affection.
        
        userInterface("img_newspaper.gif", '"' + player.name + '''! What a surprise! I’m glad you’re here
though! We really are short on staff right now, so
I’m really happy you’re here!"''')

        changeInterface("img_newspaper.gif", '''That was overwhelming. Not in a bad way, just a lot
to take in when you walk into a room.''')

        changeInterface("img_newspaper_elliot.gif", '''"Hi Elliot, fancy seeing you here."''')

        changeInterface("img_newspaper_elliot.gif", "She laughs.")

        changeInterface("img_newspaper_elliot.gif", '''And work begins. Everyone is working quietly.
Sometimes, someone would break the silence to read
something funny they read, it was a very nice
atmosphere.''')

        changeInterface("img_newspaper_elliot.gif", '''You are working on layout when Elliot comes up
behind you. Her head is right next to yours, peering
at the screen. Elliot smells nice. Vanilla with
hints of orange, fresh.''')

        changeInterface("img_newspaper_elliot.gif", "She’s blushing. Did you say that out loud?")

        changeInterface("img_newspaper_elliot.gif", '''"Aaaahhh I’m so sorry, did I say that out loud?"''')

        changeInterface("img_newspaper_elliot.gif", '''"Yes… but I was thinking the same thing. Except
you smell coconut-y, more tropical pina colada."''')

        changeInterface("img_newspaper_elliot.gif", "She blushes harder. It’s cute.")

        changeInterface("img_newspaper_elliot.gif", '''"Ahhh I had something important to say, thanks a
lot. It had something that actually had to do with the
paper. I’ll come back later."''')

        changeInterface("img_newspaper_elliot.gif", "She’s back soon.")

        changeInterface("img_newspaper_elliot.gif", '''"Yes, it’s the way you’re doing the captions, they
should be about a millimetre off from your picture.
No, not like that that’s too much, slightly less.
Nono, too little. Ugh, let me show you."''')

        changeInterface("img_newspaper_elliot.gif", '''She grabs the mouse – over your hand. She’s too
focused and doesn’t notice, but you feel your face
heating up.''')

        changeInterface("img_newspaper_elliot.gif", '"Like that!" she exclaims, her hand still on yours."')

        changeInterface("img_newspaper_elliot.gif", '"Why are you so still?"')

        changeInterface("img_newspaper_elliot.gif", 'She then notices her hand on yours. "Oh."')

        changeInterface("img_newspaper_elliot.gif", '''Your faces are both red now. She’s covering her
face with both hands. It would be cute if you didn’t
feel like dying yourself.''')

        changeInterface("img_newspaper.gif", '''The rest of newspaper went about relatively
uneventfully. You can’t stop thinking about Elliot,
but you’re glad you got a chance to see this other,
less-together side of her.''')

        changeInterface("img_newspaper_elliot.gif", '"Hey ' + player.name + ', do you want to go home together?"')

        changeInterface("img_newspaper_elliot.gif", "You can’t help the butterflies in your chest.")

        changeInterface("img_newspaper_elliot.gif", "You waste no time and nod enthusiastically.")

    changeInterface("img_black.gif", "Going home with " + player.clubpartner.name + " is a highlight.") # partner name

    changeInterface("img_black.gif", '''You guys talk about anything and everything between
school, TV, life, gossip, dreams...''')

    changeInterface("img_black.gif", "Sometimes you just walk in silence.")

    changeInterface("img_black.gif", "It’s always a good time.")

    
    characters = [player, luke, vincent, elliot]

    return characters


