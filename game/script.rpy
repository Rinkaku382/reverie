﻿define slowfade = Fade(1.0, 0, 3.0)
define slowerfade = Fade (3.0, 0, 3.0)
define slowdissolve = Dissolve(1.0)
define fadehold = Fade(3.0, 1.0, 3.0)
define config.hard_rollback_limit = 0

define s = Character("Sofia", color="#C69AF9")
define ug = Character("Unknown Girl", color="#C69AF9")
define stm = Character("Strange Man", color="#7BC2F4")
define scm = Character("Scary Man", color="#ED5259")


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
    s """
    I'm here to help you.

    We know each other very well, but you've lost your memory, so...

    But don't worry.

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
            if mood <= 40:
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
    show narrator
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
    $ strangeman = False
    $ scaryman = False
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
        $ scaryman = True
        """
        The dark place again.

        It seems different yet similar than last time.

        The strange, scary man is still there.

        He still watches you.

        Between the shadows, you have the impression he's pointing his finger at you.
        """
        scm """
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
        $ strangeman = True
        stm """
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
        stm """
        Do you remember this poem?

        It brings back so many memories...

        Yet, you don't seem to recall any of them...

        That makes me sad.

        So sad...
        """
        menu:
            "This place...":
                stm """
                It rings some bell?

                It does, right?

                But I guess you still aren't ready.

                Memories can't come back in a second, you know?

                Take it easy, rest some more...

                We'll see each other again soon.
                """
            "Who are you...?":
                stm """
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
    show narrator
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
    $ sofiatalk = False
    $ windowseen = False
    $ books = False
    $ trash = False
    $ plant = False
    $ letter = False
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
    if windowseen == False and sofiatalk == True:
        """
        It'a late night.

        Outside the window you see darkness and dim lights.
        """
        menu:
            "Watch more carefully.":
                $ mood += 5
                $ windowseen = True
                """
                The street outside is empty.

                Everything is silent, illuminated by numerous street lights.

                There is a deep beauty in this scenary.

                From your window you can see lots of other apartments.

                The lights behind their windows are on, so you wonder...

                What are all those people doing so late at night?
                """
            "Step back.":
                """
                Deciding to not watch outside, you step back from the window.

                Around you the night's shadows make the apartment looks empty.
                """
    if windowseen == True:
        "Everything still looks calm."
    jump roomdownscreen3
label bed3:
    """
    You just woke up, so you're not tired.
    """
    jump roomupscreen3
label books3:
    if sofiatalk == False:
        """
        You're not so much in the mood for reading, now.
        """
    if books == False and sofiatalk == True:
        """
        In the night's pale light, the library seems different.

        It's a strange sensation, but it's as if everything in it has become more sad than before.

        All the books' titles...

        You still can't recognize many of them but the words have become...

        Different.

        As if melancholy has caught them.

        One title, though, attracts you.

        'No longer human'.

        It seems gloomy, from the cover.

        It sends to you shivers, coming from your deepest memories.
        """
        menu:
            "Read a passage.":
                $ mood -= 5
                $ books = True
                """
                You open it and leaf through, searching for something.

                As the pages pass by, you realize there might be something for you, in there.

                Then you find it.

                'The weak fear happiness itself.'

                'They can harm themselves on cotton wool.'

                'Sometimes they are wounded even by happiness.'

                The sensation ends. Now, you feel slightly sadder than before.

                A block has taken form in your heart.
                """
            "Put it back.":
                """
                The scary sensation the book gives you convinces you to put it back on the shelf.

                As your fingers no longer hold it, you feel better.
                """
    if windowseen == True:
        "Everything still looks calm."
    jump roomdownscreen3
label plant3:
    if sofiatalk == False:
        """
        As you look at the plant, you feel some kind of distant calling.

        A soft voice that whispers your name, smiling.

        Strangely, you turn towards the computer.
        """
    if plant == False and sofiatalk == True:
        """
        The plant seems to be flooded by melancholic waves, just like the entire apartment.

        While watching it, you wonder which flowers will grow.

        Then you realize it needs water.
        """
        menu:
            "Water it.":
                $ mood += 5
                $ plant = True
                """
                Just as you pour the water in the vase, the plant seems to rejoice instantly.

                It's a nice feeling.

                Calm, and tender.
                """
            "Not now...":
                "You step away, turning back towards the room."
    if plant == True:
        "You're filled with expectations everytime you watch it."
    jump roomdownscreen3
