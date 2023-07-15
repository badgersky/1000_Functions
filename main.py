import random
from math import pi, atan
from random import randint
from string import ascii_lowercase


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

    :param height: int/float: height of water column between object and surface in meters
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


def triangle_are(a, h):
    """

    :param a: int/float: length of the base
    :param h: int/float: length of the height
    :return: int/float: triangle are
    """
    return (a * h) / h


def my_max(col):
    """

    :param col: list/tuple: collection of numbers
    :return: int/float: the biggest number in collection
    """
    if col:
        biggest = col[0]
    else:
        raise ValueError('Argument is an empty collection')
    for num in col:
        if num > biggest:
            biggest = num
        else:
            continue
    return biggest


def fahrenheit_to_celsius(temp_f):
    """

    :param temp_f: int/float: temperature in fahrenheit
    :return: int/float: temperature in celsius
    """
    return (temp_f - 32) * 0.5556


def guess_number():
    print('Try to guess number between 0 and 50 in 5 tries.')
    secret_num = randint(0, 50)
    counter = 0
    while counter < 5:
        guess = int(input('Enter your guess: '))
        if guess == secret_num:
            print('You win!')
            break
        else:
            counter += 1
    print('You lose')


def rad_to_deg(rad):
    """

    :param rad: int/float: value of angle in radians
    :return: int/float: value of angle in degree
    """
    return rad * (180 / pi)


def calculate_azimuth(x1, y1, x2, y2):
    """

    :param x1: int/float: x coordinate of first point
    :param y1: int/float: y coordinate of first point
    :param x2: int/float: x coordinate of second point
    :param y2: int/float: y coordinate of second point
    :return: int/float: section azimuth
    """
    dx = x2 - x1
    dy = y2 - y1
    q_angle_rad = atan(dy / dx)
    q_angle_deg = rad_to_deg(q_angle_rad)
    if dx > 0 and dy > 0:
        return q_angle_deg
    elif dx > 0 > dy:
        return 180 - q_angle_deg
    elif dx < 0 and dy < 0:
        return 180 + q_angle_deg
    else:
        return 360 - q_angle_deg


def generate_dividers(number):
    """

    :param number: int: number that you want to find dividers of
    :return: list: list of dividers
    """
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


def my_range(start=0, stop=None, step=1):
    """

    :param start: int: number you want to start generating from default=0
    :param stop: int: range of generator
    :param step: int: step by which numbers will be incremented
    :return: generator object
    """
    if stop is None:
        stop=start
        start=0

    if not isinstance(start, int) or not isinstance(stop, int) or not isinstance(step, int):
        raise ValueError(f'my_range function accepts only integers')

    while start < stop:
        yield start
        start += step


def shuffle_cards():
    """

    :return: list: shuffled deck of cards
    """
    suits = ('clubs', 'diamonds', 'hearts', 'spades')
    face_cards = ('king', 'queen', 'jack', 'ace')

    deck = []
    for suit in suits:
        for i in range(2, 11):
            deck.append((i, suit))

        for face_card in face_cards:
            deck.append((face_card, suit))

    random.shuffle(deck)
    return deck


def factorial2(num):
    """

    :param num: int: will be used in calculating factorial
    :return: int: factorial of num
    """
    if not isinstance(num, int):
        raise TypeError(f'Invalid input: {num}')
    if num < 0:
        raise ValueError(f'Invalid input {num}')

    if num <= 1:
        return 1
    else:
        return num * factorial2(num - 1)
    

def power_number(num, power=2):
    """
    
    :param num: int: number you want to calculate power of
    :param power: int: exponent
    :return: int: factorial of num
    """
    if power == 0:
        return 1
    elif power == 1:
        return num
    else:
        return num * power_number(num, power - 1)
    

