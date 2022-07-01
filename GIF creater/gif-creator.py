"""
Slide Show - Make an application that shows various pictures in a slide show format.
Optional: Try adding various effects like fade in/out, star wipe and window blinds transitions.
"""

import imageio.v2 as imageio
filenames = ["mountains.jpg","lakes.png"]
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images,'GIF',duration=1)