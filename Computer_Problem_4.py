# AUTHOR: Caleb Hoffman
# CLASS: Optics and Photonics
# ASSIGNMENT: Computer Problem 4
# REMARKS: 

import matplotlib.pyplot as plt
import math
from math import tan
from math import pi


# The primary function of this program is to compute the result of light
# striking a thin lens of a specific angle and focal length
def main():

    d = 10.0 # centimeters
    alpha1 = float(input("Enter Incident Angle: "))
    if alpha1 >= 2:
        alpha1 = float(input("Try an incident angle less than 2 degrees: "))
    alpha1 *= (pi/180)
    
    f = float(input("Enter Objective Focal Length: "))
    f2 = float(input("Enter Eyepiece Focal Length: "))
    if f > f2:
        f_e = f2
        f_o = f 
    if f < f2:
        f_e = f
        f_o = f2

    # Declares domain for both sides of the lens as a list constrained to f input
    xRange = [x for x in range(int(-f_o*2), 1)]
    xRange2 = [x for x in range(0, int(f_o)+1)]
    xRange3 = [x for x in range(int(f_o)+1, int(f_e+f_o)+1)]
    xRange4 = [x for x in range(int(f_o+f_e)+1, int(f_e+f_o)*2)]

    # The slope of the line is the tangent of the input angle
    m = tan(alpha1)
    m_a = -(f_o/f_e)
    
    
    # Chart labels
    if f_e > 0:
        plt.title("Telescope"+'\n'+r'$M_A = %0.3f$' %m_a \
              + '\t'*2)
    else:
        plt.title("Galilean Telescope"+'\n'+r'$M_A = %0.3f$' %m_a \
              + '\t'*2)
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

        # This section computes incidents rays on the objective lens
        zDomain = [m*x+((1-i)*(d/2)) for x in xRange]
        plt.plot(xRange, zDomain, color = 'red')

        # This section computes ray propogation through the telescope
        alpha2 = (alpha1) - (((1-i)*(d/2))/f_o)
        m2 = tan(alpha2) 
        zDomain2 = [m2*x+((1-i)*(d/2)) for x in xRange2]
        plt.plot(xRange2, zDomain2, color = 'blue')

        
        # Computes rays transmitted through the eyepiece
        #alpha4 = alpha2*(-f_o/f_e)
        #m3 = tan(alpha4)
        #zDomain4 = [m3*x+(1-i)*(d/2) for x in xRange4]
        #plt.plot(xRange4, zDomain4, color = "green")
        
    # THIS IS A TEST
    alpha4 = alpha2*(-f_o/f_e)
    m3 = tan(alpha4)
    zDomain4 = [m3*x+0 for x in xRange4]
    plt.plot(xRange4, zDomain4, color = "green")

    
    # This displays the generated plot (ray trace display)
    plt.show()


    
    
# Invokes main 
main()
