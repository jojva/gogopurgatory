init python:

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        # renpy.music.play("sound/sound.wav", "music")
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking

        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

init python:
    overriding_on = None
    def overriding_overlay():
        if not overriding_on:
            return
        ui.keymap(mousedown_1=ui.returns(None))
        ui.keymap(mouseup_1=ui.returns(None))

    config.overlay_functions.append(overriding_overlay)


# LOAD BACKGROUNDS

image bg title = "img/title_screen.png"
image bg one   = "img/bg/back01.png"
image bg two   = "img/bg/back02.png"
image bg three = "img/bg/back04.png"
image bg four  = "img/bg/back05.png"
image bg five  = "img/bg/back06.png"



# LOAD TRANSITIONS

image tr act1 = "img/transitions/act1.png"
image tr bed = "img/transitions/bed.png"
image tr eye_anim:
    "img/transitions/eyes_03.png"
    .2
    "img/transitions/eyes_02.png"
    .2
    "img/transitions/eyes_01.png"
    .2
    "img/transitions/eyes_00.png"
    1.4
image tr point = "img/transitions/point.png"

image tr act2 = "img/transitions/act2.png"
image tr act2tr1 = "img/transitions/act2_transi1.png"
image tr act2tr2 = "img/transitions/act2_transi2.png"
image tr act2tr3 = "img/transitions/act2_transi3.png"
image tr act2tr4 = "img/transitions/act2_transi4.png"
image tr act2tr5 = "img/transitions/act2_transi5.png"
image tr act2tr6 = "img/transitions/act2_transi6.png"

image tr act3 = "img/transitions/act3.png"
image tr act3tr1 = "img/transitions/act3_transi1.png"
image tr act3tr2 = "img/transitions/act3_transi2.png"
image tr act3tr3 = "img/transitions/act3_transi3.png"
image tr act3tr4 = "img/transitions/act3_transi4.png"
image tr act3tr5 = "img/transitions/act3_transi5.png"
image tr act3tr6 = "img/transitions/act3_transi6.png"

image tr act4 = "img/transitions/act4.png"
image tr act4tr1 = "img/transitions/act4_transi1.png"
image tr act4tr2 = "img/transitions/act4_transi2.png"
image tr act4tr3 = "img/transitions/act4_transi3.png"
image tr act4tr4 = "img/transitions/act4_transi4.png"
image tr act4tr5 = "img/transitions/act4_transi5.png"
image tr act4tr6 = "img/transitions/act4_transi6.png"
image tr act4tr7 = "img/transitions/act4_transi7.png"
image tr act4tr8 = "img/transitions/act4_transi8.png"
# LOAD CHARACTERS

image octopolis base = "img/char/O/base.png"


# Aguaron
# Aguaron normal
image aguaron normal = LiveComposite(
    (520, 768),
    (0, 0), "img/char/A/anim/normal_body.png",
    (0, 0), "aguaron normal eyes",
    (0, 0), WhileSpeaking("aguaron", "aguaron normal mouth", "img/char/A/anim/normal_mouthclose.png"),
    )

image aguaron normal eyes:
    "img/char/A/anim/normal_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/A/anim/normal_eyesclose.png"
    .25
    repeat

image aguaron normal mouth:
    "img/char/A/anim/normal_mouthopen1.png"
    .2
    "img/char/A/anim/normal_mouthopen2.png"
    .2
    repeat

# Aguaron evil
image aguaron evil = LiveComposite(
    (520, 768),
    (0, 0), "img/char/A/anim/evil_body.png",
    (0, 0), "aguaron evil eyes",
    (0, 0), WhileSpeaking("aguaron", "aguaron evil mouth", "img/char/A/anim/evil_mouthclose.png"),
    )

image aguaron evil eyes:
    "img/char/A/anim/evil_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/A/anim/evil_eyesclose.png"
    .25
    repeat

image aguaron evil mouth:
    "img/char/A/anim/evil_mouthopen1.png"
    .2
    "img/char/A/anim/evil_mouthopen2.png"
    .2
    repeat

