##########################################################################
# AUTHOR: Caleb Hoffman                                                  #
# CLASS: Optics and Photonics                                            #
# ASSIGNMENT: Traditional Telescope/Galilean Telescope                   #
# REMARKS: This program simulates a traditional telescope optical system #
##########################################################################

import matplotlib.pyplot as plt
import math
from math import tan
from math import pi
from matplotlib.patches import Ellipse


def main():

    ans = True
    while ans:
        print("""
        1: Traditional Telescope Instructions
        2: Galilean Telescope Instructions
        3: Continue Without Instructions
        """)
        ans = input("Please select one of the following options: ")
        print()
        if ans == "1":
            print("""
                    ************************************************************
                    For a Traditional Telescope the objective focal length
                    must be greater than the eyepiece focal length, and both
                    values must be positive. Incident angle should be no greater
                    than 2 degrees from the optical axis.
                    TEST VALUES --> Incident Angle: 0.5, Objective Lens: 70
                                                         Eyepiece Lens: 10
                    ************************************************************
                    """)
        elif ans == "2":
            print("""
                    *************************************************************
                    For a Galilean Telescope the objective focal length must be
                    positive, and the eyepiece focal length negative. Hoewever 
                    the absolute value of objective focal length must be greater
                    than eyepiece focal length. Incident angle should be no
                    greater than 2 degrees from the optical axis.
                    TEST VALUES --> Incident Angle: 0.5, Objective Lens: 70
                                                         Eyepiece Lens: -10
                    *************************************************************
                    """)
        elif ans == "3":
            break
        else:
            print("Unknown option selected")
    # User input
    d = 10.0
    alpha1 = float(input("Enter Incident Angle: "))
    if alpha1 >= 2.1:
        alpha1 = float(input("Try an incident angle less than 2 degrees: "))
    alpha1 *= (pi/180)
    f_o = float(input("Enter Objective Focal Length: "))
    f_e = float(input("Enter Eyepiece Focal Length: "))

    # Safe gaurd to assure user produces appropriate input for focal lengths
    if f_e > f_o:
        f_o, f_e = f_e, f_o
    f_sum = f_e + f_o

    # Declares domain for both sides of the lens as a list wrt f_e & f_o
    xRange = [x for x in range(int(-f_o*2), 1)]
    xRange2 = [x for x in range(0, int(f_o+f_e)+1)]
    xRange3 = [x for x in range(int(f_o+f_e), int(f_e+f_o)*2)]

    # Angular magnification
    m_a = (-f_o/f_e) 
    
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
    
    # vlines (x=0, ymin, ymax) draws out the lens
    plt.vlines(0, (-d/2), (d/2), linestyles = ':', color = 'grey')
    plt.vlines((f_e+f_o), (-d/2), (d/2), linestyles = ':', color = 'grey')
    if f_e > 0:
        draw_convex(f_e, f_o, d,f_sum)
    else:
        draw_concave(f_e, f_o, d,f_sum)

    # Optical Axis
    plt.hlines(0, -2*f_o, (f_e+f_o)*2, linestyles = ':', color = 'black')
    
    # Draw three identical rays
    draw_rays(f_e,f_o,d,xRange,xRange2,xRange3,alpha1,f_sum)

    # This displays the generated plot (ray trace display)
    plt.show()

# These following two functions draw the lenses for visualization
def draw_convex(f_e, f_o, d,f_sum):
    fig = plt.gcf()
    ax =fig.gca()
    pos_lens_o = Ellipse(xy=(0,0), width=d/3, height=d*1.2, fc = "cyan")
    pos_lens_e = Ellipse(xy=(f_sum,0), width=d/3, height=d*1.2, fc = "cyan")
    ax.add_patch(pos_lens_o)
    ax.add_patch(pos_lens_e)

def draw_concave(f_e, f_o, d,f_sum):
    fig = plt.gcf()
    ax =fig.gca()
    pos_lens_o = Ellipse(xy=(0,0), width=d/3, height=d*1.2, fc = "cyan")
    neg_lens_e = Ellipse(xy=(f_sum,0), width=d/3, height=d*1.2, fc = "cyan")
    ax.add_patch(pos_lens_o)
    ax.add_patch(neg_lens_e)
    
def draw_rays(f_e,f_o,d,xRange,xRange2,xRange3,alpha1,f_sum):
        
    for i in range(3):
        
        x_1 = (d/2)*(1-i)

    # This section computes incidents rays on the objective lens
        zDomain = [alpha1*x+x_1 for x in xRange]
        plt.plot(xRange, zDomain, color = 'red')

    # This section computes ray propogation through the telescope
        alpha2 = (alpha1) - (x_1/f_o)
        zDomain2 = [alpha2*x+ x_1 for x in xRange2]
        plt.plot(xRange2, zDomain2, color = 'blue')

    # Computes rays transmitted through the eyepiece
        alpha3 = alpha1*(-f_o/f_e)
        zDomain3 = [alpha3*(x-(f_sum)) + x_1*(-f_e/f_o) + alpha1*(f_sum)  for x in xRange3]
        plt.plot(xRange3, zDomain3, color = "green")

# Invokes main 
main()
