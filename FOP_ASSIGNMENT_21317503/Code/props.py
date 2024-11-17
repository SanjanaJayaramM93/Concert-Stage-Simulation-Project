####################3.	Props/Band: The props/band should be objects with a position and shape, and may be stationary or moving. 
#You should decide how they impact the lighting on stage Prompts: How will the props/band be represented in the simulation? 
#Will the stage view become back/white/coloured or have a halo around the props/band?
####Dependencies

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np
import random
import pygame
#############Class definition##############
class Prop:
    def __init__(self, position, shape, size, color):
        self.position = position
        self.shape = shape
        self.size = size
        self.color = color
        self.patch = None

    def create_patch(self):
        if self.shape == 'circle':
            self.patch = patches.Circle(self.position, self.size, color=self.color)
        elif self.shape == 'rectangle':
            self.patch = patches.Rectangle(self.position, *self.size, color=self.color)

    def update(self, frame):
        
        pass
#####################################################################
#pygame mixer for music 
pygame.mixer.init()
pygame.mixer.music.load("sound.wav")  
######################################################
# Create props
props = [
    Prop([150, 200], 'circle', 20, 'goldenrod'),
    Prop([150, 230], 'circle', 15, 'darkgoldenrod'),
    Prop((145, 245), 'rectangle', (10, 50), 'maroon'),
    Prop([250, 250], 'circle', 30, 'saddlebrown'),
    Prop((280, 180), 'rectangle', (10, 70), 'wheat'),
    Prop((210, 180), 'rectangle', (10, 70), 'wheat'),
    Prop((150, 100), 'rectangle', (200, 70), 'dimgrey')
]
for prop in props:
    prop.create_patch()

# piano keys
piano_keys = [patches.Rectangle((value, 150), 5, 20, color="white") for value in range(160, 350, 15)]
#####################################################################################
#  figure and axes
fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 10))
ax0.set_aspect("equal")
ax0.set_title("Plot 1")
ax0.fill([0, 500, 500, 0], [0, 0, 50, 50], color="black")

ax1.set_aspect("equal")
ax1.set_title("Plot 2")
ax1.fill([0, 500, 500, 0], [0, 0, 500, 500], color="black")
##############################################################################################3
#  props and piano keys
for prop in props:
    ax1.add_patch(prop.patch)
for piano_key in piano_keys:
    ax1.add_patch(piano_key)

# halo effect 
halo = patches.Circle([250, 250], 180, facecolor="none", edgecolor="red", linewidth=5, alpha=0.5)
ax1.add_patch(halo)
halo_visible = True

#  animation
def update(frame):
    global halo_visible

    # Update props
    for prop in props:
        prop.update(frame)

    # Toggle - halo
    if frame % 20 == 0:  
        halo_visible = not halo_visible

    if halo_visible:
        halo.set_center(props[3].position)  
        halo.set_visible(True)
    else:
        halo.set_visible(False)

    
    return [prop.patch for prop in props] + [halo]

#  handle mouse click event
def on_click(event):
    if event.inaxes == ax1:
        for prop in props:
            if prop.patch is not None and prop.patch.contains(event)[0]:
                pygame.mixer.music.play()

# Connect the click event handler to the figure
fig.canvas.mpl_connect('button_press_event', on_click)

#  animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 361, 5), interval=50)

# Display the figure
plt.show()