# Carrot
# Carrot normal
image carrot normal = LiveComposite(
    (520, 768),
    (0, 0), "img/char/C/anim/normal_body.png",
    (0, 0), "carrot normal eyes",
    (0, 0), WhileSpeaking("carrot", "carrot normal mouth", "img/char/C/anim/normal_mouthclose.png"),
    )

image carrot normal eyes:
    "img/char/C/anim/normal_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/C/anim/normal_eyesclose.png"
    .25
    repeat

image carrot normal mouth:
    "img/char/C/anim/normal_mouthopen1.png"
    .2
    "img/char/C/anim/normal_mouthopen2.png"
    .2
    repeat
    
# Carrot angry
image carrot angry = LiveComposite(
    (520, 768),
    (0, 0), "img/char/C/anim/angry_body.png",
    (0, 0), "carrot angry eyes",
    (0, 0), WhileSpeaking("carrot", "carrot angry mouth", "img/char/C/anim/angry_mouthclose.png"),
    )

image carrot angry eyes:
    "img/char/C/anim/angry_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/C/anim/angry_eyesclose.png"
    .25
    repeat

image carrot angry mouth:
    "img/char/C/anim/angry_mouthopen1.png"
    .2
    "img/char/C/anim/angry_mouthopen2.png"
    .2
    repeat
    
# Carrot hit
image carrot hit = LiveComposite(
    (520, 768),
    (0, 0), "img/char/C/anim/hit_body.png",
    (0, 0), "carrot hit eyes",
    (0, 0), WhileSpeaking("carrot", "carrot hit mouth", "img/char/C/anim/hit_mouthclose.png"),
    )

image carrot hit eyes:
    "img/char/C/anim/hit_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/C/anim/hit_eyesclose.png"
    .25
    repeat

image carrot hit mouth:
    "img/char/C/anim/hit_mouthopen1.png"
    .2
    "img/char/C/anim/hit_mouthopen2.png"
    .2
    repeat
    
# Carrot happy
image carrot happy = LiveComposite(
    (520, 768),
    (0, 0), "img/char/C/anim/happy_body.png",
    (0, 0), "carrot happy eyes",
    (0, 0), WhileSpeaking("carrot", "carrot hit mouth", "img/char/C/anim/happy_mouthclose.png"),
    )

image carrot happy eyes:
    "img/char/C/anim/happy_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/C/anim/happy_eyesclose.png"
    .25
    repeat

image carrot happy mouth:
    "img/char/C/anim/happy_mouthopen1.png"
    .2
    "img/char/C/anim/happy_mouthopen2.png"
    .2
    repeat
    
    
    
# Flick
# Flick normal
image flick normal = LiveComposite(
    (520, 768),
    (0, 0), "img/char/F/anim/normal_body.png",
    (0, 0), "flick normal eyes",
    (0, 0), WhileSpeaking("flick", "flick normal mouth", "img/char/F/anim/normal_mouthclose.png"),
    )

image flick normal eyes:
    "img/char/F/anim/normal_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/F/anim/normal_eyesclose.png"
    .25
    repeat
    
image flick normal mouth:
    "img/char/F/anim/normal_mouthopen1.png"
    .2
    "img/char/F/anim/normal_mouthopen2.png"
    .2
    repeat

# George
# George blase
image george blase = LiveComposite(
    (520, 768),
    (0, 0), "george blase body",
    (0, 0), "george blase eyes",
    )

image george blase body:
    "img/char/G/anim/blase_body1.png"
    .5
    "img/char/G/anim/blase_body2.png"
    .5
    repeat

image george blase eyes:
    "img/char/G/anim/blase_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/G/anim/blase_eyesclose.png"
    .25
    repeat



# George normal
image george normal = LiveComposite(
    (520, 768),
    (0, 0), "george normal body",
    (0, 0), "george normal eyes",
    )

image george normal body:
    "img/char/G/anim/normal_body1.png"
    .5
    "img/char/G/anim/normal_body2.png"
    .5
    repeat

image george normal eyes:
    "img/char/G/anim/normal_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/G/anim/normal_eyesclose.png"
    .25
    repeat


