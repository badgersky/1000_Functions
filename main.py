from math import pi
from random import randint


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


def my_sorted(col, reverse=False):
    """
    :param col: list: list of integers, floats
    :param reverse: bool: true-collection will be sorted with descending order, false-opposite
    :return: list: incrementing sorted input list
    """
    new_col = []
    while col:
        new_col.append(col[col.index(min(col))])
        col.pop(col.index(min(col)))
    if reverse:
        return new_col[::-1]
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
        new_word = first.upper() + word.lower()
        new_words.append(new_word)
    return ' '.join(new_words)


def my_count(s, pattern):
    """
    :param s: string/list: characters/list in which we are counting pattern
    :param pattern: string/int/float: character we want to get number of in string
    :return: int: number of patterns in string/list
    """
    result = 0
    for char in s:
        if char == pattern:
            result += 1
    return result


def my_min(col):
    """
    :param col: list: list of integers/floats
    :return: integer/float: the lowest number in collection
    """
    if col:
        lowest = col[0]
    else:
        raise ValueError(f'argument is an empty collection: {col}')
    for num in col:
        if num < lowest:
            lowest = num
        else:
            continue
    return lowest


def quadratic_equation(a, b, c):
    """
    :param a: int/float: parameter a in equation: ax^2+bx+c = 0
    :param b: int/float: parameter b in equation: ax^2+bx+c = 0
    :param c: int/float: parameter c in equation: ax^2+bx+c = 0
    :return: int/float/tuple: values/value of x in ax^2+bx+c = 0
    """
    delta = get_delta(a, b, c)
    if delta < 0:
        return f'No solution for the equation'
    elif delta == 0:
        return (-b + delta**0.5) / (2 * a)
    else:
        return (-b + delta**0.5) / (2 * a), (-b - delta**0.5) / (2 * a)


def get_delta(a, b, c):
    """
    :param a: int/float: parameter a in equation: ax^2+bx+c = 0
    :param b: int/float: parameter b in equation: ax^2+bx+c = 0
    :param c: int/float: parameter c in equation: ax^2+bx+c = 0
    :return: int/float: value of delta for equation: ax^2+bx+c = 0
    """
    try:
        return b**2 - 4 * a * c
    except TypeError:
        return f'Invalid parameters: {a, b, c}'


def rock_paper_scissors():
    while True:
        choice_value = get_choice()
        if not choice_value:
            break
        else:
            pc_choice = randint(1, 3)
            check_win(pc_choice, choice_value)


def get_choice():
    choice_values = {'r': 1, 'rock': 1, 'p': 2, 'paper': 2, 's': 3, 'scissors': 3}
    valid_choices = ['r', 's', 'p', 'paper', 'rock', 'scissors']
    p_choice = input('Enter your choice: [r/p/s/rock/paper/scissors], type "q" to stop: ')
    if p_choice.lower() == 'q':
        return False
    elif p_choice.lower() in valid_choices:
        return choice_values[p_choice.lower()]
    else:
        raise ValueError(f'Invalid choice: {p_choice}')


def check_win(pc_choice, p_choice):
    if pc_choice == 1 and p_choice == 2:
        print('You win')
    elif pc_choice == 2 and p_choice == 3:
        print('You win')
    elif pc_choice == 3 and p_choice == 1:
        print('You win')
    else:
        print('Pc wins')


def get_percent_of_value(number, percent):
    """

    :param number: int/float: number from which percentage will be calculated
    :param percent: int/float: percent value
    :return: int/float: percent of number - parameter
    """
    return number * (percent / 100)


def my_sum(numbers):
    """

    :param numbers: list/tuple: collection of int/float
    :return: int/float: sum of numbers in collection
    """
    result = 0
    for num in numbers:
        result += num
    return result
