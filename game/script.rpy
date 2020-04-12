define slowfade = Fade(1.0, 0, 3.0)
define slowerfade = Fade (3.0, 0, 3.0)
define slowdissolve = Dissolve(1.0)
define fadehold = Fade(3.0, 1.0, 3.0)

define y = Character("You")
define n = Character("Narrator")
define s = Character("Sofia")
define ug = Character("Unknown Girl")
define m = Character("Strange Man")


label start:
    stop music fadeout (2)
    scene black
    with slowerfade
    """
    Home.

    The safest place of all, isn't it?

    Well, maybe it is. Or maybe not.

    But one thing is certain...

    Home is where your memories linger.

    Your deepest memories.

    Be them happy memories or sad ones, that doesn't matter.

    They all stay there.

    Hidden in the shadows, perhaps.
    """
    play music "roombgm.ogg" fadein (3)
    scene roomd_dawn
    with fadehold
    $ mood = 50
    $ menth = 5
    $ mem = 0
    $ trauma = 0
    $ sofiatalk = False
    """
    You open your eyes.

    The morning's soft colours linger from the window.

    A small apartment, with an upper floor. You...

    You don't recognize it.

    Or you do recognize it but something is different.

    Missing, maybe?

    Or perhaps there are things there weren't before...

    But there is something, in there.

    Something that attracts you, that calls you.

    Is it the door?

    The computer?

    Or something else?
    """
    jump roomdownscreen

label roomdown:
    scene roomu_dawn
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen
label sofiagoodfade:
    scene computergood_dawn
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen
label sofiasadfade:
    scene computerbad_dawn
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen
label roomdownscreen:
    scene roomd_dawn
    call screen roomdownscreen

label roomup:
    scene roomd_dawn
    $ renpy.pause(0.5)
    scene roomu_dawn
    with fade
    $ renpy.pause(1)
    jump roomupscreen
label roomupscreen:
    scene roomu_dawn
    call screen roomupscreen
label window:
    """
    The weather outside is nice.

    It's still early morning, so there are not many people around.
    """
    jump roomdownscreen
label bed:
    """
    You are not tired, now.

    Maybe later...
    """
    jump roomupscreen
label tv:
    """
    There's a film on the tv.

    Maybe it's a bit sad, but you've never seen it.

    It seems still at the beginning.

    A car advances through a thic fog and a boy is playing at the street's border.

    Then...a crash, and the boy turns around.

    You look away, feeling a soft pain in the head.
    """
    jump roomdownscreen
label books:
    """
    A library filled with books.

    They seem to be all classics.
    """
    jump roomdownscreen
label plant:
    """
    The first Spring's sprouts are starting to appear on this plant.

    You wonder which flowers will grow.
    """
    jump roomdownscreen
label trash:
    """
    Just a normal trash bin, nothing special about it.
    """
    jump roomdownscreen
label phone:
    """
    An old and dusty phone.

    Not so useful, as you never call anyone.
    """
    jump roomdownscreen
label cds:
    """
    An ominous pile of CDs.

    They really are a lot.
    """
    jump roomdownscreen
label toy:
    """
    You remember someone gave this to you.

    You can't exactly remember when, but it was a lot of years ago.
    """
    jump roomupscreen
label mirror:
    """
    You see yourself.

    Is it a pleasant view?
    """
    jump roomupscreen
label guit:
    """
    An old classic guitar.

    You faintly remember some chords...
    """
    jump roomupscreen

label computer:
    if sofiatalk == False:
        jump sofianeut
    if sofiatalk == True and mood >= 55:
        jump sofiagood
    if sofiatalk == True and mood <= 45:
        jump sofiasad
label sofiagood:
    scene gmood_sgood_dawn
    with slowfade
    s "I see you're doing fine, today!"
    jump sofiagoodfade
label sofiasad:
    scene smood_sbad_dawn
    with slowfade
    s "You look so sad..."
    jump sofiasadfade
