<<<<<<< HEAD
# Concert Stage Simulation Project

## Contents

- **`light.py`**: 
  - Simulation of lights using Python. 
  - Includes click functionality to interact with lights on `plot1`.

- **`light_group.py`**: 
  - Grouping of lights for synchronized effects.

- **`props.py`**: 
  - Simulation of props with sound effects triggered on interaction.

- **`backdrop.py`**: 
  - Changes the backdrop using data from an external file.

- **`smoke_machine.py`**: 
  - Simulation for a smoke machine with dispersion effects.

- **`choreography.py`**: 
  - Design and control the choreography for lights and stage elements.

- **`spinal_tap.py`**: 
  - Final version of the project (not fully implemented).

---

## Dependencies

The project relies on the following Python libraries:
- `matplotlib.pyplot` - For plotting and visualization
- `numpy` - For numerical computing and array operations
- `pygame` - For handling multimedia and events
- `scipy` - For scientific computing

---

## Version Information

- **Project**: Concert Stage Simulation Project (COMP1005 - Fundamentals of Programming)
- **Technologies**: Object-Oriented Programming, Python
- **Duration**: April 2023 – May 2023
- **Date**: 25/05/2023

### Project Overview
Developed a Concert Stage Simulation for a fictional rock band, **Spinal Tap**, using object-oriented principles to model key components of the stage, including lights, smoke machines, props, backdrop, and choreography.

### Key Features and Contributions
- **Lights**:
  - Modeled various light types (solid, patterned, and lasers) as objects with attributes such as color, position, direction, and intensity.
  - Implemented a mechanism to group and synchronize lights for dynamic lighting effects.

- **Smoke Machine**:
  - Simulated smoke dispersion and interaction with lighting using object-oriented design.
  - Incorporated neighborhood diffusion models (Moore and Van-Neumann) to control smoke behavior.

- **Props and Band**:
  - Created objects to represent the band members and stage props with dynamic positioning.
  - Ensured accurate visual effects with interaction between props and lights.

- **Backdrop**:
  - Developed a flexible backdrop system with options for dynamic loading and scaling, allowing for interactive stage designs.

- **Choreography**:
  - Enabled pre-set lighting and stage movements via choreography files.
  - Automated the simulation with time-based control.

- **Automation and Parameter Control**:
  - Used command-line arguments to control input parameters.
  - Enabled experiments and tests with different setups and configurations.

---

## How to Run the Project
Ensure all dependencies are installed:
```bash
pip install matplotlib numpy pygame scipy
