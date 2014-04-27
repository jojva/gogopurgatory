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
image bg one = "img/bg/back01.png"
image bg two = "img/bg/back02.png"


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
image tr act2tr7 = "img/transitions/act2_transi7.png"
image tr act2tr8 = "img/transitions/act2_transi8.png"
image tr act2tr9 = "img/transitions/act2_transi9.png"


# LOAD CHARACTERS

image dick cute = "img/D/base_cute.png"
image dick evil = "img/D/base_evil.png"

image flick base = "img/F/base.png"


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


image octopolis base = "img/O/base.png"


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


# Jeanette shocked
image jeanette shocked = LiveComposite(
    (520, 768),
    (0, 0), "img/char/J/anim/shocked_body.png",
    (0, 0), "jeanette shocked eyes",
    (0, 0), WhileSpeaking("jeanette", "jeanette shocked mouth", "img/char/J/anim/shocked_mouthclosed.png"),
    )

image jeanette shocked eyes:
    "img/char/J/anim/shocked_eyesopen.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "img/char/J/anim/shocked_eyesclosed.png"
    .25
    repeat

image jeanette shocked mouth:
    "img/char/J/anim/shocked_mouthopen1.png"
    .2
    "img/char/J/anim/shocked_mouthopen2.png"
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


# DEFINE CHARACTERS

define d = Character('Dick', color="#a4b172", what_slow_cps=20, callback=speaker('dick'))
define f = Character('Flick', color="#99cb99", what_slow_cps=20, callback=speaker('flick'))
define g = DynamicCharacter("georgename", color="#ffe960", what_slow_cps=20, callback=speaker('george'))
define j = Character('Jeanette', color="#cc6666", what_slow_cps=20, callback=speaker('jeanette'))
define o = Character('Octopolis', color="#d0687d", what_slow_cps=20, callback=speaker('octopolis'))
define s = Character('Secretary', color="#c9d2d7", what_slow_cps=20, callback=speaker('secretary'))
# You can change god's name later in the game using: $ godname = "some_name"
# Quick name: "a" as in "all-mighty"
define a = DynamicCharacter("godname", color="#17649b", what_slow_cps=20, callback=speaker('god'))

# DEFINE EFFECTS

define mydissolve = Dissolve(0.5)
define flash = Fade(0.25, 0.0, 0.75, color="#fff")