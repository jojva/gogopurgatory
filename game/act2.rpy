label act2:
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
    scene tr act2tr7
    $ renpy.pause(0.5, hard='True')
    scene tr act2tr8
    $ renpy.pause(0.5, hard='True')
    scene tr act2tr9
    $ renpy.pause(0.5, hard='True')

    $ ui.interact()

    scene black

    centered "Bad end."

    # jump return2

    # return à mettre au dernier acte
    return
