from math import sqrt
from typing import Tuple

def quadratic(a: float, b: float, c: float) -> Tuple[float, float]:
    '''Compute roots of the quadratic equation:

            a*x**2 + b*x + c = 0

        For example:

            >>> x1, x2 = quadratic(a=4, b=11, c=7)
            >>> x1
            -1.0
            >>> x2
            -1.75
            >>> 4*x1**2 + 11*x1 + 7
            0.0
            >>> 4*x2**2 + 11*x2 + 7
            0.0
    '''
    discriminant = sqrt(b**2.0 - 4.0*a*c)
    x1 = (-b + discriminant) / (2.0 * a)
    x2 = (-b - discriminant) / (2.0 * a)
    return x1, x2