label trash3:
    if sofiatalk == False:
        """
        Just a normal trash bin.

        Even though everything looks sadder...

        There's still nothing special about it.
        """
    if trash == False and sofiatalk == True:
        """
        Looks like it keeps filling.

        It's just unbelievable how much trash can pile and pile up.
        """
        menu:
            "Toss everything away.":
                $ mood += 5
                $ trash = True
                "The apartment already looks cleaner, now."
            "Leave it there, for now.":
                """
                Maybe later...

                Or maybe tomorrow, who knows.
                """
    if trash == True:
        "It's empty."
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
    s "Everytime I see you happy, my heart starts pounding very fast!"
    scene roomd_night
    with slowfade
    $ renpy.pause(1)
    jump roomdownscreen4
label sofiasad3:
    scene smood_sbad_ni
    with slowfade
    s """
    You look very sad...

    Please, hang in there, ok?
    """
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
    if strangeman == True:
        scene neutmood_sneut_ni
        with slowfade
        $ sofiatalk = True
        """
        You calmly sit at your desk.

        The computer is already turned on, as always.

        Sofia is still there.

        She hasn't abandoned you and waits smiling, gently.
        """
        s """
        Welcome back again.

        How did it go, this time?
        """
        menu:
            "I...don't know...":
                $ mood -= 5
                s "Did something happen?"
            "I feel strange.":
                $ mood += 5
                s "Well, I'm here for you, so..."
        s "Do you want to talk about it?"
        menu:
            "My memories...":
                menu:
                    "I'm scared by them.":
                        scene smood_sbad_ni
                        with dissolve
                        $ mood -= 10
                        menu:
                            "I just don't understand.":
                                $ mood -= 10
                                s """
                                I don't think you should be scared...

                                I can only imagine how difficult this all is, but...

                                You know I'm here for you, right?

                                We can work this out...together?

                                You know...I realize it's not easy at all to trust me...

                                I mean, I'm talking with you about all this but after all you don't remember who I am.

                                And it might be strange or shady, to listen to someone that talks to you like this.

                                But please, try to not surrender to the situation!

                                It's easy to do that, when we're alone, but...
                                """
                                scene smood_sneut_ni
                                with dissolve
                                """
                                Just resist, ok? And trust your choices.

                                And me, if you can.
                                """
                            "What should I do?":
                                $ mood -= 5
                                s """
                                Well...

                                I realize it's not simple at all.

                                But I think you're doing good.

                                I'm afraid I can't tell you much about it, since our relation developed only online, but...
                                """
                    "This seems so pointless.":
                        $ mood -= 10
                        menu:
                            "Just...who am I?":
                                $ mood -= 5
                                s "Well..."
                            "Is this all I can do?":
                                $ mood -= 10
                                s """
                                Sincerely...

                                I really don't know, I'm sorry.

                                I think the only thing you can do i trust yourself and your choices.

                                It's the only way you can be free from those images...

                                And, if you want to...

                                You can also trust me.

                                I know it's not easy to trust someone that you don't even remember.

                                Especially in a situation like this.

                                But please, let me help you.
                                """
                                scene smood_sneut_ni
                                with dissolve
                                """
                                Oh, I know...!
                                """
    if scaryman == True:
        scene smood_sbad_ni
        with slowfade
        s """
        Hi there...!

        Oh, you are shaking! What happened?
        """
        if trauma >= 2:
            menu:
                "I saw that man again...":
                    s "Oh...I guess it wasn't something nice..."
        if trauma == 1:
            menu:
                "There was this man...":
                    s "A man?"
        menu:
            "Tell me, who is he?!":
                s "I don't know! How could I?"
        s "Listen, let's try to figure this out together, ok?"
        menu:
            "How can you not know?":
                menu:
                    "Aren't you my best friend?":
                        $ mood -= 10
                        s """
                        I am, but I don't know everything about you!

                        We...we actually never managed to meet...

                        And we developed our relation only through internet.

                        You never told me many things, and now, of course, you can't do that anymore.

                        Uhmm, I was wandering...
                        """
            "Ok, let's try.":
                scene gmood_sbad_ni
                with dissolve
                $ mood += 5
                s """
                I know I told you I'm your best friend...

                And it's true!

                But we never managed to talk about many things...

                And never managed to see each other outside of this computer too.

                So there are many things I don't know about you.

                And that's part of why I want to help you.

                I want to get closer to you, to know more about you.
                """
        s "I'm really sorry..."
        menu:
            "Don't worry, it's ok.":
                $ mood += 5
                if mood == 50:
                    scene neutmood_sneut_ni
                    with dissolve
                if mood >= 55:
                    scene gmood_sneut_ni
                    with dissolve
                if mood <= 45:
                    scene smood_sneut_ni
                    with dissolve
                s"""
                Thanks...

                Oh, now that I think about it...
                """
            "Of course you are.":
                scene smood_sbad_ni
                with dissolve
                $ mood -= 10
                s """
                Yeah...I am...
                """
                scene smood_sneut_ni
                with dissolve
                """
                Well, anyway...
                """
    s "What if I tell you what I know about you?"
    menu:
        "Uhm sure, why not?":
            s """
            Well, you still attend a writing class at university.

            And you're very good at writing, too!

            I read almost everything you wrote, and I love all of your works.

            Even if you haven't published any!

            But it doesn't matter, because I think you'll be able to do it one day.

            And you often talk about what you feel and how you feel about writing.

            I don' do anything special, so I admire a lot what you do.

            And we spent a lot of nights talking about all this.

            Oh and now that I remember...

            You often talk about your professor!

            He seems like a very important person, to you.
            """
            if mood == 50:
                scene neutmood_sbad_ni
                with dissolve
            if mood >= 55:
                scene gmood_sbad_ni
                with dissolve
            if mood <= 45:
                scene smood_sbad_ni
                with dissolve
            """
            We shared all those things, before you lost your memory...

            I hope this will be useful, out there...

            You know, every time I think about us, I feel a little...sad.
            """
            if mood == 50:
                scene neutmood_sgood_ni
                with dissolve
            if mood >= 55:
                scene gmood_sgood_ni
                with dissolve
            if mood <= 45:
                scene smood_sgood_ni
                with dissolve
            """
            But it's ok, I guess.

            As long as I'm helping you I feel fine.

            But, well...

            I think now it's time for you to go, right?

            See you later!
            """
            scene roomd_night
            with slowfade
            jump roomdownscreen3
        "I prefer not...":
            if mood == 50:
                scene neutmood_sbad_ni
                with dissolve
            if mood >= 55:
                scene gmood_sbad_ni
                with dissolve
            if mood <= 45:
                scene smood_sbad_ni
                with dissolve
            s """
            Oh...

            Yeah, I undestrand...no problem.

            And I guess you should go, now, right?

            See you later.
            """
            scene roomd_night
            with slowfade
            jump roomdownscreen3