label sofianeut:
    scene neutmood_sbad_dawn
    with slowfade
    $ sofiatalk = True
    """
    You sit at your desk and discover that the PC is already turned on.

    On the screen there's a young girl.
    """
    ug "You're awake!"
    menu:
        "Sorry, but...who are you?":
            $ mood += 5
            with dissolve
            ug """
            Guess your memory still isn't alright, huh...?

            Well, anyway, my name is Sofia. I'm your...best friend.
            """
        "I don't feel like talking to a stranger.":
            $ mood -= 5
            with dissolve
            ug "A stranger? Well, I'm not a stranger, I'm Sofia...your best friend!"
    s "I'm here to help you."
    y "Help?"
    s "Yes, of course. We know each other very well, but you've lost your memory, so..."
    y "Yeah, I don't remember..."
    s """
    Don't worry.

    Like I said, I'm here to help.

    First of all, as you already know, this is your computer.

    By interacting with it, you'll be able to talk with me.

    Now, second...have you already tried opening the door?
    """
    menu:
        "Yes.":
            s """
            Very well. Then you should have noticed it's close.
            """
        "No.":
            s """
            Well, doesn't matter since it's closed.
            """
    s """
    In all sincerity, I don't really know how to open it...

    But it seems to be related to that icon on this screen.
    """
    if mood <= 45:
        scene smood_sneut_dawn
        with dissolve
    if mood >= 55:
        scene gmood_sgood_dawn
        with dissolve
    """
    It changes in relation to your mood.

    And when it does, I guess you should try to check on the door.

    Last time you did, something strange happened...
    """
    menu:
        "Something strange?":
            $ mood += 15
            if mood == 55:
                scene gmood_sneut_dawn
                with dissolve
            if mood >= 60:
                scene gmood_sgood_dawn
                with dissolve
            if mood == 50:
                scene neutmood_sneut_dawn
                with dissolve
            if mood <= 45:
                scene smood_sneut_dawn
                with dissolve
            s "Don't worry, there's nothing dangerous out there! Not that I know, at least..."
        "...What should happen?":
            $ mood -= 15
            if mood == 55:
                scene gmood_sbad_dawn
                with dissolve
            if mood <= 45:
                scene smood_sbad_dawn
                with dissolve
            if mood == 50:
                scene computerneut_dawn
                with dissolve
            s "Please, don't worry so much!"
    s """
    Well, how to explain it...

    The last time you managed to get out.

    But I haven't seen you for a lot of time, after that.

    And here you are now!

    ...without memory, as well as before.
    """
    menu:
        "Were you here all this time?":
            s """
            Yes, since before you lost your memory.

            In fact, I waited for some days, but...

            You're here, now, so that's the important thing, isn't it?
            """
        "So, how did we know each other?":
            s """
            It's been something like...five years.

            We were at school together.

            But then, we separated at University and kept contact only through this program, online.

            I see your room and you see mine,so we're...

            Connected? Sort of, at least.
            """
    s """
    In any case, why don't you try that door?

    I think it should be alright, by now...

    Oh and...I have some kind of request...?

    When you come back could you tell me how it was?
    """
    menu:
        "I will.":
            if mood == 50:
                $ mood += 10
            else:
                $ mood += 5
            if mood == 55:
                scene gmood_sneut_dawn
                with dissolve
                s "Thanks. Go now!"
                scene roomd_dawn
                with slowfade
                jump roomdownscreen
            if mood >= 60:
                scene gmood_sgood_dawn
                s "Thanks. Go now!"
                scene roomd_dawn
                with slowfade
                jump roomdownscreen
            if mood == 45:
                scene smood_sneut_dawn
                s "Thanks. Go now!"
                scene roomd_dawn
                with slowfade
                jump roomdownscreen
        "Hmm, we'll see...":
            if mood == 50:
                $ mood -= 10
            else:
                $ mood -= 5
            if mood == 55:
                scene gmood_sneut_dawn
                s "Ok, it's fine..."
                scene roomd_dawn
                with slowfade
                jump roomdownscreen
            if mood == 45:
                scene smood_sbad_dawn
                with dissolve
                s "Ok, it's fine..."
                scene roomd_dawn
                with slowfade
                jump roomdownscreen
            if mood == 40:
                scene smood_sbad_dawn
                s "Ok, it's fine..."
                scene roomd_dawn
                with slowfade
                jump roomdownscreen

label door:
    if mood >= 46 and mood <= 54:
        "I can't get outside, it's tightly closed."
        jump roomdownscreen
    if mood <= 45:
        stop music fadeout (2)
        scene black
        with slowfade
        $ renpy.pause(1.5)
        scene trauma
        with slowfade
        play music "traumabgm.ogg" fadein (2)
        $ menth -= 1
        $ trauma += 1
        """
        You find yourself in a dark place, ruled by sad and heavy feelings.

        A garden, it seems.

        Yet the entire place seems to be falling apart.

        In front of you there is a man. He's looking at you, his eyes glittering in the darkness.

        Suddenly, you feel a stabbing pain hitting you.

        You feel alone, somehow, and that black shadow seem to be connected to that feeling.

        He doesn't talk nor move. He just watches you silently as a strange sense of guilt caughts you.

        And so the memory ends, without a word spoken.
        """
        stop music fadeout (3)
        jump narrator2
    elif mood >= 55:
        stop music fadeout (2)
        scene black
        with slowfade
        $ renpy.pause(1.5)
        scene mem
        with slowfade
        play music "membgm.ogg" fadein (2)
        $ menth += 1
        $ mem += 1
        """
        There is a small and feeble garden ahead of you.

        A big tree casts his leaves towards the sky and all the colours are pale, as if you're in a dream.

        The wind blows softly, caressing your skin. It's a cold breeze, yet tender.

        In the middle of the garden there is a man, sitted on an old chair.

        He gives you his back, so you can't see his face, yet it reminds you of something.

        A memory that you thought was gone is silently appearing in front of you as a pale shadow,

        You don't know how, but you understand he's smiling even though you can't see it.

        He doesn't talk and not even move, yet there is a deep feeling of calmness that comes with the memory's end.
        """
        stop music fadeout (3)
        jump narrator2

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################START PASSAGE 2 #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label narrator2:
    show black
    with fadehold
    """
    Memories.

    Do you remember who you are? Or where you come from?

    Even the apartment where you lived seems to be blurring away from your memories.

    But don't worry, I'm here with you. To help you.

    Or even guide you, we could say.

    You've seen a glimpse of...memories, didn't you?

    Were them yours? Or someone else's?

    You're doubting, aren't you?

    That's good. Because doubt is the only certainty someone could obtain in this world.
    """
    play music "roombgm.ogg" fadein (3)
    scene roomd_aft
    with fadehold
    $ mood = 50
    $ sofiatalk = False
    $ windowseen = False
    $ books= False
    $ trash = False
    $ plant = False
    if menth >= 6:
        """
        Waking up, you feel a bittersweet sensation in your heart.

        It flows through your whole body towards your mind.

        It's a melancholic feeling, as if you've just seen an old friend whom you forgot.

        Lost in time, he's now nothing more than a pale figure in your head.

        The door...it's silently waiting for you to be ready.
        """
    if menth <= 4:
        """
        A strong headache wakes you up.

        Your mind is screaming for help, crowded with dark and horrific images.

        Pressing your fingers on the forehead, you try to calm it.

        The headache then suddenly disappears, leaving a deep emptiness behind.

        The door...you feel it calling to you, asking if you're ready to go out again.
        """
    jump roomdownscreen2

