"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Bryce Pruemer.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.

import rosegraphics as rg
window = rg.TurtleWindow()

tom = rg.SimpleTurtle()
tom.speed = 100
phil = rg.SimpleTurtle()
phil.speed = 100
size_1=40
size_2=70

tom.pen = rg.Pen('black', 10)
for k in range (15):
    tom.draw_circle(size_1)
    size_1 = size_1-5

phil.pen = rg.Pen('yellow', 2)
for i in range(5):
    phil.draw_regular_polygon(8,size_2)
    size_2 = size_2-10

window.close_on_mouse_click()

#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
