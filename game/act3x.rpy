# Expressions, Typo
label act3x:
    play music "sound/music/act3x.mp3"

    scene black
    with dissolve

    scene tr act3x
    $ renpy.pause(2.0, hard='True')

    scene tr act3xtr1
    $ renpy.pause(0.2, hard='True')
    scene tr act3xtr2
    $ renpy.pause(0.2, hard='True')
    scene tr act3xtr3
    $ renpy.pause(0.2, hard='True')
    scene tr act3xtr4
    $ renpy.pause(0.2, hard='True')
    scene tr act3xtr5
    $ renpy.pause(0.5, hard='True')
    scene tr act3xtr6
    $ renpy.pause(0.5, hard='True')

    scene bg seven
    with None

    show mayor normal at right
    show jeanette normal:
        xpos -1.0
        linear 1.5 left
    with Dissolve(1)
    $ renpy.pause(1.5, hard='True')
    $ ui.saybehavior()
    $ ui.interact()

    show jeanette normal at left

    m "Welcome Stranger!"

    j "Yeah... Hi..."

    m "I’m the mayor of this World, nice to meet you. Why did you come to the City hall?"

    j "In fact, I'm here by mistake and I’m just trying to go home."
    j "I’m not from this world."

    show mayor normal at right
    m "Not from this world? Aren’t you... like dead or something?"

    j "Dead? No, not really, I’m here by mystake. Woke up in the wrong bed. By the way why did you put a bed in the middle of nowhere?"

    m "An awakened hero... It reminds me of something..."

    show jeanette badass at left
    j"So what? Will you help me or not?"

    show mayor angry at right
    m "Secretary! Would you bring the X523 form please?"

    s "Immediately Ma’am."

    show mayor inter at right
    m "Thanks... Mmh... Mmh..."

    show jeanette angry at left
    j "..."
    j "Helloo?"

    show mayor normal at right
    m "Sorry, sorry... I maybe have something for you. Take a sit."

    j "..."

    m " Or... Stay up anyway."

    j "What’s this shit?"

    m "A form... A legendary form to be precise."

    j "And?"

    m "It’s a form... Fill it!"

    j "Okay okay."

    m "So... First, your name?"

    show jeanette normal at left

    menu:
        "Jeanette the third":
            j "Jeanette the third"

        "DaRkL3g0lassRoxxor177":
            j"DaRkL3g0lassRoxxor177"

    show mayor inter at right
    m "Hum... Okay okay... Interesting."
    show mayor angry at right
    m "Did a fairy wake you up this morning?"

    menu:
        "Yes":
            j "Yes."

        "A fairy? Nooo... Nobody, never!":
            j "A fairy? Nooo... Nobody, never!"

    show mayor inter at right
    m "... Alright!"
    show mayor normal at right
    m "How long have you lived in the Kokori forest?"

    menu:
        "What...?":
            j "What...?"

        "For about ten years perhaps.":
            j "For about ten years perhaps."


    show mayor inter at right
    m "Interesting."
    show mayor normal at right
    m "On a scale of one to ten, how do you like green?"

    menu:
        "Mmh... Yeah... One?":
            j "Mmh... Yeah... One?"

        "I think... I have no opinion on this subject":
            j "I think... I have no opinion on this subject"

    show mayor inter at right
    m "Yeah... Okay."
    show mayor normal at right
    m "Last one: are you the heroin that the prophecy speaks?"

    menu:
        "Well... I really don’t know.":
            j "Well... I really don’t know."

        "Yeah ! Of course.":
            j "Yeah ! Of course."

    show mayor normal at right
    m "It was a pretty cool form I think we need to talk…"
    m "Do you want to become the savior of the underworld?"

    j "What?"

    m "Well, it’s a well-paid job you know? And you are housed. So?"

    menu:
        "I can try.":
            j "I can try."
            jump a3x_try

        "I just want to go back home.":
            j "I just want to go back home."
            jump a3x_home

    label a3x_try:
        show mayor angry at right
        m "Good! Take this, it’s dangerous to go alone."
        m "Especially without the appropriate form."

        j "And? Where should I go?"

        m "Hoo... Just walk in town and say \"Vote Mayor\"! You're gonna love this job!"

        show jeanette blase at left
        j "..."

        stop music fadeout 1.0

        jump act4x

    label a3x_home:

        show mayor normal at right
        m "Hum... That’s sad..."

        j "Just explain to me how to return to my world."

        m "Maybe you should try to find god..."

        j "God?"

        show mayor angry at right
        m "Yes, he is often wandering around the nightclub."

        j "Fuck... I hate this place right now..."

        m "Go to the north, you’ll see the light."

        show jeanette badass at left
        j "See you slug."

        stop music fadeout 1.0

        jump act4