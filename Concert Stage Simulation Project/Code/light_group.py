import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import random

class Light:
    def __init__(self, color, position, intensity, direction, spread_angle, speed):
        self.color = color
        self.position = position
        self.intensity = intensity
        self.direction = direction
        self.spread_angle = spread_angle
        self.speed = speed

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

lights = [
    Light("red", [45, 500], 0.8, 270, 10, 10),
    Light("green", [90, 500], 0.6, 270, 10, 15),
    Light("blue", [135, 500], 0.7, 270, 10, 20),
    Light("red", [180, 500], 0.5, 270, 10, 10),
    Light("red", [225, 500], 0.9, 270, 10, 15),
    Light("green", [270, 25], 0.4, 270, 10, 20),
    Light("red", [315, 25], 0.6, 270, 10, 10),
    Light("green", [360, 25], 0.8, 270, 10, 15),
    Light("skyblue", [405, 25], 0.7, 270, 10, 20),
    Light("pink", [495, 25], 0.7, 270, 10, 20)
]

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
ax1.fill([0, 500, 500, 0], [0, 0, 500, 500], color='black')

iteration_count = 0  # Counter to keep track of iterations
max_iterations = 20  # Maximum number of iterations

# Create light groups
group1 = LightGroup([lights[0], lights[2],lights[4],lights[6],lights[8]])
group2 = LightGroup([lights[2], lights[3],lights[5],lights[7],lights[9]])

while iteration_count < max_iterations:
    ax0.cla()
    ax0.set_aspect("equal")
    ax0.fill([0, 500, 500, 0], [0, 0, 50, 50], color="black")
    ax0.set_xlim(0, 500)
    ax0.set_ylim(0, 50)

    for light in lights:
        circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        ax0.add_patch(circle)

    for group in [group1, group2]:
        group.set_spread_angle(random.randint(10, 20))
        group.set_intensity(random.uniform(0, 1))
        group.set_color("blue")

    for light in group1.lights:
        direction = light.direction
        x, y = light.position
        spread_angle = light.spread_angle
        speed = light.speed

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

        if iteration_count % 2 == 0:  # Change color in even iterations
            group1.set_color("salmon")
        else:  # Revert back to original color in odd iterations
            group1.set_color("beige")

        circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        ax0.add_patch(circle)
        min_radius = 50
        max_radius = 100
        radius = random.uniform(min_radius, max_radius)

        cone = Wedge((x, y), radius, direction - spread_angle, direction + spread_angle, color=light.color, alpha=light.intensity)
        ax1.add_patch(cone)
        cone = Wedge((x, y), 200, direction - spread_angle, direction + spread_angle, color=light.color, alpha=light.intensity)
        ax1.add_patch(cone)

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

        light.position = [x, y]  # Update the light's position

        if iteration_count % 2 != 0:  # Change color in odd iterations
            group2.set_color("ivory")
        else:  # Revert back to original color in even iterations
            group2.set_color("teal")

        circle = plt.Circle(light.position, 10, color=light.color, zorder=10)
        ax0.add_patch(circle)
        min_radius = 10
        max_radius = 50
        radius = random.uniform(min_radius, max_radius)
        cone = Wedge((x, y), 100, direction - spread_angle, direction + spread_angle, color=light.color, alpha=light.intensity)
        ax1.add_patch(cone)

    plt.suptitle("STAGEVIEW", fontsize="18")
    plt.pause(1)

    iteration_count += 1

plt.close()