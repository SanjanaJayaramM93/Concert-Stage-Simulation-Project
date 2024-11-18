import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Wedge
from matplotlib.animation import FuncAnimation
import numpy as np
import random
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
class SmokeMachine:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity
        
        self.flow = 0
        self.smoke = []
  
    def startSmoke(self):
        self.flow = 1

    def stopSmoke(self):
        self.flow = 0

    def stepChange(self):
        if self.flow == 1:
            self.smoke.append([self.position[0], self.position[1]])
        for s in self.smoke:
            random_x = np.random.randint(0, 100)
            random_y = np.random.randint(0, 100)
            s[0] += random_x
            s[1] += random_y

    def plotSmokes(self, ax1):
        xvalues = [s[0] for s in self.smoke]
        yvalues = [s[1] for s in self.smoke]
        ax1.scatter(xvalues, yvalues, s=[500], c="beige", alpha=0.3)
####################################################################################################3
lights = [
    Light("tomato", [45, 500], 0.8, 270, 10, 10),
    Light("gold", [90, 500], 0.6, 270, 10, 15),
    Light("tomato", [135, 500], 0.7, 270, 10, 20),
    Light("gold", [180, 500], 0.5, 270, 10, 10),
    Light("tomato", [225, 500], 0.9, 270, 10, 15),
    Light("gold", [270, 25], 0.4, 270, 10, 20),
    Light("tomato", [315, 25], 0.6, 270, 10, 10),
    Light("gold", [360, 25], 0.8, 270, 10, 15),
    Light("tomato", [405, 25], 0.7, 270, 10, 20),
    Light("gold", [495, 25], 0.7, 270, 10, 20)
]
##############################################################################################
fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 10))

ax0.set_aspect("equal")
ax0.fill([0, 500, 500, 0], [0, 0, 50, 50], color="black")
ax0.set_xlim(0, 500)
ax0.set_ylim(0, 50)

for light in lights:
    circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
    ax0.add_patch(circle)

ax1.set_aspect("equal")
ax1.set_xlim(0, 500)
ax1.set_ylim(0, 500)
backdrop_image = plt.imread("logo.jpg")
ax1.imshow(backdrop_image, extent=[0, 500, 0, 500])
#######################################################################################################3
halo = Circle([250, 250], 180, facecolor="none", edgecolor="red", linewidth=5, alpha=0.5)
ax1.add_patch(halo)
halo_visible = True
piano1 = Rectangle((150, 100), 200, 70, color="dimgrey")
ax1.add_patch(piano1)

for value in range(160, 350, 15):
    piano2 = Rectangle((value, 150), 5, 20, color="white")
    ax1.add_patch(piano2)
###############################################################################################
iteration_count = 0  
max_iterations = 20 
#################################################################################################
group1 = LightGroup([lights[0], lights[2],lights[4],lights[6],lights[8]])
group2 = LightGroup([lights[2], lights[3],lights[5],lights[7],lights[9]])
#group3 = LightGroup([lights[0], lights[1],lights[2],lights[3],lights[4]])
#group3 = LightGroup([lights[5], lights[6],lights[7],lights[8],lights[9]])
###################################################################################################
smoke_machine1 = SmokeMachine([0, 220], 0.5)
smoke_machine2 = SmokeMachine([400, 0], 0.5)
##################################################################################################
def update_frame(frame):
    global iteration_count
    #####################
    ax0.cla()
    ax0.set_aspect("equal")
    ax0.fill([0, 500, 500, 0], [0, 0, 50, 50], color="black")
    ax0.set_xlim(0, 500)
    ax0.set_ylim(0, 50)
    ####################
    #for light in lights:
        #circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        #ax0.add_patch(circle)
    #####################
    for group in [group1, group2]:
        group.set_spread_angle(random.randint(10, 12))
        group.set_intensity(random.uniform(0, 11)/11.0)
        #group.set_color("brown")
    ##################################
    #for light in lights:
        #circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        #ax0.add_patch(circle)

    #for group in [group1, group2]:
        #group.set_spread_angle(random.randint(10, 10))
        #
        # group.set_intensity(random.uniform(0, 11)/11.0)
        #group.set_color("blue")

    for light in group1.lights:
        direction = light.direction
        x, y = light.position
        spread_angle = light.spread_angle
        speed = light.speed
         #################################3
        # Update x position
        if x < 495:
            x += 45
        else:
            x = 45
         # Update y position - movemnt in y axis
        if y == 500:
            y= 25
        elif y==25:
            y=500
     
        light.position = [x, y]  # Update the light's position
        ##########################
        if iteration_count % 2 == 0:  # Change color in even iterations
            group1.set_color("wheat")
        else:  # Revert back to original color in odd iterations
            group1.set_color("brown")

        circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        #backdrop_image = plt.imread("logo.jpg")
        #ax0.imshow(backdrop_image, extent=[0, 500, 0, 50])
        ax0.add_patch(circle)
        min_radius = 50
        max_radius = 100
        radius = random.uniform(min_radius, max_radius)

        cone = Wedge((x, y), radius, direction - spread_angle, direction + spread_angle, color=light.color, alpha=light.intensity)
        ax1.add_patch(cone)
        ##cone = Wedge((x, y), 200, direction - spread_angle, direction + spread_angle, color=light.color, alpha=light.intensity)
        #ax1.add_patch(cone)
    #########################################################
    for light in group2.lights:
        direction = light.direction
        x, y = light.position
        spread_angle = light.spread_angle
        speed = light.speed

        # Update x position
        if x < 405:
            x += 45
        else:
            x = 45

        light.position = [x, y]  
        # Change color in odd iterations
        if iteration_count % 2 != 0:  
            group2.set_color("ivory")
        else:  
            group2.set_color("salmon")

        circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        ax0.add_patch(circle)
        
        cone = Wedge((x, y), 100, direction - spread_angle, direction + spread_angle, color=light.color, alpha=light.intensity)
        ax1.add_patch(cone)

    #####################################################################
    if iteration_count == max_iterations:
        ax1.cla()
        ax1.set_aspect("equal")
        ax1.set_xlim(0, 500)
        ax1.set_ylim(0, 500)
        ax1.imshow(backdrop_image, extent=[0, 500, 0, 500], alpha=0.5)

        ax1.add_patch(halo)
       
        ax1.add_patch(piano1)

        for value in range(160, 350, 15):
            piano2 = Rectangle((value, 150), 5, 20, color="white")
            ax1.add_patch(piano2)
#########################################################################
        smoke_machine1.startSmoke()
        smoke_machine2.startSmoke()
    if smoke_machine1.flow == 1:
        smoke_machine1.stepChange()
        smoke_machine1.plotSmokes(ax1)

    if smoke_machine2.flow == 1:
        smoke_machine2.stepChange()
        smoke_machine2.plotSmokes(ax1)
    iteration_count += 1
###################################################################################
animation = FuncAnimation(fig, update_frame, frames=range(0, max_iterations + 30), interval=200)
######################################################################################
plt.show()
