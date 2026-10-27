def is_even(number):
    """ Return True if number is even and False if it is odd.

    :param number: The number to check if it is even.
    :return: True if number is EVEN, otherwise False
    """
    if number % 2 ==0:
        return True
    else:
        return False


def count_vowels(text):
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text: Insert word to count vowels
    :return: Counted vowels from word
    """
    value = 0
    for letter in text:
        if letter.lower() in "aeiou":
            value += 1
    return value


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius: The celcius value to be converted into Fahrenheit.
    :return: The converted tempertaure to Fahrenheit.
    """
    farhenheit=(celsius * 9/5)+32
    return farhenheit


def reverse_text(text):
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text: Any word to be reversed
    :return: The reversed word
    """
    reversed_text = text[::-1]
    return reversed_text



def larger_number(a, b):
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a: THe first integer
    :param b: The second integer
    :return: The greatest integer
    """
    if a>=b:
        value = a
    else:
        value=b
    return value

def average_two(a, b):
    """Calculate and return the average of two integers.

    :param a: First value
    :param b: Second value
    :return: Average between the two numbers
    """
    average = (a+b)/2
    return average


def can_afford(balance: float, cost:float):
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance: Avaiable balance
    :param cost: cost of something
    :return:total cost/can afford
    """
    value = balance >= cost
    return value


def repeat_text(text, times):
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text: needed to be repeated
    :param times: number of times to repeat
    :return: the repeated version
    """
    value = text * times
    return value


def contains_word(sentence, word):
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence: Sentence
    :param word: The word to look for
    :return: True if found, otherwise false
    """
    value = word in sentence
    return value


def calculate_tip(cost:float, percent:float):
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost: The base cost
    :param percent: tip percentage
    :return: the tipped amount
    """
    value = cost *(percent/100)
    return value

def make_initials(first_name, last_name):
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name: The first name
    :param last_name:The last name
    :return: Intials from first and last name
    """
    first_name = first_name[0]
    last_name = last_name[0]
    initials = first_name + last_name

    return initials.upper()

def percent_score(points:float, possible:float):
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points: number of points achieved
    :param possible: maximum number of points possible to achieve
    :return: overall percentage
    """
    value = (points/possible) * 100
    return value

def is_between(number:float, minimum:float, maximum:float):
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number: number to check
    :param minimum: minimum amount
    :param maximum: maximum amount
    :return: number in between
    """
    value = minimum <=number<=maximum
    return value


def all_different(a, b, c):
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a: one type of string
    :param b: second type of string
    :param c: thrid type of string
    :return: acheck if all different
    """
    if a==b or b==c or a==c:
        value = False
    else:
        value = True
    return value


def average_three(a, b, c):
    """Calculate and return the average of three integers.

    :param a: first value
    :param b: second value
    :param c: third value
    :return: average overall from 3
    """
    value = (a+b+c)/3
    return value


def describe_temperature(temperature, cold_limit, hot_limit):
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature: current temperature
    :param cold_limit: when is cosnidered cold
    :param hot_limit: when is considered hot
    :return:
    """
    if temperature < cold_limit:
        value = "cold"
    elif temperature > hot_limit:
        value = "hot"
    else:
        value = "comfortable"
    return value

if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    value = larger_number(12, 19)
    print( value)

