from svgelements import SVG, Path, Move, Line, CubicBezier, Curve
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

def getBezierCurve(x, y, c = None):
    return 0

svg = SVG.parse('shape.svg')

# Iterate through all elements in the SVG
for element in svg.elements():
    # Check if the element is a Path and has a 'd' attribute
    if isinstance(element, Path):
        for e, i in enumerate(element.segments()):
            segment = element.segments()[e]
            if isinstance(segment, Move):
                print(f'Segment {i}: "M" - Move to {segment.end}')
            elif isinstance(segment, Line):
                print(f'Segment {i}: "L" - Line to {segment.end}')
            elif isinstance(segment, CubicBezier):
                print(f'Segment {i}: "C" - Cubic to {segment.end}')
        # for i in range(len(element.segments())):
        #     for i in range(len(path)):
        #         print(path[i])
            # print(f'Segment: {segment}')
