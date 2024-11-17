import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Wedge
from matplotlib.animation import FuncAnimation
import numpy as np
import random
import pygame
#############################################################################33
class Light:
    def __init__(self, color, position, intensity, direction, spread_angle, speed):
        self.color = color
        self.position = position
        self.intensity = intensity
        self.direction = direction
        self.spread_angle = spread_angle
        self.speed = speed
###################################################################################3
class LightGroup:
    def __init__(self, lights):
        self.lights = lights
    
    def set_color(self, color):
        for light in self.lights:
            light.color = color
    
    def set_intensity(self, intensity):
        for light in self.lights:
            light.intensity = intensity
    
    def set_direction(self, direction):
        for light in self.lights:
            light.direction = direction
    
    def set_spread_angle(self, spread_angle):
        for light in self.lights:
            light.spread_angle = spread_angle
    
    def set_speed(self, speed):
        for light in self.lights:
            light.speed = speed
    
    def get_lights(self):
        return self.lights
############################################################################################

#pygame mixer for music 
pygame.mixer.init()
pygame.mixer.music.load("sound.wav")  
    
####################################################################################################3
lights = [
    Light("black", [45, 500], 0.8, 270, 10, 10),
    Light("red", [90, 500], 0.6, 270, 10, 15),
    Light("black", [135, 500], 0.7, 270, 10, 20),
    Light("red", [180, 500], 0.5, 270, 10, 10),
    Light("black", [225, 500], 0.9, 270, 10, 15),
    Light("red", [270, 500], 0.4, 270, 10, 20),
    Light("black", [315, 500], 0.6, 270, 10, 10),
    Light("red", [360, 500], 0.8, 270, 10, 15),
    Light("black", [405, 500], 0.7, 270, 10, 20),
    Light("red", [450, 500], 0.7, 270, 10, 20),
    
    Light("cornsilk", [495, 500], 0.7, 270, 10, 20)
]
##############################################################################################
fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 10))
backdrop_image = plt.imread("backdrop.jpg")

ax0.set_aspect("equal")
ax0.fill([0, 500, 500, 0], [0, 0, 50, 50])
ax0.set_xlim(0, 500)
ax0.set_ylim(0, 50)
ax0.imshow(backdrop_image, extent=[0, 500, 0, 50])

for light in lights:
    circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
    ax0.add_patch(circle)

ax1.set_aspect("equal")
ax1.set_xlim(0, 500)
ax1.set_ylim(0, 500)


ax1.imshow(backdrop_image, extent=[0, 500, 0, 500])
#######################################################################################################3
#halo = Circle([250, 250], 180, facecolor="none", edgecolor="red", linewidth=5, alpha=0.5)
#ax1.add_patch(halo)
#halo_visible = False
guitar1 = Circle([150, 200], 20, color="black")
ax1.add_patch(guitar1)
guitar2 = Circle([150, 230], 15, color="black")
ax1.add_patch(guitar2)
guitar3 = Rectangle((145, 245), 10, 50, color="wheat")
ax1.add_patch(guitar3)
drum1 = Circle([250, 250], 30, color="black")
ax1.add_patch(drum1)
drum2 = Rectangle((280, 180), 10, 70, color="wheat")
ax1.add_patch(drum2)
drum3 = Rectangle((210, 180), 10, 70, color="wheat")
ax1.add_patch(drum3)
piano1 = Rectangle((150, 100), 200, 70, color="black")
ax1.add_patch(piano1)

for value in range(160, 350, 15):
    piano2 = Rectangle((value, 150), 5, 20, color="white")
    ax1.add_patch(piano2)
###############################################################################################
iteration_count = 0  
max_iterations = 20 
#################################################################################################
#group1 = LightGroup([lights[0], lights[2],lights[4],lights[6],lights[8]])
#group2 = LightGroup([lights[2], lights[3],lights[5],lights[7],lights[9]])
group1 = LightGroup([lights[0], lights[1],lights[2],lights[3],lights[4]])
group2 = LightGroup([lights[5], lights[6],lights[7],lights[8],lights[9]])
###################################################################################################

##################################################################################################
def update_frame(frame):
    global iteration_count
    #####################
    ax0.cla()
    ax0.set_aspect("equal")
    ax0.fill([0, 500, 500, 0], [0, 0, 50, 50],color='black')
    ax0.set_xlim(0, 500)
    ax0.set_ylim(0, 50)
    ####################
    #for light in lights:
        #circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        #ax0.add_patch(circle)
    #####################
    for group in [group1, group2]:
        group.set_spread_angle(random.randint(10, 25))
        group.set_intensity(random.uniform(8, 11)/11.0)
        #group.set_color("brown")
    ##################################
    

    for light in group1.lights:
        direction = light.direction
        x, y = light.position
        spread_angle = light.spread_angle
        speed = light.speed
         #################################3
     
     
        #light.position = [x, y]  # Update the light's position
        ##########################
        
        #circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        #ax0.add_patch(circle)
        

        #cone = Wedge((x, y), radius, direction - spread_angle, direction + spread_angle, color=light.color, alpha=light.intensity)
        #ax1.add_patch(cone)
        cone = Wedge((x, y), 145, direction - spread_angle, direction + spread_angle, color=light.color, alpha=light.intensity)
        ax1.add_patch(cone)
    #########################################################
    for light in group2.lights:
        direction = light.direction
        x, y = light.position
        spread_angle = light.spread_angle
        speed = light.speed

        # Update x position
        #if x < 405:
            #x += 45
        #else:
           # x = 45

        light.position = [x, y]  
        # Change color in odd iterations
        

        #circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        #ax0.add_patch(circle)
        
        cone = Wedge((x, y), 150, direction - spread_angle, direction + spread_angle, color=light.color, alpha=light.intensity)
        ax1.add_patch(cone)

    #####################################################################
    if iteration_count == max_iterations:
        ax1.cla()
        ax1.set_aspect("equal")
        ax1.set_xlim(0, 500)
        ax1.set_ylim(0, 500)
        ax1.imshow(backdrop_image, extent=[0, 500, 0, 500])

        #ax1.add_patch(halo)
        ax1.add_patch(guitar1)
        ax1.add_patch(guitar2)
        ax1.add_patch(guitar3)
        ax1.add_patch(drum1)
        ax1.add_patch(drum2)
        ax1.add_patch(drum3)
        ax1.add_patch(piano1)

        for value in range(160, 350, 15):
            piano2 = Rectangle((value, 150), 5, 20, color="white")
            ax1.add_patch(piano2)
    #  handle mouse click event
def on_click(event):
    if event.inaxes == ax1:
        if guitar1.contains(event)[0]:
            pygame.mixer.music.play()

# Connect the click event handler to the figure
fig.canvas.mpl_connect('button_press_event', on_click)




#########################################################################
        
###################################################################################
animation = FuncAnimation(fig, update_frame, frames=range(0, max_iterations + 30), interval=200)
######################################################################################
plt.show()