label door3:
    if mood >= 46 and mood <= 54:
        "I can't get outside, it's tightly closed."
        jump roomdownscreen3
    if mood <= 45 and trauma == 0:
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
        jump narrator4
    if mood <= 45 and trauma == 1:
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
        scm """
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
        jump narrator4
    if mood <= 45 and trauma == 2:
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
        On the other side of the door, the man is standing still.

        He watches you, silently.

        You're afraid, yet you feel a desire to get closer to him.

        Maybe to understand who he is?
        """
        menu:
            "Just...what do you want from me?":
                """
                He does not answer.

                He's waiting for something, and he continues to look at you.

                Only after some time, he starts talking.
                """
            "What have I done to you?":
                """
                He's still silent.

                The eerie sensation you're feeling keeps on intensifying.

                You'd like to go away.

                To escape from this place.

                But there is no way out.
                """
        scm """
        I was...abandoned.

        Completely...

        Lonely.

        And you stood there.

        Watching

        You didn't do anything...

        To help me.

        You abandoned me.
        """
        menu:
            "I can't remember...":
                scm """
                You...

                ...can't...

                ...remember?
                """
                """
                He stops for some seconds.

                As if he's thinking about something.

                He seems...

                Disappointed?
                """
            "What...abandoned you...?":
                scm """
                You were the most important.

                The only one.

                The best one among them all.

                Yet...

                You...

                Turned your back towards me.
                """
        scm """
        You may not remember.

        But soon...

        You'll be able to.

        And what you've done...

        Will be revealed.
        """
        """
        Shivers of fear run through your spine.

        His eyes are the last thing you see, as the scene starts to...
        """
        stop music fadeout (2)
        scene black
        with slowfade
        """
        Fade away.
        """
        jump narrator4
    if mood >= 55 and mem == 0:
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
        jump narrator4
    elif mood >= 55 and mem == 1:
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
        stm """
        Do you remember this poem?

        It brings back so many memories...

        Yet, you don't seem to recall any of them...

        That makes me sad.

        So sad...
        """
        menu:
            "This place...":
                stm """
                It rings some bell?

                It does, right?

                But I guess you still aren't ready.

                Memories can't come back in a second, you know?

                Take it easy, rest some more...

                We'll see each other again soon.
                """
            "Who are you...?":
                stm """
                A friend.

                An old friend that you can't seem to let go...

                And it's so sad, all this.

                Losing every memory of me...

                And yet, not being able to completely forget.
                """
        """
        You feel a tear falling slowly.

        Its warmth melts the ice that has frozen your heart.

        It's strange, but you feel as if an image is appearing in your mind.

        But it's still faded, as the scene that slowly disappears.
        """
    if mood >= 55 and mem == 2:
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
        You're in the garden.

        In front of you, the strange man is reading, again.
        """
        stm """
        I remember...

        Some time ago.

        Maybe a year, I think.

        When I finished talking, and all the student started to gather their things to go away...

        You came to me, curious about everything I said during the lesson.

        Normally, students just pass by.

        They don't really stay forever.

        But that day I felt...something different.

        I felt as if...somehow, you would have stayed.

        Guess I wasn't right at all...
        """
        menu:
            "What do you mean?":
                stm """
                That you didn't stayed.

                But...I can understand that.

                It's not so simple, to stay in contact with someone.

                Too bad it all happened that time...
                """
        menu:
            "That time?":
                $ letter == True
                stm """
                Yes, a difficult one.

                For me, at least.

                But I can't tell you much about it.

                Every game has a precise rule, and the rule of this game is that you retrieve your memories by yourself.

                Still, that doesn't forbids me from giving you a hint.

                Look carefully into your library.

                Long time ago, I sent you a letter.

                It'a hidden in a book I gave you. A book about dreams.

                Now...goodbye.

                I'm sorry I didn't give you many choices, this time.

                But I'll manage to do better the next time we see each other, ok?
                """
        stop music fadeout (3)
        jump narrator4

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################START PASSAGE 4 #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label narrator4:
    show narrator
    with fadehold
    """
    And here you are, again.

    What was, this time?

    A comfortable memory?

    A scary trauma?

    I wonder...

    But whatever it is, they both bring leftovers with them, in any case.

    But anyway, that does not matter.

    It will matter only when you'll get back to your room.

    I was thinking about something.

    Have you ever wondered what divides fear and serenity?

    Don't worry, I know it's not a simple question.

    So, I'll not wait for your answer.

    But you can answer to this...

    Have you felt safe, until now?
    """
    menu:
        "Yes.":
            """
            Interesting.

            I'm sorry if my questions may seem strange, to you.

            I ask you these questions because I want to know about your experience until this moment.
            """
        "No.":
            """
            We never feel truly safe, right?

            Or maybe we do, but we don't realize it.
            """
    """
    Yet, your answer really tells me something about you.

    And I guess that now it's time to go back to the room...
    """
    play music "roombgm.ogg" fadein (3)
    scene roomd_ghosts
    with fadehold
    $ mood = 50
    $ menth = 5
    $ sofiatalk = False
    $ windowseen = False
    $ books = False
    $ trash = False
    $ plant = False
    $ bed = False
    $ truth = False
    $ ghost = True
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
label roomdownscreen4:
    if ghost == True:
        scene roomd_ghosts
        call screen roomdownscreen4g
    if ghost == False:
        scene roomd_ev
        call screen roomdownscreen4

label roomup4:
    if ghost == True:
        scene roomd_ghosts
        $ renpy.pause(0.5)
        scene roomu_ghosts
        with fade
        $ renpy.pause(1)
        jump roomupscreen4
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
        Everything is dark outside.
        """
    if windowseen == True:
        """
        The scenery hasn't changed.
        """
    if sofiatalk == True and ghost == True:
        """
        From the window, everything is immersed in dark shadows.

        You feel attracted by that darkness, even if you feel it's dangerous.

        It makes your body shiver.
        """
        menu:
            "Look outside.":
                $ mood -= 5
                $ windowseen = True
                """
                As you look outside, the shivers infensify.

                You feel worst than before.

                As if the darkness that covers everything outside has penetrated your heart.
                """
            "Step back.":
                """
                Stepping back from it the bad feeling you had softly disappears.
                """
    if sofiatalk == True and ghost == False:
        """
        It looks like a simple and solitary evening.

        Soft colours come from the window.
        """
        menu:
            "Look outside.":
                $ mood += 5
                $ windowseen = True
                """
                Few people's shadows on the street.

                Wind is blowing through the trees, which slowly dance.

                It's so peaceful...
                """
            "Step back.":
                """
                You turn away, looking at the room and thinking about what to do.
                """
    jump roomdownscreen4
