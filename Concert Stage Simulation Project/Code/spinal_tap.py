import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import sys
import importlib

def display_menu():
    print("Choreography Menu:")
    print("1. Choreography 1")
    print("2. Choreography 2")
    print("3. Choreography 3")
    print("0. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 0 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def setup_plot():
    fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 10))

    ax0.set_aspect("equal")
    ax0.fill([0, 500, 500, 0], [0, 0, 50, 50], color="black")
    ax0.set_xlim(0, 500)
    ax0.set_ylim(0, 50)

    ax1.set_aspect("equal")
    ax1.set_xlim(0, 500)
    ax1.set_ylim(0, 500)
    backdrop_image = plt.imread("backdrop.jpg")
    ax1.imshow(backdrop_image, extent=[0, 500, 0, 500], alpha=0.5)

    return fig, ax0, ax1


def main():
    fig, ax0, ax1 = setup_plot()

    while True:
        choice = display_menu()

        if choice == 0:
            sys.exit("Exiting...")
        #file name
        module_name = f"choreography{choice}"
        try:
            choreography_module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            print(f"Choreography {choice} is not available.")
            continue

        #  animation object from the choreography script
        animation = choreography_module.animation

        # Call the animation object
        animation(fig, ax0, ax1)

        # Show the plot
        plt.show()


if __name__ == "__main__":
    main()
