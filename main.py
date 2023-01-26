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


def factorial(num):
    """

    :param num: int: will be used in calculating factorial
    :return: int: factorial of num
    """
    if type(num) not in [int, float]:
        raise TypeError(f'Invalid input: {num}')
    if num < 0:
        raise ValueError(f'Invalid input {num}')
    if num == 0:
        return 1
    else:
        result = 1
        while num != 1:
            result *= num
            num -= 1
        return result


def simple_calculator():
    """

    :return: int: calculated result
    """
    problem = input(f'Enter your problem [number | - | + | / | * | number]: ')
    problem = problem.split()
    operator = problem[1]
    try:
        num1, num2 = int(problem[0]), int(problem[2])
    except ValueError:
        return f'Invalid input'
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return f'You cannot divide by 0'


def check_palindrome(s):
    """

    :param s: str: string which will be checked
    :return: bool: true - if str is palindrome
    """
    if s == s[::-1]:
        return True
    return False


def count_vowels(s):
    """

    :param s: str: string in which function will count vowels
    :return: int: number of vowels
    """
    vowels = 'e y u i o a'.split()
    counter = 0
    for char in s:
        if char in vowels:
            counter += 1
    return counter


def dice_roll(num_dices, num_sides):
    """

    :param num_dices: int: number of dices
    :param num_sides: int: number of sides
    :return: list: result of the roll
    """
    if num_dices < 0 or num_sides < 0:
        raise ValueError('Invalid input')
    result = [randint(1, num_sides) for _ in range(num_dices)]
    return result


def tic_tac_toe():
    board = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
        print(board[i])

    insert_x_o(board)


def insert_x_o(board):
    turn = 1
    while turn <= 9:
        if turn % 2 != 0:
            cords = input('Enter coordinates where do you want to type X: ').split()
            x, y = list(map(int, cords))
            if board[x][y] is None:
                board[x][y] = 'X'
            else:
                print('you lose your turn!')
        if turn % 2 == 0:
            cords = input('Enter coordinates where do you want to type O: ').split()
            x, y = list(map(int, cords))
            if board[x][y] is None:
                board[x][y] = 'O'
            else:
                print('you lose your turn')

        for i in range(3):
            print(board[i])

        is_win = check_if_win(board)
        if True in is_win:
            print(f'player {is_win[0]} has won!')
            break
        turn += 1


def check_if_win(board):
    for row in board:
        if row.count('X') == 3:
            return 'X', True
        elif row.count('O') == 3:
            return 'O', True

    for row in range(3):
        result = [board[row][i] for i in range(3)]
        if result.count('X') == 3:
            return 'X', True
        elif result.count('O') == 3:
            return 'O', True

    result = [board[i][i] for i in range(3)]
    if result.count('X') == 3:
        return 'X', True
    elif result.count('O') == 3:
        return 'O', True

    if board[0][2] == board[1][1] == board[2][0] == 'X':
        return 'X', True
    elif board[0][2] == board[1][1] == board[2][0] == 'O':
        return 'O', True
    return 'draw', False


def sphere_volume(radius):
    """

    :param radius: int/float: sphere radius
    :return: int/float: sphere volume
    """
    if radius < 0:
        raise ValueError(f'Invalid radius: {radius}')
    return (4 / 3) * pi * radius ** 3


def smallest_biggest_dif(collection):
    """

    :param collection: list/tuple: collection of numbers
    :return: int/float: difference between biggest and smallest number in collection
    """
    smallest = min(collection)
    biggest = max(collection)
    return biggest - smallest


def bmi_calculator(weight, height):
    """

    :param weight: int/float: weight in kilograms
    :param height: int?float: height in meters or centimeters
    :return:
    """
    if height > 10:
        height /= 100

    bmi = weight / height**2
    if 18.5 <= bmi <= 22.9:
        return f'(Your bmi is perfect: {bmi}'
    return bmi


def cost_of_floor(cost_per_m2, length, width):
    """

    :param cost_per_m2: int/float: cost per square meter of floor
    :param length: int/float: length of the floor
    :param width: int/float: width of the floor
    :return:
    """
    area = length * width
    return area / cost_per_m2


def how_many_spins(r, road):
    """

    :param r: int/float: radius of wheel in meters
    :param road: int/float: length of the road in kilometers
    :return: int/float: how many times the wheel will spin
    """
    wheel_circuit = 2 * pi * r
    road_meters = road * 1000
    return road_meters / wheel_circuit


def get_water_pressure(height):
    """

    :param height: int/float: height of water column between object and surface
    :return: int/float: pressure in Pascals
    """
    density = 997
    return density * height * 9.81


def how_long_for_the_light(planet):
    """
    function calculates time that sunlight need to get to different planets in Solar System

    :param planet:
    :return:
    """
    distances_from_sun = {
        'mercury': 57_909_170,
        'venus': 108_208_926,
        'earth': 149_597_887,
        'mars': 227_936_637,
        'jupiter': 778_412_027,
        'saturn': 1_426_725_413,
        'uranus': 2_870_972_220,
        'neptune': 4_498_252_900,
    }

    lightspeed_kms = 299_792.458
    distance = distances_from_sun[planet.lower()]
    time_seconds = distance // lightspeed_kms

    time_minutes = time_seconds // 60
    time_seconds = time_seconds % 60
    if time_minutes > 60:
        time_hours = time_minutes // 60
        time_minutes = time_minutes % 60
        return f'It takes {int(time_hours)}h, ' \
               f'{int(time_minutes)}min ' \
               f'and {int(time_seconds)}s for the light to get to {planet.title()}.'
    else:
        return f'It takes {int(time_minutes)}min and {int(time_seconds)}s for the light to get to {planet.title()}'


def pythagorean_theorem(a, b):
    """

    :param a: int/float: first side next to the right angle in right triangle
    :param b: int/float: second side next to the right angle in right triangle
    :return: int/float: side opposite to the right triangle
    """
    c = (a**2 + b**2)**0.5
    return c
