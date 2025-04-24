import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N: int) -> list[Tuple[float, float]]:
    r"""Make N amount of random points on a 2D plane.

    Args:
    ----
        N: Number of points

    Returns:
    -------
        A list or array containing N amount of points (2D points)

    """
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N: int) -> Graph:
    r"""Make a graph containing N amount of points (2D points, x and y).
    The points are the nodes of the graph.
    The data has 2 classes or labels.

    A point will have the class 1 if its x-coordinate is less than 0, otherwise the class will be 0.

    In the form of mathematical formula:
    class(x, y) = 1 if x < 0.5
    class(x, y) = 0 if x >= 0.5

    Args:
    ----
        N: Number of points

    Returns:
    -------
        A graph containing N amount of points or nodes (2D points) with 2 classes or labels

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N: int) -> Graph:
    r"""Make a graph containing N amount of points (2D points, x and y).
    The points are the nodes of the graph.
    The data has 2 classes or labels.

    A point will have the class 1 if its x-coordinate + y-coordinate is less than 0.5, otherwise the class will be 0.

    In the form of mathematical formula:
    class(x, y) = 1 if x + y < 0.5
    class(x, y) = 0 if x + y >= 0.5

    Args:
    ----
        N: Number of points

    Returns:
    -------
        A graph containing N amount of points or nodes (2D points) with 2 classes or labels

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N: int) -> Graph:
    r"""Make a graph containing N amount of points (2D points, x and y).
    The points are the nodes of the graph.
    The data has 2 classes or labels.

    A point will have the class 1 if its x-coordinate is less than 0.2 or greater than 0.8, otherwise the class will be 0.

    In the form of mathematical formula:
    class(x, y) = 1 if x < 0.2 or x > 0.8
    class(x, y) = 0 if 0.2 <= x <= 0.8

    Args:
    ----
        N: Number of points

    Returns:
    -------
        A graph containing N amount of points or nodes (2D points) with 2 classes or labels

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N: int) -> Graph:
    r"""Make a graph containing N amount of points (2D points, x and y).
    The points are the nodes of the graph.
    The data has 2 classes or labels.

    A point will have the class 1 if its
        - x-coordinate is less than 0.5 and y-coordinate is greater than 0.5
        OR
        - x-coordinate is greater than 0.5 and y-coordinate is less than 0.5
    , otherwise the class will be 0.

    In the form of mathematical formula:
    class(x, y) = 1 if (x < 0.5 and y > 0.5) or (x > 0.5 and y < 0.5)
    class(x, y) = 0 if (x >= 0.5 and y >= 0.5) or (x <= 0.5 and y <= 0.5)

    Args:
    ----
        N: Number of points

    Returns:
    -------
        A graph containing N amount of points or nodes (2D points) with 2 classes or labels

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 and x_2 > 0.5 or x_1 > 0.5 and x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N: int) -> Graph:
    r"""Make a graph containing N amount of points (2D points, x and y).
    The points are the nodes of the graph.
    The data has 2 classes or labels.
    The 2 classes are separated by a circle of radius sqrt(0.1) with the center of the circle in coordinate (0.5, 0.5).

    A point will have the class 1 if it is outside the circle, otherwise the class will be 0.

    In the form of mathematical formula:
    class(x, y) = 1 if (x < 0.5 and y > 0.5) or (x > 0.5 and y < 0.5)
    class(x, y) = 0 if (x >= 0.5 and y >= 0.5) or (x <= 0.5 and y <= 0.5)

    Args:
    ----
        N: Number of points

    Returns:
    -------
        A graph containing N amount of points or nodes (2D points) with 2 classes or labels

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = x_1 - 0.5, x_2 - 0.5
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N: int) -> Graph:
    r"""Make a graph containing N amount of points (2D points, x and y).
    The points are the nodes of the graph.
    The data has 2 classes or labels.
    The points are in the shape of 2 spirals (one spiral for each class).

    Args:
    ----
        N: Number of points

    Returns:
    -------
        A graph containing N amount of points or nodes (2D points) with 2 classes or labels

    """

    def x(t: float) -> float:
        return t * math.cos(t) / 20.0

    def y(t: float) -> float:
        return t * math.sin(t) / 20.0

    X = [
        (x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    X = X + [
        (y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {
    "Simple": simple,
    "Diag": diag,
    "Split": split,
    "Xor": xor,
    "Circle": circle,
    "Spiral": spiral,
}
