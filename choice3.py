from time import *
from charclasses import *
from interface import *

# DEFINE CHOICE 3 FUNCTION ---------------------------------

def choice3(characters):

    player = characters[0]
    luke = characters[1]
    vincent = characters[2]
    elliot = characters[3]
    
    changeInterface("img_black.gif",'''Between school and clubs,
you’re really starting to enjoy your new school.''')
    
    changeInterface("img_black.gif", '''Soon it’s nearing the end of the year,
and that means, sports day!''')

    changeInterface("img_class.gif", '''"Okay class, you each have got three options,
relay, cheer, or first-aid. Pick wisely, it’s your
last sports day."''')

    changeInterface("img_class.gif", '''Oh right, you’re a senior. This is it.
What will you choose?

1. Relay
2. Cheer
3. First-Aid''')

    # User chooses activiity for sports day.

    sports_day = win.getKey() # get keyboard input

    # while not one of the 2 options, wait.
    while sports_day not in ['1', '2', '3']:
            sports_day = win.getKey()

    # if one of 2 options, return string to game
    if sports_day == "1":
        sports_day = "1"
    elif sports_day == "2":
        sports_day = "2"
    elif sports_day == "3":
        sports_day = "3"


    # If user chooses 1, relay or 2, cheer.

    if sports_day == "1" or sports_day == "2":
        
        userInterface("img_black.gif", '''Finally, it’s the day before sports day.''')
        
        changeInterface("img_street.gif", '''Mom sent you out to buy rice last minute.''')

        changeInterface("img_street.gif", '''On your way back, you see your bus approaching.''')

        changeInterface("img_street.gif", '''You decide to run for it.''')

        changeInterface("img_street.gif", '''You might have made it if you weren’t carrying a
kilogram of rice, but you were.''')

        changeInterface("img_street.gif", '''And you trip.''')

        changeInterface("img_street.gif",'''Your ankle feels funny, and it’s difficult to stand up. ''')
        
        changeInterface("img_street.gif", '''You call your Mom, and she picks you up, complaining
that she should have known this was going to happen
and should have just gone to pick it up herself.''')

        changeInterface("img_street.gif", '''But she didn’t. And here you guys are, on the way
back home.''')

        changeInterface("img_street.gif", '''That was an eventful shopping trip. And now you’ve
got a choice.''')

        changeInterface("img_black.gif", '''...''') # Passage of time.
        
        if sports_day == "1": # If user chose relay.

            changeInterface("img_black.gif", '''Will you still run the relay? Your classmates,
and Luke are all counting on you. But if you do,
you risk hurting your ankle more. What will you do?

1. Continue
2. Sit out''')

        elif sports_day == "2": # If user chose cheer.
            
            changeInterface("img_black.gif", '''Are you going to continue with doing cheer? Your
team, Vincent, are all counting on you. But if you
do, you risk hurting your ankle more. What will you do?

1. Continue
2. Sit out''')

        sit_out_choice = win.getKey() # get keyboard input

        # while not one of the 2 options, wait.
        while sit_out_choice not in ['1', '2']:
                sit_out_choice = win.getKey()

        # if one of 2 options, return string to game
        if sit_out_choice == "1":
            sit_out_choice = "1"
        elif sit_out_choice == "2":
            sit_out_choice = "2"

        # If user chooses to continue.
        if sit_out_choice == "1":
            
            userInterface("img_black.gif", '''...''') # Passage of Time.

            changeInterface("img_track.gif", '''It's sports day.''')

            # If user chose relay.
            
            if sports_day == "1":
                
                changeInterface("img_track_luke.gif", '''"Morning ''' + player.name +'''! I’m so ready for this race.
Our last sports day! It’s kind of bittersweet,
isn’t it?"''')

                changeInterface("img_track_luke.gif", '''You smile. Well you definitely can’t say no to
that face.''')

                changeInterface("img_track_luke.gif", '''"Yeah, let’s make it a good one."''')

                changeInterface("img_track.gif", '''...''') # Passage of Time.

                changeInterface("img_track.gif", '''It’s going well, you’re in first place, your ankle
only aches slightly, and you’ve only got 10 metres
to go before you pass the baton on to Luke.''')

                changeInterface("img_track.gif", '''And then there it is, the turn of the track.''')

                changeInterface("img_track.gif", '''You swerve, and you lose your balance, just as you
reach Luke.''')

                changeInterface("img_black.gif", '''You fall. And you can’t get up.''')

                changeInterface("img_black.gif", '''"''' + player.name.upper() + '''!"''')

                changeInterface("img_track.gif", '''Luke has the baton, but he’s at a loss of what
to do. The second team just passed him, and the
third team is approaching.''')

                changeInterface("img_track.gif", '''"GO. DON’T WORRY ABOUT ME."''')

                changeInterface("img_track.gif", '''He gives you one more worried look, and he’s off.''')

                changeInterface("img_track.gif", '''And he’s back.''')

                changeInterface("img_track_luke.gif", '''"DUDE, YOU GAVE ME A HEART ATTACK. CAN YOU STAND?"''')

                changeInterface("img_track_luke.gif", '''You try. But your ankle can’t handle the weight of
your body and you fall back down. Man, this is
worse than it was yesterday.''')

                changeInterface("img_track_luke.gif", '''"Did we win at least?" You attempt to smile.''')

                changeInterface("img_track_luke.gif", '''"Second place, but what happened back there, ''' + player.name +'''?"''')

                changeInterface("img_track_luke.gif", '''He’s picks you up and carries you toward the
first-aid tent.''')

                changeInterface("img_track_luke.gif", '''"Heh, yesterday I was running for the bus while
carrying rice and fell down…"''')

                if player.club == "Track and Field": # User's club choice was track and field

                    changeInterface("img_track_luke.gif", '''"Dude, you’re on the track team, do better."''')

                    changeInterface("img_track_luke.gif", '''He’s trying to lighten the mood but he’s
obviously worried. You appreciate the effort.''')

                    changeInterface("img_track_luke.gif", '''"Sorry."''')

                else: # User's club choice was not track and field

                    changeInterface("img_track_luke.gif", '''"''' + player.name + ''', are you serious? Why didn’t you tell
me? You should have sat it out."''')

                    changeInterface("img_track_luke.gif", '''"I didn’t want to get in the way! I know how
much you cared about this competition and I didn’t
want to throw it away for you."''')

                    changeInterface("img_track_luke.gif", '''"All of this training, or even winning, means
nothing if you get hurt..."''')

                    changeInterface("img_track_luke.gif", '''"Sorry."''')

                    changeInterface("img_track_luke.gif", '''"Don’t be sorry, I just…"''')

                    changeInterface("img_track_luke.gif", '''He sighs.''')

                    changeInterface("img_track_luke.gif", '''"Wish you took better care of yourself."''')

                # If most affection points with Luke:
                                        
                if luke.affection > vincent.affection and luke.affection > elliot.affection:

                    player.dating = "Luke" # Append character to self.dating trait.

                    changeInterface("img_track_luke.gif", '''"''' + player.name + ''', I didn’t think this was going to be how
    I did it, but…"''')

                    changeInterface("img_track_luke.gif", '''He blushes.''')

                    changeInterface("img_track_luke.gif", '''"I like you."''')

                    changeInterface("img_track_luke.gif", '''He’s as red as a tomato...''')

                    changeInterface("img_track_luke.gif", '''"I really really like you. And I hate to see
    you hurt like this. And I know this isn’t the ideal
    situation but... would you go out with me?"''')

                    changeInterface("img_track_luke.gif", '''You can feel your face heating up.
Will you go out with him?

1. YES
2. yES''')

                    placebo = win.getKey() # get keyboard input

                    # while not one of the 2 options, wait.
                    while placebo not in ['1', '2']:
                            placebo = win.getKey()

                    # if one of 2 options, return string to game
                    if placebo == "1":
                        placebo = "1"
                    elif placebo == "2":
                        placebo = "2"

                    userInterface("img_track_luke.gif", '''"I like you too."''')

                    changeInterface("img_track_luke.gif", '''You grin at each other.''')
                                    
                else: # Luke does not have most affection points

                    changeInterface("img_black.gif", '''After first aid fixes you up, you and your
    team attend the award ceremony.''')

                    changeInterface("img_black.gif", '''Luke brings you home.''')

                    changeInterface("img_street_luke.gif", '''"What an eventful last sports day, huh?
    Sorry we didn’t win first place."''')

                    changeInterface("img_street_luke.gif", '''"Dude, at least we got a medal. I’m just
    glad you’re okay."''')

                    changeInterface("img_street_luke.gif", '''You grin.''')


            # User chooses Cheer.

            elif sports_day == "2":

                changeInterface("img_track_vincent.gif", '''"Morning, ''' + player.name + '''."''')

                changeInterface("img_track_vincent.gif", '''Over the year, Vincent has gotten increasingly
comfortable with you.''')

                changeInterface("img_track_vincent.gif", '''That thought itself warms you up a great deal.''')

                changeInterface("img_track_vincent.gif", '''"Morning Vincent!"''')

                changeInterface("img_track_vincent.gif", '''You’re definitely going to do your best for this
cheer.''')

                changeInterface("img_track_vincent.gif", '''"Let’s do our best today!"''')

                changeInterface("img_track.gif", '''It’s going well, you only have one more flip to do
before the end of the routine.''')

                changeInterface("img_track.gif", '''You flip.''')

                # If player has most affection points with Vincent:
                
                if vincent.affection > luke.affection and vincent.affection > elliot.affection:

                    player.dating = "Vincent" # Append Vincent to self.dating trait

                    changeInterface("img_black.gif", '''And… you lose your balance.''')

                    changeInterface("img_black.gif", '''You’re on the ground, and you can’t get up.''')

                    changeInterface("img_black.gif", '''"'''+ player.name.upper() + '''!''')

                    changeInterface("img_track.gif", '''Everyone stops, and Vincent runs toward you,
his eyes wide in panic.''')

                    changeInterface("img_track_vincent.gif", '''Honestly, this is the most emotion you’ve seen
him express.''')

                    changeInterface("img_track_vincent.gif", '''"Are you okay? Can you stand?"''')

                    changeInterface("img_track_vincent.gif", '''You try. But your ankle can’t handle the weight
of your body, and you fall back down. Man, this
is worse than it was yesterday. Vincent sighs,
but he picks you up, and is carries you toward
the first aid tent.''')

                    changeInterface("img_track_vincent.gif", '''"Man, ''' + player.name + ''', you’re scaring me. What happened
back there?"''')

                    changeInterface("img_track_vincent.gif", '''"Haha well, it’s a funny story, I was running
for the bus yesterday and I fell."''')

                    changeInterface("img_track_vincent.gif", '''He laughs, you giggle.''')

                    changeInterface("img_track_vincent.gif", '''"You really worried me back there. How are you
feeling now?"''')

                    changeInterface("img_track_vincent.gif", '''"Good, I’m kind of glad that you’re worried
about me. This is the most emotion you’ve shown me."''')

                    changeInterface("img_track_vincent.gif", '''With your close proximity, you can feel his
face heat up.''')

                    changeInterface("img_track_vincent.gif", '''"''' + player.name + ''', I really care about you.
And I wish I could have do this under better
circumstances, but here goes…"''')

                    changeInterface("img_track_vincent.gif", '''He takes a deep breath, and if possible,
his face gets even redder.''')
                                
                    changeInterface("img_track_vincent.gif", '''"I… I like you.
Really, really, really like you."''')

                    changeInterface("img_track_vincent.gif", '''Now you feel your own face heating up.''')
                    
                    changeInterface("img_track_vincent.gif", '''"I… like you too."''')

                    changeInterface("img_track_vincent.gif", '''And you grin at each other.''')

                else: # Vincent does not have most affection

                    changeInterface("img_track.gif", '''And you make it.''')

                    changeInterface("img_track.gif", '''Thank god.''')

                    changeInterface("img_track.gif", '''You grin at Vincent, and he smiles back.''')

        # If user decided to sit out.
        
        if sit_out_choice == "2":

            # If user chose relay.
            
            if sports_day == "1":

                userInterface("img_track_luke.gif", '''"Hi, ''' + player.name +'''! I’m so excited for today’s
race! Wait, you’re not in running clothes, what’s up?"''')

                changeInterface("img_track_luke.gif", '''"Oh, I fell down running for the bus yesterday
and I didn’t think I’d be able to run today. I’m sorry."''')

                changeInterface("img_track_luke.gif", '''"Sorry? What for? I’d rather have you safe than
run with me. It’d be awful if you get injured more.
Are you going to come cheer me on though?"''')

                changeInterface("img_track_luke.gif", '''"Of course!"''')

                changeInterface("img_track.gif", '''...''') # Passage of time.

                changeInterface("img_track.gif", '''Luke is running the last 100 metres, he’s
first but the second team is catching up.''')

                changeInterface("img_track.gif", '''"LUKE. FASTER. YOU GOT THIS."''')

                changeInterface("img_track.gif", '''And it seems like... he’s speeding up.''')

                changeInterface("img_track.gif", '''"AAAAAAAAAAA GO LUKE!!!!!"''')

                changeInterface("img_track.gif", '''The distance between him and the second runner
is widening, you yell louder.''')

                changeInterface("img_track.gif", '''And he makes it. First place.''')

                changeInterface("img_track.gif", '''You’re still screaming.''')

                # If player has most affection points with Luke:
                                
                if luke.affection > vincent.affection and luke.affection > elliot.affection:

                    player.dating = "Luke" # Append Luke to self.dating trait.

                    changeInterface("img_track.gif", '''Luke crosses the finish line and runs toward you.''')

                    changeInterface("img_track_luke.gif", '''He grabs you and spins you around.''')

                    changeInterface("img_track_luke.gif", '''"I heard you cheering for me."''')

                    changeInterface("img_track_luke.gif", '''"Of course, you’re track captain, you couldn’t
lose, that’d be shameful."''')
                                
                    if player.club == "Track and Field": # User's club choice was track and field

                        changeInterface("img_track_luke.gif", '''He laughs.''')

                        changeInterface("img_track_luke.gif", '''"Well you’re on the track team, how could
you fall running for the bus?"''')

                        changeInterface("img_track_luke.gif", '''"Hey! I was carrying a kilogram of rice,
it was heavy."''')

                    else: # User's club choice was not track and field

                        changeInterface("img_track_luke.gif", '''He laughs.''')

                    changeInterface("img_track_luke.gif", '''"Well, thank you for your support. Not just today,
thank you for always being there to support me."''')

                    changeInterface("img_track_luke.gif", '''He scratches the back of his neck. His flushed
face gets even redder.''')

                    changeInterface("img_track_luke.gif", '''"I… I like you. I really really really like
you. And I know I’m sweaty and gross and everything so
the situation is not ideal, but I told myself that if
I won this I’d do it so…"''')

                    changeInterface("img_track_luke.gif", '''His face is as red as a tomato now.''')

                    changeInterface("img_track_luke.gif", '''"Will you go out with me?"''')

                    changeInterface("img_track_luke.gif", '''Will you go out with him?

1. YES
2. yES''')

                    placebo = win.getKey() # get keyboard input

                    # while not one of the 2 options, wait.
                    while placebo not in ['1', '2']:
                            placebo = win.getKey()

                    # if one of 2 options, return string to game
                    if placebo == "1":
                        placebo = "1"
                    elif placebo == "2":
                        placebo = "2"

                    userInterface("img_track_luke.gif", '''You hug him, sweat and all.''')

                else: # Luke does not have highest affection

                    changeInterface("img_track.gif", '''He makes it.''')

                    changeInterface("img_track.gif", '''You’re yelling, everyone’s screaming. And
honestly, it’s pretty amazing.''')

            # User chooses cheer.

            if sports_day == "2":

                userInterface("img_track_vincent.gif", '''"''' + player.name + '''? You’re not in uniform. What’s up?"''')

                changeInterface("img_track_vincent.gif", '''You love how Vincent notices the small things
immediately.''')

                changeInterface("img_track_vincent.gif", '''"Oh, I fell down running for the bus yesterday and
my ankle’s kind of screwed up. So I think I’m going to
sit cheerleading out. I’m sorry."''')

                changeInterface("img_track_vincent.gif", '''"No it’s okay. I mean I was looking forward to doing
it with you,’ he blushes, ‘but I’d rather not have you
get injured, you know."''')

                changeInterface("img_track_vincent.gif", '''You smile. "Thank you, Vincent, I really appreciate
it. Listen out, because I’ll be cheering for YOU from
the sidelines."''')

                changeInterface("img_track_vincent.gif", '''His blush deepens.''')

                changeInterface("img_track.gif", '''Not performing has its perks - you get to appreciate
the art.''')

                changeInterface("img_track.gif", '''The whole team was amazing, Vincent is so good.''')

                changeInterface("img_track.gif", '''For such a talented guy, Vincent is so shy. You’re
so glad you get to appreciate his talents.''')

                changeInterface("img_track.gif", '''You yell till your voice goes hoarse.''')


                # If player has the most affection points with Vincent:

                if vincent.affection > luke.affection and vincent.affection > elliot.affection:

                    player.dating = "Vincent" # Append Vincent to self.dating trait.

                    changeInterface("img_track_vincent.gif", '''"YOU WERE SO GOOD."''')

                    changeInterface("img_track_vincent.gif", '''Vincent, already red from the physical activity,
gets even redder.''')

                    changeInterface("img_track_vincent.gif", '''"Thank you. I heard you throughout the
performance. Is your voice okay."''')
                    
                    changeInterface("img_track_vincent.gif", '''"It’s great, I’m so glad I could watch you.
You’re so talented!!"''')       

                    changeInterface("img_track_vincent.gif", '''Vincent is so red now, he’s covering his face
in his hands.''')

                    changeInterface("img_track_vincent.gif", '''"Thank you. Really. Not just for coming to watch
me. Thank you. For always supporting me. I really
appreciate it."''')

                    changeInterface("img_track_vincent.gif", '''He scratches his neck.''')

                    changeInterface("img_track_vincent.gif", '''"I… I… I like you. I reallylikeyou. And I wanted
to ask you if… you’dliketogooutwithme."''')

                    changeInterface("img_track_vincent.gif", '''Now it’s your turn to blush.''')

                    changeInterface("img_track_vincent.gif", '''"I like you too, and I would be honoured to have
you as my boyfriend."''')

                    
                    changeInterface("img_track_vincent.gif", '''He smiles.''')
                    
                    changeInterface("img_track_vincent.gif", '''And you hug the sweaty boy.''')

                else:  # Vincent does not have most affection points

                    changeInterface("img_track_vincent.gif",'''"YOU WERE SO GOOD."''')
                    
                    changeInterface("img_track_vincent.gif", '''He blushes.''')

                    changeInterface("img_track_vincent.gif", '''"Thank you. I heard you from the stands. Thank you,
for always supporting me. I really appreciate it."''')

                    changeInterface("img_track_vincent.gif", '''You smile. "Of course."''')

                    changeInterface("img_track_vincent.gif", '''And he smiles back.''')

    # User chooses first aid.

    elif sports_day == "3":

        userInterface("img_track_elliot.gif", '''"Fancy seeing you here, Elliot. Always thought you’d
be the one to go for relay or cheer, seeing that you
love physical activity to much."''')

        changeInterface("img_track_elliot.gif", '''"Well I’m glad I’m not alone doing this first
aid thing, I actually have no idea how to wrap
a wound."''')

        changeInterface("img_track_elliot.gif", '''"DUDE, not cool. What if someone actually gets hurt."''')

        changeInterface("img_track_elliot.gif", '''You grin. "Then it’ll be up to you, I guess."''')

        # If player has most affection points with Elliot:

        if elliot.affection > luke.affection and elliot.affection > vincent.affection:

            player.dating = "Elliot" #append Elliot to self.dating trait

            changeInterface("img_track_elliot.gif", '''Thankfully, sports day passed by pretty
uneventfully. You and Elliot spend the day lying on the floor,
just talking. About graduation, about life, about the future...''')

            changeInterface("img_track_elliot.gif", '''"Hey Elliot. Have you ever liked anybody?"''')

            changeInterface("img_track_elliot.gif", '''"Yeah sure, tons of people."''')

            changeInterface("img_track_elliot.gif", '''"Do you like anyone now?"''')

            changeInterface("img_track_elliot.gif", '''She blushes. "Do you?"''')

            changeInterface("img_track_elliot.gif", '''Well now it’s your turn to blush.''')

            changeInterface("img_track_elliot.gif", '''"Hey, I asked first."''')

            changeInterface("img_track_elliot.gif", '''"Okay, we won’t say the name. We’ll take turns
describing the person."''')

            changeInterface("img_track_elliot.gif", '''"You start."''')

            changeInterface("img_track_elliot.gif", '''"Hmph. Fine. Well my person is smart. She’s capable,
and responsible, and I’m am in awe at how together she
is most of the time."''')

            changeInterface("img_track_elliot.gif", '''"Her face goes red, she knows"''')

            changeInterface("img_track_elliot.gif", '''"Well, my person smells like a pina colada. It’s kinda
stupid, but I dig it."''')

            changeInterface("img_track_elliot.gif", '''And you guys are covering your faces, rolling on
the floor laughing.''')

            changeInterface("img_track_elliot.gif", '''"Hey I complimented you and you call me stupid."''')

            changeInterface("img_track_elliot.gif", '''"Who said I was talking about you? Maybe I was talking
about James."''')

            changeInterface("img_track_elliot.gif", '''"James smells of AXE, dude.
What are you talking about."''')

            changeInterface("img_track_elliot.gif", '''"UGH FINE. ''' + player.name.upper() + ''', I. LIKE. YOU. I REALLY REALLY LIKE
YOU. WILL YOU DO ME THE HONOUR OF GOING OUT WITH ME."''')

            changeInterface("img_track_elliot.gif", '''"I. WOULD. LOVE. TO."''')

        else: # Elliot does not have most affection points

            changeInterface("img_track.gif", '''The day passed by pretty uneventfully. No one
got injured. Except maybe your pride. Elliot can
be mean. But you guys had fun, and you’re glad you
got to spend the day together.''')

    if player.dating == []:  # If player does not get with a partner

        changeInterface("img_black.gif", '''Senior year comes and goes, you had a good year.
You didn't find "the one" though...''')

        changeInterface("img_black.gif", '''"Another year, another Christmas alone I guess."''')

        changeInterface("img_black.gif", '''You're not too upset about it.''')

    else:  # If player does find a partner

        changeInterface("img_black.gif", '''"If I could live forever in this moment, I would."''')


