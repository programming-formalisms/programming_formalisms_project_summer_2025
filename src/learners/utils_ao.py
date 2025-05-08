
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