label sofiagoodfade2:
    scene computergood_aft
    $ renpy.pause(0.5)
    scene roomd_aft
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2
label sofiasadfade2:
    scene computerbad_aft
    $ renpy.pause(0.5)
    scene roomd_aft
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2
label sofianeutfade2:
    scene computerneut_aft
    $ renpy.pause(0.5)
    scene roomd_aft
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2

label roomdown2:
    scene roomu_aft
    $ renpy.pause(0.5)
    scene roomd_aft
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2
label roomdownscreen2:
    scene roomd_aft
    call screen roomdownscreen2

label roomup2:
    scene roomd_aft
    $ renpy.pause(0.5)
    scene roomu_aft
    with fade
    $ renpy.pause(1)
    jump roomupscreen2
label roomupscreen2:
    scene roomu_aft
    call screen roomupscreen2
label window2:
    if sofiatalk == False:
        """
        The weather doesn't seem very nice.
        """
    if windowseen == True:
        """
        Everything outside really looks grim.
        """
    if sofiatalk == True and windowseen == False:
        """
        Looks like a gloomy day outside.

        Do you want to take a look?
        """
        menu:
            "Why not?":
                if mood == 55:
                    $ mood -= 10
                else:
                    $ mood -= 5
                $ windowseen = True
                """
                Everything seems strangely empty.

                And the grey sky does not make you feel better.
                """
            "Not now.":
                "You step away from the window."
    jump roomdownscreen2
label bed2:
    """
    You can't sleep now.

    There are things you have to do.
    """
    jump roomupscreen2
label books2:
    if sofiatalk == False:
        """
        A library filled with books.

        Now that you pay more attention to it...

        You realize there are plenty of books about art.
        """
    if books == True:
        """
        You've already read.

        Maybe later...
        """
    if sofiatalk == True and books == False:
        "You look at the titles, unable to choose which book read."
        menu:
            "Choose one randomly.":
                if mood == 45:
                    $ mood += 10
                else:
                    $ mood += 5
                $ books = True
                """
                You pick and old essay about cinema.

                You remember the author's name, but not the title.

                'It's a film about you, your father, your grandfather.'

                'About someone who will live after you and who is still 'you'.'

                That seems to hit deep in your mind.
                """
            "You don't feel like reading.":
                "You leave the books be."
    jump roomdownscreen2
label plant2:
    if sofiatalk == False:
        """
        The leaves' green is brilliant...

        Yet there seems to be some dust on them.
        """
    if plant == True:
        """
        The plant is overflowing with joy.
        """
    if sofiatalk == True and plant == False:
        "This plant sure needs some water."
        menu:
            "Water it.":
                if mood == 45:
                    $ mood += 10
                else:
                    $ mood += 5
                $ plant = True
                "As you pour the water in the vase, the plant regains some light."
            "Maybe later...":
                """
                You don't really feel like it.

                Not now, at least.
                """
    jump roomdownscreen2
label trash2:
    if sofiatalk == False:
        """
        Trash seems to be piling up...
        """
    if trash == True:
        """
        Empty.

        It makes the house look cleaner.
        """
    if sofiatalk == True and trash == False:
        "Maybe it's better to throw it away..."
        menu:
            "Empty the bin.":
                if mood == 45:
                    $ mood += 10
                else:
                    $ mood += 5
                $ trash = True
                "Now you feel better with yourself."
            "Leave it as it is.":
                "You don't really want to do that now."
    jump roomdownscreen2
label phone2:
    """
    The dust never disappear from this phone, huh?
    """
    jump roomdownscreen2
label tv2:
    """
    There's a french movie on the tv.

    A young boy is running through an empty street at night.

    A song by David Bowie is playing in the background.

    Its seems very interesting.
    """
    jump roomdownscreen2
label cds2:
    """
    Whenever you watch at this pile of CDs...

    You think it's a shame you don't have a CD-player.
    """
    jump roomdownscreen2
label toy2:
    """
    You're unable to toss it away.

    Even after all this time, you can't undestrand why.

    Maybe you're sill connected with the person who gave it to you.
    """
    jump roomupscreen2
