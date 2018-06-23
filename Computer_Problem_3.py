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
    alpha1 = float(input("Enter Incident Angle: "))*(pi/180)
    f = float(input("Enter Focal Length: "))
    f2 = float(input("Enter Second Focal Length: "))
    if f > f2:
        f_e = f2
        f_o = f 
    if f < f2:
        f_e = f
        f_o = f2

    # Declares domain for both sides of the lens as a list constrained to f input
    xRange = [x for x in range(int(-f_o*1.5), 1)]
    xRange2 = [x for x in range(0, int(f_o+f_e)+1)]
    xRange3 = [x for x in range(int(f_o+f_e), int(f_o+f_e)*2)]

    # The slope of the line is the tangent of the input angle
    m = tan(alpha1)
    
    
    # Chart labels
    plt.title("Thin Lens-Object at Infinity")
    plt.xlabel("Optical Axis (cm)")
    plt.ylabel("Ray Elevation (cm)")

    # Imposes a grid making the plot easier to read
    plt.grid(color='black', linestyle=':', linewidth = 0.5)
    
    # vlines (x=0, ymin, ymax) draws out the lens (in black)
    plt.vlines(0, (-d/2), (d/2), color = 'black')
    plt.vlines((f_e+f_o), (-d/2), (d/2), color = 'black')
    


    
    # This loop computes three identical rays striking
    # the lens. Followed by the output 
    for i in range(3):

        # This section computes incidents rays
        zDomain = [m*x+((1-i)*(d/2)) for x in xRange]
        plt.plot(xRange, zDomain, color = 'red')

        # This section computes transmitted rays
        alpha2 = (alpha1) - (((1-i)*(d/2))/f_o)
        m2 = tan(alpha2) 
        zDomain2 = [m2*x+((1-i)*(d/2)) for x in xRange2]
        plt.plot(xRange2, zDomain2, color = 'blue')

        #
        #alpha3 = ((1-(f_e+f_o)/f_e)*alpha1-(1/(f_o)*(1-((f_e+f_o)/f_e)+(1/f_e))))*(1-i)*(d/2)
        alpha3 = (-f_o/f_e)*alpha1
        #zDomain3 = [((f_e+f_o)*alpha3 + (1 - (f_e+f_o)/f_o)*(x-(f_e+f_o)))*(0.123) for x in xRange3]
        zDomain3 = [(-f_e/f_o)*(f_e+f_o) + alpha3*(f_o+f_e) for x in xRange3]
        plt.plot(xRange3, zDomain3, color = "green")
        

    # This displays the generated plot (ray trace display)
    plt.show()


    
    
# Invokes main 
main()
