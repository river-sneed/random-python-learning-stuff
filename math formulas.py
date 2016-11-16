# This program contains functions that evaluate formulas used in geometry.
#
# River Sneed
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a
def circle_area(r):
    a = math.pi * r**2
    return a
def parallelogram_area(b, h):
    a = b * h
    return a
def trapezoid_area (a, b, h):
    a = ((1/2) * (a + b)) * h
    return a
def rectangularprism_volume (h, l, w):
    v = h * l * W
    return v
def cone_volume (r, h):
    v = math.pi * r**2 * (h/3)
    return v
def sphere_volume (r):
    v = (4/3) * math.pi * r**3
    return v
def rectangularprism_surfacearea (h, l, w):
    s = 2 * ((w * l) * (h * l) * (h * w))
    return s
def sphere_surfacearea (r):
    s = 4 * math.pi * r**2
    return s
def hypotenuse (a , b):
    c = math.sqrt((a**2)+(b**2))
    return c

def heron_formula (a, b, c):
    p = (.5) * (a + b + c)
    f = (.5) ** ((p) * (p - a) * (p - b) * (p - c))
    return f
    
