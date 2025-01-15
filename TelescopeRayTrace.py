##########################################################################
# Revised - Traditional Telescope/Galilean Telescope                     #
# REMARKS: This program simulates a traditional telescope optical system #
##########################################################################

import matplotlib.pyplot as plt
from math import tan, pi
from matplotlib.patches import Ellipse

def display_instructions():
    """Displays the instructions for using the telescope simulation."""
    instructions = [
        """
        1: Traditional Telescope Instructions
        2: Galilean Telescope Instructions
        3: Continue Without Instructions
        """,
        """
        ************************************************************
        For a Traditional Telescope, the objective focal length
        must be greater than the eyepiece focal length, and both
        values must be positive. The incident angle should be no greater
        than 2 degrees from the optical axis.
        SAMPLE VALUES --> Incident Angle: 0.5, Objective Lens: 70
                                                   Eyepiece Lens: 10
        ************************************************************
        """,
        """
        *************************************************************
        For a Galilean Telescope, the objective focal length must be
        positive, and the eyepiece focal length negative. However, 
        the absolute value of the objective focal length must be greater
        than the eyepiece focal length. The incident angle should be no
        greater than 2 degrees from the optical axis.
        SAMPLE VALUES --> Incident Angle: 0.5, Objective Lens: 70
                                                   Eyepiece Lens: -10
        *************************************************************
        """
    ]
    return instructions

def get_user_input() -> tuple[float, float, float]:
    """Prompts the user for input values."""
    while True:
        try:
            incident_angle = float(input("Enter Incident Angle (degrees): "))
            if incident_angle >= 2.1:
                print("Incident angle must be less than 2 degrees. Please try again.")
                continue

            objective_focal_length = float(input("Enter Objective Focal Length (cm): "))
            eyepiece_focal_length = float(input("Enter Eyepiece Focal Length (cm): "))
            return incident_angle, objective_focal_length, eyepiece_focal_length
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def draw_lens(f_sum: float, d: float, is_convex: bool):
    """Draws the lenses for the telescope visualization."""
    fig = plt.gcf()
    ax = fig.gca()
    objective_lens = Ellipse(xy=(0, 0), width=d/3, height=d*1.2, fc="cyan")
    eyepiece_lens = Ellipse(xy=(f_sum, 0), width=d/3, height=d*1.2, fc="cyan")
    ax.add_patch(objective_lens)
    ax.add_patch(eyepiece_lens)

def draw_rays(f_e: float, f_o: float, d: float, alpha1: float, f_sum: float):
    """Draws the light rays passing through the telescope."""
    for i in range(3):
        y_offset = (d / 2) * (1 - i)

        # Incident rays on the objective lens
        x_incident = list(range(int(-2*f_o), 1))
        y_incident = [alpha1 * x + y_offset for x in x_incident]
        plt.plot(x_incident, y_incident, color='red')

        # Rays through the telescope
        x_through = list(range(0, int(f_sum) + 1))
        alpha2 = alpha1 - (y_offset / f_o)
        y_through = [alpha2 * x + y_offset for x in x_through]
        plt.plot(x_through, y_through, color='blue')

        # Rays exiting the eyepiece
        x_exit = list(range(int(f_sum), int(2*f_sum)))
        alpha3 = alpha1 * (-f_o / f_e)
        y_exit = [alpha3 * (x - f_sum) + y_offset * (-f_e / f_o) + alpha1 * f_sum for x in x_exit]
        plt.plot(x_exit, y_exit, color='green')

def main():
    instructions = display_instructions()

    while True:
        print(instructions[0])
        choice = input("Select an option (1, 2, or 3): ").strip()

        if choice == "1":
            print(instructions[1])
            break
        elif choice == "2":
            print(instructions[2])
            break
        elif choice == "3":
            break
        else:
            print("Invalid selection. Please try again.")

    try:
        incident_angle, f_o, f_e = get_user_input()
        incident_angle_rad = incident_angle * (pi / 180)  # Convert to radians

        # Ensure focal lengths are appropriate
        if f_e > f_o:
            f_o, f_e = f_e, f_o

        d = 10.0  # Diameter of the lenses
        f_sum = f_o + f_e  # Distance between lenses

        # Angular magnification
        magnification = -f_o / f_e

        # Set up the plot
        plt.title(f"{'Galilean' if f_e < 0 else 'Traditional'} Telescope\n" +
                  rf"$M_A = {magnification:.3f}$")
        plt.xlabel("Optical Axis (cm)")
        plt.ylabel("Ray Elevation (cm)")
        plt.grid(color='black', linestyle=':', linewidth=0.5)

        # Draw the optical axis
        plt.hlines(0, -2*f_o, 2*f_sum, linestyles=':', color='black')
        plt.vlines(0, -d/2, d/2, linestyles=':', color='grey')
        plt.vlines(f_sum, -d/2, d/2, linestyles=':', color='grey')

        # Draw lenses and rays
        draw_lens(f_sum, d, is_convex=f_e > 0)
        draw_rays(f_e, f_o, d, incident_angle_rad, f_sum)

        # Show the plot
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
