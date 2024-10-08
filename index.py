
# bezier curve equation: 
#   x = ((1 - t)^2)(x1) + 2(t - 1)t(x2) + (t^2)(x3)
#   y = ((1 - t)^2)(y1) + 2(t - 1)t(y2) + (t^2)(y3)

# center of mass = average(x,y) -> shift each coordinate by average(x,y)

# In order to redraw svg image:
    # 1. write script to read svg file and return data as x,y coordinates as well as extract bezier curve equations and line equations
    # 2. translate coordinatesta so that center of mass hovers around the origin.
    # 4. iterate through the number of samples/iterations (1000 for example).
    # 5. find the fourier coefficients for each sample/iteration(1000 for example). 
    #    this means all the coefficients calculated from the fourier series will be from 0 < 2pi / 1000