label mirror2:
    """
    Still no one but yourself.

    Is it a pleasant view?
    """
    jump roomupscreen2
label guit2:
    """
    This guitar...

    As you watch it, you remember playing it sometimes.

    But how much time has passed since then?
    """
    jump roomupscreen2

label computer2:
    if sofiatalk == False:
        jump sofianeut2
    if sofiatalk == True and mood >= 55:
        jump sofiagood2
    if sofiatalk == True and mood <= 45:
        jump sofiasad2
label sofiagood2:
    scene gmood_sgood_aft
    with slowfade
    s "It's nice seeing you smiling like this, you know?"
    jump sofiagoodfade2
label sofiasad2:
    scene smood_sbad_aft
    with slowfade
    s """
    Is it me or you seem a little down?

    Please, take care of yourself...
    """
    jump sofiasadfade2
label sofianeut2:
    scene neutmood_sgood_aft
    with slowfade
    $ sofiatalk = True
    s """
    You're finally back!

    Where were you?
    """
    menu:
        "I...got out of the door.":
            $ mood += 5
            scene gmood_sneut_aft
            with dissolve
            s """
            Really?

            That...

            That is just incredible!

            And tell me, how did it go?
            """
        "Nowhere, just resting.":
            $ mood -= 5
            scene smood_sbad_aft
            with dissolve
            s """
            Hmm, if you say so...

            Uhmm, you went out of the door, didn't you?

            Guess you don't want to talk about it...right?
            """
    if menth >= 6:
        menu:
            "I saw a strange man in a garden.":
                $ mood += 5
                if mood >= 55:
                    scene gmood_sneut_aft
                if mood == 50:
                    scene neutmood_sneut_aft
                    with dissolve
                if mood == 45:
                    scene smood_sneut_aft
                s """
                That sounds very interesting!

                I think that was a piece of your memories...

                Unfortunately, I don't know much about it.

                How did that makes you feel?
                """
                menu:
                    "It was...sad.":
                        $ mood -= 5
                        if mood == 55:
                            scene gmood_sbad_aft
                        if mood == 50:
                            scene neutmood_sbad_aft
                        if mood <= 45:
                            scene smood_sbad_aft
                            with dissolve
                        s """
                        Oh, I see...

                        Maybe it's not a very happy memory.

                        Or maybe it's somehow painful to remember about it.

                        Anyway, I have something important to tell you.
                        """
                    "Peaceful, I guess.":
                        $ mood += 5
                        if mood == 55:
                            scene gmood_sgood_aft
                            with dissolve
                        if mood >= 60:
                            scene gmood_sgood_aft
                            with dissolve
                        if mood == 50:
                            scene neutmood_sgood_aft
                            with dissolve
                        if mood <= 45:
                            scene smood_sgood_aft
                            with dissolve
                        s """
                        I'm glad to hear that!

                        It's nice to know it's a good memory for you.

                        That really is a good thing, don't you think?

                        Your smile tells me it is!

                        But anyway, ther's something important I forgot to tell you...
                        """
            "I prefer not to talk about it.":
                $ mood -= 5
                if mood >= 55:
                    scene gmood_sbad_aft
                    with dissolve
                if mood == 50:
                    scene neutmood_sbad_aft
                    with dissolve
                if mood == 45:
                    scene smood_sbad_aft
                    with dissolve
                if mood <= 40:
                    scene smood_sbad_aft
                    with dissolve
                s """
                Oh, I understand...guess it was too sad, right...?

                But anyway, I remembered to tell you something.
                """
    if menth <= 4:
        menu:
            "There was a scary man...":
                $ mood -=5
                if mood >= 55:
                    scene gmood_sbad_aft
                    with dissolve
                if mood == 50:
                    scene neutmood_sbad_aft
                    with dissolve
                if mood <= 45:
                    scene smood_sbad_aft
                    with dissolve
                s """
                A scary man...?

                That sound really bad, doesn't it...

                And can you tell me something about him?
                """
                menu:
                    "I just want to forget him, now...":
                        $ mood += 5
                        if mood == 55:
                            scene gmood_sgood_aft
                            with dissolve
                        if mood == 50:
                            scene neutmood_sgood_aft
                            with dissolve
                        if mood <= 45:
                            scene smood_sgood_aft
                            with dissolve
                        s """
                        I bet you do!

                        I guess I would do the same...

                        Well, let's change argument, then.

                        I just remembered about something, in fact!
                        """
                    "I think I'm still scared.":
                        $ mood -= 5
                        if mood == 55:
                            scene gmood_sbad_aft
                            with dissolve
                        if mood == 50:
                            scene neutmood_sbad_aft
                            with dissolve
                        if mood <= 45:
                            scene smood_sbad_aft
                        s """
                        I can only imagine how terrible it could have been...

                        And I guess that's why you're so pale, huh?

                        But please, hang on in there, ok?
                        I'm with you!

                        Oh and now that I think about it...
                        """
            "I don't want to think about it.":
                $ mood += 5
                if mood == 55:
                    scene gmood_sneut_aft
                    with dissolve
                if mood >= 60:
                    scene gmood_sneut_aft
                if mood == 50:
                    scene neutmood_sneut_aft
                    with dissolve
                if mood == 45:
                    scene smood_sneut_aft
                s """
                I understand, I don't want to force you.

                Uhmm, well, guess it's better to change argument, huh?

                Oh, I know! I just remembered something that could be useful.
                """
    s """
    Last time I forgot to tell you about your room.

    Maybe you already noticed that there are plenty of interesting things, right?

    But, anyway, the thing is that they might be useful to keep you busy.

    You know, they say that distractions sometimes make us happier, somehow.

    I think it's because by distracting ourselves we focus less on what's painful.

    Or what troubles us, anyway.

    But it's true that not all distractions can make us happier, isn't it?

    So be careful with your mood out there.
    """
    menu:
        "Ok, thanks for your help.":
            if mood == 45:
                $ mood += 10
            else:
                $ mood += 5
            if mood == 55:
                scene gmood_sneut_aft
                with dissolve
                s """
                Very well!

                I hope it's all clear...

                See you later, then!
                """
                scene roomd_aft
                with slowfade
                jump roomdownscreen2
            if mood >= 60:
                scene gmood_sgood_aft
                with dissolve
                s """
                Very well!

                I hope it's all clear...

                See you later, then!
                """
                scene roomd_aft
                with slowfade
                jump roomdownscreen2
            if mood == 50:
                scene neutmood_sneut_aft
                with dissolve
                s """
                Very well!

                I hope it's all clear...

                See you later, then!
                """
                scene roomd_aft
                with slowfade
                jump roomdownscreen2
            if mood <= 45:
                scene smood_sneut_aft
                with dissolve
                s """
                Very well!

                I hope it's all clear...

                See you later, then!
                """
                scene roomd_aft
                with slowfade
                jump roomdownscreen2
        "Uhmm yeah, right...":
            if mood == 55:
                $ mood -= 10
            else:
                $ mood -= 5
            if mood == 55:
                scene gmood_sneut_aft
                with dissolve
                s """
                Well, I hope it's all clear.

                See you later!

                And remember, whatever happens...I'm here.
                """
                scene roomd_aft
                with slowfade
                jump roomdownscreen2
            if mood >= 60:
                scene gmood_sgood_aft
                with dissolve
                s """
                Well, I hope it's all clear.

                See you later!

                And remember, whatever happens...I'm here.
                """
                scene roomd_aft
                with slowfade
                jump roomdownscreen2
            if mood == 50:
                scene neutmood_sneut_aft
                with dissolve
                s """
                Well, I hope it's all clear.

                See you later!

                And remember, whatever happens...I'm here.
                """
                scene roomd_aft
                with slowfade
                jump roomdownscreen2
            if mood == 45:
                scene smood_sbad_aft
                with dissolve
                s """
                Well, I hope it's all clear.

                And remember, whatever happens...I'm here.
                """
                scene roomd_aft
                with slowfade
                jump roomdownscreen2
            if mood <= 40:
                scene smood_sbad_aft
                with dissolve
                s """
                Well, I hope it's all clear.

                And remember, whatever happens...I'm here.
                """
                scene roomd_aft
                with slowfade
                jump roomdownscreen2

