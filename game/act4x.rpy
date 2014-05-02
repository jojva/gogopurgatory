label act4x:
    play music "sound/music/act4x.mp3"

    scene black
    with dissolve

    scene tr act4x
    $ renpy.pause(2.0, hard='True')

    scene tr act4xtr1
    $ renpy.pause(0.2, hard='True')
    scene tr act4xtr2
    $ renpy.pause(0.2, hard='True')
    scene tr act4xtr3
    $ renpy.pause(0.2, hard='True')
    scene tr act4xtr4
    $ renpy.pause(0.2, hard='True')
    scene tr act4xtr5
    $ renpy.pause(0.2, hard='True')
    scene tr act4xtr6
    $ renpy.pause(0.2, hard='True')
    scene tr act4xtr7
    $ renpy.pause(0.2, hard='True')
    scene tr act4xtr8
    $ renpy.pause(0.2, hard='True')

    scene bg eight
    with None

    show jeanette normal
    with Dissolve(1.)

    $ ui.saybehavior()
    $ ui.interact()

    g "Hey! Listen!"

    hide jeanette
    show george p at right

    g "Hey ! Lis...\nJeanette?!"

    show jeanette blase:
        xalign -1.0
        linear 2.0 left
    $ renpy.pause(2.0, hard='True')

    j "What the hell are you doin’?"

    g "Hum, nothing, I’m just looking for free food."

    g "You know, since I’m wanted by the police, the angel, the bountyhunter, the demon and some children, restaurants don’t want to serve me..."

    show jeanette normal at left
    j "In fact, I really don’t care."

    g "I’ve got a price on my head, I’m pretty famous now."

    g "Maybe I could denounce myself and take the reward..."

    j "You're brilliant."

    g "Seriously? I’ve always wanted to be rich."

    g "I really really love money."

    menu:
        "Call the police station":
            j "I‘m calling the police station. You, stay here."
            jump a4x_moneyend

        "Live your life as a wanderer":
            jump a4x_teleportend


    label a4x_moneyend:

        g "Really? Cool."

        show jeanette phone at left
        j "Yes, I know I know, just close your ears."

        j "Yeah, police?\nI’ve got something for you. A crappy creepy fairy."

        j "I’m in town!"

        phone "..."

        j "Yes yes, and how long can I live with this money?"

        phone "..."

        j "Okay okay, maybe I'm gonna stay here a bit longer."

        show jeanette badass at left
        j "I, too, really love money."

        scene black
        with Dissolve(4)
        $ renpy.pause(4, hard='True')
        scene tr endmoney
        with None
        $ renpy.pause(8, hard='True')
        scene black
        with Dissolve(4)
        $ renpy.pause(4, hard='True')
        return

    label a4x_teleportend:

        g "A Wanderer?"

        g "Yeah! A wanderer!\nThat’s great!"

        j "Yeah yeah… Do whatever you want, I don't care…"

        g "By the way… Do you know how to get back to your world?"

        j "No…"

        g "If you want, I can teleport you to the upperworld, it’s easy, I’m full of magic you know?"

        show jeanette fear at left
        j "Really?!"

        g "Yep, touch my magic wand."

        show jeanette blase at left
        j "I think I don't really have a choice…"

    menu :
        "Touch the magic wand":
            scene black
            with Dissolve(4)
            $ renpy.pause(4, hard='True')
            scene tr endmagic
            with None
            $ renpy.pause(8, hard='True')
            scene black
            with Dissolve(4)
            $ renpy.pause(4, hard='True')
            return