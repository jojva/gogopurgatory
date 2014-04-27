# You can place the script of your game in this file.

init python:

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        renpy.music.play("sound.wav", "music")
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


# Create such a character.
define girlslow = Character("Girl", callback=speaker("girl"), what_slow_cps=20)

# Composite things together to make a character with blinking eyes and
# lip-flap.
image girl normal = LiveComposite(
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



# Declare images below this line, using the image statement.
image bg one = "img/bg/Back01.png"
image bg two = "img/bg/Back02.png"

image jeanette angry = "img/char/J/Angry.png"
image jeanette eyes_closed = "img/char/J/Base_EC.png"
image jeanette eyes_open = "img/char/J/Base_EO.png"
image jeanette eyes_animated:
    "img/char/J/Base_EO.png"
    pause (5)
    "img/char/J/Base_EC.png"
    pause.1
    repeat
image jeanette indifferent = "img/char/J/Blase.png"
image jeanette fear = "img/char/J/Fear.png"
image jeanette threatening = "img/char/J/Menace.png"
image jeanette shocked = "img/char/J/Shock.png"

image george basic_one = "img/char/G/Base_01.png"
image george basic_two = "img/char/G/Base_02.png"
image george depressed = "img/char/G/Depressed.png"

# Declare characters used by this game.
define e = Character('Jeanette', color="#cc6666")
define g = Character('George', color="#ffea60")


# The game starts here.
label start:

    scene black
    show girl normal

    "Not speaking."

    girlslow "Now I'm speaking. Blah blah blah blah blah blah blah."

    "Not speaking any more."

    girl "Now I'm speaking once again. Blah blah blah blah blah blah blah."

    scene bg one
    show jeanette eyes_animated at left
    show george basic_one at right

    e "I think I'm pretty. bla bla bla bla dfuh iuh gs kh kjhsjkhgsdfhkjh  hohgsshh kljh kj kg hkj ghkjg hjfgjh jfh jj ffrt fg fgj ff jf jfjjhjhf uff jf jfjfjf jfh "

    show bg two
    show jeanette threatening
    show george depressed

    g "I'm fucking pretty too, bitch."

    "A dreadful place for all respectful dead."

    return
