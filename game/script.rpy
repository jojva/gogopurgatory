# You can place the script of your game in this file.

init python:

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        renpy.music.play("sound/sound.wav", "music")
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


# Declare images below this line, using the image statement.
image bg one = "img/bg/back01.png"
image bg two = "img/bg/back02.png"

image dick cute = "img/D/base_cute.png"
image dick evil = "img/D/base_evil.png"

image flick base = "img/F/base.png"

image george basic_one = "img/char/G/base_01.png"
image george basic_two = "img/char/G/base_02.png"
image george depressed = "img/char/G/depressed.png"

image octopolis base = "img/O/base.png"

image secretary base = "img/S/secretary.png"

image god base = "img/V/base.png"

image jeanette angry = "img/char/J/angry.png"
# TODO: Unused?
# image jeanette eyes_closed = "img/char/J/base_EC.png"
# image jeanette eyes_open = "img/char/J/base_EO.png"
image jeanette blase = "img/char/J/blase.png"
image jeanette fear = "img/char/J/fear.png"
image jeanette badass = "img/char/J/badass.png"
image jeanette shocked = "img/char/J/shocked.png"

# Composite things together to make a character with blinking eyes and lip-flap.
image jeanette normal = LiveComposite(
    (520, 768),
    (0, 0), "img/char/J/anim/normal_body.png",
    (0, 0), "girl eyes normal",
    (0, 0), WhileSpeaking("girl", "girl mouth normal", "img/char/J/anim/normal_mouthclosed.png"),
    )

image girl eyes normal:
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

image girl mouth normal:
    "img/char/J/anim/normal_mouthopen1.png"
    .2
    "img/char/J/anim/normal_mouthopen2.png"
    .2
    repeat

# Create such a character.
define d = Character('Dick', color="#cc6666", what_slow_cps=20)
define f = Character('Flick', color="#cc6666", what_slow_cps=20)
define g = Character('George', color="#cc6666", what_slow_cps=20)
define j = Character('Jeanette', color="#cc6666", what_slow_cps=20, callback=speaker('girl'))
define o = Character('Octopolis', color="#cc6666", what_slow_cps=20)
define s = Character('Secretary', color="#cc6666", what_slow_cps=20)
# You can change god's name later in the game using: $ godname = "some_name"
# Quick name: "a" as in "all-mighty"
define a = DynamicCharacter("godname", color="#cc6666", what_slow_cps=20)


# The game starts here.
label start:
    $ godname = 'God'

    scene black
    show jeanette normal

    "Not speaking."

    j "Now I'm speaking. Blah blah blah blah blah blah blah."

    "Not speaking any more."

    j "Now I'm speaking once again. Blah blah blah blah blah blah blah."

    scene bg one
    show jeanette eyes_animated at left
    show george basic_one at right

    j "I think I'm pretty. bla bla bla bla dfuh iuh gs kh kjhsjkhgsdfhkjh  hohgsshh kljh kj kg hkj ghkjg hjfgjh jfh jj ffrt fg fgj ff jf jfjjhjhf uff jf jfjfjf jfh "

    show bg two
    show jeanette threatening
    show george depressed

    a "I'm fucking pretty too, bitch."

    "A dreadful place for all respectful dead."

    return
