# from number to word
def n2w(n):
    num2words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        0: "zero",
    }

    try:
        return num2words[n]
    except KeyError:
        try:
            return num2words[n - n % 10] + num2words[n % 10].lower()
        except KeyError:
            return "unknown"


if __name__ == "__main__":
    print(n2w(99))
