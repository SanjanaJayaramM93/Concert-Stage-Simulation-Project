###2.	Smoke machine: There should be one or more smoke machine objects, which should include position, direction, intensity (0-11). 
#Smoke should diffuse using a choice of Moore or Van-Neumann neighbourhoods.
#Prompts: How will the light interact with the smoke? What forces will apply to the movement of the smoke? 
#How will the neighbourhood options affect your simulation? How will the timesteps for the smoke simulation sit within the overall program?
############################################Dependencies##############################################################################################3
import matplotlib.pyplot as plt
import numpy as np
import random
####################################SmokeMachine Class#########################################3
class SmokeMachine:
    def __init__(self, position, direction, intensity):
        self.position = position
        self.direction = direction
        self.intensity = intensity
        self.moore_neighborhood = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0]
        self.von_neumann_neighborhood = [(-1, 0), (1, 0), (0, -1), (0, 1)]
     #smoke diffusion
    def diffuse(self, grid, neighborhood='moore'):
        if neighborhood == 'moore':
            neighbors = self.moore_neighborhood
        else:
            neighbors = self.von_neumann_neighborhood

        x, y = self.position
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                neighbor_smoke = grid[nx][ny]
                currg_slice = grid[x-1:x+2, y-1:y+2]
                neighbor_sum = currg_slice.sum() + grid[x][y]
                next_smoke = 0.1 * neighbor_sum
                grid[nx][ny] = next_smoke
    #update smoke
    def update(self, grid, neighborhood='moore'):
        self.diffuse(grid, neighborhood)


def main():
    #set grid size
    grid_size = 500 ####later updation
    ###object of class SmokeMachine
    smoke_machine1 = SmokeMachine((0, 0), random.choice(['up', 'down', 'left', 'right']), random.uniform(0, 11))
    #####creating array
    grid = np.zeros((grid_size, grid_size))
    ################################Plot####################################################3
    fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 10))
    ax0.set_aspect("equal")
    ax0.set_title("Plot 1")
    ax0.fill([0, 500, 500, 0], [0, 0, 50, 50], color="black")

    ax1.set_aspect("equal")
    ax1.set_title("Plot 2")
    ax1.fill([0, 500, 500, 0], [0, 0, 500, 500], color="black")
    ###############################################################################################
    ###################set values ################################################################
    x_values_1 = []
    y_values_1 = []
    for _ in range(1000):
        x_values_1.append(random.randint(0, grid_size - 1))
        y_values_1.append(random.randint(0, grid_size - 1))

    for x, y in zip(x_values_1, y_values_1):
        smoke_machine1.update(grid, neighborhood='moore')
        alpha = random.uniform(0.1, 1.0)
        size = random.uniform(50, 1000)
        colors = ['red', 'blue','yellow']
        x_repeated = np.repeat(x, len(colors))
        y_repeated = np.repeat(y, len(colors))
        ax1.scatter(x_repeated, y_repeated, color=colors, alpha=alpha, s=size)
        plt.pause(0.1)

    ax1.imshow(grid, cmap='hot', interpolation='nearest', origin='lower', extent=[0, grid_size, 500, grid_size], vmax=11)
    plt.show()

main()
