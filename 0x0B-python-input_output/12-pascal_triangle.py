#!/usr/bin/python3
"""Define Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal Triangle size n.
    Return list of lists of integers representing triangle.
    """
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for a in range(len(tri) - 1):
            tmp.append(tri[a] + tri[a + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
