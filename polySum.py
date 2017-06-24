'''
Week-2:Exercise-grader-polysum
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: (0.25∗n∗s^2)/tan(π/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
'''
#code
import math
def polysum(n,s):
    '''
    Input: n - number of sides(should be an integer)
    s- length of each sides(can be an intger or a float)
    
    Output: Returns Sum of area and the square of the perimeter of the regular polygon(gives a float)
    '''
    #Code
    def areaOfPolygon(n,s):
        #Pi = 3.1428
        area = (0.25 * n * s ** 2)/math.tan(math.pi/n)
        return area
    def perimeterOfPolygon(n,s):
        perimeter = n * s
        return perimeter
    sum = areaOfPolygon(n,s) + (perimeterOfPolygon(n,s) ** 2)
    return round(sum,4)
