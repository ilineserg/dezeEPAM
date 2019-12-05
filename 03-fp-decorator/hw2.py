def is_armstrong(number):
    return sum(map(lambda x: int(x) ** len(str(number)), [i for i in str(number)])) == number