label bed4:
    if sofiatalk == False or bed == True:
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
                $ bed = True
                $ mood -= 10
                scene roomu_ev
                "Everything seems fine, now."
            "No.":
                "You bravely step away."
        jump roomupscreen4
label books4:
    if sofiatalk == False:
        """
        From the library come an ominous feeling.
        """
    if books == True:
        "You've already read enough."
    if sofiatalk == True and ghost == True:
        """
        Even though you feel bad, looking at the library...

        There is a book that caughts your attention.

        Do you read it?
        """
        menu:
            "I do.":
                $ mood -= 5
                $ books = True
                if letter == False:
                    """
                    You grab the book, which title is impossible to be read.

                    An old collection of poems.

                    You decide to read the first one.

                    'Solitary smiles.'

                    'Lonely souls.'

                    'This is everything you can see.'

                    'A perfect reflection'

                    'Of yourself.'
                    """
                if letter == True:
                    $ truth == True
                    $ mood += 5
                    $ books = True
                    """
                    The words of the man in your memories come to your mind.

                    A book about dreams.

                    And there it is, next to the one you intended to take.

                    It's simply titled 'Dreams'.

                    A collection of short stories, it seems.

                    You open it and find the letter. It's darkened by time.

                    Or maybe it seems dark because of the atmosphere in the room.

                    It's already opened, so you start reading it.
                    """
                    stm """
                    My dear friend...

                    It seems this is my last gift for you.

                    My favourite student.

                    I wonder, how many words won't be exchanged ever again, in that garden?

                    It lasted only for few years.

                    Yet, it was so peaceful that I completely lost myself in it.

                    We were both alone. Bot in search of a companion soul.

                    Me and you.

                    But we know it can't continue, right?

                    It seems I made some mistakes. And you don't trust me anymore.

                    But I understand. It's not simple at all, for you.

                    I hope we'll see each other again, one day.

                    Now, I'll simply go, far away from here. From the memories this place holds for me.

                    But please, don't feel guilty for stepping away from me.

                    If you will, the memories and remorse will be inescapable.

                    Walk the right path.

                    Don't fall into your feeling's trap.

                    With love...your old professor, Andrei.
                    """
            "I don't.":
                """
                You turn away, looking at the room and thinking about what to do.
                """
    if sofiatalk == True and ghost == False:
        """
        You look at the library, finding an interesting book.

        Do you read it?
        """
        menu:
            "I do.":
                if letter == False:
                    $ mood += 5
                    $ books = True
                    """
                    You grab the book, which title is impossible to be read.

                    An old collection of poems.

                    You decide to read the third one.

                    'The expression on my grandfather's face.'

                    'The pale shadows of those gone before him.'

                    'And those who'll be gone after him.'

                    'They are all beside me.'

                    'Loneliness fades away.'
                    """
                if letter == True:
                    $ mood += 5
                    $ books = True
                    $ truth == True
                    """
                    The words of the man in your memories come to your mind.

                    A book about dreams.

                    And there it is, next to the one you intended to take.

                    It's simply titled 'Dreams'.

                    A collection of short stories, it seems.

                    You open it and find the letter. It's darkened by time.

                    Or maybe it seems dark because of the atmosphere in the room.

                    It's already opened, so you start reading it.
                    """
                    stm """
                    My dear friend...

                    It seems this is my last gift for you.

                    My favourite student.

                    I wonder, how many words won't be exchanged ever again, in that garden?

                    It lasted only for few years.

                    Yet, it was so peaceful that I completely lost myself in it.

                    We were both alone. Bot in search of a companion soul.

                    Me and you.

                    But we know it can't continue, right?

                    It seems I made some mistakes. And you don't trust me anymore.

                    But I understand. It's not simple at all, for you.

                    I hope we'll see each other again, one day.

                    Now, I'll simply go, far away from here. From the memories this place holds for me.

                    But please, don't feel guilty for stepping away from me.

                    If you will, the memories and remorse will be inescapable.

                    Walk the right path.

                    Don't fall into your feeling's trap.

                    With love...your old professor, Andrei.
                    """
            "I don't.":
                """
                You turn away, looking at the room and thinking about what to do.
                """
    jump roomdownscreen4
