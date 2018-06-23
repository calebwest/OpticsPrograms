# AUTHOR: Caleb Hoffman
# CLASS: Optics and Photonics
# ASSIGNMENT: Computer Problem 2
# REMARKS: Enter a value for the incident angle on a thin lens of 2.0cm, and
# the focal length. A plot will open in  a seperate window, which will display
# light striking a thin lens, and the resulting output rays. This program uses
# a derived ray transfer matrix equation to compute the ouput angle of a thin
# lens.
# DISCLAIMER: This program will be further developed to compute a series of
# lenses to achieve other various tasks.

import matplotlib.pyplot as plt
import math
from math import tan
from math import pi


# The primary function of this program is to compute the result of light
# striking a thin lens of a specific angle and focal length
def main():

    d = 2.0 # centimeters
    input_angle = float(input("Enter Incident Angle: "))*(pi/180)
    f = float(input("Enter Focal Length: "))

    # Declares domain for both sides of the lens as a list constrained to f input
    xDomain = [x for x in range(int(-f*1.3), 1)]
    xDomain_Output = [x for x in range(0, int(f*1.3))]

    # The slope of the line is the tangent of the input angle
    m = tan(input_angle)
    
    
    # Chart labels
    plt.title("Thin Lens-Object at Infinity")
    plt.xlabel("Optical Axis (cm)")
    plt.ylabel("Ray Elevation (cm)")

    # Imposes a grid making the plot easier to read
    plt.grid(color='black', linestyle=':', linewidth = 0.5)
    
    # vlines (x=0, ymin, ymax) draws out the lens (in black)
    plt.vlines(0, (-d/2), (d/2), color = 'black')


    
    # This loop computes three identical rays striking
    # the lens. Followed by the output 
    for i in range(3):

        # This section computes incidents rays
        zRange = [m*x+((1-i)*(d/2)) for x in xDomain]
        plt.plot(xDomain, zRange, color = 'red')

        # This section computes transmitted rays
        output_angle = (input_angle) - (((1-i)*(d/2))/f)
        m_Output = tan(output_angle) 
        zRange_Output = [m_Output*x+((1-i)*(d/2)) for x in xDomain_Output]
        plt.plot(xDomain_Output, zRange_Output, color = 'blue')

    # This displays the generated plot (ray trace display)
    plt.show()


    
    
# Invokes main 
main()
