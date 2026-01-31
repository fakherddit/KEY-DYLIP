"""
Roman Numeral III Implementation
Represents the number 3 in Roman numerals
"""

def roman_to_int(roman):
    """Convert Roman numeral to integer"""
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_values.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

def int_to_roman(num):
    """Convert integer to Roman numeral"""
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ''
    for value, numeral in values:
        count = num // value
        if count:
            result += numeral * count
            num -= value * count
    
    return result

if __name__ == "__main__":
    # Demonstrate III
    roman = "III"
    integer = roman_to_int(roman)
    print(f"Roman numeral: {roman}")
    print(f"Integer value: {integer}")
    print(f"Convert back: {int_to_roman(integer)}")
