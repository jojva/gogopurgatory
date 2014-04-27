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

    scene bg two

    show jeanette normal at left
    show secretary normal at right
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
    j "No, i dont have anything like that, but a fairy told me k could if i went to the City Hall !"

    show jeanette normal at left

    # jump return2

    # The rest should be put in the last act

    scene black

    centered "Bad end."

    return
