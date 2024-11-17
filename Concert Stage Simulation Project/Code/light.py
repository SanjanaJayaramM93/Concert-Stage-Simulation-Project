###1.	Lights: Represented as objects that “know” their colour, position, direction and intensity (0-11). 
#We are mainly focussed on down-lighting, Lights can be grouped to work as synchronised sets.
# Lights may be solid colours, combinations of colours, patterns/shapes (gobo stencils) or lasers.
#Prompts: How will you represent the “spread” of the light – the cone it shines through? 
#How will you group lights and provide a mechanism to drive them as a collection? What types of lights will you include?

###Dependencies######################################################################################
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import random
####Light class definition##################################################################################
class Light:
    def __init__(self, color, position, intensity, direction, spread_angle, speed):
        self.color = color
        self.position = position
        self.intensity = intensity
        self.direction = direction
        self.spread_angle = spread_angle
        self.speed = speed
########################################################################################################
lights = [
    Light("skyblue", [45, 500], 0.8, 270, 10, 10),
    Light("pink", [90, 500], 0.6, 270, 10, 15),
    Light("skyblue", [135, 500], 0.7, 270, 10, 20),
    Light("pink", [180, 500], 0.5, 270, 10, 10),
    Light("skyblue", [225, 500], 0.9, 270, 10, 15),
    Light("pink", [270, 500], 0.4, 270, 10, 20),
    Light("skyblue", [315, 500], 0.6, 270, 10, 10),
    Light("pink", [360, 500], 0.8, 270, 10, 15),
    Light("skyblue", [405, 500], 0.7, 270, 10, 20),
    Light("pink", [495, 25], 0.7, 270, 10, 20)
]
#####################################################################################################################
###################################PLOT#############################################################################
#fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 10))
fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 20))

#subplot1
ax0.set_aspect("equal")
ax0.fill([0, 500, 500, 0], [0, 0, 50, 50], color="black")
ax0.set_xlim(0, 500)
ax0.set_ylim(0, 50)
#axo-lights-circles
for light in lights:
    circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
    ax0.add_patch(circle)
#ax1-plot
ax1.set_aspect("equal")
ax1.set_xlim(0, 500)
ax1.set_ylim(0, 500)
ax1.fill([0, 500, 500, 0], [0, 0, 500, 500], color='black')
#####################################################################################################################
######Iteration###############
iteration_count = 0  
max_iterations = 10 ######will change  with conditions

while iteration_count < max_iterations:
    ax0.cla()
    ax0.set_aspect("equal")
    ax0.fill([0, 500, 500, 0], [0, 0, 50, 50], color="black")
    ax0.set_xlim(0, 500)
    ax0.set_ylim(0, 50)
    ####circles for ax0
    for light in lights:
        #circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        #ax0.add_patch(circle)
        circle = plt.Circle(light.position,10, color=light.color, zorder=10, alpha=0.8)
        ax0.add_patch(circle)
    
    ###lights for ax1
    for i, light in enumerate(lights):
        direction = light.direction
        x, y = light.position
        spread_angle = light.spread_angle
        speed = light.speed
        intensity = light.intensity

        # Update x position-movement to lights -x axis
        if x < 495:
            x += 45
        else:
            x = 45
        # Update y position - movemnt in y axis
        if y == 500:
            y= 25
        elif y==25:
            y=500
         # Update the light's position x,y-for colour change
        light.position = [x, y] 
        ##even number lights
        if i % 2 == 0:  
            if iteration_count % 2 == 0:  
                light.color = "salmon"
            else:  
                light.color = "wheat"
        ##odd number lights
        else:  
            if iteration_count % 2 != 0:  
                light.color = "crimson"
            else:  
                light.color = "gold"
        
        circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        ax0.add_patch(circle)
        ##change in cone angle
        spread_angle = random.randint(10, 12)
        ##change in intensity(0-11)
        intensity = random.uniform(0, 11)/11.0
        ###wedge-cone
        #class matplotlib.patches.Wedge(center, r, theta1, theta2, *, width=None, **kwargs)
        cone = Wedge((x, y), 300, direction - spread_angle, direction + spread_angle, color=light.color, alpha=intensity)
        ax1.add_patch(cone)
     
    plt.suptitle("STAGEVIEW", fontsize="18")
    plt.pause(1)
    ##loop-increment
    iteration_count += 1

plt.close()
