__author__ = 'WaterPython'

import math

# area of a circle
def GEO_geometry_acircle(d):
    pi = 4*math.atan(1.0)
    acircle= pi*d**2/4.0
    return (acircle);

#hydraulic radius of a circle
def GEO_geometry_hrcircle(d):
    hrcircle= d/4
    return (hrcircle);

#hydraulic radius of a circle
def GEO_geometry_wpcircle(d):
    pi = 4*math.atan(1.0)
    wrcircle= pi * d
    return (wrcircle);

# Area of a prism (rectangle, triangle and trapeze) in free surface flow
def GEO_geometry_aprism(y, b, ml, mr):
    aprism = y *(b + ml*y*0.5 + mr*y*0.5)
    return (aprism);

# Wet perimeter of a prism channel (rectangle, triangle and trapeze)
def GEO_geometry_wpprism(y, b, ml, mr):
    wpprism = b + y*((1 + ml**2)**0.5 + (1 + mr**2)**0.5)
    return (wpprism);

#hydraulic radius of a prism channel (rectangle, triangle and trapeze)
def GEO_geometry_hrprism(y, b, ml, mr):
    aprism = GEO_geometry_aprism(y, b, ml, mr)
    wpprism = GEO_geometry_wpprism(y, b, ml, mr)
    hrprism = aprism/wpprism
    return (hrprism);

#surface lenght of a prism channel (rectangle, triangle and trapeze)
def GEO_geometry_wlprism(y, b, ml, mr):
    wlprism = b + ml*y + mr*y
    return (wlprism);