label plant4:
    if sofiatalk == False:
        """
        Even the plant now seems sadder in this darkness.

        You feel bad only by looking at it.
        """
    if plant == True:
        """
        You wonder when it'll grow.
        """
    if sofiatalk == True and ghost == True:
        """
        There seems to be a lot of dust on it.

        And that sensation of sadness doesn't seem to leave the plant.

        Do you clean it?
        """
        menu:
            "Yes.":
                $ mood -= 5
                $ plant = True
                """
                You have the impression that the dust on it remains on your hand.

                And from it a strange sensation comes.

                As if your whole body has become heavier.

                A weight you can't sustain.
                """
            "Not now.":
                "You look away, still with a bad feeling."
    if sofiatalk == True and ghost == False:
        """
        It's strange...

        There seems to be a lot of dust on it.

        Do you clean it?
        """
        menu:
            "Yes.":
                $ mood += 5
                $ plant = True
                """
                Now it shines, a bright green as usual.
                """
            "Not now.":
                "Maybe later."
    jump roomdownscreen4
label trash4:
    if sofiatalk == False:
        """
        Even in this darkness...

        The trashbin remains a normal trashbin.
        """
    if trash == True:
        "You feel better now that it's empty."
    if sofiatalk == True and ghost == True:
        """
        Even in this darkness...

        The trashbin remains a normal trashbin.
        """
    if sofiatalk == True and ghost == False:
        """
        Looking closely...

        You still have to toss the trash.
        """
        menu:
            "Toss it.":
                $ mood += 5
                $ trash = True
                "You toss it right away."
            "Not now.":
                "Maybe another time."
    jump roomdownscreen4