label door2:
    if mood >= 46 and mood <= 54:
        "I can't get outside, it's tightly closed."
        jump roomdownscreen2
    if mood <= 45:
        stop music fadeout (2)
        scene black
        with slowfade
        $ renpy.pause(1.5)
        scene trauma
        with slowfade
        play music "traumabgm.ogg" fadein (3)
        $ menth -= 1
        $ trauma += 1
        """
        The dark place again.

        It seems different yet similar than last time.

        The strange, scary man is still there.

        He still watches you.

        Between the shadows, you have the impression he's pointing his finger at you.
        """
        m """
        You saw it...

        The fall of everything...

        You saw it...

        Didn't you?
        """
        """
        You don't understand what he's saying.

        You don't understand at all.

        What 'fall' is he talking about?

        What does it mean you saw it?

        You try to remember.

        Hard. Harder.

        But nothing comes to your mind.

        Absolutely nothing.

        And the memory starts to disappear.
        """
        stop music fadeout (3)
        jump narrator3
    elif mood >= 55:
        stop music fadeout (2)
        scene black
        with slowfade
        $ renpy.pause(1.5)
        scene mem
        with slowfade
        play music "membgm.ogg" fadein (3)
        $ menth += 1
        $ mem += 1
        m """
        When we first met

        Our hands were cold

        The wind blew gently on the forest

        Silence, all around

        And a smile of happiness on my face.
        """
        """
        You look at the mysterious man in front of you.

        He just finished reading a passage from the book he's holding.
        """
        m """
        Do you remember this poem?

        It brings back so many memories...

        Yet, you don't seem to recall any of them...

        That makes me sad.

        So sad...
        """
        menu:
            "This place...":
                m """
                It rings some bell?

                It does, right?

                But I guess you still aren't ready.

                Memories can't come back in a second, you know?

                Take it easy, rest some more...

                We'll see each other again soon.
                """
            "Who are you...?":
                m """
                A friend.

                An old friend that you seem to can't let go...

                And it's so sad, all this.

                Losing every memories of me...

                And yet, not being able to completely forget.
                """
        """
        You feel a tear falling slowly.

        Its warmth melts the ice that has frozen your heart.

        It's strange, but you feel as if an image is appearing in your mind.

        But it's still faded, as the scene that slowly disappears.
        """
        stop music fadeout (3)
        jump narrator3

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################START PASSAGE 3 #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label narrator3:
    show black
    with fadehold
    """
    You're now ready to go back to your room, aren't you?

    Well, I'm afraid things are not so simple.

    You see, each one of us tries to hide something away.

    Some kind of pain we want to lose.

    Painful feelings, memories or even both of them.

    After all, pain, feelings and memories are strictly connected.

    And it's clear to me that you can't obtain your memories back because something blocks them.

    A rather...painful event? Or a dark memory...a sad one.

    But...

    It seems you're not listening to what I'm saying.

    Not carefully, at least.

    Maybe it's something about me...

    I don't know, maybe my voice or something like that.

    Or maybe...

    Are you getting bored, perhaps?
    """
    menu:
        "Yes.":
            """
            Hmmm...

            I guess that's understandable.

            Maybe you need some 'excitement', huh?

            Let's try something a little different, then.
            """
        "What...?":
            """
            Oh, come on.

            I'm just playing with you a little.

            Can't I?

            After all, that's why you are here, right?

            So, now, let's play something a little different.
            """
        "No":
            """
            I guess that's fine, then.

            No boredom is good.

            But I'm all up for excitement, today.

            So let's make a little experiment.
            """
    """
    Let's make a little experiment, shall we?

    Not that you have any kind of choice, of course.

    You do it or you just go away, that's all.

    But anyway...

    There is a woman, in your life.

    You've known her for so much time...

    Yet you remember nothing about her, now.

    She said she'll help you, no matter what.

    And she said that with a strong and sincere smile on your face.

    But what about you?

    What do you think?

    Do you trust her?
    """
    menu:
        "I do.":
            """
            To trust her...

            Or not.

            A nice question, huh?

            One that a narrator should never do.

            As it's true that narrator should never interfere with the story or the characters.

            But something about you moved me.

            Your dreams...your memories...seem to be so sad.

            And sad memories are the sweetest ones.

            The dearest ones.

            And it seems you're a rather simple and sincere person.

            That's really something. At least for now.
            """
        "I don't.":
            """
            Seems like you listened to me, after all...

            Doubt is the only thing you'll achieve, here.

            That really is true.

            But...only if you care to interpret what happens.

            Interpretation is semplicity's killer.

            The more you'll try to understand, the more you'll doubt and the less simple everything will appear to you.

            If you want to truly try to interpret or not...

            Well, that's up to you.

            I'm just here to look at the path you choose.
            """
    """
    Well, now I think it's time for you to go back.

    Please, enjoy yourself some more in your room.
    """
    play music "roombgm.ogg" fadein (3)
    scene roomd_night
    with fadehold
    $ mood = 50
    $ menthealth = 0
    $ sofiatalk = False
    $ windowseen = False
    $ books = False
    $ trash = False
    $ plant = False
    if menth >= 6:
        scene roomd_night
        with fadehold
        """
        As you wake up you feel calm.

        It's night.

        You don't know the hour, but it seems to be very late.

        The light coming through the windows is weak and paints everything in deep blue shadows.

        How beautiful, you think, to see such beauty in front of you.

        You're not afraid, even though what you just experienced.

        You're starting to get used to this feeling.

        This strange sensation of sadness and longing which you still can't completely understand.
        """
    if menth <= 4:
        scene black
        with fadehold
        """
        A headache.

        Strong.

        As you wake up, it's the first thing you realize.

        Even before noticing it's night.
        """
        scene roomd_night
        with fadehold
        """
        You can't really understand why, but the silence and dark colours in the room scare you.

        You feel completely alone.

        Even more than you did before.

        And as you notice there is only one source of light in the entire apartment...

        You turn to it.

        Desperately.
        """
    if menth == 5:
        """
        You wake up in the middle of the night.

        Alone, as always.

        Finding yourself surrounded by silence.

        There's almost no light and the few there is colours the apartment in deep shades of blue.

        Long shadows casted from every object.

        And a total sense of solitude that resonates with your heart...
        """
    jump roomdownscreen3

