from math import pi


def rectangle_area(a, b):
    """

    :param a: int/float: length of one side
    :param b: int/float: length of other side
    :return: float/int: area of rectangle
    """
    return a * b


def circle_area_from_radius(r):
    """

    :param r: float/int: circle radius
    :return: float: circle area
    """
    return pi * r ** 2


def trapezoid_ares(a, b, h):
    """

    :param a: float/int: length of the first base
    :param b: float/int: length of the second base
    :param h: float/int: height of the trapezoid
    :return: float/int: area of the trapezoid
    """
    return ((a + b) * h) / 2


def line_length(x1, y1, x2, y2):
    """

    :param x1: float/int: startpoint x coordinate
    :param y1: float/int: startpoint y coordinate
    :param x2: float/int: endpoint x coordinate
    :param y2: float/int: endpoint y coordinate
    :return: float/int: length of the section
    """
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def check_parentheses(s):
    """

    :param s: string: parentheses
    :return: bool: True if parentheses are in good order
    """
    parentheses = ['()', '{}', '[]']
    while '()' in s or '{}' in s or '[]' in s:
        for par in parentheses:
            s = s.replace(par, '')
    if len(s) == 0:
        return True
    else:
        return False


def my_sorted(col):
    """

    :param col: list: list of integers, floats
    :return: list: incrementing sorted input list
    """
    new_col = []
    while col:
        new_col.append(col[col.index(min(col))])
        col.pop(col.index(min(col)))
    return new_col


def my_title(s):
    """

    :param s: string: alphabetic characters (multiple words possible
    :return: string: first letter-uppercase, the rest-lowercase (of every word)
    """
    words = s.split()
    new_words = []
    for word in words:
        first = word[0]
        word = word.replace(first, '')
        new_word = first.upper() + word
        new_words.append(new_word)
    return ' '.join(new_words)
