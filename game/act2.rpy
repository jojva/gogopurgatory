label act2:
    play music "sound/music/act2.mp3" fadein 2.0

    scene black
    with dissolve

    scene tr act2
    $ renpy.pause(2.0, hard='True')

    scene tr act2tr1
    $ renpy.pause(0.2, hard='True')
    scene tr act2tr2
    $ renpy.pause(0.2, hard='True')
    scene tr act2tr3
    $ renpy.pause(0.2, hard='True')
    scene tr act2tr4
    $ renpy.pause(0.2, hard='True')
    scene tr act2tr5
    $ renpy.pause(0.5, hard='True')
    scene tr act2tr6
    $ renpy.pause(0.5, hard='True')

    scene bg two
    with None

    show jeanette normal at left
    show secretary normal at right
    with Dissolve(1)
    $ ui.saybehavior()
    $ ui.interact()
    j "Hum... Hello?"
    j "I come to request you on how to get out of here please."

    s "Do you have a request form?"

    show jeanette blase at left
    j "No I don't."

    show jeanette normal at left
    s "In any case you can't get out of the purgatory. Especially if you don't have a request form."

    j "Can any request form actually help me?"

    s "No. Do you have a request form for anything else? You can get a free baseball hat with X25-B34 form."

    show jeanette blase at left
    j "No, i dont have anything like that..."

    show jeanette normal at left
    menu:
        "But a fairy told me I could get out if i went to the City Hall!":
            j "But a fairy told me I could get out if i went to the City Hall!"
            jump a2_fairy
        "Are you messing with me you lousy spirit?":
            j "Are you messing with me you lousy spirit?"
            jump a2_spirit

    label a2_fairy:

        s "Are you talking about George the hobo? I have to tell the police if you’ve been close to him."

        show secretary:
            linear 3.0 ypos -2.0
        $ renpy.pause(1.5, hard='True')
        hide secretary

        show flick normal at right:
            xalign 0.75
            ypos 2.0
            linear 1.5 right
        $ renpy.pause(1.5, hard='True')

        f "Please follow us to the station, Ma'am."

        stop music fadeout 1.0

        jump act3

    label a2_spirit:

        show secretary pissed at right
        s "Oi! I am the Vengeful Death… assistant secretary!"

        s "Besides you look way too sleazy to request information from me!\nYou should see the mayor, he knows much more than I do."

        j "Ok thanks bye."

        stop music fadeout 1.0

        jump act3x

