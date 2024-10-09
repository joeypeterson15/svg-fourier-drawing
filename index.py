from svgelements import SVG, Path, Move, Line, CubicBezier, Curve
# bezier quadratic curve equation: 
#   x = ((1 - t)^2)(x1) + 2(t - 1)t(x2) + (t^2)(x3)
#   y = ((1 - t)^2)(y1) + 2(t - 1)t(y2) + (t^2)(y3)
# bezier cubic curve equation:
#   x = (1 - t)^3(x1) + 3(1 - t)^2(tx2) + 3(1 - t)t^2(tx2) + t^3(x3)
#   y = (1 - t)^3(y1) + 3(1 - t)^2(ty2) + 3(1 - t)t^2(ty2) + t^3(y3)

# center of mass = average(x,y) -> shift each coordinate by average(x,y)

# In order to redraw svg image:
    # 1. write script to read svg file and return data as x,y coordinates as well as extract bezier curve equations and line equations
    # 2. translate coordinatesta so that center of mass hovers around the origin.
    # 4. iterate through the number of samples/iterations (1000 for example).
    # 5. find the fourier coefficients for each sample/iteration(1000 for example). 
    #    this means all the coefficients calculated from the fourier series will be from 0 < 2pi / 1000

def getBezierCurve(x, y, c = None):
    return 0

svg = SVG.parse('shape.svg')

# Iterate through all elements in the SVG
for element in svg.elements():
    # Check if the element is a Path and has a 'd' attribute
    if isinstance(element, Path):
        for i, e in enumerate(element.segments()):
            segment = element.segments()[i]
            if isinstance(segment, Move):
                print(f'Segment {e}')
            elif isinstance(segment, Line):
                print(f'Segment {e}')
            elif isinstance(segment, CubicBezier):
                print(f'Segment {e}: "C" - Cubic to {segment.end}')
            print('type', type(e))
        # for i in range(len(element.segments())):
        #     for i in range(len(path)):
        #         print(path[i])
            # print(f'Segment: {segment}')