def tower_of_hanoi(num=64):
    """
    
    :param num: int: number of discs in hanoi tower puzzle
    :return: int, 3xlist: int - number of steps until hanoi tower solved, each list represent single rod in puzzle
    """

    # setting variables
    A = list(range(num, 0, -1))
    B = []
    C = []
    counter = 0

    if num % 2 == 0:
        while True:
            counter, B, A = move_AB(counter, B, A)
            if check_solved(num, C):
                return counter, C, B, A
            counter, C, A = move_AC(counter, C, A)
            if check_solved(num, C):
                return counter, C, B, A
            counter, C, B = move_BC(counter, C, B)
            if check_solved(num, C):
                return counter, C, B, A
    else:
        while True: 
            counter, C, A = move_AC(counter, C, A)
            if check_solved(num, C):
                return counter, C, B, A
            counter, B, A = move_AB(counter, B, A)
            if check_solved(num, C):
                return counter, C, B, A
            counter, C, B = move_BC(counter, C, B)
            if check_solved(num, C):
                return counter, C, B, A


def move_AB(counter, B, A):
    # legal move between A and B
    if A and not B:
        disc = A.pop()
        B.append(disc)
    elif not A and B:
        disc = B.pop()
        A.append(disc)
    elif A[-1] > B[-1]:
        disc = B.pop()
        A.append(disc)
    elif B[-1] > A[-1]:
        disc = A.pop()            
        B.append(disc)
    counter += 1

    return counter, B, A


def move_AC(counter, C, A):
    # legal move between A and C
    if A and not C:
        disc = A.pop()
        C.append(disc)
    elif not A and C:
        disc = C.pop()
        A.append(disc)
    elif A[-1] > C[-1]:
        disc = C.pop()
        A.append(disc)
    elif C[-1] > A[-1]:
        disc = A.pop()
        C.append(disc)
    counter += 1

    return counter, C, A


def move_BC(counter, C, B):
    # legal move between B and C
    if B and not C:
        disc = B.pop()
        C.append(disc)
    elif C and not B:
        disc = C.pop()
        B.append(disc)
    elif C[-1] > B[-1]:
        disc = B.pop()
        C.append(disc)  
    elif B[-1] > C[-1]:
        disc = C.pop()
        B.append(disc)
    counter += 1

    return counter, C, B


def check_solved(num, C):
    if C == list(range(num, 0, -1)):
        return True
    return False


def get_coins_for_change():
    """

    Function calculates which coins sum up to randomly generated change
    """
    available_coins = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    change = round(random.random(), 2)
    coins = []

    while round(sum(coins), 2) != change:
        biggest_coin = max(available_coins)
        if round(sum(coins) + biggest_coin, 2) > change:
            available_coins.remove(biggest_coin)
        else:
            coins.append(biggest_coin)
    
    return f'Coin for change {change}: ' + ', '.join(str(num) for num in coins)


def sphere_volume(r):
    """
    
    :param r: radius of sphere
    :return: volume of sphere with radius r
    """
    return (4 / 3) * pi * r**3
    

def clear_text(text):
    """
    Function clears text of non alphabetic characters leaves spaces

    :param text: str: text to clear
    :return: str: cleared text
    """

    new_text = ''
    for char in text:
        if char.isalpha() or char == ' ':
            new_text += char

    return new_text


def count_word_occurences1(word, text):
    """
    Function counts how many occurences of word are in the text

    :param word: str: word which will be counted
    :param text: str: text to count the word in
    :return: int: number of occurences of the word in the text
    """

    text = clear_text(text)
    text = text.lower()
    text_arr = text.split()
    word = word.lower()
    return text_arr.count(word)


def count_word_occurences2(word, text):
    """
    Function counts how many occurences of word are in the text

    :param word: str: word which will be counted
    :param text: str: text to count the word in
    :return: int: number of occurences of the word in the text
    """

    text = clear_text(text)
    text = text.lower()
    word = word.lower()
    counter = 0

    for s in text.split():
        if word == s:
            counter += 1
    return counter
  

def count_words(text):
    """
    Function counts number of words in text
    
    :param text: str: text to count words of
    :return: int: number of words in text
    """

    text = clear_text(text)
    return len(text.split())


def encoding_rules():
    rules = {char: ascii_lowercase[-i] for i, char in enumerate(ascii_lowercase, start=1)}
    return rules


