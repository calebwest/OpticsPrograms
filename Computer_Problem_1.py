# AUTHOR: Caleb Hoffman
# CLASS: Optics and Photonics
# ASSIGNMENT: Computer Problem 1
# REMARKS: The program computes and displays three incident rays on a thin lens


import matplotlib.pyplot as plt
import math




# Main function
def main():

    # Variables
    d = 2
    input_angle = float(input("Enter incident angle: "))*(math.pi/180)
    xDomain = [0.1*x for x in range(-8, 1)]
    m = math.tan(input_angle)

    # Axis labels
    plt.title("Thin Lens-Object at Infinity")
    plt.xlabel("Optical Axis (cm)")
    plt.ylabel("Ray Elevation (cm)")

    # Imposes grid
    plt.grid()

    # Draws lens
    plt.vlines(0, (-d/2), (d/2))

    # This loop draws each ray at equal distance apart striking the lens
    for i in range(3):
        
        zRange = [m*x+((1-i)*(d/2)) for x in xDomain]
        plt.plot(xDomain, zRange, color = "red")
        
    # Displays the graph with computed ray    
    plt.show()


    
    
    
    
    
# Invokes main  
main()