label roomdown3:
    scene roomu_night
    $ renpy.pause(0.5)
    scene roomd_night
    with fade
    $ renpy.pause(1)
    jump roomdownscreen3
label roomdownscreen3:
    scene roomd_night
    call screen roomdownscreen3

label roomup3:
    scene roomd_night
    $ renpy.pause(0.5)
    scene roomu_night
    with fade
    $ renpy.pause(1)
    jump roomupscreen3
label roomupscreen3:
    scene roomu_night
    call screen roomupscreen3

label window3:
    if sofiatalk == False:
        """
        From the window you can see the stars.

        They shine through the dark and calm sky.

        It's a kind of melancholic sight.
        """
    if windowseen == True:
        "Already watched."
    if sofiatalk == True:
        $ mood += 5
        $ windowseen = True
    jump roomdownscreen3
label bed3:
    """
    You just woke up, so you're not tired.
    """
    jump roomupscreen3
label books3:
    if sofiatalk == False:
        """
        In the night's pale light, the library seems different.

        It's a strange sensation, but it's as if everything in it has become more sad than before.

        All the books' titles...

        You still can't recognize many of them but the words have become...

        Different.

        As if melancholy has caught them.
        """
    if books == True:
        "Already read."
    if sofiatalk == True:
        $ mood += 5
        $ books = True
    jump roomdownscreen3
