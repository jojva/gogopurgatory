label act1:
    play music "sound/music/act1.mp3"

    scene black

    pause 1

    centered "Sometimes by accident, we fly, for by falling we miss the floor." with mydissolve
    centered "There is only one explanation..." with mydissolve
    centered "I fell asleep at home and I think I made a mistake." with mydissolve

    scene tr bed
    $ renpy.pause(1.5, hard='True')

    scene tr act1
    $ renpy.pause(2.0, hard='True')
    # saybehavior: FORCE user to CLICK to continue
    # $ ui.saybehavior()
    # $ ui.interact()

    show tr eye_anim
    $ renpy.pause(2.0, hard='True')

    show tr point
    $ renpy.pause(1.0, hard='True')

    scene bg one

    show jeanette normal with Dissolve(1)
    $ ui.saybehavior()
    $ ui.interact()
    j "I woke up in the wrong place."
    g "Hey! Listen!"
    g "Hey! Listen!"

    hide jeanette
    show george normal at right
    # \n : entrée
    g "Hey! Listen! You pretty...\nHey! Listen! You female!"
    g "What are you doing here?"

    show jeanette angry at left
    j "?"

    show jeanette normal at left
    menu:
        "Erm... I'm waking up obviously.":
            j "Erm... I'm waking up obviously."
            jump a1_wakeupdone
        "Gnee gueuaah gne?":
            j "Gnee gueuaah gne?"
            jump a1_wakeupdone
        "I don’t know, how about you, \”weird cardbox thing\”?":
            j "I don’t know, how about you, \”weird cardbox thing\”?"
            jump a1_magicpowers

    label a1_magicpowers:
        g "Heeey! This is no cardbox, these are magical powers! M’kay?!"

    label a1_wakeupdone:
        g "Were you alone? In the middle of nowhere?"

    j "How about that? I sleep wherever I want! But I don’t like waking up anywhere..."
    j "Speaking of that, where are we exactly? And you, what are you, crapwood fairy?"

    g "Oi! This is no shitty wood! My name is George."
    $ georgename = "George"
    g "And you are here in the {b}purgatory{/b}."

    menu:
        "The purgatory? Like… The land of the dead and all?":
            j "The purgatory? Like… The land of the dead and all?"
            jump a1_landdead
        "Ok ok the purgatory, but is your name really George? Yuck…":
            j "Ok ok the purgatory, but is your name really George? Yuck…"
            jump a1_yuck
        "Oh shit...":
            j "Oh shit..."
            jump a1_purgatorydone

    label a1_landdead:
        g "Yes this is indeed what you think, the place where dead people end up."
        jump a1_purgatorydone

    label a1_yuck:
        show george blase at right
        g "My mother called me George and I'm very proud."

    label a1_purgatorydone:
        show george normal at right
        g "So you seem really lost.\nMaybe I can change that with a little wave of my magic wand...?"

    show jeanette badass at left
    show george blase:
        xpos 2.0
        linear 5.0 right
    with flash

    $ renpy.pause(5.0, hard='True')

    g "You didn't have to hit me. I will tell you where to go."

    j "Quite fortunate for you."

    show jeanette normal
    g "Very well, go towards this path and you will find..."
    show george normal at right
    g "The City Hall!"

    j "Seriously? There's a City Hall in the purgatory?"

    g "Well yes in the village!"

    j "There's a village... Farewell dumbass."

    show jeanette normal:
        linear 2.0 xpos -2.0
    $ renpy.pause(3.0, hard='True') # 2.0 + 1.0 : Jeanette leaves + George waits 1 second
    g "Well, I think she's into me."

    stop music fadeout 1.0

    jump return1