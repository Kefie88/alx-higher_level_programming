#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Represnt Pascal's Traingle of size n.

    Return:
        A list of lists of integers represnting
        the triangle
    """
    if n <= 0:
        return []

    traingles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