# Secretary
# Secretary normal
image secretary normal = LiveComposite(
    (520, 768),
    (0, 0), "img/char/S/anim/normal_body.png",
    (0, 0), WhileSpeaking("secretary", "secretary normal mouth", "img/char/S/anim/normal_mouthclose.png"),
    )

image secretary normal mouth:
    "img/char/S/anim/normal_mouthopen1.png"
    .15
    "img/char/S/anim/normal_mouthopen2.png"
    .15
    repeat

# Secretary pissed
image secretary pissed = LiveComposite(
    (520, 768),
    (0, 0), "img/char/S/anim/pissed_body.png",
    (0, 0), WhileSpeaking("secretary", "secretary pissed mouth", "img/char/S/anim/pissed_mouthclose.png"),
    )

image secretary pissed mouth:
    "img/char/S/anim/pissed_mouthopen1.png"
    .15
    "img/char/S/anim/pissed_mouthopen2.png"
    .15
    repeat

image god base = "img/V/base.png"


# TODO: Unused?
# image jeanette eyes_closed = "img/char/J/base_EC.png"
# image jeanette eyes_open = "img/char/J/base_EO.png"

# Jeanette
# Jeanette angry
image jeanette angry = LiveComposite(
    (520, 768),
    (0, 0), "img/char/J/anim/angry_body00.png",
    (0, 0), "jeanette angry head",
    (0, 0), "jeanette angry eyes",
    (0, 0), WhileSpeaking("jeanette", "jeanette angry mouth", "img/char/J/anim/angry_mouthclosed.png"),
    )

image jeanette angry head:
    "img/char/J/anim/angry_head00.png"
    .5
    # This randomizes the time between blinking.
    "img/char/J/anim/angry_head01.png"
    .5
    repeat


image jeanette angry eyes:
    "img/char/J/anim/angry_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/J/anim/angry_eyesclose.png"
    .25
    repeat

image jeanette angry mouth:
    "img/char/J/anim/angry_mouthopen1.png"
    .2
    "img/char/J/anim/angry_mouthopen2.png"
    .2
    repeat

# Jeanette badass
image jeanette badass = LiveComposite(
    (520, 768),
    (0, 0), "img/char/J/anim/badass_body.png",
    (0, 0), "jeanette badass eyes",
    (0, 0), WhileSpeaking("jeanette", "jeanette badass mouth", "img/char/J/anim/badass_mouthclosed.png"),
    )

image jeanette badass eyes:
    "img/char/J/anim/badass_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/J/anim/badass_eyesclosed.png"
    .25
    repeat

image jeanette badass mouth:
    "img/char/J/anim/badass_mouthopen1.png"
    .2
    "img/char/J/anim/badass_mouthopen2.png"
    .2
    repeat

# Jeanette blase
image jeanette blase = LiveComposite(
    (520, 768),
    (0, 0), "img/char/J/anim/blase_body00.png",
    (0, 0), "jeanette blase eyes",
    (0, 0), WhileSpeaking("jeanette", "jeanette blase mouth", "img/char/J/anim/blase_mouthclosed.png"),
    )

image jeanette blase eyes:
    "img/char/J/anim/blase_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/J/anim/blase_eyesclosed.png"
    .25
    repeat

image jeanette blase mouth:
    "img/char/J/anim/blase_mouthopen1.png"
    .2
    "img/char/J/anim/blase_mouthopen2.png"
    .2
    repeat

# Jeanette fear
image jeanette fear = LiveComposite(
    (520, 768),
    (0, 0), "img/char/J/anim/fear_body00.png",
    (0, 0), "jeanette fear eyes",
    )

image jeanette fear eyes:
    "img/char/J/anim/fear_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/J/anim/fear_eyesclosed.png"
    .25
    repeat

# Jeanette normal
image jeanette normal = LiveComposite(
    (520, 768),
    (0, 0), "img/char/J/anim/normal_body.png",
    (0, 0), "jeanette normal eyes",
    (0, 0), WhileSpeaking("jeanette", "jeanette normal mouth", "img/char/J/anim/normal_mouthclosed.png"),
    )

