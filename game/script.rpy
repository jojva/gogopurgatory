# You can place the script of your game in this file.

import "defs.rpy"
import "act1.rpy"
#import "act2.rpy"
# import "act3.rpy"
# import "act4.rpy"

# The game starts here.
label start:
    $ georgename = '???'
    $ godname = 'God'
    #jump act1
    label return1:
    jump act2
    label return2:
    # jump act3