label act3:
    play music "sound/music/act3.mp3"

    scene black
    with dissolve

    scene tr act3
    $ renpy.pause(2.0, hard='True')

    scene tr act3tr1
    $ renpy.pause(0.2, hard='True')
    scene tr act3tr2
    $ renpy.pause(0.2, hard='True')
    scene tr act3tr3
    $ renpy.pause(0.2, hard='True')
    scene tr act3tr4
    $ renpy.pause(0.2, hard='True')
    scene tr act3tr5
    $ renpy.pause(0.5, hard='True')
    scene tr act3tr6
    $ renpy.pause(1.5, hard='True')

    scene bg four
    with None

    show jeanette blase at left
    show aguaron normal at right
    with Dissolve(1)
    $ ui.saybehavior()
    $ ui.interact()

    a "A heartful welcome…"

    show aguaron evil at right
    a "Bitch!"

    show jeanette fear at left
    show aguaron normal at right
    a "So… so so so...\nWhat’ve we got here…"
    show jeanette angry at left

    show aguaron evil at right
    a "Whatcha doing here, wuss?"
    show aguaron normal at right
    show jeanette normal at left
    a "You want water?"
    show aguaron evil at right
    a "In ya face?"
    show jeanette fear at left
    show aguaron normal at right
    a"You worked with George?"
    show jeanette blase at left
    a"Are you hungry?\nI can make you a little meal if ya want…"
    show aguaron evil at right
    a"Hell no I don’t care… ha… haha. Mouahahahahaha!!"

    menu:
        "Listen, I don’t have time for this, the only thing that matters to me is to get home!":
            j "Listen, I don’t have time for this, the only thing that matters to me is to get home!"
            jump a3_dead
        "Hum hum… so. I got lost, I’d actually want water, but not in the face thank you.":
            j "Hum hum… so. I got lost, I’d actually want water, but not in the face thank you."
            j "And I didn’t work with George, are you done with this George?"
            jump a3_george

    label a3_dead:
        show aguaron normal at right
        a "Oh you want to go home? Very well, I can help you."
        show aguaron evil at right
        a "Although you’ll get home DEAD!!!"

    label a3_george:
        show aguaron normal at right
        a "Hum… Anyway you didn’t work for George ? This is adorable..."
        show aguaron evil at right
        a "SON OF A BITCH!"

    show jeanette angry at left
    j "I am telling you I didn’t! Take a look at me! Do you think I would work with such a creepy fairy?"
    show aguaron normal at right
    a "Hmmm… You’re probably right… Agent, please escort this lady in a comfortable cell with..."
    show aguaron evil at right
    a "\"Him\"!"
    show octopolis base:
        xalign 0.5
        ypos 2.0
        linear 3.0 center
    $ renpy.pause(1.5, hard='True')

    o "No...!"
    show aguaron evil at right
    a "Yes !!!"
    show aguaron normal at right
    a "No... I'm kidding!"
    show aguaron evil at right
    a "No I'm not! Just throw her there!"
    show jeanette blase
    j "Fuck..."

    scene black
    with dissolve
    scene bg five
    with dissolve

    show prisoner souspi at right
    show jeanette normal:
        xpos -2.0
        yalign 0
        linear 3.0 left
    $ renpy.pause(3.0, hard='True')
    $ ui.saybehavior()
    $ ui.interact()

    p "What are you doing in my cell? Nobody ever comes in my cell... MY cell... I want to be alone! What are you doing in my cell?"

    j "I wonder the same thing... Look I'm about to get out of here hopefully, so don't panic I will leave you alone."
    j "Soo... What are you doing in jail? I mean no offense."
    show prisoner normal at right
    p "I tattooed the prison map on my skull! So I had to be arrested to check whether the map is correct, right?"
    show jeanette blase at left
    j "Erm yeah I guess."

    menu:
        "My purpose right now is to escape from the purgatory, not just the prison to be fair.":
            j "My purpose right now is to escape from the purgatory, not just the prison to be fair."
            jump a3_escape

        "Escaping this place could be a nice progress, would you show me your map?":
            j "Escaping this place could be a nice progress, would you show me your map?"
            jump a3_skull

    label a3_escape:
        j "Up until now I've been wandering around only meeting shady people."
        show prisoner souspi at right
        p "Actually if you want to escape you will have to meet a crapload more of shady people."
        jump a3_next

    label a3_skull:
        show prisoner back
        p "Check this out, it's on the back of my head. I'm clever."
        show jeanette shock at left
        $ renpy.pause(5.0, hard='True')
        j "Nevermind..."
        show prisoner souspi at right

    label a3_next:

    p "On the other hand I know how you can get out..."

    show jeanette normal at left
    j "Hmm... I'm listening."

    show prisoner normal at right
    p "When I was at the tattoo's I met a completely naked guy, who told me about a \"key\" for the \"Stairway\"."

    j "Aaah finally some good news in this crazy world! Where can I find that key?"

    show prisoner souspi at right
    p "I don't know, let me recall you I'm in jail! But I believe he often hangs out at this place..."

    j "What place??"

    show prisoner normal at right
    p "It's the city's nightclub, Dance! Dance! Purgatory!\n\"Come as you are in our obscene place for all respectful dead\"."

    show jeanette blase at left
    j "Damn I hate that kind of place... But I have a solution anyway!\nThank you, O strange Sir."

    a "Having come up with nothing against you, you are free to go."

    show jeanette normal:
        linear 1.5 xpos -2.0
    $ renpy.pause(1.5, hard='True')

    scene black
    with dissolve
    scene bg four
    with dissolve

    show jeanette normal:
        yalign 0
        xpos 2.0
        linear 1.5 right
    show aguaron normal at left
    $ renpy.pause(1.5, hard='True')


    a "And I hope you won't cross paths with George the Fairy again..."

    show aguaron evil at left
    a "Or I will hunt you down."

    show jeanette angry at right
    j "Then what do I do if I meet him again?"

    a "George has a 1,000,000 Gils reward for his capture!!! You would provide us a valuable service."

    show jeanette blase at right
    j "Whatever."

    menu:
        "Go to the Dance! Dance! Purgatory! night club":
            stop music fadeout 1.0
            jump act4
        "Look for George":
            stop music fadeout 1.0
            jump act4x