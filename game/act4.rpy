label act4:
    play music "sound/music/act4.mp3"

    scene black
    with dissolve

    scene tr act4
    $ renpy.pause(2.0, hard='True')

    scene tr act4tr1
    $ renpy.pause(0.5, hard='True')
    scene tr act4tr2
    $ renpy.pause(0.2, hard='True')
    scene tr act4tr3
    $ renpy.pause(0.2, hard='True')
    scene tr act4tr4
    $ renpy.pause(0.2, hard='True')
    scene tr act4tr5
    $ renpy.pause(0.2, hard='True')
    scene tr act4tr6
    $ renpy.pause(0.2, hard='True')
    scene tr act4tr7
    $ renpy.pause(0.2, hard='True')
    scene tr act4tr8
    $ renpy.pause(0.2, hard='True')

    scene bg six
    with None

    show carrot angry at right
    with Dissolve(1.)

    show jeanette normal:
        xpos -1.0
        linear 1.5 left
    $ renpy.pause(1.5, hard='True')

    $ ui.saybehavior()
    $ ui.interact()

    show jeanette normal at left

    c "Hey you! Yes you the tall one! Do you have your ghostly card?"

    j "My what? Sorry I’m not from here."

    c "To pass you need to have your membership card."

    j "Oh, well I didn’t know."

    menu:
        "Charm him":
            jump a4_drague

        "Beat him up":
            jump a4_hit

    label a4_drague:
        show jeanette cute at left
        j "Sorry tall handsome bouncer, I didn’t think I’d meet a man of your splendour."
        c "I don’t believe you!"
        j "You don’t think I could hang out with a skinny carrot?"
        show carrot normal at right
        c "Hmm.."
        j "Maybe we could meet inside and party together?"
        c "Okay but take care of yourself!"

        jump a4_next

    label a4_hit:

        show jeanette badass at left

        j "Look, scumbag, I’m having a shitty day so you better let me in, NOW!"

        c "Sorry but no!"

        j "Oh you will!!"

        show carrot hit:
            xpos 2.0
            linear 5.0 right
        with flash

        $ renpy.pause(5.0, hard='True')

        j "Is it better now? Maybe my ghostly card is not required now?"

        show carrot hit at right
        c "Oh, it’s good for this time. You can go."

        show jeanette normal at left
        j "Dumbass..."

    label a4_next:

    scene black
    with dissolve

    scene tr act45tr1
    $ renpy.pause(0.2, hard='True')
    scene tr act45tr2
    $ renpy.pause(0.2, hard='True')
    scene tr act45tr3
    $ renpy.pause(0.2, hard='True')
    scene tr act45tr4
    $ renpy.pause(0.2, hard='True')
    scene tr act45tr5
    $ renpy.pause(0.2, hard='True')
    scene tr act45tr6
    $ renpy.pause(0.2, hard='True')
    scene tr act45tr7
    $ renpy.pause(0.2, hard='True')
    scene tr act45tr8
    $ renpy.pause(0.2, hard='True')
    scene tr act45tr9
    $ renpy.pause(0.2, hard='True')

    scene bg nine
    with dissolve

    show god party at right
    show jeanette normal:
        xpos -1.0
        linear .75 left
    $ renpy.pause(.75, hard='True')

    j "Seriously, you’re the guy I need to see to get the hell out of here?"
    d "Yes gal, I’m taking care of everything here, there and nowhere. I’m everything in this world and yours and especially in your heart. What’s your name gal?"
    j "Hum... Jeanette... You?"
    d "I do have a name, that I was given by the one who raised me. But the ones who love me, the ones who have faith in me have decided to call me… God."
    show jeanette fear at left
    j "Huh. Are you kidding me now?"
    d "No gal, this is my name, have faith in me."
    # Elevator
    # j "But are you the same guy I met in the elevator?"
    # d "No, no no no no gal, you must be mistaking me for someone else…"
    show jeanette normal at left
    j "If that is right, what are you doing here? Isn't God supposed to be in Heaven, doing miracles or stuff like that?"
    d "Well, look around you. Good people come here and enjoy themselves for eternity."
    d "Yes Heaven is in the purgatory! Everybody is accepted in Heaven but only vertuous people can be accepted in the VIP room."
    d "You must be pure to come here."

    # if:
    #     j "Well, in fact I didn’t let the choice to the bouncer":
    #         "Well, in fact I didn’t let the choice to the bouncer"
    #         jump a4_nochoice
    #     j "This carrot butthole, I had to use my charm to pass…":
    #         "This carrot butthole, I had to use my charm to pass…"

    j "I dealt with it. Anyway, I’m here because a tatooed man told me you can get me back to earth."
    d "A tattooed man? You must be speaking about angel Gabriel, that obstinate Gabby..."
    d "I may have met him at the tattoo shop for reasons I can’t remember -- he was drunk."
    d "I indeed have a way to get you out of here, but do you really wish it?"
    show jeanette badass at left
    j "Hum, yeah, yeah and honestly I have no haste to die."
    d "Very well, in that case, here is the key you need to give the guard of the stairwell to the living world."
    d "He will let you pass if you say my name, but you should stay, we have champagne…"
    show jeanette normal at left
    j "No thanks, I prefer cookies."

    show jeanette normal:
        linear 2.0 xpos -2.0
    $ renpy.pause(2.0, hard='True')

    stop music fadeout 1.0

    jump act5