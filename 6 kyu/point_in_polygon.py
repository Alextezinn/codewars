"""

The problem
In this kata, you're going write a function called point_in_polygon to test if a point is inside a polygon.

Points will be represented as tuples (x,y).

The polygon will be an array of points which are the polygon's vertices. The last point in the array
connects back to the first point.

You can assume:

The polygon will be a valid simple polygon. That is, it will have at least three points, none of
its edges will cross each other, and exactly two edges will meet at each vertex.

In the tests, the point will never fall exactly on an edge of the polygon.

"""
from typing import List, Tuple
# Input parameters for visualize_polygon are the same, as for point_in_polygon
from preloaded import visualize_polygon


def point_in_polygon(polygon: List[Tuple[float, float]], point: Tuple[float, float]) -> bool:
    result = False

    for i, _ in enumerate(polygon):
        if (((polygon[i][1] <= point[1] and polygon[i - 1][1] > point[1]) or
             (polygon[i - 1][1] <= point[1] and polygon[i][1] > point[1])) and
                ((polygon[i - 1][0] - polygon[i][0]) * (point[1] - polygon[i][1]) /
                 (polygon[i - 1][1] - polygon[i][1]) + polygon[i][0]) < point[0]):
            result = not result

    return result