label phone4:
    if ghost == True:
        """
        You want to call someone.

        But you don't remember any phone number.

        You're left almost completely alone.
        """
    if ghost == False:
        """
        You wonder...

        What if you toss this phone away?

        After all, there's never anyone to call.
        """
    jump roomdownscreen4
label tv4:
    if ghost == True:
        """
        Only a black mirror.
        """
    if ghost == False:
        """
        You don't now how, but the tv is now on.

        On the screen there is a silent scene.

        A boy and a girl are watching the sea, without talking.

        It seems peaceful.
        """
    jump roomdownscreen4
label cds4:
    if ghost == True:
        """
        The usual pile of CDs.
        """
    if ghost == False:
        """
        You look at all the CDs' titles.

        But none attracts you.
        """
    jump roomdownscreen4
label toy4:
    if ghost == True:
        """
        Only bad memories come from it.

        You wish it wasn't here.
        """
    if ghost == False:
        """
        Everytime you watch it, now, it makes you smile.
        """
    jump roomupscreen4
label mirror4:
    if ghost == True:
        """
        Are you looking at yourself?
        """
    if ghost == False:
        """
        Same old you.
        """
    jump roomupscreen4
label guit4:
    if ghost == True:
        """
        It's silent.
        """
    if ghost == False:
        """
        Sometimes you'd like to remember how to play it.
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
        s "You seem to be happy...despite all, I guess."
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
    if ghost == False:
        scene gmood_sgood_ev
        with slowfade
        s "Is that a smile I'm seeing?"
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
label sofiasad4:
    if ghost == True:
        scene smood_sbad_gh
        with slowfade
        s "Uhmm, maybe you should rest for a while...?"
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
    if ghost == False:
        scene smood_sbad_ev
        with slowfade
        s "It seems you're feeling very bad..."
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
label sofianeutmood4:
    if ghost == True:
        scene neutmood_sbad_gh
        with slowfade
        s "I think you should rest..."
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
    if ghost == False:
        scene neutmood_sneut_ev
        with slowfade
        s """
        It seems like you're a little down.

        Come on, there are lots of things you can do in there!
        """
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen4
label sofianeut4:
    scene neutmood_sneut_gh
    with slowfade
    $ sofiatalk = True
    s "Welcome back!"
    menu:
        "What is happening?":
            s """
            Uhmm, what do you mean?

            What should be happening?
            """
            menu:
                "It's all dark in here...":
                    $ mood -= 5
                    s """
                    Dark...?

                    It all seems normal to me.

                    But I guess you're not lying...

                    Why should you, after all...?
                    """
                "You really can't see it?":
                    $ mood += 5
                    s """
                    Uhm no, I'm sorry...

                    But really, what's wrong?
                    """
                    menu:
                        "The entire apartment is...strange. Darker.":
                            s """
                            That's very strange...it appears completely normal to me.
                            """
        "Why are you so happy?":
            s """
            aaa
            """
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
    jump narrator5

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################START PASSAGE 5 #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
label narrator5:
    show narrator
    with fadehold
    """
    aaa
    """
    play music "roombgm.ogg" fadein (3)
    scene
    with fadehold
    $ mood = 45
    $ sofiatalk = False
    $ windowseen = False
    $ books = False
    $ trash = False
    $ plant = False
    $ ghost = True
    if menth >= 6:
        scene roomd_
        with fadehold
        """
        aaa
        """
    if menth <= 4:
        scene roomd_ghosts
        with fadehold
        """
        a
        """
    jump roomdownscreen5

label roomdown5:
    if ghost == True:
        scene roomu_ghosts
        $ renpy.pause(0.5)
        scene roomd_ghosts
        with fade
        $ renpy.pause(1)
        jump roomdownscreen5g
    if ghost == False:
        scene roomu_ev
        $ renpy.pause(0.5)
        scene roomd_ev
        with fade
        $ renpy.pause(1)
        jump roomdownscreen5
label roomdownscreen5:
    if ghost == True:
        scene roomd_ghosts
        call screen roomdownscreen5g
    if ghost == False:
        scene roomd_ev
        call screen roomdownscreen5

label roomup5:
    if ghost == True:
        scene roomd_ghosts
        $ renpy.pause(0.5)
        scene roomu_ghosts
        with fade
        $ renpy.pause(1)
        jump roomupscreen5g
    if ghost == False:
        scene roomd_ev
        $ renpy.pause(0.5)
        scene roomu_ev
        with fade
        $ renpy.pause(1)
        jump roomupscreen5
label roomupscreen5:
    if ghost == True:
        scene roomu_ghosts
        call screen roomupscreen5g
    if ghost == False:
        scene roomu_ev
        call screen roomupscreen5

label window5:
    if sofiatalk == False:
        """
        From the window you can see the stars.

        They shine through the dark and calm sky.

        It's a kind of melancholic sight.
        """
    if sofiatalk == True and ghost == True:
        $ mood -= 5
        $ windowseen = True
        jump roomdownscreen5g
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ windowseen = True
        jump roomdownscreen5
label bed5:
    if sofiatalk == False:
        """
        You just woke up, so you're not tired.
        """
        jump roomupscreen5
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
        jump roomupscreen5
label books5:
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
        jump roomdownscreen5g
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ books = True
        jump roomdownscreen5
label plant5:
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
        jump roomdownscreen5g
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ plant = True
        jump roomdownscreen5
label trash5:
    if sofiatalk == False:
        """
        Just a normal trash bin.

        Even though everything looks sadder...

        There's still nothing special about it.
        """
    if sofiatalk == True and ghost == True:
        $ mood -= 5
        $ trash = True
        jump roomdownscreen5g
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ trash = True
        jump roomdownscreen5
label phone5:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomdownscreen5g
    if ghost == False:
        """
        aaa
        """
        jump roomdownscreen5
label tv5:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomdownscreen5g
    if ghost == False:
        """
        aaa
        """
        jump roomdownscreen5
label cds5:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomdownscreen5g
    if ghost == False:
        """
        aaa
        """
        jump roomdownscreen5
label toy5:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomupscreen5g
    if ghost == False:
        """
        aaa
        """
        jump roomupscreen5
label mirror5:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomupscreen5g
    if ghost == False:
        """
        aaa
        """
        jump roomupscreen5
label guit5:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomupscreen5g
    if ghost == False:
        """
        aaa
        """
        jump roomupscreen5

label computer5:
    if sofiatalk == False:
        jump sofianeut5
    if sofiatalk == True and mood >= 55:
        jump sofiagood5
    if sofiatalk == True and mood <= 45:
        jump sofiasad5
    if sofiatalk == True and mood == 50:
        jump sofianeutmood5
label sofiagood5:
    if ghost == True:
        scene gmood_sbad_gh
        with slowfade
        s "I see you're doing fine, today!"
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen5
    if ghost == False:
        scene gmood_sgood_ev
        with slowfade
        s "a"
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen5
label sofiasad5:
    if ghost == True:
        scene smood_sbad_gh
        with slowfade
        s "I see you're doing fine, today!"
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen5
    if ghost == False:
        scene smood_sbad_ev
        with slowfade
        s "a"
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen5
label sofianeutmood5:
    if ghost == True:
        scene neutmood_sbad_gh
        with slowfade
        s "I see you're doing fine, today!"
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen5
    if ghost == False:
        scene neutmood_sneut_ev
        with slowfade
        s "a"
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen5
label sofianeut5:
    scene smood_sbad_gh
    with slowfade
    $ sofiatalk = True
    """
    You calmly sit at your desk.

    The computer is already turned on, as always.

    Sofia is still there.

    She hasn't abandoned you and waits smiling, gently.
    """
    s ""
    if mood >= 55:
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen5
    if mood <= 45:
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen5


label door5:
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
    jump narrator6

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################START PASSAGE 6 #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label narrator6:
    show black
    with fadehold
    """
    aaa
    """
    play music "roombgm.ogg" fadein (3)
    scene
    with fadehold
    $ mood = 45
    $ sofiatalk = False
    $ windowseen = False
    $ books = False
    $ trash = False
    $ plant = False
    $ ghost = True
    if menth >= 6:
        scene roomd_
        with fadehold
        """
        aaa
        """
    if menth <= 4:
        scene roomd_ghosts
        with fadehold
        """
        aaa
        """
    jump roomdownscreen6

label roomdown6:
    if ghost == True:
        scene roomu_ghosts
        $ renpy.pause(0.5)
        scene roomd_ghosts
        with fade
        $ renpy.pause(1)
        jump roomdownscreen6g
    if ghost == False:
        scene roomu_ev
        $ renpy.pause(0.5)
        scene roomd_ev
        with fade
        $ renpy.pause(1)
        jump roomdownscreen6
label roomdownscreen6:
    if ghost == True:
        scene roomd_ghosts
        call screen roomdownscreen6g
    if ghost == False:
        scene roomd_ev
        call screen roomdownscreen6

label roomup6:
    if ghost == True:
        scene roomd_ghosts
        $ renpy.pause(0.5)
        scene roomu_ghosts
        with fade
        $ renpy.pause(1)
        jump roomupscreen6g
    if ghost == False:
        scene roomd_ev
        $ renpy.pause(0.5)
        scene roomu_ev
        with fade
        $ renpy.pause(1)
        jump roomupscreen6
label roomupscreen6:
    if ghost == True:
        scene roomu_ghosts
        call screen roomupscreen6g
    if ghost == False:
        scene roomu_ev
        call screen roomupscreen6

label window6:
    if sofiatalk == False:
        """
        From the window you can see the stars.

        They shine through the dark and calm sky.

        It's a kind of melancholic sight.
        """
    if sofiatalk == True and ghost == True:
        $ mood -= 5
        $ windowseen = True
        jump roomdownscreen6g
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ windowseen = True
        jump roomdownscreen6
label bed6:
    if sofiatalk == False:
        """
        You just woke up, so you're not tired.
        """
        jump roomupscreen6
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
        jump roomupscreen6
label books6:
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
        jump roomdownscreen6g
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ books = True
        jump roomdownscreen6
label plant6:
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
        jump roomdownscreen6g
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ plant = True
        jump roomdownscreen6
label trash6:
    if sofiatalk == False:
        """
        Just a normal trash bin.

        Even though everything looks sadder...

        There's still nothing special about it.
        """
    if sofiatalk == True and ghost == True:
        $ mood -= 5
        $ trash = True
        jump roomdownscreen6g
    if sofiatalk == True and ghost == False:
        $ mood += 5
        $ trash = True
        jump roomdownscreen6
label phone6:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomdownscreen6g
    if ghost == False:
        """
        aaa
        """
        jump roomdownscreen6
label tv6:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomdownscreen6g
    if ghost == False:
        """
        aaa
        """
        jump roomdownscreen6
label cds6:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomdownscreen6g
    if ghost == False:
        """
        aaa
        """
        jump roomdownscreen6
label toy6:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomupscreen6g
    if ghost == False:
        """
        aaa
        """
        jump roomupscreen6
label mirror6:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomupscreen6g
    if ghost == False:
        """
        aaa
        """
        jump roomupscreen6
label guit6:
    if ghost == True:
        """
        Maybe you could call someone...

        But there really isn't anyone to call.
        """
        jump roomupscreen6g
    if ghost == False:
        """
        aaa
        """
        jump roomupscreen6

label computer6:
    if sofiatalk == False:
        jump sofianeut6
    if sofiatalk == True and mood >= 55:
        jump sofiagood6
    if sofiatalk == True and mood <= 45:
        jump sofiasad6
    if sofiatalk == True and mood == 50:
        jump sofianeutmood6
label sofiagood6:
    if ghost == True:
        scene gmood_sbad_gh
        with slowfade
        s "I see you're doing fine, today!"
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen6g
    if ghost == False:
        scene gmood_sgood_ev
        with slowfade
        s "a"
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen6
label sofiasad6:
    if ghost == True:
        scene smood_sbad_gh
        with slowfade
        s "I see you're doing fine, today!"
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen6
    if ghost == False:
        scene smood_sbad_ev
        with slowfade
        s "a"
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen6
label sofianeutmood6:
    if ghost == True:
        scene neutmood_sbad_gh
        with slowfade
        s "I see you're doing fine, today!"
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen6
    if ghost == False:
        scene neutmood_sneut_ev
        with slowfade
        s "a"
        scene roomd_ev
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen6
label sofianeut6:
    scene smood_sbad_gh
    with slowfade
    $ sofiatalk = True
    """
    You calmly sit at your desk.

    The computer is already turned on, as always.

    Sofia is still there.

    She hasn't abandoned you and waits smiling, gently.
    """
    s ""
    if mood >= 55:
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen6
    if mood <= 45:
        scene roomd_ghosts
        with slowfade
        $ renpy.pause(1)
        jump roomdownscreen6


label door6:
    if mood >= 29 and mood <= 69:
        "I can't get outside, it's tightly closed."
        jump roomdownscreen6
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