label plant3:
    if sofiatalk == False:
        """
        You still wonder which flowers will grow.

        And as you look at the plant, you feel some kind of distant calling.

        A soft voice that whispers your name, smiling.

        Strangely, you turn towards the computer.
        """
    if plant == True:
        "Already watered."
    if sofiatalk == True:
        $ mood += 5
        $ plant = True
    jump roomdownscreen3
label trash3:
    if sofiatalk == False:
        """
        Just a normal trash bin.

        Even though everything looks sadder...

        There's still nothing special about it.
        """
    if trash == True:
        "Alteady tossed."
    if sofiatalk == True:
        $ mood += 5
        $ trash = True
    jump roomdownscreen3
label phone3:
    """
    Maybe you could call someone...

    But there really isn't anyone to call.
    """
    jump roomdownscreen3
label tv3:
    """
    There's a strange danish tv series...

    It's entirely set in a hospital.

    An old man is now on the hospital's roof.

    He screams about how much he hates Denmark.
    """
    jump roomdownscreen3
label cds3:
    """
    You look closely at it.

    There are a lot of albums of a band named...'Tool'.

    Interesting.
    """
    jump roomdownscreen3
label toy3:
    """
    You're starting to accept it.

    After all, it's a nice teddy bear.
    """
    jump roomupscreen3
label mirror3:
    """
    You keep looking at it.

    Yet there's only you.

    Is the view so pleasant?
    """
    jump roomupscreen3
label guit3:
    """
    An old classic guitar.

    If you close your eyes and listen to the silence...

    You can faintly hear some chords playing in the wind.
    """
    jump roomupscreen3

label computer3:
    if sofiatalk == False:
        jump sofianeut3
    if sofiatalk == True and mood >= 55:
        jump sofiagood3
    if sofiatalk == True and mood <= 45:
        jump sofiasad3
    if sofiatalk == True and mood == 50:
        jump sofianeutmood3
label sofiagood3:
    scene gmood_sneut_ni
    with slowfade
    s "I see you're doing fine, today!"
    scene roomd_night
    with slowfade
    $ renpy.pause(1)
    jump roomdownscreen4
label sofiasad3:
    scene smood_sbad_ni
    with slowfade
    s "You look so sad..."
    scene roomd_night
    with slowfade
    $ renpy.pause(1)
    jump roomdownscreen4
label sofianeutmood3:
    scene neutmood_sbad_ni
    with slowfade
    s "You should distract yourself a little."
    scene roomd_night
    with slowfade
    $ renpy.pause(1)
    jump roomdownscreen4
label sofianeut3:
    scene neutmood_sneut_ni
    with slowfade
    $ sofiatalk = True
    """
    You calmly sit at your desk.

    The computer is already turned on, as always.

    Sofia is still there.

    She hasn't abandoned you and waits smiling, gently.
    """
    s "Welcome back again."
    show black
    with fadehold
    stop music fadeout (3)
    return

    if mood >= 55:
        jump sofiagoodfade3
    if mood <= 45:
        jump sofiasadfade3


label door3:
    if mood >= 46 and mood <= 54:
        "I can't get outside, it's tightly closed."
        jump roomdownscreen3
    if mood <= 45:
        scene trauma
        with slowfade
        $ trauma += 1
        """
        trauma
        """
    elif mood >= 55:
        scene mem
        with slowfade
        $ mem += 1
        """
        memory
        """

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################START PASSAGE 4 #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label narrator4:
    show black
    with fadehold
    """
    a
    """
    play music "roombgm.ogg" fadein (3)
    scene roomd_night
    with fadehold
    $ mood = 45
    $ menthealth = 0
    $ sofiatalk = False
    $ windowseen = False
    $ books = False
    $ trash = False
    $ plant = False
    $ ghost = True
    if menth >= 7:
        scene roomd_ghosts
        with fadehold
        """
        a
        """
    if menth == 3:
        scene roomd_ghosts
        with fadehold
        """
        a
        """
        """
        a
        """
        jump pass4ghosts
    if menth >= 4 and menth <= 6:
        scene roomd_ghosts
        with fadehold
        """
        a
        """
    jump roomdownscreen4

label roomdown4:
    if ghost == True:
        scene roomu_ghosts
        $ renpy.pause(0.5)
        scene roomd_ghosts
        with fade
        $ renpy.pause(1)
        jump roomdownscreen4g
    if ghost == False:
        scene roomu_ev
        $ renpy.pause(0.5)
        scene roomd_ev
        with fade
        $ renpy.pause(1)
        jump roomdownscreen4
label roomdownscreen3:
    if ghost == True:
        scene roomd_ghosts
        call screen roomdownscreen4g
    if ghost == False:
        scene roomd_ev
        call screen roomdownscreen4