def encode_message(message):
    """
    Function encodes message according to encoding rules

    :param message: str: message to encode
    :return: str: encoded message
    """
    rules = encoding_rules()

    message = message.lower()

    encoded_message = ''
    for char in message:
        encoded_message += rules.get(char, char)

    return encoded_message


def decoding_rules():
    rules = {char: ascii_lowercase[i] for i, char in enumerate(ascii_lowercase[::-1])}
    return rules


def decode_message(message):
    """
    Function dencodes message according to dencoding rules

    :param message: str: message to dencode
    :return: str: dencoded message
    """   
    rules = decoding_rules()

    message = message.lower()

    decoded_message = ''
    for char in message:
        decoded_message += rules.get(char, char)

    return decoded_message


def count_prymitive_elements(arr):
    """
    Function returns number of primitive elements

    :param arr: list: list to count primitive elements 
    :return: int: number of primitive elements
    """

    counter = 0
    for element in arr:
        if not isinstance(element, list):
            counter += 1
        else:
            counter += count_prymitive_elements(element)

    return counter


def get_median(arr):
    """
    Function returns median value of array
    
    :param arr: list: list of numbers 
    :return: int/float: median value
    """

    arr.sort()
    if not len(arr) % 2:
        center_values = arr[len(arr) // 2 - 1: len(arr) // 2 + 1]
        return sum(center_values) / 2
    else:
        return arr[len(arr) // 2]


def arithmetic_average(arr):
    """
    Function calculates arithmetic average
    
    :param arr: list: list of numbers
    :return: int/float: calculated average
    """

    return sum(arr) / len(arr)


def geometric_average(arr):
    """
    Function calculates geometric average
    
    :param arr: list: list of numbers
    :return: float: calculated average
    """

    product = 1
    for num in arr:
        product *= num
    
    return product**(1/len(arr))


def harmonic_average(arr):
    """
    Function calcualtes harmonic average

    :param arr: list: list of numbers
    :return: float: calculated average
    """

    return len(arr) / sum([1/num for num in arr])


def weighted_average(arr):
    """
    Function calculates weighted average

    :param arr: list: list of tuples made of number and weight
    :return: float: calculated average
    """

    number_weight_prod = sum([tup[0] * tup[1] for tup in arr])
    weights_sum = sum(tup[1] for tup in arr)
    return number_weight_prod / weights_sum


def travelling_salesman_problem():
    """
    Function will find solution for travelling salesman problem

    :return: str: length of the route and cities listed from start to finish
    """

    cities = ['warszawa', 'gdańsk', 'kraków', 'wrocław', 'poznań']
    graph = [
        (cities[0], cities[1], 341),
        (cities[0], cities[2], 299),
        (cities[0], cities[3], 341),
        (cities[0], cities[4], 304),
        (cities[1], cities[2], 584),
        (cities[1], cities[3], 486),
        (cities[1], cities[4], 304),
        (cities[2], cities[3], 304),
        (cities[2], cities[4], 403),
        (cities[3], cities[4], 280),
    ]

    route = [cities[0]]
    curr_city = cities[0]
    visited = []
    length = 0
    while len(route) != len(cities):
        curr_nodes = []
        for branch in graph:
            if curr_city in branch and branch not in visited:
                curr_nodes.append(branch)
        
        # chosing the most optimal choice - branch has the lowest weight
        optimal_choice = list(min(curr_nodes, key=lambda node: node[2]))
        length += optimal_choice[2]  # incrementing lenght of route
        optimal_choice.remove(curr_city)  # removing current city from choice
        visited.extend(curr_nodes)  # extending visited list by used graph branches
        curr_city = optimal_choice[0]  # setting current city
        route.append(curr_city)  # appending current city to route

    # finding end route to close the cicle
    start_city = route[0]
    last_city = route[-1]
    for branch in graph:
        if start_city in branch and last_city in branch:
            length += branch[-1]
            route.append(start_city)

    return f'Route has length: {length} and goes like this: ' + ' - '.join(route)

print(travelling_salesman_problem())