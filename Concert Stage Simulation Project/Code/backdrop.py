#4.	Backdrop: The backdrop for the stage defaults to black or is read from a file. You need to decide a suitable file format and whether it defines the stage size, or is scaled to the pre-defined stage size.
#Prompts: Will the backdrop be colour or monochrome (clack and white)? How will it be affected by the lights?
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

face = plt.imread("logo.jpg")

stage_height, stage_width = face.shape[:2]

# grayscle
face_gray = np.dot(face[..., :3], [0.2989, 0.5870, 0.1140])

# Create sub-sampled versions of the image
pixel_face = face[::10, ::10]
pixel_face2 = face[::50, ::50]

# Set initial parameters
is_grayscale = False
alpha = 0.5

#  toggle 
def toggle_grayscale():
    global is_grayscale
    is_grayscale = not is_grayscale

#  change alpha value
def update_alpha():
    global alpha
    alpha += 0.1
    if alpha > 1.0:
        alpha = 0.0  
# Update the backdrop image, grayscale/color, and alpha values in each iteration
def update_figure():
    if is_grayscale:
        img_display = face_gray
        cmap = 'gray'
    else:
        img_display = face
        cmap = None

    ax0.imshow(img_display, extent=[0, stage_width, 0, stage_height], cmap=cmap, alpha=alpha)
    ax1[0].imshow(pixel_face, extent=[0, stage_width // 10, 0, stage_height // 10], cmap=cmap, alpha=alpha)
    ax1[1].imshow(pixel_face2, extent=[0, stage_width // 50, 0, stage_height // 50], cmap=cmap, alpha=alpha)
    ax1[2].imshow(face, extent=[0, stage_width, 0, stage_height], cmap=cmap, alpha=alpha)

    # Set title and labels
    ax0.set_title("Plot 1 (Grayscale: {})".format(is_grayscale))
    ax0.set_xlabel("X-axis")
    ax0.set_ylabel("Y-axis")

    ax1[0].set_title("Plot 2 (Sub-sampled 1) (Grayscale: {})".format(is_grayscale))
    ax1[0].set_xlabel("X-axis")
    ax1[0].set_ylabel("Y-axis")

    # Display the figure
    plt.draw()

#  figure and axes
fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 10))
ax0.set_aspect("equal")
ax0.set_title("Plot 1")
ax0.fill([0, stage_width, stage_width, 0], [0, 0, 50, 50], color="black")

# Initialize the ax1 subplots
ax1 = [ax1] * 3

# Call the update_figure function to display the initial figure
update_figure()

# Update loop
for _ in range(10):
    toggle_grayscale()
    update_alpha()

    # Apply rotation to the image
    angle = np.random.randint(0, 360)  # Random angle between 0 to 360 
    face = ndimage.rotate(face, angle, reshape=False)
    face_gray = np.dot(face[..., :3], [0.2989, 0.5870, 0.1140])

    update_figure()
    plt.pause(0.5)
