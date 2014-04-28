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
    $ renpy.pause(0.5, hard='True')
    scene tr act4tr6
    $ renpy.pause(1,5, hard='True')
    scene tr act4tr7
    $ renpy.pause(1,0, hard='True')
    scene tr act4tr8
    $ renpy.pause(1.5, hard='True')
    
    
    
    scene bg five
    show jeanette normal at left
    show carrot angry at right
    c "eh dis donc toi ! oui toi la grande la ! tu as ta carte fantomatique ?"
    
    j "Ma quoi ? pardon je ne suis pas d'ici."
    
    c "pour passer tu dois avoir ta carte d'adérent au club fantomatique"
    
    j "ah, et bien je ne savais pas..."
    
    menu:
        "Le draguer":
            jump a4_drague
        
        "Le taper":
            jump a4_hit
        
    label a4_drague:
        
        j "dsjqldsqdhjql"
    jump a4_next
        
    label a4_hit:
        
        j "dsqyhduoqshduosq"
        
        
    label a4_next:
    
    stop music fadeout 1.0
   
    jump return4
    
    return

