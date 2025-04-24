"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.


# Mathematical functions:
# - mul
def mul(a: float, b: float) -> float:
    """Multiplies two numbers"""
    return a * b


# - id
def id(a: float) -> float:
    """Returns the input unchanged"""
    return a


# - add
def add(a: float, b: float) -> float:
    """Adds two numbers"""
    return a + b


# - neg
def neg(a: float) -> float:
    """Negates a number"""
    return -a


# - lt
def lt(a: float, b: float) -> bool:
    """Checks if one number is less than another"""
    return a < b


# - eq
def eq(a: float, b: float) -> bool:
    """Checks if two numbers are equal"""
    return a == b


# - max
def max(a: float, b: float) -> float:
    """Returns the larger of two numbers"""
    return a if a > b else b


# - is_close
def is_close(a: float, b: float) -> bool:
    """Checks if two numbers are close in value"""
    return abs(a - b) < 1e-2


# - sigmoid
def sigmoid(x: float) -> float:
    r"""$f(x) =  \frac{1.0}{(1.0 + e^{-x})}$

    (See https://en.wikipedia.org/wiki/Sigmoid_function )

    Calculate as

    $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$

    for stability.
    """
    return 1 / (1 + math.exp(-x)) if x >= 0 else math.exp(x) / (1 + math.exp(x))


# - relu
def relu(x: float) -> float:
    """$f(x) =$ x if x is greater than 0, else 0

    (See https://en.wikipedia.org/wiki/Rectifier_(neural_networks) .)
    """
    return x if x > 0 else 0


# - log
def log(x: float) -> float:
    """$f(x) = log(x)$"""
    return math.log(x)


# - exp
def exp(x: float) -> float:
    """$f(x) = e^{x}$"""
    return math.exp(x)


# - log_back
def log_back(a: float, b: float) -> float:
    r"""If $f = log$ as above, compute $d \times f'(x)$"""
    return b / a


# - inv
def inv(x: float) -> float:
    """$f(x) = 1/x$"""
    return 1 / x


# - inv_back
def inv_back(a: float, b: float) -> float:
    r"""If $f(x) = 1/x$ compute $d \times f'(x)$"""
    return -b / (a * a)


# - relu_back
def relu_back(a: float, b: float) -> float:
    r"""If $f = relu$ compute $d \times f'(x)$"""
    return (1 if a > 0 else 0) * b


#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# ## Task 0.3

# Small practice library of elementary higher-order functions.


# Implement the following core functions
# - map
def map(f: Callable[[float], float]) -> Callable[[Iterable[float]], Iterable[float]]:
    """Higher-order map.

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
    ----
        f: Function from one value to one value.

    Returns:
    -------
        A function that takes a list, applies `fn` to each element, and returns a
         new list

    """
    return lambda l: [f(element) for element in l]


# - zipWith
def zipWith(
    f: Callable[[float, float], float],
) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    """Higher-order zipwith (or map2).

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
    ----
        f: combine two values

    Returns:
    -------
        Function that takes two equally sized lists `ls1` and `ls2`, produce a new list by
         applying fn(x, y) on each pair of elements.

    """
    return lambda l1, l2: [f(e1, e2) for e1, e2 in zip(l1, l2)]


# - reduce
def reduce(
    f: Callable[[float, float], float], start: float
) -> Callable[[Iterable[float]], float]:
    r"""Higher-order reduce.

    Args:
    ----
        f: combine two values
        start: start value $x_0$

    Returns:
    -------
        Function that takes a list `ls` of elements
         $x_1 \ldots x_n$ and computes the reduction :math:`fn(x_3, fn(x_2,
         fn(x_1, x_0)))`

    """

    def reduce_inside(l: Iterable[float]) -> float:
        ret = start
        for element in l:
            ret = f(ret, element)
        return ret

    return reduce_inside


#
# Use these to implement
# - negList : negate a list
def negList(l: Iterable[float]) -> Iterable[float]:
    """Use `map` and `neg` to negate each element in `ls`"""
    return map(lambda x: -x)(l)


# - addLists : add two lists together
def addLists(l1: Iterable[float], l2: Iterable[float]) -> Iterable[float]:
    """Add the elements of `ls1` and `ls2` using `zipWith` and `add`"""
    return zipWith(lambda x, y: x + y)(l1, l2)


# - sum: sum lists
def sum(l: Iterable[float]) -> float:
    """Sum up a list using `reduce` and `add`."""
    return reduce(lambda x, y: x + y, 0)(l)


# - prod: take the product of lists
def prod(l: Iterable[float]) -> float:
    """Product of a list using `reduce` and `mul`."""
    return reduce(lambda x, y: x * y, 1)(l)
