label act5:
    play music "sound/music/act5.mp3"

    scene black
    with dissolve

    scene tr act5
    $ renpy.pause(2.0, hard='True')

    scene tr act5tr1
    $ renpy.pause(0.2, hard='True')
    scene tr act5tr2
    $ renpy.pause(0.2, hard='True')
    scene tr act5tr3
    $ renpy.pause(0.2, hard='True')
    scene tr act5tr4
    $ renpy.pause(0.2, hard='True')
    scene tr act5tr5
    $ renpy.pause(0.2, hard='True')
    scene tr act5tr6
    $ renpy.pause(0.2, hard='True')

    scene bg ten
    with None

    show zealot normal at left
    with Dissolve(1.)

    show jeanette normal:
        xpos 1.0
        linear 1.5 right
    $ renpy.pause(1.5, hard='True')

    $ ui.saybehavior()
    $ ui.interact()


    z "Hello, flesh creature, I was waiting for you!"

    j "Were you waiting for me?"

    z "Yes, I have a painful message to deliver. I heard that you are looking for a way to go back to the living world because you woke up in the wrong place?"

    j "Yes, I simply woke up in the wrong place… I have travelled across this crazy world to get out!"

    z "Well, the message is this one: you are not here by accident, you are dead…"

    show jeanette fear at right

    $ renpy.pause(1.0, hard='True')

    j "WHAT? But? I was alive last night when I got to bed!"

    z "Last night at 11:45 PM when you were asleep, your parents came to your room. They took benefit of your deep sleep to murder you!"

    j "..."

    z "Then they hang themselves... I'm sorry..."

    show jeanette shock at right

    j "..."

    z "Hahaha, okay, that was a joke. The look on your face! Haha!"
    show jeanette blase at right
    z "You can go now, dummy."

    $ renpy.pause(2.0, hard='True')

    stop music fadeout 1.0

    scene black
    with Dissolve(2)
    $ renpy.pause(2, hard='True')
    scene tr endstairway
    with None
    $ renpy.pause(6, hard='True')
    scene black
    with Dissolve(4)
    $ renpy.pause(4, hard='True')
    return
