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

    scene bg three

    show jeanette blase at left with Dissolve(1)
    $ ui.saybehavior()
    $ ui.interact()
    show aguaron normal at right:
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
        "Listen, I don’t have time for this, the only that matters to me is to get home!":
            j "Listen, I don’t have time for this, the only that matters to me is to get home!"
            jump a3_dead
        "Hum hum… so. I got lost, I’d actually want water, but not in the face thank you.And I didn’t work with George, are you done with this George?":
            j "Hum hum… so. I got lost, I’d actually want water, but not in the face thank you."
            jump a3_george
        "OBJECTION!":
            j "OBJECTION!"
            jump a3_george

    label a3_dead:
        show aguaron normal at right
        a "Oh you want to go home? Very well, I can help you."
        show aguaron evil at right
        a "Although you’ll get home DEAD!!!"

    label a3_george:
        show aguaron normal at right
        a "Hum… Anyway you didn’t work for George ? This adorable..."
        show aguaron evil at right
        a "SON OF A BITCH!"

    show jeanette angry at left
    j "I am telling you I didn’t! Take a look at me! Do you think I would work with such an creppy fairy?"
    show aguaron normal at right
    a "Hmmm… You’re probably right… Agent, please escort this lady in a comfortable cell with"
    show aguaron evil at right
    a "”Him”"
    show octopolis base
    o "No...!"
    show aguaron evil at right
    a "Yes !!!"
    show aguaron normal at right
    a "No...I'm kidding!"
    show aguaron evil at right
    a "No I'm not! Just throw her there!"
    show jeanette blase
    j "fuck..."

    # pepito ! fais des trucs jolis batard !!

    hide jeanette blase
    hide octopolis base
    hide aguaron evile

    show bg four

    show prisoner souspi at right
    p "  tu fais quoi dans ma cellule ? personne ne vient jamais dansma cellule...ma cellule...je veux etre seul ! Tu fais quoi dans ma cellule ?"
    show jeanette normal at left
    j "je me pose la meme question...Ecoute j'espere sortire assez vite  d'ici, donc ne panique pas je vais te laisser seul !"
    j " ...tu fais quoi en prison ? sans vouloir te deranger..."
    show prisoner normal at right
    p "Sur mon crane est tatoué le plan de la prison ! ducoup il fallait bien que j'y sois enfermé pour savoir si le plan est bon non ?"
    show jeanette blase at left
    j " euh...ouais je suppose…"

    menu:
        "Mon but est de s'échapper non pas de la prison mais du 'purgatoire' a vrai dire... pour linstant  je me balade et croise que des gens chelou…":
            j "Mon but est de s'échapper non pas de la prison mais du 'purgatoire' a vrai dire... pour linstant  je me balade et croise que des gens chelou…"
            jump a3_escape

        "m’échapper de cet endroit pourrais deja etre utile, pourrais-tu me montrer ton plan ??":
            j "m’échapper de cet endroit pourrais deja etre utile, pourrais-tu me montrer ton plan ??"
            jump a3_skull

    label a3_escape:

        show prisoner souspi at right
        p "et bien si tu veux sortir d'ici il va falloir croiser encore pas mal de monde étrange…"
        jump a3_next

    label a3_skull:

        show prisoner back
        p "voila voila..."
        show jeanette shock at left
        $ renpy.pause(5.0, hard='True')
        j "Nevermind..."
        show prisoner souspi at right

    label a3_next:


    p "mais en revanche je sais comment tu pourrais sortire..."

    show jeanette normal at left
    j "mmh...continue"

    show prisoner normal at right
    p "quand j'etait chez le tatoueur j'ai croisé un type completement nu qui parlé d'une 'clé' pour le portail du monde."

    j "aaah enfin une bonne nouvelle dans ce monde de fou !!! ou est-il ?"

    show prisoner souspi at right
    p "j'sais pas trop je te rappel que je suis en prison ! mais je pense qu’il traine souvent a cet endroit..."

    j "quel endroit ???"

    show prisoner normal at right
    p "la discoteque de la ville, le : Dance ! Dance ! Purgatory !\nLieu de débauche pour tout mort qui ce respect !"

    show jeanette blase at left
    j "arf je deteste ce genre d'endroit... bon j'ai quand meme une solution !\n je te remerci O etrange monsieur !"

    a "Et bien vous etes libre, n'ayant rien contre vous..."

    hide prisoner
    hide jeanette

    scene bg three

    #jeanette ce barre par la gauche et elle ce retrouve a droit sur l'écran d'apres

    show jeanette normal at right
    show aguaron normal at left
    a "bon et bien jespere que vous ne recroiserais pas George la fée..."

    show aguaron evil at left
    a "ou sinon je vous traquerez jusqu'a la mort.."

    show jeanette angry at right
    j "bon,et si je le recroise je fais quoi ?"

    a "George a une prime de 1.000.000 de Gils !! il faut le capturer"

    show jeanette blase at right
    j "Bon ok..."


    stop music fadeout 1.0

    jump return3
