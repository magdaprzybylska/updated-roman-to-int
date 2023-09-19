def romanToInt(s: str) -> int:

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    letters = list(s)

    result = 0

    for x in range(len(letters)):
        if x == len(letters) - 1:
            result += roman_dict[letters[x]]
        else:
            if roman_dict[letters[x]] >= roman_dict[letters[x + 1]]:
                result += roman_dict[letters[x]]
            else:
                result -= roman_dict[letters[x]]

    return result


integer = romanToInt("MCMXCIV")
print(f"this is your converted int {integer}")