image jeanette normal eyes:
    "img/char/J/anim/normal_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/J/anim/normal_eyesclosed.png"
    .25
    repeat

image jeanette normal mouth:
    "img/char/J/anim/normal_mouthopen1.png"
    .2
    "img/char/J/anim/normal_mouthopen2.png"
    .2
    repeat


# Jeanette shock
image jeanette shock = LiveComposite(
    (520, 768),
    (0, 0), "img/char/J/anim/shock_body.png",
    (0, 0), "jeanette shock eyes",
    (0, 0), WhileSpeaking("jeanette", "jeanette shock mouth", "img/char/J/anim/shock_mouthclosed.png"),
    )

image jeanette shock eyes:
    "img/char/J/anim/shock_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/J/anim/shock_eyesclosed.png"
    .25
    repeat

image jeanette shock mouth:
    "img/char/J/anim/shock_mouthopen1.png"
    .2
    "img/char/J/anim/shock_mouthopen2.png"
    .2
    repeat

# Jeanette fear
image jeanette fear = LiveComposite(
    (520, 768),
    (0, 0), "img/char/J/anim/fear_body00.png",
    (0, 0), "jeanette fear eyes",
    )

image jeanette fear eyes:
    "img/char/J/anim/fear_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/J/anim/fear_eyesclosed.png"
    .25
    repeat
    
    
# Prisoner
# Prisoner normal
image prisoner normal = LiveComposite(
    (520, 768),
    (0, 0), "img/char/P/anim/normal_body.png",
    (0, 0), "prisoner normal eyes",
    (0, 0), WhileSpeaking("prisoner", "prisoner normal mouth", "img/char/P/anim/normal_mouthclose.png"),
    )

image prisoner normal eyes:
    "img/char/P/anim/normal_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/P/anim/normal_eyesclose.png"
    .25
    repeat

image prisoner normal mouth:
    "img/char/P/anim/normal_mouthopen1.png"
    .2
    "img/char/P/anim/normal_mouthopen2.png"
    .2
    repeat
    
    
    
# Prisoner souspi
image prisoner souspi = LiveComposite(
    (520, 768),
    (0, 0), "img/char/P/anim/souspi_body.png",
    (0, 0), "prisoner souspi eyes",
    (0, 0), WhileSpeaking("prisoner", "prisoner souspi mouth", "img/char/P/anim/souspi_mouthclose.png"),
    )

image prisoner souspi eyes:
    "img/char/P/anim/souspi_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/P/anim/souspi_eyesclose.png"
    .25
    repeat

image prisoner souspi mouth:
    "img/char/P/anim/souspi_mouthopen1.png"
    .2
    "img/char/P/anim/souspi_mouthopen2.png"
    .2
    repeat

    # Prisoner back
    
image prisoner back = "img/char/P/body_dos.png"
    
    
    
# DEFINE CHARACTERS

define a = Character('Aguaron', color="#bdcc7d", what_slow_cps=20, callback=speaker('aguaron'))
define c = Character('Pierre', color="#ce2c2c", what_slow_cps=20, callback=speaker('pierre'))
define p = Character('Prisoner', color="#e94e1b", what_slow_cps=20, callback=speaker('prisoner'))
define f = Character('Flick', color="#99cb99", what_slow_cps=20, callback=speaker('flick'))
define g = DynamicCharacter("georgename", color="#ffe960", what_slow_cps=20, callback=speaker('george'))
define j = Character('Jeanette', color="#cc6666", what_slow_cps=20, callback=speaker('jeanette'))
define o = Character('Octopolis', color="#d0687d", what_slow_cps=20, callback=speaker('octopolis'))
define s = Character('Secretary', color="#c9d2d7", what_slow_cps=20, callback=speaker('secretary'))
# You can change god's name later in the game using: $ godname = "some_name"
# Quick name: "a" as in "all-mighty"
define d = DynamicCharacter("godname", color="#ebeff9", what_slow_cps=20, callback=speaker('god'))

# DEFINE EFFECTS

define mydissolve = Dissolve(0.5)
define flash = Fade(0.25, 0.0, 0.75, color="#fff")