label roomup3:
    if ghost == True:
        scene roomd_ghosts
        $ renpy.pause(0.5)
        scene roomu_ghosts
        with fade
        $ renpy.pause(1)
        jump roomupscreen4g
    if ghost == False:
        scene roomd_ev
        $ renpy.pause(0.5)
        scene roomu_ev
        with fade
        $ renpy.pause(1)
        jump roomupscreen4
label roomupscreen4:
    if ghost == True:
        scene roomu_ghosts
        call screen roomupscreen4g
    if ghost == False:
        scene roomu_ev
        call screen roomupscreen4

label window4:
    if sofiatalk == False:
        """
        From the window you can see the stars.

        They shine through the dark and calm sky.

        It's a kind of melancholic sight.
        """
    if sofiatalk == True and ghost == True:
        $ mood -= 5
        $ windowseen = True
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ windowseen = True
    jump roomdownscreen4
label bed4:
    if sofiatalk == False:
        """
        You just woke up, so you're not tired.
        """
        jump roomupscreen4
    if sofiatalk == True:
        """
        Do you want to sleep?
        """
        menu:
            "Yes.":
                $ ghost = False
                $ mood -= 10
                scene roomu_ev
                "Everything seems fine, now."
            "No.":
                "You're ok as you are."
        jump roomupscreen4
label books4:
    if sofiatalk == False:
        """
        In the night's pale light, the library seems different.

        It's a strange sensation, but it's as if everything in it has become more sad than before.

        All the books' titles...

        You still can't recognize many of them but the words have become...

        Different.

        As if melancholy has caught them.
        """
    if sofiatalk == True and ghost == True:
        $ mood -= 5
        $ books = True
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ books = True
    jump roomdownscreen4
label plant4:
    if sofiatalk == False:
        """
        You still wonder which flowers will grow.

        And as you look at the plant, you feel some kind of distant calling.

        A soft voice that whispers your name, smiling.

        Strangely, you turn towards the computer.
        """
    if sofiatalk == True and ghost == True:
        $ mood -= 5
        $ plant = True
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ plant = True
    jump roomdownscreen4
label trash4:
    if sofiatalk == False:
        """
        Just a normal trash bin.

        Even though everything looks sadder...

        There's still nothing special about it.
        """
    if sofiatalk == True and ghost == True:
        $ mood -= 5
        $ trash = True
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ trash = True
    jump roomdownscreen4
label phone4:
    """
    Maybe you could call someone...

    But there really isn't anyone to call.
    """
    jump roomdownscreen4
label tv4:
    """
    There's a strange danish tv series...

    It's entirely set in a hospital.

    An old man is now on the hospital's roof.

    He screams about how much he hates Denmark.
    """
    jump roomdownscreen4
label cds4:
    """
    You look closely at it.

    There are a lot of albums of a band named...'Tool'.

    Interesting.
    """
    jump roomdownscreen4
label toy4:
    """
    You're starting to accept it.

    After all, it's a nice teddy bear.
    """
    jump roomupscreen4
label mirror4:
    """
    You keep looking at it.

    Yet there's only you.

    Is the view so pleasant?
    """
    jump roomupscreen4
label guit4:
    """
    An old classic guitar.

    If you close your eyes and listen to the silence...

    You can faintly hear some chords playing in the wind.
    """
    jump roomupscreen4

label computer4:
    if sofiatalk == False:
        jump sofianeut4
    if sofiatalk == True and mood >= 55:
        jump sofiagood4
    if sofiatalk == True and mood <= 45:
        jump sofiasad4
    if sofiatalk == True and mood == 50:
        jump sofianeutmood4
label sofiagood4:
    if ghost == True:
        scene gmood_sbad_gh
        with slowfade
        s "I see you're doing fine, today!"
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
    if ghost == False:
        scene gmood_sgood_ev
        with slowfade
        s "a"
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
label sofiasad4:
    if ghost == True:
        scene smood_sbad_gh
        with slowfade
        s "I see you're doing fine, today!"
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
    if ghost == False:
        scene smood_sbad_ev
        with slowfade
        s "a"
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
label sofianeutmood4:
    if ghost == True:
        scene neutmood_sbad_gh
        with slowfade
        s "I see you're doing fine, today!"
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
    if ghost == False:
        scene neutmood_sneut_ev
        with slowfade
        s "a"
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
label sofianeut4:
    scene smood_sbad_gh
    with slowfade
    $ sofiatalk = True
    """
    You calmly sit at your desk.

    The computer is already turned on, as always.

    Sofia is still there.

    She hasn't abandoned you and waits smiling, gently.
    """
    s "Welcome back again."
    if mood >= 55:
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
    if mood <= 45:
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4


label door4:
    if mood >= 29 and mood <= 69:
        "I can't get outside, it's tightly closed."
        jump roomdownscreen4
    if mood <= 30:
        scene trauma
        with slowfade
        $ trauma += 1
        """
        trauma
        """
    elif mood >= 70:
        scene mem
        with slowfade
        $ mem += 1
        """
        memory
        """

    show black
    with fadehold
    stop music fadeout (3)
    return
