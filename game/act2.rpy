label act2:
    play music "sound/music/act2.mp3"
    
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
    j "No, i dont have anything like that..."
    
    show jeanette normal at left
    menu:
        "but a fairy told me I could if i went to the City Hall !":
            j "but a fairy told me I could if i went to the City Hall !"
            jump a2_fairy
        "Are you messing with me you lousy spirit?":
            j "Are you messing with me you lousy spirit?"
            jump a2_spirit
        "What a shitty place...":
            j "What a shitty place..."
            jump a2_shit

    label a2_fairy:
        
        s "Are you talking about George the hobo? I have to tell the police if you’ve been close to him."
        
        hide secretary
        show flick normal at right
        
        f "please follow us to the station, Ma'am."
        jump a2_next
            
    label a2_spirit:
        
        show secretary pissed at right
        s "Oi! I am the Vengeful Death… assistant secretary!"
        
        s "Besides you look way too sleazy to request information from me!\nI will call the spectral police at once and bring you to the police station!"
        
        hide secretary 
        show flick normal at right
        f"I believe a questioning is required, you are too much alive not to be sleazy."
        jump a2_next
        
    label a2_shit:
        
        s "As you say… You’re in the purgatory by the way…\nAh, Here a policeman, i hope he'll help you to find your way!"
        
        hide secretary
        show flick normal at right
        f "Hello we will try our best to untie the situation at the station, Ma’am ."
        
    label a2_next:
       
    stop music fadeout 1.0
   
    jump return2

