def triangle_zhonxin(a: tuple, b: tuple, c: tuple) -> tuple:
    """
    Calculate the centroid (Zhongxin) of a triangle.

    Parameters:
    - a (tuple): Coordinates of point A.
    - b (tuple): Coordinates of point B.
    - c (tuple): Coordinates of point C.

    Returns:
    tuple: Coordinates of the centroid (Zhongxin) G.
    """
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    x = round((x1 + x2 + x3) / 3)
    y = round((y1 + y2 + y3) / 3)

    return x, y