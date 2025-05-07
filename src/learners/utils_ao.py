
def is_roman_numeral(numeral):
    """Determines if the 'numeral' is a roman numeral"""
    if not isinstance(numeral, str):
        return False
    valid_nums = ["I","V","X","L","M","C","D"]
    # Check if the numeral contains these characters only
    for s in numeral:
        if s not in valid_nums:
            return False
    return True


def roman_to_numeral(roman):
    """Converts a single roman numeral into an integer"""
    roman_num = ["I","V","X","L","C","D","M"]
    int_num = [1, 5, 10, 50, 100, 500, 1000]

    #TODO: add buffer for numbers to subtract and numbers to add before calculating the integer